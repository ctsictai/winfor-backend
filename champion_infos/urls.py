from django.urls import path
from .views import ListView, DetailView

urlpatterns = [
    path('/all', ListView.as_view()),
    path('/<int:champion_id>', DetailView.as_view()),
]
