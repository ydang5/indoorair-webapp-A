from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login, logout

def register_page(request):
   return render(request, "gateway/register.html", {})


def post_register_api(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")

    try:
       user = User.objects.create_user(username, email, password)
       user.last_name = last_name
       user.first_name = first_name
       user.save()
       return JsonResponse({
            "was_registered": True,
       })
    except Exception as e:
       return JsonResponse({
            "was_registered": False,
            "reason": str(e)
       })


def register_ok_page(request):
    return render(request, "gateway/register_ok_page.html",{})


def login_page(request):
   user = request.user
   return render(request, "gateway/login.html", {})


def post_login_api(request):
   username = request.POST.get("username")
   password = request.POST.get("password")
   print("For debugging purposes", username, password)
   try:
       user = authenticate(username=username, password=password)
       if user:
           print("PRE-LOGIN", user.get_full_name())
           login(request, user)
           print("POST-LOGIN", user.get_full_name())
           # A backend authenticated the credentials
           return JsonResponse({
                "was_successful": True,
                "reason": None,
           })
       else:
           # No backend authenticated the credentials
           return JsonResponse({
                "was_successful": False,
                "reason": "Cannot log in, username or password is wrong.",
           })
   except Exception as e:
       print(e)
       return JsonResponse({
            "was_successful": False,
            "reason": "Cannot log in, username or password is wrong.",
       })



def get_logout_api(request):
    logout(request)
    return redirect("/login")
