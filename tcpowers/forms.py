from django import forms

class TCPowersCalc(forms.Form):
    WCRatio = forms.FloatField(min_value=0, max_value=1)
    DegOfHydra = forms.FloatField(min_value=0, max_value=1)