from django.urls import path

from schoolmanagement import views

urlpatterns = [
    path("", views.lista_scuole, name="lista_scuole"),
    path("<int:pk>/", views.dettaglio_scuola, name="dettaglio_scuola"),
]
