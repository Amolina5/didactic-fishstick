from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def index(request):
    return render(request, 'pages/home.html')

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', home, name='home'),
#    path('about/', about, name='about'),
#]