from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login, logout
from foundation.models import Instrument

def instrument_create_page(request):
   return render(request, "instrument/create.html", {})


def instrument_list_page(request):
   return render(request, "instrument/list.html", {})


def instrument_retrieve_page(request):
   return render(request, "instrument/retrieve.html", {})


def instrument_update_page(request):
   return render(request, "instrument/update.html", {})


def post_instrument_create_api(request):
    name = request.POST.get("create_instrument")

    try:
        instrument = Insrtument.objects.create(
        name = name,
        user = request.user
    )
        return JsonResponse({
            'was_created': True
      })
    except Exception as e:
        return JsonResponse({
            'was_created': False,
            'reason': str(e)
        })


def get_instrument_list_api(request):
    instruments = Instrument.objects.filter(user=request.user)
    return JsonResponse ({
        'insturments':instruments
    })


def get_instrument_retrieve_api(request,name):
    result = BlogDatum.objects.get(name = name)
    return HttpResponse(result)

def post_instrument_update_api(request,name,user):
    datum = Insrtument.objects.get(user=update_instrument_user)
    datum.user = update_instrument_name
    datum.save()

    return HttpResponse(datum)
