from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('triangle/', views.triangle, name='triangle'),
]
