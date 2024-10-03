from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('sell/', views.sell_view, name='sell'),
    path('register/', views.register, name='register'),
]
