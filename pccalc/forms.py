from django import forms


class ZipCodeForm(forms.Form):
    zip_code = forms.IntegerField(label='Zip Code', required="True")

    def clean_zip_code(self):
        data = self.cleaned_data['zip_code']

        # If necessary, zip-codes will be validated and cleaned here.
        # TODO: Determine the necessary zip format for NOAA API.

        return data