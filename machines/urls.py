from django.urls import path
from . import views

urlpatterns = [

    path('create/', views.create_machine, name='create_machine'),

    path('<int:machine_id>/',
         views.machine_detail,
         name='machine_detail'),
    path(
    '<int:machine_id>/',
    views.machine_detail
),
    path(
    '',
    views.machine_list
),

]