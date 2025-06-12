from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.new_listing, name='new_listing'),
    path('', views.home, name='home'),                     
    path('<int:listing_id>/', views.listing_detail, name='listing_detail'),
]
