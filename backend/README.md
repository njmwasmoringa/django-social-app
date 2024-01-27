# Social App Django API
This is the API that powers the social application

## Technologies
- Python 3.10.* ^
- [Django 5.0.1 ^](https://www.djangoproject.com/)
- [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/)
- [Cloudinary](https://cloudinary.com)

## Set Up
- You start by setting up the developer environment through the steps outlined [here](https://github.com/njmwasmoringa/django-social-app)
- Then run the following command that navigates you to the application's Django backend project, installs the Python modules needed to run this application, and start and activates the python virtual environment
```
cd /backend/socialmedia && pipenv install && pipenv shell
```
- Make and run migrations
  ```
  python manage.py makemigrations && python manage.py migrate
  ```
