# PR01000
Structure of the source code is as follows. 

BLOG // This is the main app where most of our code is made

-admin.py // here we configure the Django admin site on how it will filter and search diffrents class models from models.py
-models.py // here we display the fields we want the user to type inn or auto added to the new object. 
-urls.py // here we redirect the user to right html file based on urls slug
-views.py // simple render request functions for returing the right html site



MYSITE

- settings.py // where we inclued all the innstalled apps like bootstrap 4 and the blog site "app". We also set the static files location and upload path here. 
- urls.py // when Django is started, it will look here first to where it can redirect the path. Example "127.0.0.1:8000/" will redirect to the blog.urls file

STATIC 

// all css, javascript and pictures is stored here.

MEDIA

- Documents // where all the uploaded files will be stored, the database will have a referenece to this file

TEMPLATES

// all the different html files are stored here. 

For testing site please user provided test user account. 
User: test
Password: En9m_V3V





