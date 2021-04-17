from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TCPowersCalc
# Create your views here.
def index(request):
    form = TCPowersCalc()
    return render(request, 'tcpowers/index.html')

def calculate(request):
    if request.method == 'POST':
        form = TCPowersCalc(request.POST)
        if form.is_valid():
            #process data
            args = {}
            wcr = form.cleaned_data['WCRatio']
            doh = form.cleaned_data['DegOfHydra']

            if(1):#(wcr * .01) > (0.42 * doh)):
                wa = .24 * doh
                wg = .18 * doh
                vhp = .68 * doh
                vg = .18 * doh
                vc =  ((wcr * .01) - (.36 * doh * .01)) * 100
                vu = 100 * ((1 - (doh * .01)) * .32)
                pg = 100 * wg / vhp
                pc = (vc * 100) / (wcr + 32)
                x = (.68 * doh) / ((.32 * doh) + wcr) * 100

                args['wa'] = wa
                args['wg'] = wg
                args['vhp'] = vhp
                args['vg'] = wg
                args['vc'] = vc
                args['vu'] = vu
                args['pg'] = pg
                args['pc'] = pc
                args['x'] = x
                args['form'] = form
                return render(request, 'tcpowers/result.html', args)
            else:
                form = TCPowersCalc()
    else:
        form = TCPowersCalc()
    return render(request, 'tcpowers/index.html', {'form':form})