from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from foundation.models import Instrument, Sensor, TimeSeriesDatum


def dashboard_page(request):
    user = request.user


    if user.is_authenticated == False:
        return HttpResponse("Cannot view page - you must login first")

    context = {
        'user': user,
    }
    return render(request,'dashboard/dashboard.html',context)

def get_dashboard_api(request):
    return JsonResponse({
    "average_temperature": get_average_temperature(),
    "average_pressure": get_average_pressure(),
    "average_co2": get_average_co2(),
    "average_tvoc": get_average_tvoc(),
    "average_humidity": get_average_humidity(),
    })

def get_average_temperature():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor__name = "Temperature")
    for datum in data:
        sum = sum + datum.value
    try:
        output = sum/len(data)

        return output
    except Exception as e:
        return None

def get_average_pressure():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor__name = "Pressure")
    for datum in data:
        sum = sum + datum.value
    try:
        output = sum/len(data)

        return output
    except Exception as e:
        return None


def get_average_co2():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor__name = "CO2")
    for datum in data:
        sum = sum + datum.value
    try:
        output = sum/len(data)

        return output
    except Exception as e:
        return None


def get_average_tvoc():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor__name = "TVOC")
    for datum in data:
        sum = sum + datum.value
    try:
        output = sum/len(data)

        return output
    except Exception as e:
        return None


def get_average_humidity():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor__name = "Humidity")
    for datum in data:
        sum = sum + datum.value
    try:
        output = sum/len(data)

        return output
    except Exception as e:
        return None
