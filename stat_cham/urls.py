from django.urls import path
from .views import StatChampionsView

urlpatterns = [
    path('/champion', StatChampionsView.as_view()),
]
