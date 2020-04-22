from django import forms
from django.contrib.auth.models import User
from .models import SharesHeld,Shares
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm



class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user



class sharesUpdateForm(forms.Form):
    Name = forms.ModelChoiceField(queryset = Shares.objects.all())
    Price = forms.FloatField()
    Quantity = forms.IntegerField()

    class Meta:
        model = SharesHeld
        fields = ['Name','Price','Quantity']

    def save(self, commit=True):
        sharesHeld = SharesHeld()
        sharesHeld.Name = self.cleaned_data['Name']
        sharesHeld.Price = self.cleaned_data['Price']
        sharesHeld.Quantity = self.cleaned_data['Quantity']

        if commit:
            sharesHeld.save()

        return sharesHeld
class plotCol(forms.Form):
    options = (
        ("Series", "Series"),("Prev Close", "Prev Close"),("Open", "Open"),
        ("High", "High"),("Low", "Low"),
        ("Last", "Last"),("CLose", "Close"),("VWAP", "VWAP"),("Volume", "Volume"),
        ("Turnover", "Turnover"),
        ("Trades", "Trades"),("Deliverable Volume", "Deliverable Volume"),
        ("Deliverble", "%Deliverble"),
    )
    Choice = forms.ChoiceField(choices=options)
    SelectStock = forms.ModelChoiceField(queryset=Shares.objects.all())
    StartDate = forms.DateField(input_formats=['%d/%m/%Y'])
    EndDate = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        fields = ['Choice','SelectStock','StartDate','EndDate']

class getDataSets(forms.Form):
    options = (
        ("1", "Nifty 50"),
        ("2", "Historic DataSet"),
    )
    Choice = forms.ChoiceField(choices=options)
    SelectStock = forms.ModelChoiceField(queryset = Shares.objects.all())
    StartDate = forms.DateField(input_formats=['%d/%m/%Y'])
    EndDate = forms.DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        #model = SharesHeld
        fields = ['Choice','SelectStock','StartDate','EndDate']

