from django.urls import path
from .views import convert_image
from .views import PAGE

API_VERSION = 'v1/'

urlpatterns = [
    path('', PAGE.as_view()),
    path(API_VERSION + 'convertImage', convert_image),
]