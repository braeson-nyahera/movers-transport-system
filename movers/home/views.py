from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView

# Create your views here.

def home(request):
    context={
        'posts':Post.objects.all(),
        'title':'home'
    }
    return render(request,'home/home.html', context,)

class PostListView(ListView):
    model=Post
    template_name='home/home.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request_user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request_user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

def landing(request):
    return render(request, 'home/landing.html')

def base(request):
    return render(request, 'home/new.html')

def about(request):
    return render(request,'home/about.html',{'title':'About'})