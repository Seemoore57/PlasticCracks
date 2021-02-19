from django import forms

class BogueCalculator(forms.Form):
    lime = forms.FloatField(min_value=0, max_value=100)
    silica = forms.FloatField(min_value=0, max_value=100)
    alumina = forms.FloatField(min_value=0, max_value=100)
    rust = forms.FloatField(min_value=0, max_value=100)

class CompareForm(forms.Form):
    lime = forms.FloatField(min_value=0, max_value=100)
    silica = forms.FloatField(min_value=0, max_value=100)
    alumina = forms.FloatField(min_value=0, max_value=100)
    rust = forms.FloatField(min_value=0, max_value=100)
    oldLime = forms.FloatField(min_value=0, max_value=100)
    oldSilica = forms.FloatField(min_value=0, max_value=100)
    oldAlumina = forms.FloatField(min_value=0, max_value=100)
    oldRust = forms.FloatField(min_value=0, max_value=100)
