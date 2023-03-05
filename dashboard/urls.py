from django.urls import path
from . import views

app_name = 'dashboard'


urlpatterns = [
    path('dash/', views.dash, name="dash")
]