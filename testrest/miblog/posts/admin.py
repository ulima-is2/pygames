from django.contrib import admin

from posts.models import Post, Usuario
admin.site.register(Usuario)
admin.site.register(Post)
