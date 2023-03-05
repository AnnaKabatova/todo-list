# ToDo List

"ToDo List" is a Django-based project, that is visualised into a site. On this site you can create tasks, mark them as done (or make undo to completion), see deadlines, when it was created, what you need to do and its tags.

You can create, update and delete all of the objects - both tasks and tags.

This project is a simple analog for popular to-do managers.

## Installation

1. Copy this repository, by using your terminal:
```git
git clone <repository-url>
```
2. Checkout the latest commit to be up-to-date
```git
git checkout <code-of-specific-commit>
```
3. Change directory to main project folder. Use this commang:
```git
cd path-where-you've-installed-project/todo-list/
```
4. Install venv, and activate it by using following commands:
```git
python3 -m venv myvenv
```
to activate on Windows:
```git
myvenv\Scripts\activate.bat
```
to activate on Unix or Linux:
```git
source myvenv/bin/activate
```
5. Install dependencies (requirements):
```git
pip install -r requirements.txt
```
6. Run migrations to initialize database. Use this command:
```git
python manage.py migrate
```
7. Run the server of app
```git
python manage.py runserver
```
8. All is set, now you can use the site!

## A couple words on .env
In main folder you'll find a file .env_sample. In this file an example of SECRET_KEY is stored, required for the project.

You may need create a file .env and write here you secret key as in example.

## Usage
This site is free for all - you don't need to create any account or login.

This site is pretty much easy to use - after running it, you'll be on the main page (tasks list), from which you can switch to tags page and vice versa. Then you can just follow the buttons and links.

## Contributing

For major changes, please open an issue first to discuss what you would like to change.
