from django.shortcuts import render
from django.http import HttpResponse
from .forms import MixDesignCalculator

# Create your views here.
def index(request):
    form = MixDesignCalculator()
    return render(request, 'mixdesign/index.html',{'form':form})

def calculate(request):
    if request.method == 'POST':
        meters = request.POST.get('meters', '')
        feet = request.POST.get('feet', '')
        print('in calculate')
        form = MixDesignCalculator(request.POST)
        print(request.POST.get('value'))
        if form.is_valid():
            print('form is valid')
            args = {}
            cement = form.cleaned_data['Cement']
            fly_ash = form.cleaned_data['Fly_Ash']
            slag = form.cleaned_data['Slag']
            water = form.cleaned_data['Water']
            fine_aggregates = form.cleaned_data['Fine_Aggregates']
            coarse_aggregates = form.cleaned_data['Coarse_Aggregates']
            air_entrained = form.cleaned_data['Air_Entrained']
            wc_ratio = form.cleaned_data['WC_Ratio']
            slag_SG= form.cleaned_data['Slag_SG']
            fly_ash_SG = form.cleaned_data['Fly_Ash_SG']
            fine_aggregates_SG = form.cleaned_data['Fine_Aggregates_SG']
            coarse_aggregates_SG = form.cleaned_data['Coarse_Aggregates_SG']
            slump_test = form.cleaned_data['Slump_Test']
            air_test = form.cleaned_data['Air_Test']
            formwork_volume = form.cleaned_data['Formwork_Volume']
            moisture_content_FA = form.cleaned_data['Moisture_Content_FA']
            moisture_content_CA = form.cleaned_data['Moisture_Content_CA']

            args['cement']= cement
            args['fly_ash']= fly_ash
            args['slag']= slag
            args['water']= water
            args['fine_aggregates']= fine_aggregates
            args['coarse_aggregates']= coarse_aggregates
            args['wc_ratio']=wc_ratio
            args['fly_ash_SG']= fly_ash_SG
            args['slag_SG']= slag_SG
            args['fine_aggregates_SG']= fine_aggregates_SG
            args['coarse_aggregates_SG']= coarse_aggregates_SG
            args['formwork_volume']= formwork_volume
            args['moisture_content_FA']= moisture_content_FA
            args['moisture_content_CA']= moisture_content_CA
            if(feet):
                if (slump_test):
                    args['formwork_volume']= args['formwork_volume'] + 0.2036186343
                if (air_test):
                    args['formwork_volume'] = args['formwork_volume'] + 0.25

                args['mix_volume'] = (args['formwork_volume'] * 0.15) + args['formwork_volume']
                args['total'] = args['cement']+args['fly_ash']+args['slag']+args['water']+args['fine_aggregates']+args['coarse_aggregates']

                args['cement_ft3']= args['cement']/(3.15*62.4)
                args['fly_ash_ft3']= args['fly_ash']/args['fly_ash_SG']*62.4
                args['slag_ft3']= args['slag']/args['slag_SG']*64.2
                args['water_ft3']= args['water']/(1.0*62.4)
                args['fine_aggregates_ft3'] = args['fine_aggregates'] / args['fine_aggregates_SG'] * 64.2
                args['coarse_aggregates_ft3'] = args['coarse_aggregates'] / args['coarse_aggregates_SG'] * 64.2

                args['air_ft3']=args['cement_ft3']+args['fly_ash_ft3']+args['slag_ft3']+args['fine_aggregates_ft3']/(0.94)+args['cement_ft3']+args['fly_ash_ft3']+args['slag_ft3']+args['fine_aggregates_ft3']

                args['total_ft3']=args['cement_ft3']+args['fly_ash_ft3']+args['slag_ft3']+args['water_ft3'] + args['coarse_aggregates_ft3']+ args['fine_aggregates_ft3']+args['air_ft3']

                args['cement_1ft3']= args['cement_ft3']/args['total_ft3']
                args['fly_ash_1ft3'] = args['fly_ash_ft3'] / args['total_ft3']
                args['slag_1ft3']= args['slag_ft3'] / args['total_ft3']
                args['water_1ft3']= args['water_ft3'] / args['total_ft3']
                args['fine_aggregates_1ft3']= args['fine_aggregates_ft3'] / args['total_ft3']
                args['coarse_aggregates_1ft3']= args['coarse_aggregates_ft3'] / args['total_ft3']
                args['air_1ft3']= args['air_ft3'] / args['total_ft3']

                args['total_1ft3'] = args['cement_1ft3'] + args['fly_ash_1ft3'] + args['slag_1ft3'] + args['water_1ft3'] + \
                                    args['coarse_aggregates_1ft3'] + args['fine_aggregates_1ft3'] + args['air_1ft3']
                args['cement_1yd3']= args['cement_1ft3']*27
                args['fly_ash_1yd3']= args['fly_ash_1ft3']*27
                args['slag_1yd3']= args['slag_1ft3']*27
                args['water_1yd3']= args['water_1ft3']*27
                args['fine_aggregates_1yd3']= args['fine_aggregates_1ft3']*27
                args['coarse_aggregates_1yd3']= args['coarse_aggregates_1ft3']*27
                args['air_1yd3']= args['air_1ft3']*27

                args['total_1yd3'] = args['cement_1yd3'] + args['fly_ash_1yd3'] + args['slag_1yd3'] + args['water_1yd3'] + args['coarse_aggregates_1yd3'] + args['fine_aggregates_1yd3'] + args['air_1yd3']

                args['cement_ssd_ft3']= args['cement_1ft3']* args['mix_volume']
                args['fly_ash_ssd_ft3']= args['fly_ash_1ft3']* args['mix_volume']
                args['slag_ssd_ft3']= args['slag_1ft3']* args['mix_volume']
                args['water_ssd_ft3']= args['water_1ft3']* args['mix_volume']
                args['fine_aggregates_ssd_ft3']= args['fine_aggregates_1ft3']* args['mix_volume']
                args['coarse_aggregates_sdd_ft3']= args['coarse_aggregates_1ft3']* args['mix_volume']
                args['air_ssd_ft3']= args['air_1ft3']* args['mix_volume']
                args['total_ssd_ft3']= args['cement_ssd_ft3'] + args['fly_ash_ssd_ft3'] + args['slag_ssd_ft3'] + args[
                    'water_ssd_ft3'] + args['coarse_aggregates_sdd_ft3'] + args['fine_aggregates_ssd_ft3'] + args['air_ssd_ft3']

                args['cement_ssd_lbs']=args['cement_ssd_ft3']* 3.15 * 62.4
                args['fly_ash_ssd_lbs']=args['fly_ash_ssd_ft3']* 2.5 * 62.4
                args['slag_ssd_lbs']= args['slag_ssd_ft3'] * 2.8 * 62.4
                args['water_ssd_lbs']= args['water_ssd_ft3'] * 1.0 * 62.4
                args['fine_aggregates_ssd_lbs']= args['fine_aggregates_ssd_ft3']* 2.5 * 62.4
                args['coarse_aggregates_sdd_lbs']= args['coarse_aggregates_sdd_ft3']* 2.6 * 62.4
                args['total_ssd_lbs']= args['cement_ssd_lbs']+ args['fly_ash_ssd_lbs']+ args['slag_ssd_lbs']+args['water_ssd_lbs']+args['fine_aggregates_ssd_lbs']+args['coarse_aggregates_sdd_lbs']

                args['coarse_aggregates_stock_mix']= args['coarse_aggregates_sdd_lbs'] * ((1 + args['moisture_content_CA'])/100)
                args['fine_aggregates_stock_mix'] = args['fine_aggregates_ssd_lbs'] * ((1 + args['moisture_content_FA']) / 100)
                args['water_stock_mix']= args['water_ssd_lbs'] + (args['fine_aggregates_ssd_lbs']-args['fine_aggregates_stock_mix'])+(args['coarse_aggregates_sdd_lbs']-args['coarse_aggregates_stock_mix'])
                args['total_stock_mix']= args['cement_ssd_lbs']+ args['fly_ash_ssd_lbs']+ args['slag_ssd_lbs']+ args['water_stock_mix']+ args['coarse_aggregates_stock_mix']+ args['fine_aggregates_stock_mix']
                return render(request, 'mixdesign/output_FT.html', args)
            if(meters):
                print('in meters')
                if (slump_test):
                    args['formwork_volume']= args['formwork_volume'] + 0.06206295973464
                if (air_test):
                    args['formwork_volume'] = args['formwork_volume'] + 0.0762

                args['mix_volume'] = (args['formwork_volume'] * 0.15) + args['formwork_volume']

                args['total'] = args['cement'] + args['fly_ash'] + args['slag'] + args['water'] + args[
                    'fine_aggregates'] + args['coarse_aggregates']

                args['cement_m3'] = args['cement'] / (3.15 * 998)
                args['fly_ash_m3'] = args['fly_ash'] / args['fly_ash_SG'] * 998
                args['slag_m3'] = args['slag'] / args['slag_SG'] * 998
                args['water_m3'] = args['water'] / (1.0 * 998)
                args['fine_aggregates_m3'] = args['fine_aggregates'] / args['fine_aggregates_SG'] * 998
                args['coarse_aggregates_m3'] = args['coarse_aggregates'] / args['coarse_aggregates_SG'] * 998

                args['air_m3'] = args['cement_m3'] + args['fly_ash_m3'] + args['slag_m3'] + args[
                    'fine_aggregates_m3'] / (0.94) + args['cement_m3'] + args['fly_ash_m3'] + args['slag_m3'] + \
                                  args['fine_aggregates_m3']

                args['total_m3'] = args['cement_m3'] + args['fly_ash_m3'] + args['slag_m3'] + args['water_m3'] + \
                                    args['coarse_aggregates_m3'] + args['fine_aggregates_m3'] + args['air_m3']

                args['cement_1m3'] = args['cement_m3'] / args['total_m3']
                args['fly_ash_1m3'] = args['fly_ash_m3'] / args['total_m3']
                args['slag_1m3'] = args['slag_m3'] / args['total_m3']
                args['water_1m3'] = args['water_m3'] / args['total_m3']
                args['fine_aggregates_1m3'] = args['fine_aggregates_m3'] / args['total_m3']
                args['coarse_aggregates_1m3'] = args['coarse_aggregates_m3'] / args['total_m3']
                args['air_1m3'] = args['air_m3'] / args['total_m3']

                args['total_1m3'] = args['cement_1m3'] + args['fly_ash_1m3'] + args['slag_1m3'] + args[
                    'water_1m3'] + \
                                     args['coarse_aggregates_1m3'] + args['fine_aggregates_1m3'] + args['air_1m3']

                args['cement_ssd_m3'] = args['cement_1m3'] * args['mix_volume']
                args['fly_ash_ssd_m3'] = args['fly_ash_1m3'] * args['mix_volume']
                args['slag_ssd_m3'] = args['slag_1m3'] * args['mix_volume']
                args['water_ssd_m3'] = args['water_1m3'] * args['mix_volume']
                args['fine_aggregates_ssd_m3'] = args['fine_aggregates_1m3'] * args['mix_volume']
                args['coarse_aggregates_sdd_m3'] = args['coarse_aggregates_1m3'] * args['mix_volume']
                args['air_ssd_m3'] = args['air_1m3'] * args['mix_volume']
                args['total_ssd_m3'] = args['cement_ssd_m3'] + args['fly_ash_ssd_m3'] + args['slag_ssd_m3'] + args[
                    'water_ssd_m3'] + args['coarse_aggregates_sdd_m3'] + args['fine_aggregates_ssd_m3'] + args[
                                            'air_ssd_m3']

                args['cement_ssd_kgs'] = args['cement_ssd_m3'] * 3.15 * 998
                args['fly_ash_ssd_kgs'] = args['fly_ash_ssd_m3'] * args['fly_ash_SG'] * 998
                args['slag_ssd_kgs'] = args['slag_ssd_m3'] * args['slag_SG'] * 998
                args['water_ssd_kgs'] = args['water_ssd_m3'] * 1.0 * 998
                args['fine_aggregates_ssd_kgs'] = args['fine_aggregates_ssd_m3'] * args['fine_aggregates_SG'] * 998
                args['coarse_aggregates_sdd_kgs'] = args['coarse_aggregates_sdd_m3'] * args['coarse_aggregates_SG'] * 998
                args['total_ssd_kgs'] = args['cement_ssd_kgs'] + args['fly_ash_ssd_kgs'] + args['slag_ssd_kgs'] + args[
                    'water_ssd_kgs'] + args['fine_aggregates_ssd_kgs'] + args['coarse_aggregates_sdd_kgs']

                args['coarse_aggregates_stock_mix'] = args['coarse_aggregates_sdd_kgs'] * (
                            (1 + args['moisture_content_CA']) / 100)
                args['fine_aggregates_stock_mix'] = args['fine_aggregates_ssd_kgs'] * (
                            (1 + args['moisture_content_FA']) / 100)
                args['water_stock_mix'] = args['water_ssd_kgs'] + (
                            args['fine_aggregates_ssd_kgs'] - args['fine_aggregates_stock_mix']) + (
                                                      args['coarse_aggregates_sdd_kgs'] - args[
                                                  'coarse_aggregates_stock_mix'])
                args['total_stock_mix'] = args['cement_ssd_kgs'] + args['fly_ash_ssd_kgs'] + args['slag_ssd_kgs'] + \
                                          args['water_stock_mix'] + args['coarse_aggregates_stock_mix'] + args[
                                              'fine_aggregates_stock_mix']
                return render(request, 'mixdesign/output_M.html', args)
    else:
        form = MixDesignCalculator()
    return render(request, 'mixdesign/index.html', {'form': form})





