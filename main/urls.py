from django.urls import path
from main.views import show_main, show_credentials

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('', show_credentials, name='show_credentials'),
]

