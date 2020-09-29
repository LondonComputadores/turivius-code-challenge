                    
                    # Turivius-Code-Challenge

This is a code challenge as part of the Turivius recruitment process

How it's being built:

- $ mkdir <project_name>
- $ cd <project-name>
- $ python3 -m venv <venv_name>
- $ source <venv_name>/bin/activate
- $ pip install django
- $ django-admin startproject <project_name>
- $ python manager.py runserver
- $ pytho manage.py startapp <app_name>
- Create the models
- Registered the models
- Created super user
- $ pip install djangorestframework
- Created serializers module
- Created views/ViewSet
- Configured urls


# Endpoints for GET, POST, PUT and DELETE:

- /lawsuits
- /lawsuits/id
- /admin
- /admin/court_app/lawsuit/


# References:

- https://www.djangoproject.com/
- https://www.django-rest-framework.org/tutorial/quickstart/#serializers
- https://www.youtube.com/watch?v=BKChTO8GADk
- https://docs.djangoproject.com/en/3.0/howto/initial-data/#providing-data-with-fixtures
- https://docs.djangoproject.com/en/3.0/topics/serialization/
- https://code.djangoproject.com/wiki/Fixtures
- https://forum.djangoproject.com/t/getting-a-deserializationerror-when-trying-to-load-data-from-json-to-db/2713
- https://stackoverflow.com/questions/54617353/django-deserialization-error-problem-installing-fixture
- https://medium.com/@beatrizuezu/visualizando-query-sql-a-partir-do-orm-django-5771370a9c55
- https://github.com/beatrizuezu/de-sql-para-orm-django/tree/master/core/categorias
- https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/