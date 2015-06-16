from django.shortcuts import render
from django.views import generic

from .models import Post, Category

class PostDetailView(generic.DetailView):
    model = Post

class PostListView(generic.ListView):
    def get_queryset(self):
        return Post.objects.filter(category__slug = self.kwargs['slug'])
    
class CategoryView(generic.ListView):
    model = Category