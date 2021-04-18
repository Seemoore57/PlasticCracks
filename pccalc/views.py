from django.shortcuts import render
from .noaa_sdk import NOAA
from .forms import ZipCodeForm
import logging


def index(request):
    if request.method == 'POST':
        form = ZipCodeForm(request.POST)
        if form.is_valid():
            args = form.cleaned_data['zip_code']
            request.session['zipcode'] = args
            print("index1")
            return render(request, 'pccalc/pcgraphs.html', {'form': form})
    else:
        form = ZipCodeForm()
    print("index2")
    return render(request, 'pccalc/index.html', {'form': form})


def pcgraphs(request):
    print("pcgraphs")
    if request.method == 'POST':
        s = request.session.get('zipcode')
        noaa_portal = NOAA()
        res = noaa_portal.get_forecasts(s, 'US')
        print("pcgraphs1")
        return render(request, 'pccalc/pcgraphs.html', {'res': res})
    else:
        print("pcgraphs2")
        return render(request, 'pccalc/index.html')


