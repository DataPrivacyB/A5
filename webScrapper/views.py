from django.shortcuts import render

def scrape(request):
    return render(request,'webScrapper/scrape.html')

# Create your views here.
