from django.shortcuts import render
from django.http import HttpResponse
data = "Hello Akshay"

def forgotPass(request):
    context = {
        'data' : data,
        'title' : 'Reset Password'
    }
    return render(request,'forgotPass/resetPassword.html',context)