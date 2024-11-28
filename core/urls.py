from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index.as_view(), name="core_index"),
    path('create/', views.create.as_view(), name="core_create"),
]

htmxpatterns = [
    path('metry/', views.metry, name="htmx_metry"),
    path('delete/<int:pk>', views.delete, name="htmx_delete"),
    path('put/<int:pk>', views.puts, name="htmx_put"),
    path('search_filter', views.filter_search, name="htmx_search")
]

urlpatterns += htmxpatterns
