from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='starting_page'),
    path('posts', views.posts, name="post_page"),
    path('posts/<slug:slug>', views.single_post, name="post_details_page")
]