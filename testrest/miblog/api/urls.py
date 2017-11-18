from django.conf.urls import url , include
from rest_framework import routers
from .views import PostViewSet , UsuarioViewSet

router = routers.DefaultRouter()
router.register( r'posts' , PostViewSet );
router.register( r'usuarios' , UsuarioViewSet );

urlpatterns = [
	url ( r'^' , include ( router.urls )),
	url ( r'^api-auth/' , include ( 'rest_framework.urls' , namespace = 'rest_framework' ))
]