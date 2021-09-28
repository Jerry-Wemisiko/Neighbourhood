# NEIGHBOURHOOD

## Author
Jerry Wemisiko

### Description
This is a Django application of a neighburhood where a user can add a neighbourhood,view various busineese, add a post that the whole neighbourhood can view and also be able to leave the neighbourhood.

### Setup and Installations
To get the code, clone the repository:  https://github.com/Jerry-Wemisiko/Neighbourhood.git
And run the following commands;

    $ cd Neighbourhood
    $ pip install -r requirements.txt

### Install and activate the virtual emvironment

    $ pipenv install
    $ pipenv shell

### Create database 

    $ psql
    $ CREATE DATABASE (name_of_databse);

### Make migrations 

    $ python3 manage.py check
    $ make migrations neighbourhood
    $ MAKE migrate 

### Testing the application 
 
    $ python3 manage.py test (app_name)

### Running the Application

    $make serve

Then once you are done, open your browser with the local host; 127.0.0.1:8000

## Dependencies
1. Python3
2. Django 3.2.7
3. Virtual environment
4. Heroku
5. Gunicorn

## Technologies used
1. Python 3
2. HTML
3. Django 3.2.7
4. Bootstrap 4
5. Heroku
6. Postgresql


## License
This project is under:  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)

