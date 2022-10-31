# hillel_hw_10
## Description
Create a new model with multiple fields. Create a share and migrate. <br />
Human <br />
name_name - charfield <br />
last_name - charfield <br />
email - email field <br />

Create modelform, view, template for - creating a new entry, and for editing an existing entry.<br />
/person - GET - get the form<br />
/person - POST - confirm and save the new Person object in the database<br />
/person/<id:int> - GET - get the form with Person data, or 404 if there is no user with this id<br />
/person/<id:int> - POST - updating Person data, or 404

--------

## Launch
* clone current repository
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver
* Go to http://127.0.0.1:8000/forms/person-list/
* Test create/update person logic

--------

## Realized

Wrote code of create and update person data with POST/GET requests. 
Code created in the 'forms' app.