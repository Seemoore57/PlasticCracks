from django.shortcuts import render
from .forms import PlasticCracksForm
import datetime
import requests
import pgeocode


def index(request):
    if request.method == 'POST':
        form = PlasticCracksForm(request.POST)
        if form.is_valid():
            print("index1")
            return render(request, 'pccalc/pcgraphs.html', {'form': form})
    else:
        form = PlasticCracksForm()
    print("index2")
    return render(request, 'pccalc/index.html', {'form': form})


def pcgraphs(request):
    print("pcgraphs")
    if request.method == 'POST':
        # Extract Form Data
        form = PlasticCracksForm(request.POST)
        zip_code = form.data['zip_code']
        concrete_temperature = form.data['concrete_temperature']

        # Calculate Latitude and Longitude from provided Zip Code
        nomi = pgeocode.Nominatim('us')
        nomi_dict = nomi.query_postal_code(zip_code)
        lat = nomi_dict['latitude']
        lon = nomi_dict['longitude']

        # Make GET request for 7-day forecast from OpenWeatherMap API
        base_url = 'https://api.openweathermap.org/data/2.5/onecall?'
        api_key = '04eb51a7a1f05c135efcddc8a13d23e8'
        full_url = base_url + 'lat=' + str(lat) + '&lon=' + str(lon) + '&units=imperial&appid=' + str(api_key)
        response = requests.get(full_url)

        dates = []
        temperatures = []
        relative_humidities = []
        wind_speeds = []
        evaporation_rates = []
        for item in response.json()['daily']:
            date = datetime.date.fromtimestamp(item['dt'])
            date.strftime("%d %b, %Y")
            dates.append(date)

            temperature = item['temp']['day']
            temperatures.append(temperature)

            relative_humidity = item['humidity']
            relative_humidities.append(relative_humidity)

            wind_speed = item['wind_speed']
            wind_speeds.append(wind_speed)

            evap_1 = ((float(concrete_temperature) ** 2.5) -
                      ((float(relative_humidity) / 100) * (float(temperature) ** 2.5)))
            evap_2 = (1 + (0.4 * float(wind_speed))) * (10 ** -6)
            evaporation_rate = abs(evap_1 * evap_2)
            evaporation_rates.append(evaporation_rate)
            print('Temp: ' + str(temperature))
            print('Relative Humidity: ' + str(relative_humidity))
            print('Wind Speed: ' + str(wind_speed))
            print('Evaporation Rate: ' + str(evaporation_rate))

        return render(request, 'pccalc/pcgraphs.html', {
            'dates': dates,
            'risks': evaporation_rates,
            'form': form
        })

    else:
        print("pcgraphs2")
        return render(request, 'pccalc/index.html')


