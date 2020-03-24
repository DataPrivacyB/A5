from django.shortcuts import render, redirect
from userRegistration.forms import RegistrationForm
from .forms import sharesUpdateForm
import gspread
import pprint
from .models import Shares
from oauth2client.service_account import ServiceAccountCredentials

from django.views.generic import CreateView
from .models import SharesHeld
from django.urls import reverse
# Create your views here.



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

    niftyData = sheet.get_all_records()

    pp = pprint.PrettyPrinter()
    for data in niftyData:
        print(data['TICKER'])
        s = Shares(Name=data['TICKER'])
        s.save()
    return render(request,'userRegistration/about.html')

def portfolio(request):
    print("Hello")
    if request.method == 'POST':# and "buy" in request.POST:
        form = sharesUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            Name = form.cleaned_data.get('Name')
            return redirect('about')
    else:
        form = sharesUpdateForm()
    data = [1, 3, 3]
    context = {
        'data': data,
        'form' : form,
        #'Name' : Name
    }
    return render(request,'userRegistration/portfolio.html',context)