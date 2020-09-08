from django.urls import path
from .views import password_generate, show_password

urlpatterns = [
    path('',password_generate,name='generate'),
    path('show/', show_password, name='show_password')
]
