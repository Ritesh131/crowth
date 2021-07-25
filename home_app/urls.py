from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('blog/<slug>', BlogView.as_view()),
    path('contact', ContactView.as_view()),
    path('thanks', ThankView.as_view()),
    path('query/submit', QuerySubmit.as_view()),
    path('loader', LoaderView.as_view()),
]
