from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('triangle/', views.triangle, name='triangle'),
    path('person-list/', views.PersonListView.as_view(), name='person-list'),
    path('person/', views.person, name='person'),
    path('person/<int:pk>', views.person_info, name='person-info'),
]
