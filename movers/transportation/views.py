from django.shortcuts import render,redirect
from .forms import make_order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import order
import folium, geocoder

# Create your views here.
@login_required
def new_order(request):
    address='nairobi'
    if request.method == 'POST':
        order_form=make_order(request.POST)
        #Create map object
        # location=geocoder.osm(address)
        # lat=location.lat
        # lng=location.lng
        #country=location.country

        # m = folium.Map(location=[12,-19],zoom_start=8)

        # folium.Marker([lat,lng], tooltip=address).add_to(m)
        
        # m = m._repr_html_()

        if order_form.is_valid():
            author=request.user
            new=order_form.save(commit=False)
            new.author=author
            new.save()
            messages.success(request, f'Order made successfully. Please wait for approval')
            return redirect('orders_list')
    else:
        # location=geocoder.osm(address)
        # lat=location.lat
        # lng=location.lng
        # #country=location.country

        # m = folium.Map(location=[12,-19],zoom_start=6)

        # folium.Marker([lat,lng], tooltip=address).add_to(m)
        
        # m = m._repr_html_()
        
        order_form=make_order()
        
    
    return render(request, 'transportation/make_order.html',{'order_form':order_form})

class OrderListView(LoginRequiredMixin,ListView):
    model=order
    template_name='transportation/order_list.html'
    context_object_name='order_form'
    ordering=['-date_ordered']

class OrderDetailView(DetailView):
    model=order