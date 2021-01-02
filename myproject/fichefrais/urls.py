from django.urls import path
from . import views

app_name = 'fichefrais'

urlpatterns = [
    path('nouveau/', views.nouveauFraisView, name='nouveau'),
    path('consulter/', views.consulterFraisView, name='consulter'),
]
