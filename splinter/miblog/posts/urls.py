from django.conf.urls import url
from . import views

urlpatterns = [
    # x: /posts/
    url(r'^$', views.main, name='main'),
    # x: /posts/detalle/1
    url(r'^detalle/(?P<post_id>[0-9]+)$', views.detalle, name='detalle'),
]
