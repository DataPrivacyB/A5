from django.shortcuts import render, redirect
from userRegistration.forms import RegistrationForm
from .forms import sharesUpdateForm,getDataSets,plotCol
import pandas as pd
from userRegistration.liveShares import liveShare
from .models import SharesHeld,Shares
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib import messages
import pandas_datareader.data as web
import datetime as dt
from nsepy import get_history

pd.set_option('display.max_columns', None)
def Home(request):
    return render(request,'userRegistration/home.html')


def AboutProject(request):
    return render(request,'userRegistration/p.html')


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

def practice(request):
    return render(request,'userRegistration/p.html')


def about(request):

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'C:\\Users\\Akshay Bali\\Desktop\\A5\\userRegistration\\FinanceA5-4cec9ccde82f.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('A5_Finance').sheet1
    chartData = []
    niftyData = ""
    headers = ""
    df = pd.DataFrame()
    print(headers)
    Name ="Nifty 50"
    labels = [0,1,2]
    if request.method == 'POST' and 'view' in request.POST:
        form = getDataSets(request.POST)
        if form.is_valid():
            Choice = form.cleaned_data.get('Choice')
            print('Choice :',Choice)
            if Choice == '1' :
                niftyData = sheet.get_all_values()
                headers = niftyData.pop(0)
                print(headers)
                df = pd.DataFrame(niftyData, columns=headers)
                df.to_csv("C:\\Users\\Akshay Bali\\Desktop\\A5Pull\\userRegistration\\datasets\\temp1.csv")
                graphForm = plotCol()
            else :
                Name = form.cleaned_data.get('SelectStock')
                Name = str(Name)
                print(Name)
                startDate = form.cleaned_data.get('StartDate')
                EndDate = form.cleaned_data.get('EndDate')
                df = get_history(symbol = Name,start=startDate,end=EndDate)
                df['Close'].values.tolist()
                chartData = df['Close'].values.tolist()
                labels = list(range(0, len(chartData)))
                #pd.date_range(startDate, EndDate).tolist()
                print(labels)
                graphForm = plotCol()

    elif request.method == 'POST' and 'plot' in request.POST:
        graphForm = plotCol(request.POST)

        if graphForm.is_valid():
            Choice = graphForm.cleaned_data.get('Choice')
            Name = graphForm.cleaned_data.get('SelectStock')
            Name = str(Name)
            startDate = graphForm.cleaned_data.get('StartDate')
            EndDate = graphForm.cleaned_data.get('EndDate')
            df = get_history(symbol=Name, start=startDate, end=EndDate)
            chartData = df[Choice].values.tolist()
            df.to_csv("C:\\Users\\Akshay Bali\\Desktop\\A5Pull\\userRegistration\\datasets\\temp.csv")
            prac = pd.read_csv("C:\\Users\\Akshay Bali\\Desktop\\A5Pull\\userRegistration\\datasets\\temp.csv")
            labels = prac['Date'].values.tolist()
            print("chartData :",chartData)
            #labels = list(range(0,len(chartData)))
            print("label leng:",len(labels))
            # print(chartData)
            print(labels)
            form = getDataSets()

    else:
        form = getDataSets()
        graphForm = plotCol()
        print(dt.datetime(2019, 2, 14))
    x = "Choice"
    context ={
        'form' : form,
        'graphForm' : graphForm,
        'head': Name,
        'labels': labels,
        'chartData': chartData,
        'data' : df.iloc[0:].to_html(classes="table-borderles table-hover table-wrapper-scroll-y my-custom-scrollbar")
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