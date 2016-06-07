# coding:utf-8
# author： ou
from django.shortcuts import render

# Create your views here.
def index(request):
        return render(request, "blogapp/test.html")
def hello(request):
        return render(request, "blogapp/index.html")