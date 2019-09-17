from django.urls import path
from generator import views


urlpatterns = [
    path('',views.index,name='index'),
    path('checker',views.checker,name='checker'),
]
