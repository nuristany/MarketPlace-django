from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from item.models import Category, Item
from .forms import SignUpForm

# Create your views here.


def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User not exist')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect('core:home')
        
        else:
            messages.error(request, 'user or pass not exists')
            
    
    context = {
        
    }
    
    return render(request, 'core/login.html', context)


def logoutUser(request):
    logout(request)
    
    return redirect('core:home')
    
    


def home(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'items':items,
        'categories':categories
    }
    return render(request, 'core/home.html',context)





def contact(request):
    return render(request, 'core/contact.html', )

def signUp(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('core:loginPage')
    
    else:
    
        form = SignUpForm()
        
        
    context = {
        'form':form
    }
    return render(request, 'core/signup.html', context)



def profile(request):
    items = Item.objects.filter(created_by= request.user)
    # item_time = Item.objects.all(Item,  created_at = request.user)
    
   
    context = {
        'items':items,
        # 'item_time':item_time
        
        
    }
    return render(request, 'core/profile.html', context)



        
    
    
    