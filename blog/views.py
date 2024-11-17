from django.shortcuts import render
from datetime import date
from django.urls import reverse

all_posts = [
    {
        'slug': 'learning-django',
        'title': 'Django Course',
        'author': 'Ibrahim Sadiqi',
        'image': 'django.png',
        'date': date(2024,11,17),
        'short_description': 'This is django course from beginner to advance',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias assumenda at atque consequatur
        doloremque dolores doloribus, eaque esse excepturi facilis fugiat itaque laboriosam laudantium
        magnam natus nobis optio possimus praesentium quod rem repellat sapiente sequi sit sunt suscipit
        vitae voluptatum.
        """
    },
    {
        'slug': 'learning-python',
        'title': 'Python Course',
        'author': 'Ibrahim Sadiqi',
        'image': 'python.png',
        'date': date(2024,11,17),
        'short_description': 'This is python course from beginner to advance',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias assumenda at atque consequatur
        doloremque dolores doloribus, eaque esse excepturi facilis fugiat itaque laboriosam laudantium
        magnam natus nobis optio possimus praesentium quod rem repellat sapiente sequi sit sunt suscipit
        vitae voluptatum.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias assumenda at atque consequatur
        doloremque dolores doloribus, eaque esse excepturi facilis fugiat itaque laboriosam laudantium
        magnam natus nobis optio possimus praesentium quod rem repellat sapiente sequi sit sunt suscipit
        vitae voluptatum.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias assumenda at atque consequatur
        doloremque dolores doloribus, eaque esse excepturi facilis fugiat itaque laboriosam laudantium
        magnam natus nobis optio possimus praesentium quod rem repellat sapiente sequi sit sunt suscipit
        vitae voluptatum.
        """
    },
    {
        'slug': 'ml-learning',
        'title': 'Machine Learning Course',
        'author': 'Ibrahim Sadiqi',
        'image': 'ml.png',
        'date': date(2024,11,17),
        'short_description': 'This is machine learning course from beginner to advance',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias assumenda at atque consequatur
        doloremque dolores doloribus, eaque esse excepturi facilis fugiat itaque laboriosam laudantium
        magnam natus nobis optio possimus praesentium quod rem repellat sapiente sequi sit sunt suscipit
        vitae voluptatum.
        """
    }
]


def get_date(post):
    return post['date']


def index(request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_posts = sorted_post[-2:]
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts(request):
    context = {
        'posts': all_posts
    }
    return render(request, 'blog/all_posts.html', context)


def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {'post': post})
