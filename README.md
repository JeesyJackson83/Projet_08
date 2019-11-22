# Projet_08 - Django pur beurre

Pur Beurre is an application made for Project 8 of OpenClassrooms DA Python.

It is a Django application that allows you to find a food product and choose a substitute with a better nutrition grade.

## Getting Started

You can use is directly at this adress: [https://jjpurbeurre.herokuapp.com/](https://jjpurbeurre.herokuapp.com/)

### Prerequisites

This application works with Python 3.6 and Django 2.2

You can choose the SGDB you want, just configure in [*settings.py*](https://github.com/JeesyJackson83/Projet_08/blob/master/purbeurre/purbeurre/settings.py)

### Installing

clone this repo

    git clone https://github.com/JeesyJackson83/Projet_08.git

create the virtualenv and install dependencies

create environment variables (here is for development config)



Run migrate and get_data for fill database 

    purbeurre/manage.py migrate
    purbeurre/manage.py get_data

Then run server

    purbeurre/manage.py runserver

## Running the tests

    purbeurre/manage.py test


## Built With

* [Django](https://www.djangoproject.com/)
* [Start Bootstrap Template](https://startbootstrap.com/themes/creative/)
* [OpenFoodFacts](https://fr.openfoodfacts.org/) : used for fill in database