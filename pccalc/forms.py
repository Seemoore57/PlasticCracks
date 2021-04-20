from django import forms


class PlasticCracksForm(forms.Form):
    zip_code = forms.IntegerField(label='Zip Code', required="True")
    concrete_temperature = forms.IntegerField(label='Concrete Temperature', required="True")

    def clean_zip_code(self):
        data = self.cleaned_data['zip_code']

        # If necessary, zip-codes will be validated and cleaned here.
        # TODO: Determine the necessary zip format for NOAA API.

        return data

    def clean_concrete_temperature(self):
        data = self.cleaned_data['concrete_temperature']

        return data
