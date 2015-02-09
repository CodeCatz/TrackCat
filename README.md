TrackCat
========

A tool for tracking the progress of the kittens (and cat{s,z}) in out CodeCatz meetup group


How to start
============

If you haven't done so, create a fork of this project, and clone that project to your computer, continue from there :wink:  It is recommended that you use a virtual environment (or the virtualenvwrapper).

Install the requirements

    pip install -r requirements.txt

Create the database (only first time)

	./manage.py migrate

Run the server

	./manage.py runserver

Coding Style
============

On this project we use tabs for indentation. Please make sure your editor is properly set up for this.

Mockup
======

https://moqups.com/superbibi101/uxDjnbyA

Install and Configure Python social authentication
======================================
Perform steps 1., 2. in 3. in your virtual environment.
1. Install the requirements:
pip install -r requirements.txt
2. Sync database to create needed models:
./manage.py makemigrations 
./manage.py syncdb
3. Run server: 
./manage.py runserver
4. In Github go to Personal Settings/Applications -> Register new application
Application name = TrackCatz
Homepage URL = http://localhost:8000/
Application Descrition = TrackCatz application
Application callback URL = http://localhost:8000/
5. In your local TrackCat directory create settings_local.py and add two lines:
SOCIAL_AUTH_GITHUB_KEY = 'enter Client ID from your github registered app '
SOCIAL_AUTH_GITHUB_SECRET = 'enter Client Secret from your github registered app'

