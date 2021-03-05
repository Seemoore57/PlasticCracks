from django.shortcuts import render

# from catalog.forms import ZipCodeForm


def index(request):

    # if request.method == 'POST':
    #     form = ZipCodeForm(request.POST)
    # else:

    return render(request, 'index.html')
