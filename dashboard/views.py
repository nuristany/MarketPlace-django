from django.contrib.auth.decorators import login_required
   
from django.shortcuts import render
from item.models import Item

# Create your views here.

def dash(request):
    items = Item.objects.filter(created_by= request.user)
    
    context = {
        'items':items
    }
    return render(request, 'dashboard/dashboard.html', context )

