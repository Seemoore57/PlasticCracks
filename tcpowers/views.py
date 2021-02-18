from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'tcpowers/index.html')

def calculate(request):
    if request.method == 'POST':
        form = TCPowersCalc(request.POST)
        if form.is_valid():
            #process data
            args = {}
            wcr = form.cleaned_data['WCRatio']
            doh = form.cleaned_data['DegOfHydra']

            wa = .24 * doh
            wg = .18 * doh
            vhp = .68 * doh
            vg = .18 * doh
            vc =  wcr - (.36 * doh)
            vu = (1 - doh) * vc
            pg = wg / vhp
            pc = vc / vp
            x = (.68 * doh) / ((.32 * doh) + wcr)

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
    return render(request, 'tcpowers/index.html', {'form':form})