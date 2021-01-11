from django.urls import path
from . import views

app_name = 'suivi'

urlpatterns = [
    path('visiteur/', views.suiviVisiteurView, name='suivi-visiteur'),
    path('comptable/', views.suiviComptableView, name='suivi-comptable'),
]
