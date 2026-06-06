from django.urls import path

from . import views

urlpatterns = [


path(
    '',
    views.purchase_list
),

path(
    'create/<int:ticket_id>/',
    views.create_purchase,
    name='create_purchase'
),

path(
    'edit/<int:purchase_id>/',
    views.edit_purchase,
    name='edit_purchase'
),

path(
    'submit-to-boss/<int:purchase_id>/',
    views.submit_to_boss,
    name='submit_to_boss'
),

path(
    'approve/<int:purchase_id>/',
    views.approve_purchase,
    name='approve_purchase'
),

path(
    'reject/<int:purchase_id>/',
    views.reject_purchase,
    name='reject_purchase'
),

path(
    '<int:purchase_id>/status/<str:status>/',
    views.update_purchase_status
),

path(
'ordered/<int:purchase_id>/',
views.mark_ordered,
name='mark_ordered'
),

path(
'arrived/<int:purchase_id>/',
views.mark_arrived,
name='mark_arrived'
),

path(
'delivered/<int:purchase_id>/',
views.mark_delivered,
name='mark_delivered'
),

path(
'accept/<int:purchase_id>/',
views.accept_delivery,
name='accept_delivery'
),

]
