from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from models import Post

def main(request):
    posts = Post.objects.all()

    template = loader.get_template('main.html')
    context = {
        'lista_posts' : posts
    }
    return HttpResponse(template.render(context, request))

def detalle(request, post_id):
    post = Post.objects.get(pk=post_id)

    template = loader.get_template('detalle.html')
    context = {
        'post' : post
    }
    return HttpResponse(template.render(context, request))
