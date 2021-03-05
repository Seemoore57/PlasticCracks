from django import forms

class ZipCodeForm(forms.Form):
    zip_code = forms.IntegerField(help_text='Enter your Zip Code', max_length = 5,  required="True")

    def clean_zip_code(self):
        data = self.cleaned_data['zip_code']

        # If necessary, zip-codes will be validated and cleaned here.
        # TODO: Determine the necessary zip format for NOAA API.

        return data