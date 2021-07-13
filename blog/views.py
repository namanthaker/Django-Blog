from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5 

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    

class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True        

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    

class PostCretaeView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']   

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True if post.author == self.request.user else False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True if post.author == self.request.user else False
    

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False       
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False       
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def about(request):
    return render(request, 'blog/about.html')