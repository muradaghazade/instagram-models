from django.shortcuts import render
from core.models import Post

def mainpage(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'insta.html', context)