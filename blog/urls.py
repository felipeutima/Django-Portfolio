from django.urls import path

from portfolio import views
from .views import render_posts,post_detail

urlpatterns = [
    path('', render_posts,name='posts'),
    path('<int:post_id>',post_detail) 
]
