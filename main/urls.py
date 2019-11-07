from django.urls import path
from .views import CheckLoginView, SearchView

urlpatterns=[
    path('/checklogin', CheckLoginView.as_view()),
    path('/search', SearchView.as_view()),
]
