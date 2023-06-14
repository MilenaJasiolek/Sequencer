from django.shortcuts import render
from .models import *
from .helpers import createPandasTable
import pandas as pd

def home(request):
    return render(request,'home.html')
# create views
def dog(request):
    dogItems = Sequencer.objects.filter(species="dog").values();
    df = createPandasTable(pd.DataFrame(dogItems))
    mydict={
        "df": df.to_html()
    }
    return render(request,'table.html',context=mydict)

def cat(request):
    catItems = Sequencer.objects.filter(species="cat").values()
    df = createPandasTable(pd.DataFrame(catItems))
    mydict={
        "df": df.to_html()
    }
    return render(request,'table.html',context=mydict)


def other(request):
    excluded_species = ['dog', 'cat']
    otherItems = Sequencer.objects.exclude(species__in=excluded_species).values()
    df = createPandasTable(pd.DataFrame(otherItems))
    mydict = {
        "df": df.to_html()
    }
    return render(request,'table.html',context=mydict)

def info(request):
    return render(request, 'info.html')
