# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_playbook, name='create_playbook'),
    path('<int:playbook_id>/', views.get_playbook, name='get_playbook'),
    path('<int:playbook_id>/graph/', views.create_playbook_graph, name='create_playbook_graph'),
    path('<int:playbook_id>/interactive_graph/', views.create_interactive_playbook_graph, name='create_interactive_playbook_graph'),
]