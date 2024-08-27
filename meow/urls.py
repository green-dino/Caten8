from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/create/', views.create_user, name='create_user'),
    path('trouble_tickets/', views.trouble_ticket_list, name='trouble_ticket_list'),
    # Add more URL patterns as needed
]