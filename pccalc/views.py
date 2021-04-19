from django.http import JsonResponse
from django.shortcuts import render
from .forms import ZipCodeForm
from django.views.generic import TemplateView
from .models import Graph
import datetime
import requests
import pgeocode


# class PcGraphView(TemplateView):
#     template_name = 'pccalc/pcgraphs.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["qs"] = Graph.objects.all()
#         return context


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
        form = ZipCodeForm(request.POST)

        Graph.objects.all().delete()
        zip_code = request.session.get('zipcode')
        date = datetime.datetime.now()
        for i in range(7):
            d = Graph(date=date, risk=(i * 15))
            d.save()
            date += datetime.timedelta(days=1)

        dates = []
        risks = []

        qs = Graph.objects.order_by('date')
        for graph in qs:
            dates.append(graph.date)
            risks.append(graph.risk)

        return render(request, 'pccalc/pcgraphs.html', {
            'dates': dates,
            'risks': risks,
            'form': form
        })
        # nomi = pgeocode.Nominatim('us')
        # nomi_dict = nomi.query_postal_code(zip_code)
        # lat = nomi_dict['latitude']
        # long = nomi_dict['longitude']
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


