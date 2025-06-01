from django.urls import path
from . import views

app_name = 'cutoffs'

urlpatterns = [
    path('', views.cutoff_list, name='cutoff_list'),
    path('create/', views.create_cutoff, name='create_cutoff'),
    path('<int:cutoff_id>/edit/', views.edit_cutoff, name='edit_cutoff'),
    path('<int:cutoff_id>/delete/', views.delete_cutoff, name='delete_cutoff'),
    path('compare/', views.compare_cutoffs_view, name='compare_cutoffs'),
]
