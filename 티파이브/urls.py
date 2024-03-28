from django.urls import path

from playground import views

app_name = '티파이브'

urlpatterns = [
    path('jihoon/', views.jihoon, name='jihoon'),
    path('junkyu/', views.junkyu, name='junkyu'),
]