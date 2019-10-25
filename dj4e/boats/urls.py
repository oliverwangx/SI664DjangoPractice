from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
app_name='boats'
urlpatterns = [
    path('', views.BoatList.as_view(), name='all'),
    path('main/create/', views.BoatCreate.as_view(), name='boat_create'),
    path('main/<int:pk>/update/', views.BoatUpdate.as_view(), name='boat_update'),
    path('main/<int:pk>/delete/', views.BoatDelete.as_view(), name='boat_delete'),
    path('lookup/', views.TypeView.as_view(), name='type_list'),
    path('lookup/create/', views.TypeCreate.as_view(), name='type_create'),
    path('lookup/<int:pk>/update/', views.TypeUpdate.as_view(), name='type_update'),
    path('lookup/<int:pk>/delete/', views.TypeDelete.as_view(), name='type_delete'),
]