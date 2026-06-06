from django.urls import path
from . import views

urlpatterns = [

    path('', views.ticket_list, name='ticket_list'),

    path('create/', views.create_ticket, name='create_ticket'),

    path(
    '<int:ticket_id>/',
    views.ticket_detail
),
    

    path('<int:ticket_id>/status/<str:status>/',views.update_purchasing_status,),

    path('<int:ticket_id>/accept/',views.accept_ticket,),

    path('<int:ticket_id>/close/',views.close_ticket,),

    path(
    'maintenance-dashboard/',
    views.maintenance_dashboard
),

path(
    'purchasing-dashboard/',
    views.purchasing_dashboard
),



    path(
        'operator-dashboard/',
        views.operator_dashboard,
        name='operator_dashboard'
    ),

path(
    '<int:ticket_id>/request-materials/',
    views.request_materials,
    name='request_materials'
),

path(
    '<int:ticket_id>/submit-to-boss/',
    views.submit_to_boss,
    name='submit_to_boss'
),


path(
    'approval-dashboard/',
    views.approval_dashboard,
    name='approval_dashboard'
),

path(
    '<int:ticket_id>/approve/',
    views.approve_ticket,
    name='approve_ticket'
),
    

]
