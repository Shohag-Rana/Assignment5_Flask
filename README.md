

# Flask Authentication Based Post project

In this project when a user run this project the browser show a dialog box(username, password) for basic authentication. After complete basic authentication user are redirect to login page for flask-login authentication. After complete flask-login authentication the user can see the dashboard with all the post list. If the user want to show single post details he/she need to complete token based authentication. Then the user can show the post details


## Technology and Tools

    - FrontEnd: HTML, CSS, JS, Bootstrap
    - Template Engine: Jinja2
    - Programming Language: Python


## Author

- [Shohag Rana](https://github.com/Shohag-Rana)


## Installation

    - cd Assignment5_Flask
    - pip install requirements.txt
    - run: python/python3 main.js


## Github Deployment Command

create a new repository on the command line

```bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Shohag-Rana/Assignment5_Flask.git
git push -u origin main
```
push an existing repository from the command line

```bash
git remote add origin https://github.com/Shohag-Rana/Assignment5_Flask.git
git branch -M main
git push -u origin main
```

## Feature of this Project

   - There are 3 types of authentication process
   - Basic Authentication when project run
   - Flask-Login Authentication
   - Token Based Authentication
   - Posts data are render from json file

## Project File Structure and Description
    - Templates:- This folder hold's all the jinja2 template engine file
    - static:- This folder contains all the static files (css, js, images).
    - forms.py:- Create login forms
    - pyjwt.py:- encoded and decoded token data
    - flask_logins.py:- this file authorized flask-login authentication and login functionality
    - main.py:- application start from this file and assign user functionality
    - user_list.py:- store static users- 



## Conculation

In this flask authentication based post project i use jinja2 template engine to render dynamic/user data into the frontend. posts data are render from https://dummyjson.com/products this site.
