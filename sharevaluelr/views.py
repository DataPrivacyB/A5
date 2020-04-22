from django.shortcuts import render
import gspread
import pandas as pd

from django.shortcuts import render,redirect

from .Valuedetermine import valuedetermine
from .forms import ShareValueDetermine

from .models import sharevaluecalculate




from oauth2client.service_account import ServiceAccountCredentials



from .valuepredictor import calculate_value

# Create your views here.




def sharevaluedetermine(request):


    if request.method == 'POST':
        form= ShareValueDetermine(request.POST)
        if form.is_valid():
            Openingvalue=form.cleaned_data.get('Openingvalue')
            High=form.cleaned_data.get('High')
            Low=form.cleaned_data.get('Low')


            shr= sharevaluecalculate(Openingvalue=Openingvalue, High=High, Low=Low)
            shr.save()

        return redirect('sharevaluedetermine')

    else:
        form = ShareValueDetermine()






    value_input=sharevaluecalculate.objects.all()
    for value_input1 in value_input:
        value1=value_input1.Openingvalue
        value2=value_input1.High
        value3=value_input1.Low
        value_calculated = calculate_value(value1, value2, value3)














    context={
        'value_calculated' : value_calculated,
        'form': form
    }






    return render(request, 'sharevaluelr/sharevaluedetermine.html', context)