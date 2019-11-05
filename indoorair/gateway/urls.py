from django.urls import path

from . import views
# from dashboard import views

urlpatterns = [
    path('register', views.register_page, name='register_page'),
    path('api/register', views.post_register_api, name='register_api'),
    path('register/ok', views.register_ok_page, name ='register_ok_page'),
    path('login', views.login_page, name='login_page'),
    path('api/login',views.post_login_api, name='login_api'),
    # path('api/logout',views.post_logout_api,name='logout_api'),
]
