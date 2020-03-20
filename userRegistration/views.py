from django.shortcuts import render
data = "Hello Akshay"

def forgotPass(request):
    context = {
        'data' : data,
        'title' : 'Reset Password'
    }
    return render(request,'userRegistration/resetPassword.html',context)