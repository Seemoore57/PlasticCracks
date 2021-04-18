from django.shortcuts import render
from .forms import ZipCodeForm
import datetime
import requests
import pgeocode


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
        zip_code = request.session.get('zipcode')
        nomi = pgeocode.Nominatim('us')
        nomi_dict = nomi.query_postal_code(zip_code)
        lat = nomi_dict['latitude']
        long = nomi_dict['longitude']

        grid_get = 'https://api.weather.gov/points/' + str(lat) + ',' + str(long)
        response = requests.get(grid_get)
        grid_id = response.json()['properties']['gridId']
        grid_x = response.json()['properties']['gridX']
        grid_y = response.json()['properties']['gridY']
        print(grid_id)
        print(grid_x)
        print(grid_y)
        print(response.json())

        forecast_url = \
            'https://api.weather.gov/gridpoints/' + str(grid_id) + '/' + str(grid_x) + ',' + str(grid_y) + '/forecast'
        response_forecast = requests.get('http://api.weather.gov/point/XXX,XXX/forecast')
        print(response_forecast.json())

        noaa_portal = NOAA()
        res = noaa_portal.get_observations(zip_code, 'US')

        return render(request, 'pccalc/pcgraphs.html', {'res': res})
    else:
        print("pcgraphs2")
        return render(request, 'pccalc/index.html')


