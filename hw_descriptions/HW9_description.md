# hillel_hw_9
## Description
Add a view along the /triangle path
On this view, you need to use a shape that will take the values ​​of the two legs of the triangle (positive, greater than zero, for simplicity, use int values ​​if you want). After submitting the form, if the values ​​were valid, display the value of the hypotenuse on the same page.

It should be one view
You can use 1 or 2 templates as needed to render the form and result.
If one template - the default hypotenuse value is None - check it in the template, and based on whether it's None or "value" render the hypotenuse shape or value
--------

## Launch
* clone current repository
* pip install -r requirements.txt
* python manage.py runserver
* Go to http://127.0.0.1:8000/forms/triangle/
* Test triangle logic

--------

## Realized

Created app 'forms' which uses Django forms to get user input of triangle legs and calculates triangle's hypotenuse