from django.urls import path
from .views import CheckLoginView, SearchView

urlpatterns=[
    path('/search', SearchView.as_view()),
]
