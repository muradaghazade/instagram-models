from django.urls import path
from accounts.views import test_account, register

app_name = 'accounts'


urlpatterns = [
    path('profile/<int:id>',test_account,name ='test_account'),
    path('register/',register,name ='register'),

]