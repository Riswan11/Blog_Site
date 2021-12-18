from django.shortcuts import render


posts = [
    {
        'author': 'RiswanA',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2021'
    },
    {
        'author': 'Bernard Wesley',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 30, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
