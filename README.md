# Class Notifier

A multi-platform app which helps to maintain attentiveness while lecture delivery by sending notification to defaulting student and notify teacher about them.

## Getting Started

Clone or fork the repo to make changes and test the site.

## Description

Use cases implemented till now:
* Student Register
* Student login
* Respond to alert

To view Entity objects check file :- notifier/models.py

Models include:
* Student
* Notification

To view Controller and check file :- notifier/views.py

Controller include:
* StateAnalyser

To view Boundary object check directory :- templates

Boundary object include:

* RegisterBoundary
* LoginBoundary
* NotificationList

To view Boundary object location :- notifier/urls.py

### Prerequisites

Install django.


### Installing

Create a vitual enviroment if you have deal with multiple python projects.

```
sudo apt-get install python-virtualenv
or
sudo easy_install virtualenv
or
sudo pip3 install virtualenv
```

```
mkdir ~/virtualenvironment
virtualenv ~/virtualenvironment/my_new_app
cd ~/virtualenvironment/my_new_app/bin
source activate
```

To install django.
Note: Use sudo only if some errors pop up.

```
sudo pip3 install -r requirements.txt
```

Finally run

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

in the directory which has manage.py to get your site up and running.


## Built With

* [Django](https://www.djangoproject.com/) - A python-based web framework
* [BootStrap](https://getbootstrap.com/) -  A front-end CSS framework, To design interactive and beautiful UI

## Authors

* **Vivek Raj**  - [Class Notifier](https://github.com/codervivek/class-notifier)
* **[Kapil Goyal](https://github.com/kapil-goyal)**
* **[Rohit Pant](https://github.com/rpant1728)**

## License

GPL 3.0
