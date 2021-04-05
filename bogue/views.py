from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import BogueCalculator
# Create your views here.
def index(request):
    form = BogueCalculator()
    return render(request, 'bogue/index.html', {'form':form})

def calculate(request):
    if request.method == 'POST':
        if 'i' in request.POST:
            form = BogueCalculator(initial={'lime': 63.2, 'silica': 20.2, 'alumina': 5.1, 'rust': 2.7})
            # process data
            args = {}
            l = 63.2
            si = 20.2
            a = 5.1
            r = 2.7
        elif 'ii' in request.POST:
            form = BogueCalculator(initial={'lime': 63.7, 'silica': 20.9, 'alumina': 4.6, 'rust': 3.3})
            # process data
            args = {}
            l = 63.7
            si = 20.9
            a = 4.6
            r = 3.3
        elif 'iii' in request.POST:
            form = BogueCalculator(initial={'lime': 63.3, 'silica': 20.4, 'alumina': 4.8, 'rust': 2.9})
            # process data
            args = {}
            l = 63.3
            si = 20.4
            a = 4.8
            r = 2.9
        elif 'iv' in request.POST:
            form = BogueCalculator(initial={'lime': 62.5, 'silica': 22.2, 'alumina': 4.6, 'rust': 5.0})
            # process data
            args = {}
            l = 62.5
            si = 22.2
            a = 4.6
            r = 5.0
        elif 'v' in request.POST:
            form = BogueCalculator(initial={'lime': 63.9, 'silica': 21.6, 'alumina': 3.8, 'rust': 3.9})
            # process data
            args = {}
            l = 63.9
            si = 21.6
            a = 3.8
            r = 3.9
        else:
            form = BogueCalculator(request.POST)
            if form.is_valid():
                # process data
                args = {}
                l = form.cleaned_data['lime']
                si = form.cleaned_data['silica']
                a = form.cleaned_data['alumina']
                r = form.cleaned_data['rust']

        if(a/r >= 0.64):
            tri = 4.071*l - 7.6024*si - 6.7187*a - 1.4297*r
            di = 8.6024*si + 1.1*r + 5.0683*a - 3.071*l
            alu = 2.6504*a - 1.692*r
            af = 3.0432*r
            leftover = 100 - tri - di - alu - af
        else:
            tri = 4.071 * l - 7.6024 * si - 4.479 * a - 2.859 * r
            di = 8.6024 * si + 0.7544 * tri
            alu = 0
            af = 2.1 * a + 1.702 * r
            leftover = 100 - tri - di - alu - af

        if(tri < 0):
            tri = 0
        if (di < 0):
            di = 0
        if (alu < 0):
            alu = 0
        if (af < 0):
            af = 0
        if (leftover < 0):
            leftover = 0

        args['trisilicate'] = tri
        args['disilicate'] = di
        args['trialumina'] = alu
        args['ferricalumina'] = af
        args['leftover'] = leftover
        args['leftover2'] = 1 - l - si - a - r
        args['form'] = form

        request.session['trisilicate'] = tri
        request.session['disilicate'] = di
        request.session['trialumina'] = alu
        request.session['ferricalumina'] = af
        request.session['leftover'] = leftover

        return render(request, 'bogue/result.html', args)
    else:
        form = BogueCalculator()
    return render(request, 'bogue/index.html', {'form':form})

