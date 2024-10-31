from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import json
import sys
import csv
import time
import requests
from datetime import datetime


sys.path.append("../../")
from Code.prediction_scripts.item_based import recommendForNewUser
from search import Search

import requests

app = Flask(__name__)
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_title = db.Column(db.String(200), nullable=False)
    review = db.Column(db.String(50))  # New column for review (like, dislike, etc.)
    recommended_on = db.Column(db.DateTime, default=datetime.utcnow)

class TopMovies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_title = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)



# Replace 'YOUR_API_KEY' with your actual OMDB API key
OMDB_API_KEY = 'b726fa05'

def get_movie_info(title):
    index=len(title)-6
    url = f"http://www.omdbapi.com/?t={title[0:index]}&apikey={OMDB_API_KEY}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        res=response.json()
        if(res['Response'] == "True"):
            return res
        else:  
            return { 'Title': title, 'imdbRating':"N/A", 'Genre':'N/A',"Poster":"https://www.creativefabrica.com/wp-content/uploads/2020/12/29/Line-Corrupted-File-Icon-Office-Graphics-7428407-1.jpg"}
    else:
        return  { 'Title': title, 'imdbRating':"N/A",'Genre':'N/A', "Poster":"https://www.creativefabrica.com/wp-content/uploads/2020/12/29/Line-Corrupted-File-Icon-Office-Graphics-7428407-1.jpg"}

@app.route("/")
def landing_page():
    return render_template("landing_page.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('landing_page'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('landing_page'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('landing_page'))

    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()  # 'user' is now defined here

        if user is None or not user.check_password(password):
            error = 'Invalid username or password'
        else:
            login_user(user)
            return redirect(url_for('landing_page'))

    # If we reach this point without returning, 'user' was not assigned due to a POST
    # Or there was an error in login, handle accordingly
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('landing_page'))


@app.route("/predict", methods=["POST"])
# def predict():
#     data = json.loads(request.data)  # contains movies
#     data1 = data["movie_list"]
#     training_data = []
#     for movie in data1:
#         movie_with_rating = {"title": movie, "rating": 5.0}
#         training_data.append(movie_with_rating)
#     recommendations = recommendForNewUser(movie_with_rating)
    
#     for movie in data1:    
#         movie_info = get_movie_info(movie)
#         if movie_info:
#             movie_with_rating["title"]=movie
#             movie_with_rating["rating"]=movie_info["imdbRating"]
    
#     recommendations = recommendations[:10]
#     resp = {"recommendations": recommendations}
#     return resp
def predict():
    data = json.loads(request.data)  # contains movies
    data1 = data["movie_list"]
    training_data = []
    for movie in data1:
        movie_with_rating = {"title": movie, "rating": 5.0}
        training_data.append(movie_with_rating)
    recommendations = recommendForNewUser(training_data)
    recommendations = recommendations[:10]

    for movie in recommendations:
        movie_info = get_movie_info(movie)
        # print(movie_info['imdbRating'])
        if movie_info:
            movie_with_rating[movie+"-r"]=movie_info['imdbRating']
            movie_with_rating[movie+"-g"]=movie_info['Genre']
            movie_with_rating[movie+"-p"]=movie_info['Poster']
        
        new_recommendation = Recommendation(user_id=current_user.id, movie_title=movie, review="yet to watch")
        db.session.add(new_recommendation)
    
    db.session.commit()

    resp = {"recommendations": recommendations, "rating":movie_with_rating, "review": "yet to watch"}
    return resp

# @app.route("/predict", methods=["POST"])
# @login_required
# def predict():
#     data = json.loads(request.data)  # contains movies
#     liked_movies = Recommendation.query.filter_by(user_id=current_user.id, review="like").all()
#     liked_movie_titles = [movie.movie_title for movie in liked_movies]

#     training_data = [{"title": title, "rating": 5.0} for title in liked_movie_titles]
#     recommendations = recommendForNewUser(training_data)[:10]

#     # Store recommendations with movie info
#     movie_with_rating = {}
#     for movie in recommendations:
#         movie_info = get_movie_info(movie)
#         if movie_info:
#             movie_with_rating[movie+"-r"] = movie_info['imdbRating']
#             movie_with_rating[movie+"-g"] = movie_info['Genre']
#             movie_with_rating[movie+"-p"] = movie_info['Poster']
        
#         # Add to Recommendation table with default 'yet to watch' review
#         new_recommendation = Recommendation(user_id=current_user.id, movie_title=movie, review="yet to watch")
#         db.session.add(new_recommendation)

#     # Commit new recommendations
#     db.session.commit()

#     resp = {"recommendations": recommendations, "rating": movie_with_rating}
#     return resp


@app.route("/history")
@login_required
def history():
    recommendations = Recommendation.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html', recommendations=recommendations)


@app.route("/search", methods=["POST"])
def search():
    term = request.form["q"]
    search = Search()
    filtered_dict = search.resultsTop10(term)
    resp = jsonify(filtered_dict)
    resp.status_code = 200
    return resp

# @app.route("/feedback", methods=["POST"])
# def feedback():
#     data = json.loads(request.data)
#     with open(f"experiment_results/feedback_{int(time.time())}.csv", "w") as f:
#         for key in data.keys():
#             f.write(f"{key} - {data[key]}\n")
#     return data

@app.route("/feedback", methods=["POST"])
def feedback():
    print("In Feedback")
    data = json.loads(request.data)
    print(data)
    user_id = current_user.id  # Assuming user is authenticated, retrieve their ID
    
    for movie_title, feedback_type in data.items():
        feedback_entry = Recommendation(
            user_id=user_id,
            movie_title=movie_title,
            review=feedback_type
        )
        db.session.add(feedback_entry)
    
    db.session.commit()  # Commit all feedback entries at once
    return jsonify({"status": "success", "message": "Feedback saved successfully"})


@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/generate_top_movies", methods=["POST"])
@login_required
def generate_top_movies():
    liked_movies = Recommendation.query.filter_by(user_id=current_user.id, review="like").all()
    liked_movie_titles = [movie.movie_title for movie in liked_movies]

    training_data = [{"title": title, "rating": 5.0} for title in liked_movie_titles]
    top_movies = recommendForNewUser(training_data)[:10]

    # Store top 10 movies in TopMovies table
    for movie in top_movies:
        top_movie_entry = TopMovies(user_id=current_user.id, movie_title=movie)
        db.session.add(top_movie_entry)

    db.session.commit()
    return jsonify({"top_movies": top_movies})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)


