from django.shortcuts import render
# from .models import*
# import pandas as pd
#create views
def home(request):
    # item=Student.objects.all().values()
    # df=pd.DataFrame(item)
    # mydict={
    #     "df":df.to_html()
    # }
    return render(request, 'index.html')