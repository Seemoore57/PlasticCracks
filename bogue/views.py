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

            if(form.cleaned_data['alumina']/form.cleaned_data['rust'] >= 0.64):
                tri = 4.071*l - 7.6*si - 6.718*a - 1.43*r - 2.852*su
                di = 2.867*si - 0.7544*tri
                alu = 2.65*a - 1.692*r
                af = 3.043*r

            args['trisilicate'] = tri
            args['disilicate'] = di
            args['trialumina'] = alu
            args['ferricalumina'] = af
            args['form'] = form
            return render(request, 'bogue/result.html', args)
    else:
        form = BogueCalculator()
    return render(request, 'bogue/index.html', {'form':form})
    