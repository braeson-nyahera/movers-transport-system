from typing import Any
from django.shortcuts import render
from .models import Post
from transportation.models import order
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView, TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name='home/home.html'
    #ordering=['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts']=Post.objects.all()
        context['complete_orders']=order.objects.filter(status='completed')
        context['in_transit_orders']=order.objects.filter(status='in-transit')
        context['pending_approval_orders']=order.objects.filter(status='pending approval')
        return context

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