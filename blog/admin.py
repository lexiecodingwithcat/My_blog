#To add, edit and delete the posts we've just modeled, we will use Django admin.
from django.contrib import admin
from .models import Post
# Register your models here.
#import the post model and to make it visible on the admin page
admin.site.register(Post)