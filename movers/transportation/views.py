from django.shortcuts import render,redirect
from .forms import make_order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import order

# Create your views here.
@login_required
def new_order(request):

    if request.method == 'POST':
        order_form=make_order(request.POST)
        if order_form.is_valid():
            author=request.user
            new=order_form.save(commit=False)
            new.author=author
            new.save()
            messages.success(request, f'Order made successfully. Please wait for approval')
            return redirect('home')
    else:
        order_form=make_order()
    
    return render(request, 'transportation/order.html',{'order_form':order_form})

class OrderListView(ListView):
    model=order
    template_name='transportation/order_list.html'
    context_object_name='order_form'
    ordering=['-date_ordered']
