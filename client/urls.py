from django.urls import path
from client import views

urlpatterns = [
    # Production
    path('list/',
         views.ClientListView.as_view(),
         name='client_list'),
]

