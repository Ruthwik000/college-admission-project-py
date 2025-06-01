from django.urls import path
from . import views

app_name = 'colleges'

urlpatterns = [
    path('', views.college_list, name='college_list'),
    path('<int:college_id>/', views.college_detail, name='college_detail'),
    path('<int:college_id>/streams/', views.stream_list, name='stream_list'),
    path('stream/<int:stream_id>/', views.stream_detail, name='stream_detail'),
]
