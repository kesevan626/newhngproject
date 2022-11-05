from django.urls import path
from.views import Home, performOperation

urlpatterns = [
    path("", Home, name='home'),
    path("operate/", performOperation, name="math-Operation"),
]
