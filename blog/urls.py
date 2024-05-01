from django.urls import path
from . import views

urlpatterns = [
    # assigning a view called post_list to the root URL
    path('', views.post_list, name='post_list'),
]