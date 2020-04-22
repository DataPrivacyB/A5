from django import forms
from django.contrib.auth.models import User
from .models import SharesType
from django.contrib.auth.forms import UserCreationForm

class typ1(forms.Form):
    SelectStock = forms.ModelChoiceField(queryset = SharesType.objects.all())

    def __init__(self, *args, **kwargs):
        cluster = kwargs.pop('cluster', None)
        super(typ1, self).__init__(*args, **kwargs)

        if cluster:
            self.fields['SelectStock'].queryset = SharesType.objects.filter(Type=cluster)


class typ2(forms.Form):
    SelectStock = forms.ModelChoiceField(queryset = SharesType.objects.filter(Type=2))

    def __init__(self, *args, **kwargs):
        cluster = kwargs.pop('cluster', None)
        super(typ2, self).__init__(*args, **kwargs)

        if cluster:
            self.fields['SelectStock'].queryset = SharesType.objects.filter(Type=cluster)


class typ3(forms.Form):
    SelectStock = forms.ModelChoiceField(queryset = SharesType.objects.filter(Type=3))
    def __init__(self, *args, **kwargs):
        cluster = kwargs.pop('cluster', None)
        super(typ3, self).__init__(*args, **kwargs)

        if cluster:
            self.fields['SelectStock'].queryset = SharesType.objects.filter(Type=cluster)

class typ4(forms.Form):
    SelectStock = forms.ModelChoiceField(queryset = SharesType.objects.filter(Type=4))
    def __init__(self, *args, **kwargs):
        cluster = kwargs.pop('cluster', None)
        super(typ4, self).__init__(*args, **kwargs)

        if cluster:
            self.fields['SelectStock'].queryset = SharesType.objects.filter(Type=cluster)