def compare(request):
    if request.method == 'POST':
        if 'i' in request.POST:
            form = BogueCalculator(initial={'lime': 63.2, 'silica': 20.2, 'alumina': 5.1, 'rust': 2.7})
            # process data
            args = {}
            l = 63.2
            si = 20.2
            a = 5.1
            r = 2.7
        elif 'ii' in request.POST:
            form = BogueCalculator(initial={'lime': 63.7, 'silica': 20.9, 'alumina': 4.6, 'rust': 3.3})
            # process data
            args = {}
            l = 63.7
            si = 20.9
            a = 4.6
            r = 3.3
        elif 'iii' in request.POST:
            form = BogueCalculator(initial={'lime': 63.3, 'silica': 20.4, 'alumina': 4.8, 'rust': 2.9})
            # process data
            args = {}
            l = 63.3
            si = 20.4
            a = 4.8
            r = 2.9
        elif 'iv' in request.POST:
            form = BogueCalculator(initial={'lime': 62.5, 'silica': 22.2, 'alumina': 4.6, 'rust': 5.0})
            # process data
            args = {}
            l = 62.5
            si = 22.2
            a = 4.6
            r = 5.0
        elif 'v' in request.POST:
            form = BogueCalculator(initial={'lime': 63.9, 'silica': 21.6, 'alumina': 3.8, 'rust': 3.9})
            # process data
            args = {}
            l = 63.9
            si = 21.6
            a = 3.8
            r = 3.9
        else:
            form = BogueCalculator(request.POST)
            if form.is_valid():
                #process data
                args = {}
                l = form.cleaned_data['lime']
                si = form.cleaned_data['silica']
                a = form.cleaned_data['alumina']
                r = form.cleaned_data['rust']

        if(a/r >= 0.64):
            tri = 4.071*l - 7.6024*si - 6.7187*a - 1.4297*r
            di = 8.6024*si + 1.1*r + 5.0683*a - 3.071*l
            alu = 2.6504*a - 1.692*r
            af = 3.0432*r
            leftover = 100 - tri - di - alu - af
        else:
            tri = 4.071 * l - 7.6024 * si - 4.479 * a - 2.859 * r
            di = 8.6024 * si + 0.7544 * tri
            alu = 0
            af = 2.1 * a + 1.702 * r
            leftover = 100 - tri - di - alu - af

        if (tri < 0):
            tri = 0
        if (di < 0):
            di = 0
        if (alu < 0):
            alu = 0
        if (af < 0):
            af = 0
        if (leftover < 0):
            leftover = 0

        args['trisilicate'] = tri
        args['disilicate'] = di
        args['trialumina'] = alu
        args['ferricalumina'] = af
        args['leftover'] = leftover
        args['leftover2'] = 1 - l - si - a - r
        args['form'] = form

        request.session['trisilicate2'] = tri
        request.session['disilicate2'] = di
        request.session['trialumina2'] = alu
        request.session['ferricalumina2'] = af
        request.session['leftover2'] = leftover

        return render(request, 'bogue/compare.html', args)
    else:
        form = BogueCalculator()
    return render(request, 'bogue/result.html', {'form':form})

def compare2(request):
    if request.method == 'POST':
        if 'i' in request.POST:
            form = BogueCalculator(initial={'lime': 63.2, 'silica': 20.2, 'alumina': 5.1, 'rust': 2.7})
            # process data
            args = {}
            l = 63.2
            si = 20.2
            a = 5.1
            r = 2.7
        elif 'ii' in request.POST:
            form = BogueCalculator(initial={'lime': 63.7, 'silica': 20.9, 'alumina': 4.6, 'rust': 3.3})
            # process data
            args = {}
            l = 63.7
            si = 20.9
            a = 4.6
            r = 3.3
        elif 'iii' in request.POST:
            form = BogueCalculator(initial={'lime': 63.3, 'silica': 20.4, 'alumina': 4.8, 'rust': 2.9})
            # process data
            args = {}
            l = 63.3
            si = 20.4
            a = 4.8
            r = 2.9
        elif 'iv' in request.POST:
            form = BogueCalculator(initial={'lime': 62.5, 'silica': 22.2, 'alumina': 4.6, 'rust': 5.0})
            # process data
            args = {}
            l = 62.5
            si = 22.2
            a = 4.6
            r = 5.0
        elif 'v' in request.POST:
            form = BogueCalculator(initial={'lime': 63.9, 'silica': 21.6, 'alumina': 3.8, 'rust': 3.9})
            # process data
            args = {}
            l = 63.9
            si = 21.6
            a = 3.8
            r = 3.9
        else:
            form = BogueCalculator(request.POST)
            if form.is_valid():
                # process data
                args = {}
                l = form.cleaned_data['lime']
                si = form.cleaned_data['silica']
                a = form.cleaned_data['alumina']
                r = form.cleaned_data['rust']

        if(a/r >= 0.64):
            tri = 4.071*l - 7.6024*si - 6.7187*a - 1.4297*r
            di = 8.6024*si + 1.1*r + 5.0683*a - 3.071*l
            alu = 2.6504*a - 1.692*r
            af = 3.0432*r
            leftover = 100 - tri - di - alu - af
        else:
            tri = 4.071 * l - 7.6024 * si - 4.479 * a - 2.859 * r
            di = 8.6024 * si + 0.7544 * tri
            alu = 0
            af = 2.1 * a + 1.702 * r
            leftover = 100 - tri - di - alu - af

        if (tri < 0):
            tri = 0
        if (di < 0):
            di = 0
        if (alu < 0):
            alu = 0
        if (af < 0):
            af = 0
        if (leftover < 0):
            leftover = 0

        args['trisilicate'] = tri
        args['disilicate'] = di
        args['trialumina'] = alu
        args['ferricalumina'] = af
        args['leftover'] = leftover
        args['leftover2'] = 1 - l - si - a - r
        args['form'] = form

        request.session['trisilicate'] = tri
        request.session['disilicate'] = di
        request.session['trialumina'] = alu
        request.session['ferricalumina'] = af
        request.session['leftover'] = leftover

        return render(request, 'bogue/compare2.html', args)
    else:
        form = BogueCalculator()
    return render(request, 'bogue/compare.html', {'form':form})