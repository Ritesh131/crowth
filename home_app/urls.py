from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('blog/<slug>', BlogView.as_view()),
    path('contact', ContactView.as_view()),
]
