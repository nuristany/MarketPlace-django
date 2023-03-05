from django.urls import path
from .import views

app_name = 'item'


urlpatterns = [
    path('items/', views.items, name='items'),
    path('newItem/', views.newItem, name='newItem'),
    path('detail/<int:pk>', views.detail, name='detail'),
     
    path('<int:pk>delete/', views.delete, name='delete'),
    path('<int:pk>EditItem/', views.EditItem, name='EditItem'),
    path('myitem/', views.myitem, name='myitem'),
    
]