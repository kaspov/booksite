from django.urls import path, include

from book.views import home

urlpatterns = [
        path('',home, name='home')
]
