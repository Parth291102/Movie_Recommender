[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/MadhurDixit13)



[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/nikki1234567/MovieRecommender/graphs/commit-activity) [![Contributors Activity](https://img.shields.io/github/commit-activity/m/nikki1234567/MovieRecommender)](https://github.com/nikki1234567/MovieRecommender/pulse) [![GitHub issues](https://img.shields.io/github/issues/nikki1234567/MovieRecommender.svg)](https://github.com/nikki1234567/MovieRecommender/issues) [![GitHub issues-closed](https://img.shields.io/github/issues-closed-raw/nikki1234567/MovieRecommender)](https://github.com/nikki1234567/MovieRecommender/issues?q=is%3Aissue+is%3Aclosed) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT) 
[![DOI](https://zenodo.org/badge/890553932.svg)](https://doi.org/10.5281/zenodo.14210856)
[![Code Coverage](https://github.com/nikki1234567/MovieRecommender/actions/workflows/codecov.yml/badge.svg)](https://github.com/nikki1234567/MovieRecommender/actions/workflows/codecov.yml) [![codecov](https://codecov.io/gh/nikki1234567/MovieRecommender/graph/badge.svg?token=9NGWAJ7BST)](https://codecov.io/gh/nikki1234567/MovieRecommender)  [![black](https://img.shields.io/badge/StyleChecker-black-purple.svg)](https://pypi.org/project/black/) 
[![Unit Tests](https://github.com/nikki1234567/MovieRecommender/actions/workflows/test.yml/badge.svg)](https://github.com/nikki1234567/MovieRecommender/actions/workflows/test.yml)
[![Python Style Checker](https://github.com/nikki1234567/MovieRecommender/actions/workflows/python_style_checker.yml/badge.svg)](https://github.com/nikki1234567/MovieRecommender/actions/workflows/python_style_checker.yml)
[![Code Formatting](https://github.com/nikki1234567/MovieRecommender/actions/workflows/code_formatting.yml/badge.svg)](https://github.com/nikki1234567/MovieRecommender/actions/workflows/code_formatting.yml)
[![Lint Python](https://github.com/nikki1234567/MovieRecommender/actions/workflows/syntax_checker.yml/badge.svg)](https://github.com/nikki1234567/MovieRecommender/actions/workflows/syntax_checker.yml)


# 🎬 Movie Recommender System V2.0 🎥

# Description
Tired of endless scrolling, trying to find the perfect movie? 🍿<br><br>
Discover Your Next Movie Night Gem!<br>

https://github.com/user-attachments/assets/40929c4c-c2c0-4f6a-9d88-f7caa1216b5d


## Contents
- [Introduction](#introduction)
- [Original Version](#core-features)
- [Our Version](#features-added-in-our-version)
- [Demo](#demo)
- [Tech Stack](#tech-stack) 
- [Installation](#installation)
- [Testing](#testing)
  - [Code Coverage](#code-coverage)
- [Usage](#usage)
- [Future Scope](#future-scope)
- [License](#lincense)
- [Supporting Files](supporting-files)

---

## Introduction   
Welcome to our Movie Recommender!  

Our **Movie Recommender System** is built using **Python** and **Natural Language Processing (NLP)** to provide personalized and engaging movie recommendations. Whether you're exploring genres, production companies, or specific tags, our system delivers tailored suggestions to enhance your movie-watching experience. 

---

## Core Features 

### 🎯 **Personalized Recommendations**  
The engine uses collaborative filtering to recommend movies that are popular among users with similar tastes. Get custom-tailored movie suggestions based on your unique interests and viewing preferences. Whether you're into action, drama, sci-fi, or indie films, our recommendation system adapts to your tastes and suggests the best movies you’re most likely to enjoy. It’s like having your own personal movie curator! 

### 👤 **User Accounts**  
Now, you can Login and Signin to your password protected account. Recommendations are continuously refined based on the movies you rate and watch. Your preferences and search history are synced across devices, so your experience stays consistent, whether you’re on your phone or desktop. 

### 💬 **Feedback System**  
Share your feedback by marking movies with like, dislike, or yet to watch to help improve future recommendations. Tell us what you think by liking or disliking movies. Your feedback directly influences your future recommendations.

### 📱 **Mobile-Friendly Design**  
Enjoy a seamless experience on any device. Our responsive interface adapts to any screen size, with intuitive navigation for smooth browsing on both mobile and desktop. Access your recommendations, rate movies, and manage your watchlist anytime, anywhere.  

---  

## Features Added in our Version  

- **🔐 User Authentication**
Seamless **Signup** and **Login** functionality for a personalized experience with a toggled visibility function for passwords.

- **🔍 Intelligent Movie Recommendations**  
Our recommendation system uses Natural Language Processing (NLP) with the Bag-of-Words model to suggest movies based on text data like descriptions, genres, tags, cast, and production companies. By analyzing word frequency and similarities, it identifies movies with similar themes or attributes, even if you haven't watched or rated them. This ensures highly relevant suggestions tailored to your preferences, improving over time as you interact with the system.

- **📊 Weekly Top 10 Trending Movies**  
Stay on top of the latest cinematic hits with our Weekly Top 10 Trending Movies feature. Every week, we showcase the hottest films that are making waves, complete with essential details like the movie poster for a visual preview, the genre(s) for quick identification of the film's style, and a brief overview to give you a taste of the plot. Whether you're looking for the most talked-about films or just seeking new recommendations, this feature helps you easily discover the must-watch movies of the week. 

- **🛠 Feedback System**  
Our Feedback System lets you actively shape your movie recommendations by providing simple feedback. After watching a suggested film, you can give it a thumbs up if it matches your preferences, or a thumbs down if it doesn't. This helps refine the recommendation engine, ensuring more accurate and personalized suggestions in the future. Your input directly influences the system’s ability to learn from your tastes, enhancing your experience over time and making it easier to discover movies you'll love. The recoreded feedbacks can be viewed on the feedback tab.

- **🗂 Recommendation History**  
The Recommendation History feature allows you to effortlessly track both your search history and our personalized recommendation history. This gives you a complete overview of the movies you've searched for, explored, or received as suggestions. You can easily revisit previous recommendations, see how your tastes have evolved over time, and pick up where you left off. Whether you're interested in a movie you found earlier or want to see how your preferences have shaped the suggestions you get, this feature ensures you never lose track of your movie journey.

- **🎬 Watch the Trailer**
Dive into the cinematic world of your next favorite film! Simply click on the movie poster or hit the "Watch Trailer" button to preview the excitement. Don't miss out on the visual journey!

- **✨ UI/UX Enhancements with Streamlit**  
We've elevated the UI/UX by transitioning from Flask to Streamlit for a more seamless and user-friendly interface. Streamlit brings a clean, interactive design that makes navigation smoother and more intuitive. With real-time updates and a more responsive layout, users can effortlessly browse movie recommendations, track history, and share feedback. This change results in a visually appealing and minimalistic experience, making it easier than ever to enjoy your movie journey!

---

## Demo
[![Link to Demo](https://github.com/user-attachments/assets/9f0facb6-bf24-4288-9117-f2ceab69e148)](https://drive.google.com/file/d/1U1ZCsC8gi3oMgrA73Jv_PUVSWXKbDV5E/view?usp=sharing)

---

## Tech Stack
- *Python*
- *Streamlit*
- *HTML, CSS, JavaScript*

---

## Installation

Follow these steps to set up and run the application:

1. **Clone the Repository:** 
    ```bash
    git clone -b Version_2.0 https://github.com/Parth291102/Movie_Recommender.git
    ```

2. **Create a Virtual Environment:** 
   Make sure you have a virtual environment set up for your project.

3. **Install Dependencies:**
   Install the required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   To start the app, execute the following command in your terminal:
   ```bash
   streamlit run main.py
   ```
---

## Testing

  We use pytest to perform testing on all unit tests together. The command needs to be run from the home directory of the project. The command is:

  ```
  python run -m pytest test/
  ```
  (OR)
  ```
  python -m pytest test/
  ```
---

## Code Coverage

Code coverage is part of the build. Every time new code is pushed to the repository, the build is run, and along with it, code coverage is computed. This can be viewed by selecting the build, and then choosing the codecov pop-up on hover.

Locally, we use the coverage package in python for code coverage. The commands to check code coverage in python are as follows:

```
coverage run -m pytest test/
coverage report
```

---

## Usage
We have tried to make this application (bot) as easy as possible. You can use this bot to manage and track you daily expenses and not worry about loosing track of your expenses. As we also have given in a functionality of graphing and plotting and history of expenses, it becomes easy for the user to track expenses.
To make your experience even better, we have added User Tutorials for all the basic operations you can perform with DollarBot!!
Here you go:
- [Learn to Sign Up!!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/SignUp.md)
- [Learn to Log In!!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Login.md)
- [Learn to Search for your Movie Recommendation!!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Recommender.md)
- [Learn to watch the trailer!!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Watch_Trailer.md)
- [Learn to Check Movie Description!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Describe_movie.md)
- [Learn to Check All Movies!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Check_all_movies.md)
- [Learn to Check Weekly Top 10 Movies!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Trending_Movies.md)
- [Learn to Check Recommendation History!!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Recommendation_History.md)
- [Learn to give and check Feedback!!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/View_feedback.md)
- [Learn to LogOut!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Logout.md)

---

## Future Scope
- **📧 Personalized Email Notifications**
In the future, we aim to enhance user engagement by sending weekly movie recommendations directly to users via email. These automated notifications will be tailored to individual preferences, making it easy for users to stay updated on the latest film suggestions without having to log in. By delivering fresh content each week, we’ll keep movie nights exciting and hassle-free!

- **🤖 ML Model for Weekly Top 10 Recommendations**
To further refine our recommendation engine, we’re integrating a machine learning model that will pick the Weekly Top 10 movies based on user feedback. By analyzing preferences, ratings, and trends, the system will continuously improve, ensuring that the most relevant and exciting films make it to the top of your list. This means more accurate and personalized suggestions with every passing week!

- **🎬 Trailer Links with Movie Posters**
To make the movie selection process even more engaging, we’re planning to add trailer links to each movie poster. With just a click, users will be able to watch a preview of the film before deciding whether it’s worth adding to their watchlist. This feature will make discovering new movies even more interactive and enjoyable!

---

## License   
This project is licensed under the [MIT License](LICENSE.md), allowing users to reuse, modify, and adapt the code to suit their needs.  

---

### Supporting Files

- *[INSTALL.md](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/INSTALL.md)*: Details on setting up the environment and installing dependencies.
- *[CODE-OF-CONDUCT.md](CODE_OF_CONDUCT.md)*: Outlines expected community behavior.
- *[CONTRIBUTING.md](CONTRIBUTING.md)*: Details coding standards, commit messages, and branching strategies.
- *[CHANGELOG.md](https://github.com/Parth291102/Movie_Recommender/issues)*: Lists updates, fixes, and new features for each release.
