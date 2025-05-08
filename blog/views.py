from django.shortcuts import render,redirect
from blog.models import Blog

def category_view(request):
    return render(request,"blog/category.html")
def about_view(request):
    return render(request,"blog/about.html")
def contact_view(request):
    return render(request,"blog/contact.html")
def index_view(request):
    return render(request,"blog/index.html")
def single_post_view(request):
    return render(request,"blog/single-post.html")

# Create your views here.
