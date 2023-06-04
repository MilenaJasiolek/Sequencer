from django.shortcuts import render
# from .models import*
# import pandas as pd
# create views
def home(request):
    return render(request,'index.html')