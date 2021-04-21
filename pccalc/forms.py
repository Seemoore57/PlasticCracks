from django import forms


class PlasticCracksForm(forms.Form):
    zip_code = forms.IntegerField(label='Zip Code', required="True")
    concrete_temperature = forms.IntegerField(label='Concrete Temperature', required="True")
