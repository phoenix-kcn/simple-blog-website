from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'home.html', {'posts': posts})

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'post_detail.html', {'post': post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'