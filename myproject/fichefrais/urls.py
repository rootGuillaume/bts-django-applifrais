from django.urls import path
from . import views

app_name = 'fichefrais'

urlpatterns = [
    path('nouveau/', views.nouveauFraisView, name='nouveau'),
    path('consulter/<int:id>/', views.consulterFraisView, name='consulter'),
]
