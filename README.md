## Django-rest

Design and implemention of Django application with User and ActivityPeriod models, write a custom management command to populate the database with some dummy data, and design an API to serve that data in the JSON format given above.

## Requirements

- Python(3.x/3.8)
- Pycharm IDE community edition
- Django(3.0.7)
- DB Sqlite3 browser
- Postman 


## Installations

- Create a virtual environment venv to install the modules/packages.
- pip install django
- pip install djangorestframework
Refer below screenshot-

![packages](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/packages.jpg)

## Project

### Step-1
Django admin can be used to create the project.
```
command: django-admin startproject restapi
```
This creates restapi folder with files init.py, asgi.py, settings.py, urls.py, wsgi.py, manage.py.<br>
Settings.py is responsibe for new apps configurations/installed apps and DB's used. The file manage.py is used to runserver and create the projects.</br>

To start the development server
```
python  manage.py runserver
```
Now apply migrations for Installed apps in settings.py to create virtual tables in DB's.
```
command: python manage.py migrate
```
Now DB is reflected with tables for modules in settings.py.

### Step-2
Create django app
```
command: python manage.py startapp productapi
```
This creates init.py, admin.py, apps.py, models.py, tests.py, views.py. files under productapi folder.<br>
Provide "productapi" and "rest_framework" in restapi/settings.py in INSTALLED APPS section of code.<br>

### Step-3
Django has ORM(object relational mapping framework) using which we can do CRUD Operations without actually writing DB queries.
Next we are creating a model for our product with class Member and Period and corresponding fields.<br>

Refer below code-
```
from timezone_field import TimeZoneField
from django.db import models

# Create your models here.


class Member (models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    real_name = models.CharField(max_length=60)
    tz = TimeZoneField(default='Europe/London')


class Period (models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

```
 To create DB tables execute below commands-
 ```
 python manage.py makemigrations
 ```
 This creates a migration script 0001_initial.py under productapi.Futher we need to apply this migration script to DB browser to create tables.
 
 Again run the below code-
 ```
  python manage.py migrate
  ```
  
  ### Step-4
  
  We need to create django admin user<br>
  ```
  command: python manage.py createsuperuser
  username: xyz
  Email address: xyz@gmail.com
  password: *********
  superuser created successfully!
  ```
  
  Refer screenshot below-
  ![Runserver](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/runserver.jpg)
  
  Next we need to write code to admin site in admin.py.
  ```
  from django.contrib import admin
from .models import Member
from .models import Period

# Register your models here.

admin.site.register(Member)
admin.site.register(Period)
```

Now dynamically the user can add the fields for classes Member and Period from models.py onto the admin site hosted.<br>
Refresh the database to populate the data entered dynamically on admin site.

Refer below screenshots-

![admin](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/admin.jpg)

![adminmember](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/adminmember.jpg)

![adminperiod](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/adminperiod.jpg)

![adminmemberobject](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/adminmemberobject.jpg)

![adminperiodobject](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/adminperiodobject.jpg)

### Step-5
**Serialization and Deserialization**
Django provides serializers to encode for model classes "Period" & "Member" and  is converted into JSON/XML and this is called as serialization.<br>
Deserialization decodes the JSON into models to serve requests and responses via Postman app.
Now we need to create productapi/serializers.py wherein we create Meta class for models and fields(tuples as attribute). We inherit serializers.ModelSerializer into MemberSerializer and PeriodSerializer classes as below code-
```
from rest_framework import serializers
from .models import Member
from .models import Period

class MemberSerializer ( serializers.ModelSerializer):
    class Meta:
        model= Member
        fields =['id', 'real_name']
class PeriodSerializer ( serializers.ModelSerializer):
    class Meta:
        model= Period
        fields = ['id', 'start', 'end', 'member_id']
 ```
 
### Step-6
We are creating restapi's by class based view in views.py.APIView is by default builtin in django.<br>
Include the below code in productapi/views.py-
```
from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import MemberSerializer
from .serializers import PeriodSerializer
from rest_framework import status


from .models import Member

from .models import Period

# Create your views here.
class MemberListView (APIView):
    def get (self, request):
        Members= Member.objects.all()
        serializer = MemberSerializer(Members, many=True)
        return Response(serializer.data)
    def post(self, request):

        serializer= MemberSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PeriodListView (APIView):
    def get (self, request):
        Periods= Period.objects.all ()
        serializer = PeriodSerializer(Periods, many=True)
        return Response(serializer.data)
    #Deserialization(JSON TO MODEL)
    def post(self, request):

        serializer= PeriodSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

![sqlite](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/db_sqlite3-1.jpg)

![sqlite](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/db_sqlite3.jpg)


Next mapp function to a url by creating productapi/url.py.

```
from django.urls import path
from .views import MemberListView
from .views import PeriodListView




urlpatterns= [

    path("api/Members", MemberListView.as_view()),
    path("api/Periods", PeriodListView.as_view())

]
```
### Step-7
Now we need to include productapi/url.py to restapi/url.py.
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('productapi.urls'))

]
```

### Step-8
We open Postman app and query the DB to get the response. Hit the url at "localhost:8000/api/Members"

![api_Members](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/api_Members.jpg)

![api_periods](https://raw.githubusercontent.com/Pythonbratty/Django-rest/master/Images/api_periods.jpg)


### Contact
- Email: shilpatc25@gmail.com
- Github: https://github.com/ShilpaJagadeeshappa
- LinkedIn: https://www.linkedin.com/in/shilpa-s-j-5b0792130/
- facebook: https://www.facebook.com/shilpasj.25






 
  
  
 


