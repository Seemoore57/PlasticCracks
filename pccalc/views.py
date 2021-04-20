from django.shortcuts import render
from .forms import PlasticCracksForm
from .models import Graph
import datetime
import requests
import pgeocode
from math import pow


# class PcGraphView(TemplateView):
#     template_name = 'pccalc/pcgraphs.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["qs"] = Graph.objects.all()
#         return context


def index(request):
    if request.method == 'POST':
        form = PlasticCracksForm(request.POST)
        if form.is_valid():
            # args = form.cleaned_data['zip_code']
            # request.session['zipcode'] = args
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
        risks = []
        temperatures = []
        relative_humidities = []
        wind_speeds = []
        evaporation_rates = []
        risk = 10
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

            risks.append(risk)
            risk += 10

            evap_1 = ((float(concrete_temperature) ** 2.5) -
                      ((float(relative_humidity) / 100) * (float(temperature) ** 2.5)))
            evap_2 = (1 + (0.4 * float(wind_speed))) * (10 ** -6)
            evaporation_rate = evap_1 * evap_2
            evaporation_rates.append(evaporation_rate)
            print('Temp: ' + str(temperature))
            print('Relative Humidity: ' + str(relative_humidity))
            print('Wind Speed: ' + str(wind_speed))
            print('Evaporation Rate: ' + str(evaporation_rate))


        # Remove old graphing objects from DB
        # Graph.objects.all().delete()

        # Grab date time group for the next 7 days
        # date = datetime.datetime.now()
        # for i in range(7):
        #     d = Graph(date=date, risk=(i * 15))
        #     d.save()
        #     date += datetime.timedelta(days=1)

        # TODO: Unsure if we even need models, since we are just injecting context with arrays
        #
        # qs = Graph.objects.order_by('date')
        # for graph in qs:
        #     dates.append(graph.date)
        #     risks.append(graph.risk)

        return render(request, 'pccalc/pcgraphs.html', {
            'dates': dates,
            'risks': risks,
            'form': form
        })

        #
        # grid_get = 'https://api.weather.gov/points/' + str(lat) + ',' + str(long)
        # response = requests.get(grid_get)
        # grid_id = response.json()['properties']['gridId']
        # grid_x = response.json()['properties']['gridX']
        # grid_y = response.json()['properties']['gridY']
        # print(grid_id)
        # print(grid_x)
        # print(grid_y)
        # print(response.json())
        #
        # forecast_url = \
        #     'https://api.weather.gov/gridpoints/' + str(grid_id) + '/' + str(grid_x) + ',' + str(grid_y) +\
        #     '/forecast'
        # response_forecast = requests.get(forecast_url, headers={'JSON-LD': 'application/ld+json',
        #                                                         'UserAgent': 'calmoor@siue.edu'})
        # print(response_forecast.json())
    else:
        print("pcgraphs2")
        return render(request, 'pccalc/index.html')


