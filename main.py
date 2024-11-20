import streamlit as st
import streamlit_option_menu
from streamlit_extras.stoggle import stoggle
from processing import preprocess
from processing.display import Main
import json
import hashlib
import pandas as pd
import random
import time

# Setting the wide mode as default
st.set_page_config(layout="wide")
displayed = []

if 'movie_number' not in st.session_state:
    st.session_state['movie_number'] = 0

if 'selected_movie_name' not in st.session_state:
    st.session_state['selected_movie_name'] = ""

if 'user_menu' not in st.session_state:
    st.session_state['user_menu'] = ""

if 'username' not in st.session_state:
    st.session_state['username'] = None

if 'recommendation_history' not in st.session_state:
    st.session_state['recommendation_history'] = []
    
if "feedback" not in st.session_state:
    st.session_state["feedback"] = {}

# Authentication Helpers
def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Dashboard State Initialization
if 'movie_number' not in st.session_state:
    st.session_state['movie_number'] = 0
if 'selected_movie_name' not in st.session_state:
    st.session_state['selected_movie_name'] = ""
if 'user_menu' not in st.session_state:
    st.session_state['user_menu'] = ""
if 'username' not in st.session_state:
    st.session_state['username'] = None

# Authentication Pages
def login_page():
    st.title("Welcome to Movie Recommender 🎥")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    # Login Section
    with tab1:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            users = load_users()
            if username in users and users[username]["password"] == hash_password(password):
                st.session_state["username"] = username
                st.success(f"Welcome back, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    # Signup Section
    with tab2:
        st.subheader("Signup")
        new_username = st.text_input("Choose a Username")
        email = st.text_input("Email ID")
        new_password = st.text_input("Create a Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Signup"):
            if not new_username or not email or not new_password:
                st.error("All fields are required.")
            elif new_password != confirm_password:
                st.error("Passwords do not match.")
            else:
                users = load_users()
                if new_username in users:
                    st.error("Username already exists.")
                elif any(user["email"] == email for user in users.values()):
                    st.error("Email already registered.")
                else:
                    users[new_username] = {
                        "email": email,
                        "password": hash_password(new_password)
                    }
                    save_users(users)
                    st.success("Account created successfully! Please login.")
                    st.rerun()

# Main Recommender Dashboard
def main_dashboard(new_df, movies):
    def initial_options():
        # To display menu
        st.session_state.user_menu = streamlit_option_menu.option_menu(
            menu_title='What are you looking for? 👀',
            options=['Trending Top 10','Recommend me a similar movie', 'Describe me a movie', 'Check all Movies', 'Recommendation History','View Feedback'],
            icons=['stars','film', 'film', 'film', 'clock-history','hand-thumbs-up'],
            menu_icon='list',
            orientation="horizontal",
        )

        if st.session_state.user_menu == 'Recommend me a similar movie':
            recommend_display()

        elif st.session_state.user_menu == 'Describe me a movie':
            display_movie_details()

        elif st.session_state.user_menu == 'Check all Movies':
            paging_movies()
        
        elif st.session_state.user_menu == 'Recommendation History':
            display_recommendation_history()
            
        elif st.session_state.user_menu == "View Feedback":
            display_feedback_summary()
        
        elif st.session_state.user_menu == "Trending Top 10":  
            display_trending_top_10()

    def recommend_display():

        st.title('Movie Recommender System')

        selected_movie_name = st.selectbox(
            'Select a Movie...', new_df['title'].values
        )

        rec_button = st.button('Recommend')
        if rec_button:
            st.session_state.selected_movie_name = selected_movie_name
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_tags.pkl',"are")
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_genres.pkl',"on the basis of genres are")
            recommendation_tags(new_df, selected_movie_name,
                                r'Files/similarity_tags_tprduction_comp.pkl',"from the same production company are")
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_keywords.pkl',"on the basis of keywords are")
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_tcast.pkl',"on the basis of cast are")
            
    def update_feedback(movie, status):
        # Update feedback in session state
        st.session_state["feedback"][movie] = status

    def recommendation_tags(new_df, selected_movie_name, pickle_file_path,description):

        movies, posters = preprocess.recommend(new_df, selected_movie_name, pickle_file_path)
        st.subheader(f'Best Recommendations {description}...')

        rec_movies = []
        rec_posters = []
        cnt = 0
        feedback = st.session_state.get("feedback", {})
        # Adding only 5 uniques recommendations
        for i, j in enumerate(movies):
            if cnt == 5:
                break
            if j not in displayed:
                rec_movies.append(j)
                rec_posters.append(posters[i])
                displayed.append(j)
                cnt += 1
        
        # Save recommendations to history
        st.session_state['recommendation_history'].append({
            "movie": selected_movie_name,
            "recommendations": rec_movies,
            "time": st.session_state.get("current_time", str(pd.Timestamp.now()))  
            })


        # Columns to display informations of movies i.e. movie title and movie poster
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(rec_movies[0])
            st.image(rec_posters[0])
            st.button(f"👍 {rec_movies[0]}", on_click=update_feedback, args=(rec_movies[0], "like"), key=f"like_{rec_movies[0]}")
            st.button(f"👎 {rec_movies[0]}", on_click=update_feedback, args=(rec_movies[0], "dislike"), key=f"dislike_{rec_movies[0]}")

        with col2:
            st.text(rec_movies[1])
            st.image(rec_posters[1])
            st.button(f"👍 {rec_movies[1]}", on_click=update_feedback, args=(rec_movies[1], "like"), key=f"like_{rec_movies[1]}")
            st.button(f"👎 {rec_movies[1]}", on_click=update_feedback, args=(rec_movies[1], "dislike"), key=f"dislike_{rec_movies[1]}")

        with col3:
            st.text(rec_movies[2])
            st.image(rec_posters[2])
            st.button(f"👍 {rec_movies[2]}", on_click=update_feedback, args=(rec_movies[2], "like"), key=f"like_{rec_movies[2]}")
            st.button(f"👎 {rec_movies[2]}", on_click=update_feedback, args=(rec_movies[2], "dislike"), key=f"dislike_{rec_movies[2]}")

        with col4:
            st.text(rec_movies[3])
            st.image(rec_posters[3])
            st.button(f"👍 {rec_movies[3]}", on_click=update_feedback, args=(rec_movies[3], "like"), key=f"like_{rec_movies[3]}")
            st.button(f"👎 {rec_movies[3]}", on_click=update_feedback, args=(rec_movies[3], "dislike"), key=f"dislike_{rec_movies[3]}")

        with col5:
            st.text(rec_movies[4])
            st.image(rec_posters[4])
            st.button(f"👍 {rec_movies[4]}", on_click=update_feedback, args=(rec_movies[4], "like"), key=f"like_{rec_movies[4]}")
            st.button(f"👎 {rec_movies[4]}", on_click=update_feedback, args=(rec_movies[4], "dislike"), key=f"dislike_{rec_movies[4]}")
            
        st.session_state["feedback"] = feedback  
    
    def display_recommendation_history():
        st.title("Recommendation History")
        if not st.session_state['recommendation_history']:
            st.write("No recommendations made yet.")
        else:
            for entry in st.session_state['recommendation_history']:
                st.write(f"**{entry['movie']}** - Recommended on {entry['time']}")
                for rec in entry["recommendations"]:
                    st.write(f"- {rec}")
    
    def display_trending_top_10():
        st.title("Trending Top 10 Movies This Week 🎬")

        # Seed based on current week
        week_number = pd.Timestamp.now().week
        random.seed(week_number)  # Ensure consistency for the week

        # Randomly select 10 movies
        trending_movies = movies.sample(n=10, random_state=week_number)
        
        for index, row in trending_movies.iterrows():
            # Use columns for layout
            col1, col2 = st.columns([1, 2])

            # Display poster in the left column
            with col1:
                poster_url = preprocess.fetch_posters(row['movie_id'])
                st.image(poster_url, width=200)

            # Display details in the right column
            with col2:
                # Combine overview into a single sentence
                overview = " ".join(row['overview']) if isinstance(row['overview'], list) else row['overview']
                st.markdown(f"### {row['title']}")
                st.markdown(f"<b>Genre:</b> 🎭 <i>{', '.join(row.iloc[3]) if isinstance(row.iloc[3], list) else row.iloc[3]}</i>", unsafe_allow_html=True)
                st.markdown(f"**Release Date**: 📅 {row['release_date']}")
                st.write(overview)

            # Add a divider
            st.markdown("---")

    def display_movie_details():

        selected_movie_name = st.session_state.selected_movie_name
        # movie_id = movies[movies['title'] == selected_movie_name]['movie_id']
        info = preprocess.get_details(selected_movie_name)

        with st.container():
            image_col, text_col = st.columns((1, 2))
            with image_col:
                st.text('\n')
                st.image(info[0])

            with text_col:
                st.text('\n')
                st.text('\n')
                st.title(selected_movie_name)
                st.text('\n')
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.text("Rating")
                    st.write(info[8])
                with col2:
                    st.text("No. of ratings")
                    st.write(info[9])
                with col3:
                    st.text("Runtime")
                    st.write(info[6])

                st.text('\n')
                st.write("Overview")
                st.write(info[3], wrapText=False)
                st.text('\n')
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.text("Release Date")
                    st.text(info[4])
                with col2:
                    st.text("Budget")
                    st.text(info[1])
                with col3:
                    st.text("Revenue")
                    st.text(info[5])

                st.text('\n')
                col1, col2, col3 = st.columns(3)
                with col1:
                    str = ""
                    st.text("Genres")
                    for i in info[2]:
                        str = str + i + " . "
                    st.write(str)

                with col2:
                    str = ""
                    st.text("Available in")
                    for i in info[13]:
                        str = str + i + " . "
                    st.write(str)
                with col3:
                    st.text("Directed by")
                    st.text(info[12][0])
                st.text('\n')

        # Displaying information of casts.
        st.header('Cast')
        cnt = 0
        urls = []
        bio = []
        for i in info[14]:
            if cnt == 5:
                break
            url, biography= preprocess.fetch_person_details(i)
            urls.append(url)
            bio.append(biography)
            cnt += 1

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(urls[0])
            # Toggle button to show information of cast.
            stoggle(
                "Show More",
                bio[0],
            )
        with col2:
            st.image(urls[1])
            stoggle(
                "Show More",
                bio[1],
            )
        with col3:
            st.image(urls[2])
            stoggle(
                "Show More",
                bio[2],
            )
        with col4:
            st.image(urls[3])
            stoggle(
                "Show More",
                bio[3],
            )
        with col5:
            st.image(urls[4])
            stoggle(
                "Show More",
                bio[4],
            )

    def paging_movies():
        # To create pages functionality using session state.
        max_pages = movies.shape[0] / 10
        max_pages = int(max_pages) - 1

        col1, col2, col3 = st.columns([1, 9, 1])

        with col1:
            st.text("Previous page")
            prev_btn = st.button("Prev")
            if prev_btn:
                if st.session_state['movie_number'] >= 10:
                    st.session_state['movie_number'] -= 10

        with col2:
            new_page_number = st.slider("Jump to page number", 0, max_pages, st.session_state['movie_number'] // 10)
            st.session_state['movie_number'] = new_page_number * 10

        with col3:
            st.text("Next page")
            next_btn = st.button("Next")
            if next_btn:
                if st.session_state['movie_number'] + 10 < len(movies):
                    st.session_state['movie_number'] += 10

        display_all_movies(st.session_state['movie_number'])
        
    def display_feedback_summary():
        st.title("Your Feedback Summary")
        feedback = st.session_state.get("feedback", {})

        if not feedback:
            st.write("No feedback given yet.")
        else:
            likes = [movie for movie, status in feedback.items() if status == "like"]
            dislikes = [movie for movie, status in feedback.items() if status == "dislike"]

            if likes:
                st.subheader("Movies You Liked:")
                for movie in likes:
                    st.write(f"👍 {movie}")

            if dislikes:
                st.subheader("Movies You Disliked:")
                for movie in dislikes:
                    st.write(f"👎 {movie}")

    def display_all_movies(start):

        i = start
        with st.container():
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col2:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col3:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col4:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col5:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

        with st.container():
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col2:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col3:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col4:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col5:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

        st.session_state['page_number'] = i

    with Main() as bot:
        bot.main_()
        new_df, movies, movies2 = bot.getter()
        initial_options()

# Main Application
def main():
    if st.session_state["username"] is None:
        login_page()
    else:
        st.sidebar.title(f"Welcome, {st.session_state['username']}!")
        st.sidebar.button("Logout", on_click=lambda: st.session_state.update(username=None))
        with Main() as bot:
            new_df, movies, _ = bot.getter()
            main_dashboard(new_df, movies)

if __name__ == '__main__':
    main()
