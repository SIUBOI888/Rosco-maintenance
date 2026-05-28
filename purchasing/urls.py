from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.purchase_list
    ),

    path(
        'create/',
        views.create_purchase
    ),

    path(
        '<int:purchase_id>/status/<str:status>/',
        views.update_purchase_status
    ),

]