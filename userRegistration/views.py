from django.shortcuts import render, redirect
from userRegistration.forms import RegistrationForm
from .forms import sharesUpdateForm
import pandas as pd
from userRegistration.liveShares import liveShare
from .models import Shares
from .models import SharesHeld
import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib import messages


def Home(request):
    return render(request,'userRegistration/Home.html')

def AboutProject(request):
    return render(request,'userRegistration/AboutProject.html')


def index(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userRegistration/registered')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'userRegistration/index.html', args)

def registered(request):
    return render(request, 'userRegistration/registered.html')


def profile(request):
    return render(request,'userRegistration/profile.html')

def about(request):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'C:\\Users\\Akshay Bali\\Desktop\\A5\\userRegistration\\FinanceA5-4cec9ccde82f.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('A5_Finance').sheet1

    niftyData = sheet.get_all_values()
    headers = niftyData.pop(0)

    df = pd.DataFrame(niftyData, columns=headers)
    print(headers)
    context ={
        'headers' : headers,
        'data' : df.iloc[0:].to_html(classes="table-bordered table-hover table-wrapper-scroll-y my-custom-scrollbar")
    }
    return render(request,'userRegistration/about.html',context)

def portfolio(request):

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'C:\\Users\\Akshay Bali\\Desktop\\A5\\userRegistration\\FinanceA5-4cec9ccde82f.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('A5_Finance').sheet1

    if request.method == 'POST':
        form = sharesUpdateForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data.get('Name')
            Quantity = form.cleaned_data.get('Quantity')
            Price = form.cleaned_data.get('Price')
            s = SharesHeld.objects.filter(Name = Name)
            if s and "buy" in request.POST:
                print(s)
                s = SharesHeld.objects.get(Name = Name)
                s.Quantity += Quantity
                s.save()
            elif s and "sell" in request.POST:
                s = SharesHeld.objects.get(Name=Name)
                if s.Quantity - Quantity >= 0:
                    s.Quantity -= Quantity
                    s.save()
                else :
                    messages.success(request, 'Not Enougn Shares!')
            elif not s and "buy" in request.POST:
                s = SharesHeld(Name = Name,Quantity =Quantity,Price=Price)
                s.save()
                print("yess")
            else:
                messages.success(request,'You do not have the share in your PortFolio!')
            return redirect('portfolio')
    else:
        form = sharesUpdateForm()




    niftyData = sheet.get_all_values()
    headers = niftyData.pop(0)
    df = pd.DataFrame(niftyData, columns=headers)
    shares = SharesHeld.objects.all()
    name = "WIPRO"
    items = []
    netProfitLoss = 0
    investment = 0
    current = 0
    avg = 0
    for share in shares:
        shareData = df.query("TICKER == '{0}'".format(share.Name))
        print("LTP : ", shareData.iloc[0]['LTP'])
        s = liveShare(share.Name,share.Quantity,
                          float(shareData.iloc[0]['LTP']),
                           share.Price)
        netProfitLoss += s.pl
        investment += s.investment
        current += s.liveValue
        items.append(s)

    context = {
        'data': items,
        'form' : form,
        'netPl' : netProfitLoss,
        'current' : current,
        'invest' : investment
    }
    return render(request,'userRegistration/portfolio.html',context)