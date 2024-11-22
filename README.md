[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/MadhurDixit13)



[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/nikki1234567/MovieRecommender/graphs/commit-activity) [![Contributors Activity](https://img.shields.io/github/commit-activity/m/nikki1234567/MovieRecommender)](https://github.com/nikki1234567/MovieRecommender/pulse) [![GitHub issues](https://img.shields.io/github/issues/nikki1234567/MovieRecommender.svg)](https://github.com/nikki1234567/MovieRecommender/issues) [![GitHub issues-closed](https://img.shields.io/github/issues-closed-raw/nikki1234567/MovieRecommender)](https://github.com/nikki1234567/MovieRecommender/issues?q=is%3Aissue+is%3Aclosed) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14027294.svg)](https://doi.org/10.5281/zenodo.14027294) [![Code Coverage](https://github.com/nikki1234567/MovieRecommender/actions/workflows/codecov.yml/badge.svg)](https://github.com/nikki1234567/MovieRecommender/actions/workflows/codecov.yml) [![codecov](https://codecov.io/gh/nikki1234567/MovieRecommender/graph/badge.svg?token=9NGWAJ7BST)](https://codecov.io/gh/nikki1234567/MovieRecommender) [![GitHub release](https://img.shields.io/github/release/nikki1234567/MovieRecommender.svg)](https://github.com/nikki1234567/MovieRecommender/releases) [![black](https://img.shields.io/badge/StyleChecker-black-purple.svg)](https://pypi.org/project/black/) 
[![Unit Tests](https://github.com/nikki1234567/MovieRecommender/actions/workflows/test.yml/badge.svg)](https://github.com/nikki1234567/MovieRecommender/actions/workflows/test.yml)
[![Python Style Checker](https://github.com/nikki1234567/MovieRecommender/actions/workflows/python_style_checker.yml/badge.svg)](https://github.com/nikki1234567/MovieRecommender/actions/workflows/python_style_checker.yml)
[![Code Formatting](https://github.com/nikki1234567/MovieRecommender/actions/workflows/code_formatting.yml/badge.svg)](https://github.com/nikki1234567/MovieRecommender/actions/workflows/code_formatting.yml)
[![Lint Python](https://github.com/nikki1234567/MovieRecommender/actions/workflows/syntax_checker.yml/badge.svg)](https://github.com/nikki1234567/MovieRecommender/actions/workflows/syntax_checker.yml)
[![Documentation](https://img.shields.io/badge/Documentation-Wiki-blue.svg)](https://github.com/nikki1234567/MovieRecommender/wiki)


# 🎬 Movie Recommender System V2.0 🎥

# Description
Tired of endless scrolling, trying to find the perfect movie? 🍿<br><br>
Discover Your Next Movie Night Gem!<br>


## Contents
- [Introduction](#introduction)
- [Previous Version](#core-features)
- [Our Version](#features-added-in-our-version)
- [Demo](#demo)
- [Tech Stack](#tech-stack) 
- [Installation](#installation)
- [Testing](#testing)
  - [Code Coverage](#code-coverage)
- [Usage](#usage)
- [License](#lincense)
- [Supporting Files](supporting-files)

---

## Introduction   
Welcome to our Movie Recommender!  

Our **Movie Recommender System** is built using **Python** and **Natural Language Processing (NLP)** to provide personalized and engaging movie recommendations. Whether you're exploring genres, production companies, or specific tags, our system delivers tailored suggestions to enhance your movie-watching experience.

---

## Core Features 

### 🎯 **Personalized Recommendations**  
💡 Get custom-tailored movie suggestions based on your unique interests and preferences.  

### 👤 **User Accounts**  
🔐 Enjoy user-specific tracking for:  
- **🎥 Personalized Recommendations**   
- **🗂 Search History**  

### 💬 **Feedback System**  
📝 Share your thoughts!  
- Provide feedback to the movie by like, dislike and yet to watch.  

### 📱 **Mobile-Friendly Design**  
📱 💻 **Fully Responsive** for both desktop and mobile devices, ensuring a seamless experience wherever you are.  

---  

## Features Added in our Version  

- **🔐 User Authentication**  
  - Seamless **Signup** and **Login** functionality for a personalized experience.

- **🔍 Intelligent Movie Recommendations**  
  - Utilizes the **Bag-of-Words** concept to suggest movies based on similarity, tags, genres, cast and production companies.  

- **📊 Weekly Top 10 Trending Movies**  
  - Displays trending movies every week, including:  
    - **🎥 Poster**  
    - **🎭 Genre**  
    - **📝 Overview**  

- **🛠 Feedback System**  
  - Share your thoughts! Let us know if the recommendations match your preferences for an improved experience by a thumps down and thumps up gesture. 

- **🗂 Recommendation History**  
  - Keep track of:  
    - Your **search history**  
    - Our **recommendation history**     
---

## Demo
[![Link to Demo](https://github.com/user-attachments/assets/9f0facb6-bf24-4288-9117-f2ceab69e148)](https://drive.google.com/file/d/1_EkBOV__bC8n0r8TRxF73vQg_7AMzNDZ/view?usp=drive_link)

---

## Getting Started  
1. *Installation*: Follow the instructions in [INSTALL.md].
2. *Code of Conduct*: Please read [CODE-OF-CONDUCT.md] to understand expected behavior in our community.
3. *Contributing*: Follow the guidelines in [CONTRIBUTING.md] for coding standards, branch naming, and commit messages.
4. *Usage Guide*: Learn about common workflows and functions in [USAGE.md].

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
- [Learn to Check Movie Description!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Describe_movie.md)
- [Learn to Check All Movies!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Check_all_movies.md)
- [Learn to Check Weekly Top 10 Movies!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Trending_Movies.md)
- [Learn to Check Recommendation History!!](https://github.com/Parth291102/Movie_Recommender/blob/Version_2.0/Tutorials/Recommendation_History.md)

---

## License   
This project is licensed under the [MIT License](LICENSE.md), allowing users to reuse, modify, and adapt the code to suit their needs.  

---

### Supporting Files

- *[INSTALL.md](Install.md)*: Details on setting up the environment and installing dependencies.
- *[CODE-OF-CONDUCT.md](CODE_OF_CONDUCT.md)*: Outlines expected community behavior.
- *[CONTRIBUTING.md](CONTRIBUTING.md)*: Details coding standards, commit messages, and branching strategies.
- *[CHANGELOG.md](https://github.com/Parth291102/Movie_Recommender/issues)*: Lists updates, fixes, and new features for each release.
