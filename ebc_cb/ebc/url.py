from . import views
from django.urls import path

urlpatterns = [
    path('callback/', views.wacallback),
    path('wadel/', views.wadel),
    path('privacy_policy/', views.pp),
    path('msan/<str:num>/', views.msan),
    path('chat_agent/<str:nums>/', views.chat_agent),
    path('msan/', views.msan1),
    path('chat_ag_pst/', views.chat_ag_pst)
   #path('icallback/', views.wacallback), #instagram
   #path('mecallback/', views.wacallback), #messenger
]