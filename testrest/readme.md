 * Configurar venv
```
py -m venv venv
venv\Scripts\activate
```
* Instalar dependencias
```
py -m pip install -r requirements.txt
```
* Configurar proyecto
```
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```
 * Usar:
   * user: admin
   * pass: admin12345

* Crear un nuevo app
```
py manage.py startapp api
```

* Test
```
py manage.py test
```

* Referencias
 * https://realpython.com/blog/python/test-driven-development-of-a-django-restful-api/
 * http://www.django-rest-framework.org/api-guide/testing/#rendering-responses
 * https://docs.djangoproject.com/en/1.11/topics/testing/overview/
 * Otros
  * https://github.com/encode/django-rest-framework/blob/master/rest_framework/viewsets.py#L69
  * https://stackoverflow.com/questions/23072730/django-rest-framework-how-to-test-viewset
  * https://www.programcreek.com/python/example/81342/rest_framework.test.APIRequestFactory