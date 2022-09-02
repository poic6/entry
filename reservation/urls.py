from django.urls import path
from . import views

app_name = "reservation"

urlpatterns = [
    path('', views.index, name="index"),
    path('reservation/', views.reservation, name="reservation"),
    path('check/<int:id>', views.check, name="check"),
    path('enter/', views.enter, name="enter"),
    path('enterChceck/', views.enterCheck, name="enterCheck"),
    path('reservation_create/', views.create, name="create"),
]