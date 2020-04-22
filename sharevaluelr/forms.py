from django import forms

from .models import sharevaluecalculate

class ShareValueDetermine(forms.Form):

    Openingvalue=forms.FloatField()
    High=forms.FloatField()
    Low=forms.FloatField()


    class Meta:
        model=sharevaluecalculate
        fields=['Openingvalue', 'High', 'Close']

    def save(self, commit=True):
        shares_value=sharevaluecalculate()
        shares_value.Openingvalue= self.cleaned_data['Openingvalue']
        shares_value.High=self.cleaned_data['High']
        shares_value.Low=self.cleaned_data['Low']
        if commit:
            shares_value.save()

        return shares_value