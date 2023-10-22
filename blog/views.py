from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

#creating update,add & delete blog
from django.views.generic import (
     ListView, 
     DetailView,
     CreateView,
     UpdateView,
     DeleteView
)

#compulsory Login to post new product
from django.contrib.auth.mixins import LoginRequiredMixin

#compulsory only author can update post
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
#dummy data
# posts = [
#      {
#           'author': 'CoreyMS',
#           'title': 'Blog Post 1',
#           'content': 'First Post Content',
#           'date_posted': 'August 27, 2018',
#      },
#       {
#           'author': 'Jane Doe',
#           'title': 'Blog Post 2',
#           'content': 'Second Post Content',
#           'date_posted': 'August 28, 2018',
#      },
# ]

def home(request):
    context = {
         'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


#creating update,add & delete blog
class PostListView(ListView):
     model = Post
     template_name = 'blog/home.html'
     context_object_name = 'posts'
     ordering = ['-date_posted'] #change order of post from lastest to oldest


class PostDetailView(DetailView):
     model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
     model = Post
     fields = ['title', 'content']

     #overiding the author that is making sure the author is automatically the user 

     def form_valid(self, form):
          form.instance.author = self.request.user 
          return super().form_valid(form)
     
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
     model = Post
     fields = ['title', 'content']

     #overiding the author that is making sure the author is automatically the user 

     def form_valid(self, form):
          form.instance.author = self.request.user 
          return super().form_valid(form)
     
     # only author can update blog

     def test_func(self):
          post = self.get_object()
          if self.request.user == post.author:
               return True
          return False
     
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
     model = Post
     success_url = '/'

     #overiding the author that is making sure the author is automatically the user 

     # def form_valid(self, form):
     #      form.instance.author = self.request.user 
     #      return super().form_valid(form)
     
     # only author can delete blog

     def test_func(self):
          post = self.get_object()
          if self.request.user == post.author:
               return True
          return False


def about(request):
     return render(request, 'blog/about.html', {'title': 'About'})


