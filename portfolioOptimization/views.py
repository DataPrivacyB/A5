from django.shortcuts import render, redirect
from django.template.defaulttags import register
import pandas as pd
from .cluster1 import *
from django.template import RequestContext
from .models import SharesType,Portfolio
from .forms import typ4,typ1,typ2,typ3
from .omtimization import Optimize
from django import forms
@register.filter
def get(dictionary, key):
    return dictionary.get(key)

def p(request):
    return render(request,'portfolioOptimization/p.html')

def optimize(request):
    Portfolio.objects.all().delete()
    return render(request,'portfolioOptimization/clustering.html')

def roundingVals_toTwoDeci(y):
    print("y =",y)
    for d in y:
        print("d=",d)
        v = (round(y[d], 2))
        y[d] = v * 100
    print(y)
    return y

def result(request):
    @register.filter
    def get(dictionary, key):
        return dictionary.get(key)

    portfolio = Portfolio.objects.all()
    p = []
    for port in list(portfolio):
        p.append(str(port))
    print("opt")
    res = Optimize(p)

    type1 = SharesType.objects.filter(Type=1)
    type2 = SharesType.objects.filter(Type=2)
    type3 = SharesType.objects.filter(Type=3)
    type4 = SharesType.objects.filter(Type=4)
    form1 = typ1(cluster=1)
    form2 = typ2(cluster=2)
    form3 = typ3(cluster=3)
    form4 = typ4(cluster=4)
    context = {
        'type1': type1,
        'type2': type2,
        'type3': type3,
        'type4': type4,
        'typ1': form1,
        'typ2': form2,
        'typ3': form3,
        'typ4': form4,
        'portfolio': portfolio,
        'r1':round(res[0].ret,2)*100,
        'v1':round(res[0].stdev,2)*100,
        'r2':res[2].ret,
        'v2': res[2].stdev,
        'companies1':roundingVals_toTwoDeci(res[1]),
        'companies2': roundingVals_toTwoDeci(res[3]),
        'res0':res[0],
        'res1':res[1],
        'i':len(res[3])
    }
    return render(request, 'portfolioOptimization/clustering.html', context)

def suggest(request):
    print("hello")
    if request.method == 'POST':
        if 'cluster1' in request.POST:
            form = typ1(request.POST)
        elif 'cluster2' in request.POST:
            form = typ1(request.POST)
        elif 'cluster3' in request.POST:
            form = typ1(request.POST)
        elif 'cluster4' in request.POST:
            form = typ1(request.POST)

        if form.is_valid():
            Choice = form.cleaned_data.get('SelectStock')
            print('Choice :',Choice)
            if len(Portfolio.objects.filter(Share=Choice))==0:
                p = Portfolio(Share=Choice)
                p.save()
        type1 = SharesType.objects.filter(Type=1)
        type2 = SharesType.objects.filter(Type=2)
        type3 = SharesType.objects.filter(Type=3)
        type4 = SharesType.objects.filter(Type=4)
        portfolio = Portfolio.objects.all()

    else:
        SharesType.objects.all().delete()
        portfolio = Portfolio.objects.all()

        type1 = []
        type2 = []
        type3 = []
        type4 = []

        dfDict = getClusters()
        for key in dfDict:
            if dfDict[key] == 0:
                type1.append(key)
                if len(SharesType.objects.filter(Name=key)) == 0:
                    print("adding")
                    s = SharesType(Name=key, Type=1)
                    s.save()
            elif dfDict[key] == 1:
                type2.append(key)
                if len(SharesType.objects.filter(Name=key)) == 0:
                    s = SharesType(Name=key, Type=2)
                    s.save()
            elif dfDict[key] == 2:
                type3.append(key)
                print(SharesType.objects.filter(Name=key))
                if len(SharesType.objects.filter(Name=key))==0:
                    s = SharesType(Name=key, Type=3)
                    s.save()
            elif dfDict[key] == 3:
                type4.append(key)
                if len(SharesType.objects.filter(Name=key)) == 0:
                    s = SharesType(Name=key, Type=4)
                    s.save()
    # print("ekde bagh",SharesType.objects.filter(Type=4))
    # print("ekde bagh", SharesType.objects.all())
    # companies = df["companies"].values.tolist()
    # labels = df["labels"].values.tolist()
    print("ran")
    form1 = typ1(cluster=1)
    form2 = typ2(cluster=2)
    form3 = typ3(cluster=3)
    form4 = typ4(cluster=4)
    context ={
        'type1': type1,
        'type2': type2,
        'type3': type3,
        'type4': type4,
        'typ1':form1,
        'typ2': form2,
        'typ3': form3,
        'typ4': form4,
        'portfolio':portfolio
    }
    return render(request, 'portfolioOptimization/clustering.html',context)