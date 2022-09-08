from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
from django.contrib.auth.views import LoginView
# Create your views here.




class HomeView(TemplateView):
    template_name = "home/index.html"






    