from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Min Suk',
        'title' : "Blog Post 1",
        'content' : "First post content",
        'date_posted' : 'October 17, 2018'
    },
    {
        'author' : 'Jane Doe',
        'title' : "Blog Post 2",
        'content' : "2nd post content",
        'date_posted' : 'October 27, 2018'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

