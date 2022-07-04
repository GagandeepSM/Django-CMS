# Ajackus-Django-CMS
 
clone the project

create and start a a virtual environment
```
virtualenv env --no-site-packages
source env/bin/activate
```

Install the project dependencies:
```
pip install -r requirements.txt
python manage.py migrate
```

create admin account
```
python manage.py createsuperuser
python manage.py makemigrations 
python manage.py migrate
```
to start the development server
```
python manage.py runserver
```
