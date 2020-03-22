from django.shortcuts import render, redirect
from userRegistration.forms import RegistrationForm
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