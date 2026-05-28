from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from purchasing.models import PurchaseRequest
from notifications.models import Notification

from django.contrib.auth.models import User
from notifications.models import Notification

from django.contrib.auth.models import User


def is_mechanic(user):

    return (
        user.is_superuser
        or
        user.groups.filter(
            name='Mechanic'
        ).exists()
    )


def is_purchasing(user):

    return (
        user.is_superuser
        or
        user.groups.filter(
            name='Purchasing'
        ).exists()
    )
    
@login_required
def ticket_list(request):


    tickets = Ticket.objects.filter(
        maintenance_closed=False
    )

    return render(
        request,
        'tickets/ticket_list.html',
        {
            'tickets': tickets
        }
    )


  

@login_required
@user_passes_test(is_mechanic)
def create_ticket(request):

    form = TicketForm(
    request.POST or None,
    request.FILES or None
)

    if form.is_valid():
        ticket = form.save()

        purchasing_users = User.objects.filter(
        groups__name='Purchasing'
        )

        for user in purchasing_users:

         Notification.objects.create(
            recipient=user,
            ticket=ticket,
            message=f'New maintenance ticket for {ticket.machine}'
        )

        return redirect('ticket_list')

    return render(request, 'tickets/create_ticket.html', {
        'form': form
    })

@login_required
@user_passes_test(is_purchasing)
def update_purchasing_status(request, ticket_id, status):


    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    ticket.purchasing_status = status

    ticket.save()

    if status == 'Delivered':

        mechanic_users = User.objects.filter(
            groups__name='Mechanic'
        )

        for user in mechanic_users:

            Notification.objects.create(
                recipient=user,
                ticket=ticket,
                message=f'Parts delivered for {ticket.machine}'
            )

    return redirect('/tickets/purchasing-dashboard/')



@login_required
@user_passes_test(is_mechanic)
def accept_ticket(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    ticket.maintenance_accepted = True

    ticket.save()

    return redirect('/tickets/')

@login_required
@user_passes_test(is_mechanic)
def close_ticket(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    ticket.maintenance_closed = True

    ticket.closed_at = timezone.now()

    ticket.save()

    return redirect('/tickets/')
@login_required
@user_passes_test(is_mechanic)
def maintenance_dashboard(request):

    tickets = Ticket.objects.filter(
    maintenance_closed=False
)

    return render(
        request,
        'tickets/maintenance_dashboard.html',
        {
            'tickets': tickets
        }
    )
@login_required
@user_passes_test(is_purchasing)
def purchasing_dashboard(request):


    tickets = Ticket.objects.filter(
        maintenance_closed=False
    ).exclude(
        purchasing_status='Delivered'
    )

    return render(
        request,
        'tickets/purchasing_dashboard.html',
        {
            'tickets': tickets
        }
    )





def ticket_detail(request, ticket_id):


    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    purchases = PurchaseRequest.objects.filter(
        ticket=ticket
    )

    return render(
        request,
        'tickets/ticket_detail.html',
        {
            'ticket': ticket,
            'purchases': purchases
        }
    )

