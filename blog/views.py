from django.shortcuts import render

posts = [
    {
        'author' : 'Ironman',
        'title' : 'First blog',
        'content' : 'Blog content',
        'date_posted' : 'Aug 24'
    },
    {
        'author' : 'Batman',
        'title' : 'Second blog',
        'content' : 'Blog 2 content',
        'date_posted' : 'Sep 24'
    },
    {
        'author' : 'spiderman',
        'title' : 'Third blog',
        'content' : 'Blog 3 content',
        'date_posted' : 'Oct 24'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title' : 'About'
    }
    return render(request, 'blog/about.html', context)