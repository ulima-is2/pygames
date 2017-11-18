from posts.models import Usuario, Post
from rest_framework import serializers

class UsuarioSerializer(serializers.HyperlinkedModelSerializer ):
	class Meta:
		model = Usuario
		fields = ('usuario', 'nombre')
		
class PostSerializer(serializers.HyperlinkedModelSerializer ):
	usuario_pub = serializers.SlugRelatedField (queryset=Usuario.objects.all(), slug_field="nombre")
	class Meta:
		model = Post
		fields = ('titulo', 'contenido', 'fecha_pub', 'usuario_pub', 'categoria')