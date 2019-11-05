from django.urls import path

from . import views

urlpatterns = [
    path('instrument/create', views.instrument_create_page, name='instrument_create_page'),
    path('instrument/list', views.instrument_list_page, name='instrument_list_page'),
    path('instrument/retrieve', views.instrument_retrieve_page, name='instrument_retrieve_page'),
    path('instrument/update', views.instrument_update_page, name='instrument_update_page'),
    path('instrument/create/api', views.post_instrument_create_api, name='post_instrument_create_api'),
    path('instrument/list/api', views.get_instrument_list_api, name='get_instrument_list_api'),
    path('instrument/retrieve/api/<name>', views.get_instrument_retrieve_api, name='get_instrument_retrieve_api'),
    path('instrument/update/api', views.post_instrument_update_api, name='get_instrument_update_api'),
]
