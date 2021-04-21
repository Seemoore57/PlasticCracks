from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import BogueCalculator
# Create your views here.
def index(request):
    form = BogueCalculator()
    return render(request, 'bogue/index.html', {'form':form})

def calculate(request):
    back = request.META.get('HTTP_REFERER')
    if back is None:
        back = 'bogue/index.html'

    if request.method == 'GET':
        return redirect('/bogue/')
    elif request.method == 'POST':
        forth = ''
        if 'compute' in request.POST or 'i' in request.POST or 'ii' in request.POST or 'iii' in request.POST or 'iv' in request.POST or 'v' in request.POST:
            forth = 'bogue/result.html'
        elif 'compare' in request.POST or 'i2' in request.POST or 'ii2' in request.POST or 'iii2' in request.POST or 'iv2' in request.POST or 'v2' in request.POST:
            forth = 'bogue/compare.html'
        elif 'compare2' in request.POST or 'i3' in request.POST or 'ii3' in request.POST or 'iii3' in request.POST or 'iv3' in request.POST or 'v3' in request.POST:
            forth = 'bogue/compare2.html'
        else:
            forth = 'bogue/index.html'

        if 'i' in request.POST or 'i2' in request.POST or 'i3' in request.POST:
            form = BogueCalculator(initial={'lime': 63.2, 'silica': 20.2, 'alumina': 5.1, 'rust': 2.7, 'sulfate': 3.3})
            # process data
            l = 63.2
            si = 20.2
            a = 5.1
            r = 2.7
            s = 3.3
        elif 'ii' in request.POST or 'ii2' in request.POST or 'ii3' in request.POST:
            form = BogueCalculator(initial={'lime': 63.7, 'silica': 20.9, 'alumina': 4.6, 'rust': 3.3, 'sulfate': 2.9})
            # process data
            l = 63.7
            si = 20.9
            a = 4.6
            r = 3.3
            s = 2.9
        elif 'iii' in request.POST or 'iii2' in request.POST or 'iii3' in request.POST:
            form = BogueCalculator(initial={'lime': 63.3, 'silica': 20.4, 'alumina': 4.8, 'rust': 2.9, 'sulfate': 3.6})
            # process data
            l = 63.3
            si = 20.4
            a = 4.8
            r = 2.9
            s = 3.6
        elif 'iv' in request.POST or 'iv2' in request.POST or 'iv3' in request.POST:
            form = BogueCalculator(initial={'lime': 62.5, 'silica': 22.2, 'alumina': 4.6, 'rust': 5.0, 'sulfate': 2.2})
            # process data
            l = 62.5
            si = 22.2
            a = 4.6
            r = 5.0
            s = 2.2
        elif 'v' in request.POST or 'v2' in request.POST or 'v3' in request.POST:
            form = BogueCalculator(initial={'lime': 63.9, 'silica': 21.6, 'alumina': 3.8, 'rust': 3.9, 'sulfate': 2.3})
            # process data
            l = 63.9
            si = 21.6
            a = 3.8
            r = 3.9
            s = 2.3
        else:
            form = BogueCalculator(request.POST)
            if form.is_valid():
                # process data
                l = form.cleaned_data['lime']
                si = form.cleaned_data['silica']
                a = form.cleaned_data['alumina']
                r = form.cleaned_data['rust']
                s = form.cleaned_data['sulfate']

        args = {}

        if l<=0 or si<=0 or a<=0 or r<=0 or s<=0:
            messages.error(request, 'Error: Input must be above zero')
            return redirect(back)

        if a/r >= 0.64:
            tri = 4.071*l - 7.60*si - 6.718*a - 1.43*r - 2.852*s
            di = 2.867*si - 0.7544*tri
            alu = 2.6504*a - 1.692*r
            af = 3.0432*r
        else:
            tri = 4.071 * l - 7.60 * si - 4.479 * a - 2.859 * r - 2.852 * s
            di = 2.867 * si - 0.7544 * tri
            alu = 0
            af = 2.1 * a + 1.702 * r

        if tri < 0:
            tri = 0
        if di < 0:
            di = 0
        if alu < 0:
            alu = 0
        if af < 0:
            af = 0

        leftover = 100 - tri - di - alu - af
        if leftover < 0:
            messages.error(request, 'Error: Calculation results over 100%')
            return redirect(back)

        args['trisilicate'] = tri
        args['disilicate'] = di
        args['trialumina'] = alu
        args['ferricalumina'] = af
        args['leftover'] = leftover
        args['leftover2'] = 1 - l - si - a - r
        args['form'] = form

        if 'compare' in request.POST or 'i2' in request.POST or 'ii2' in request.POST or 'iii2' in request.POST or 'iv2' in request.POST or 'v2' in request.POST:
            request.session['trisilicate2'] = tri
            request.session['disilicate2'] = di
            request.session['trialumina2'] = alu
            request.session['ferricalumina2'] = af
            request.session['leftover2'] = leftover
        else:
            request.session['trisilicate'] = tri
            request.session['disilicate'] = di
            request.session['trialumina'] = alu
            request.session['ferricalumina'] = af
            request.session['leftover'] = leftover

        return render(request, forth, args)
    else:
        form = BogueCalculator()
    return render(request, back, {'form':form})