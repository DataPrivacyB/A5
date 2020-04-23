# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import admin
from pred_app.lstm_prediction import *


# --------------- MAIN WEB PAGES -----------------------------
def redirect_root(request):
    return redirect('/pred_app/index')


def index(request):
	return render(request, 'pred_app/index.html')


def clustering(request):
	return render(request, 'portfolioOptimization/clustering.html')

def scrape(request):
	return render(request, 'webScrapper/scrape.html')

def sharevaluedetermine(request):
	return render(request, 'webScrapper/sharevaluedetermine.html')

def prediction(request):
    return render(request, 'pred_app/prediction.html')


def home(request):
	return render(request, 'pred_app/home.html')


def about(request):
	return render(request, 'userRegistration/about.html')

def logout(request):
	return render(request, 'userRegistration/logout.html')


def portfolio(request):
	return render(request, 'pred_app/portfolio.html')


def index(request):
	return render(request, 'pred_app/index.html')


def lstm_prediction(request):
	return render(request, 'pred_app/lstm_prediction.html')


def profile(request):
	return render(request, 'pred_app/profile.html')



def search(request, se, stock_symbol):
	import json
	predicted_result_df = ltm_prediction(se, stock_symbol)
	return render(request, 'pred_app/search.html', {"predicted_result_df": predicted_result_df})
# -----------------------------------------------------------