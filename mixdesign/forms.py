from django import forms

unit_choices = (
    ("meters", "M"),
    ("ft", "FT"),

)
class MixDesignCalculator(forms.Form):
    Cement = forms.FloatField(min_value=0, max_value=10000)
    Fly_Ash = forms.FloatField(min_value=0, max_value=10000)
    Slag = forms.FloatField(min_value=0, max_value=10000)
    Water = forms.FloatField(min_value=0, max_value=10000)
    Fine_Aggregates = forms.FloatField(min_value=0, max_value=10000)
    Coarse_Aggregates = forms.FloatField(min_value=0, max_value=10000)
    Air_Entrained = forms.BooleanField(required=False)
    WC_Ratio = forms.FloatField(min_value=0, max_value=10000)
    Fly_Ash_SG = forms.FloatField(min_value=0, max_value=10000)
    Slag_SG = forms.FloatField(min_value=0, max_value=10000)
    Fine_Aggregates_SG = forms.FloatField(min_value=0, max_value=10000)
    Coarse_Aggregates_SG = forms.FloatField(min_value=0, max_value=10000)
    Slump_Test = forms.BooleanField(required=False)
    Air_Test = forms.BooleanField(required=False)
    Formwork_Volume = forms.FloatField(min_value=0, max_value=10000)
    Moisture_Content_FA = forms.FloatField(min_value=0, max_value=10000)
    Moisture_Content_CA = forms.FloatField(min_value=0, max_value=10000)