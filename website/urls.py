from django.urls import path
from .views import refresh_learn_ai, Refresh, PAGE, convert_image

API_VERSION = 'v1/'

urlpatterns = [
    path('', PAGE.as_view()),
    path('refresh', Refresh.as_view()),
    path(API_VERSION + 'convertImage', convert_image),
    path(API_VERSION + 'refresh_ai', refresh_learn_ai)
]