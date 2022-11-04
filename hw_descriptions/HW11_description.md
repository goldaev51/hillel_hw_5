# hillel_hw_11

## Description

Add a model for logs (in the same application as the form for calculating the hypotenuse). <br />
It should contain fields - path (path), method (GET, POST etc), timestamp. "Feel free to use": choices, auto_now_add,
default, etc. You can also add a field to save the transmitted data itself (JSONField) <br />
Add a LogMiddleware middleware (write your own) that will process each request (except for requests to the admin panel)
and save the corresponding values to the database. (process_view method or call method) <br />
Add a ModelAdmin for this model to display the relevant data in the admin. <br />
Try to add some information and functionality to the admin panel for this model (display more fields or display custom
attributes instead of some fields, add search and / or filtering, etc.) <br />

--------

## Launch

* clone current repository
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* Create superuser with 'python manage.py createsuperuser'
* python manage.py runserver
* Go to http://127.0.0.1:8000/forms/person-list/
* Use site logic
* Go to http://127.0.0.1:8000/admin
* Open Logs model and look on created logs

--------

## Realized

Created custom middleware that saves logs into model of all requests on site except admin site requests. <br />
Realised model admin for the Logs model.