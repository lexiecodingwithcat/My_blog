from django.shortcuts import render
# view is the place to put the "logic" of application
# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})
