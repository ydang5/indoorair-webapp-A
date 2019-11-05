from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index_page(request):
    user = request.user

    return render(request,'homepage/index.html',{})



def contact_page(request):
        context = {}

        return render(request,'homepage/contact.html',context)

def get_version_api(request):
    return JsonResponse({'version': '0.1.0-beta'})
