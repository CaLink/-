from django.urls import path
from main import views

urlpatterns = [
    path('car/', views.car),
    path('car/<int:pk>/', views.car_current),
    path('update/', views.start_scrapping),
]