# PR01000
Structure of the source code is as follows. 

BLOG 

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

Starting Django
1. First you need to install Python, Git and a IDE. We used PyCharm, so the steps might differ. 
2. Follow the instructions in the video to access the GitHub https://www.youtube.com/watch?v=mPmmvtYoRyc

TO RUN SERVER 
Type into console
1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver
5. Open in browser http://127.0.0.1:8000/

For testing site please use provided test user accounts. 

User username: test
Admin username: benjamin

Password both: En9m_V3V





