from django.urls import path, include
from food import views

urlpatterns = [
    path('home/',views.index,name="index"),
    path('details/<int:item_id>/',views.details,name="details"),
]

