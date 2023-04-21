from django.urls import path
from core.views import mainpage

app_name = 'core'


urlpatterns = [
    path('',mainpage,name ='main'),
]