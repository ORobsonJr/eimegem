from django.urls import path
from .views import PAGE, convert_image, text_correction

API_VERSION = 'v1/'

urlpatterns = [
    path('', PAGE.as_view()),
    path(API_VERSION + 'convertImage', convert_image),
    path(API_VERSION + 'correct_text', text_correction)
]