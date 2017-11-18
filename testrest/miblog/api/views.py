from rest_framework import viewsets
from .serializers import PostSerializer, UsuarioSerializer
from posts.models import Post, Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
	"""
	API que permite un usuario ser visualizado y editado
	"""
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

class PostViewSet(viewsets.ModelViewSet):
	"""
	API que permite un post ser visualizado y editado
	"""
	queryset = Post.objects.all()
	serializer_class = PostSerializer