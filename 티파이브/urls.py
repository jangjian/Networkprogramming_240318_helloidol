from django.urls import path

from 티파이브 import views

app_name = '티파이브'

urlpatterns = [
    path('<member>', views.show_member, name='member'),
    # path('jihoon/', views.show_jihoon, name='jihoon'),
    # path('junkyu/', views.show_junkyu, name='junkyu'),
]