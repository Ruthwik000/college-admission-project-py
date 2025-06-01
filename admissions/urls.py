from django.urls import path
from . import views

app_name = 'admissions'

urlpatterns = [
    path('apply/<int:stream_id>/', views.apply_for_admission, name='apply'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('application/<int:application_id>/', views.application_detail, name='application_detail'),
    path('lists/', views.admission_lists, name='admission_lists'),
    path('lists/create/', views.create_admission_list, name='create_admission_list'),
    path('lists/<int:list_id>/publish/', views.publish_list, name='publish_list'),
    path('register/<int:application_id>/', views.register_admission, name='register_admission'),
    path('cancel/<int:application_id>/', views.cancel_admission, name='cancel_admission'),
]
