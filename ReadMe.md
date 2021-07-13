Pre-Requirements
Django is an open-source web framework, written in Python, that follows the model-view-template architectural pattern. So Python is needed to be installed in your machine. Unfortunately, there was a significant update to Python several years ago that created a big split between Python versions namely Python 2 the legacy version and Python 3 the version in active development.

Since Python 3 is the current version in active development and addressed as the future of Python, Django rolled out a significant update, and now all the releases after Django 2.0 are only compatible with Python 3.x. Therefore this tutorial is strictly for Python 3.x. Make sure you have Python 3 installed on your machine if not follow the below guides.

Windows Users
How To Install Python On Windows : https://www.python.org/downloads/
Mac And Unix Users
How To Install Python 3 on Mac OS : https://www.python.org/downloads/
Creating And Activating A Virtual Environment
While building python projects, it’s a good practice to work in virtual environments to keep your project, and it’s dependency isolated on your machine. There is an entire article on the importance of virtual environments Check it out here: How To A Create Virtual Environment for Python

Windows Users
-->cd Desktop
-->virtualenv django
-->cd django
-->Scripts\activate.bat
-->Mac and Unix Users
-->mkdir django
-->cd django
-->python3 -m venv django
-->source django/bin/activate
Now you should see (django) prefixed in your terminal, which indicates that the virtual environment is successfully activated, if not then go through the guide again.

Installing Django In The Virtual Environment
If you have already installed Django, you can skip this section and jump straight to the Setting up the project section. To Install Django on your virtual environment run the below command

pip install Django
This will install the latest version of Django in our virtual environment. To know more about Django installation read: How To Install Django

Note – You must install a version of Django greater than 2.0

Setting Up The Project
In your workspace create a directory called mysite and navigate into it.

cd Desktop
mkdir mysite
cd mysite
Now run the following command in your shell to create a Django project.

django-admin startproject mysite
This will generate a project structure with several directories and python scripts.

├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
To know more about the function of the files read: Starting A Django Project

Next, we need the create a Django application called blog. A Django application exists to perform a particular task. You need to create specific applications that are responsible for providing your site desired functionalities.


 
Navigate into the outer directory where manage.py script exists and run the below command.

cd mysite
python manage.py startapp blog
These will create an app named blog in our project.

├── db.sqlite3
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
└── blog
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
Now we need to inform Django that a new application has been created, open your settings.py file and scroll to the installed apps section, which should have some already installed apps.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
Now add the newly created app blog at the bottom and save it.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
]
Next, make migrations.

python manage.py migrate
This will apply all the unapplied migrations on the SQLite database which comes along with the Django installation.

Let’s test our configurations by running the  Django’s built-in development server.

python manage.py runserver
Open your browser and go to this address http://127.0.0.1:8000/ if everything went well you should see this page.

Starting A Django Project 
--> Now go to the base folder of Django Blog then run the server by : python manage.py runserver