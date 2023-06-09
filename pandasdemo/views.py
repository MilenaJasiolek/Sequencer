from django.shortcuts import render
from .models import *
from .helpers import createPandasTable
import pandas as pd

def home(request):
    return render(request,'home.html')
# create views
def dog(request):
    dogItems = Sequencer.objects.filter(species="dog").values()
    df = createPandasTable(pd.DataFrame(dogItems))
    mydict={
    "df":df.to_html()
    }
    return render(request,'table.html',context=mydict)

def cat(request):
    catItems = Sequencer.objects.filter(species="cat").values()
    df = createPandasTable(pd.DataFrame(catItems))
    mydict={
    "df":df.to_html()
    }
    return render(request,'table.html',context=mydict)


def other(request):
    otherItems = Sequencer.objects.all().values()
    df = createPandasTable(pd.DataFrame(otherItems))

    mydict = {
        "df": df.to_html()
    }
    return render(request,'table.html',context=mydict)