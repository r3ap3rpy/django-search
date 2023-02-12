### Welcome

This repository holds demo code for implmenting search bar in django.

Please follow these steps to reproduce and use.

``` bash
git clone https://github.com/r3ap3rpy/django-search.git
virtualenv djangoinv
djangoinv\Scripts\activate.bat
pip install django
cd django-search
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
```

Add some products manually, then you can search by name and description.