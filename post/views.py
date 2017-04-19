from django.shortcuts import render

# Create your views here.
def pos_list(request):
    return render(request, 'post/post.html', {})