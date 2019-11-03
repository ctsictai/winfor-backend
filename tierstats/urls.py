from django.urls import path
from .views      import TierstatsView

urlpatterns = [
    path('', TierstatsView.as_view()),
]

