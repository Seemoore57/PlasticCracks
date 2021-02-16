from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import BogueCalculator
# Create your views here.
def index(request):
    form = BogueCalculator()
    return render(request, 'bogue/index.html', {'form':form})

def calculate(request):
    if request.method == 'POST':
        form = BogueCalculator(request.POST)
        if form.is_valid():
            #process data
            args = {}
            l = form.cleaned_data['lime']
            si = form.cleaned_data['silica']
            a = form.cleaned_data['alumina']
            r = form.cleaned_data['rust']
            su = form.cleaned_data['sulfur']

            if(a/r >= 0.64):
                tri = 4.071*l - 7.6024*si - 6.7187*a - 1.4297*r
                di = 8.6024*si + 1.1*r + 5.0683*a - 3.071*l
                alu = 2.6504*a - 1.692*r
                af = 3.0432*r

            args['trisilicate'] = tri
            args['disilicate'] = di
            args['trialumina'] = alu
            args['ferricalumina'] = af
            args['form'] = form
            return render(request, 'bogue/result.html', args)
    else:
        form = BogueCalculator()
    return render(request, 'bogue/index.html', {'form':form})
    