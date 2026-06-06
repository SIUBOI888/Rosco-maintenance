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


    if request.user.groups.filter(
    name='Operator'
).exists():

        tickets = Ticket.objects.filter(
        created_by=request.user.username
    )

    else:

        tickets = Ticket.objects.all()

    return render(
    request,
    'tickets/ticket_list.html',
    {
        'tickets': tickets
    }
)


  

@login_required
def create_ticket(request):


    form = TicketForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():

        ticket = form.save(commit=False)

        ticket.created_by = request.user.username

        ticket.workflow_status = 'MAINTENANCE'

        ticket.save()

        purchasing_users = User.objects.filter(
            groups__name='Mechanic'
        )

        for user in purchasing_users:

            Notification.objects.create(
                recipient=user,
                ticket=ticket,
                message=f'New maintenance ticket submitted for {ticket.machine}'
            )

        return redirect('ticket_list')

    return render(
        request,
        'tickets/create_ticket.html',
        {
            'form': form
        }
    )



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
    workflow_status='MAINTENANCE'
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

@login_required
def operator_dashboard(request):


    return render(
    request,
    'tickets/operator_dashboard.html'
)


@login_required
@user_passes_test(is_mechanic)
def request_materials(request, ticket_id):


    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    ticket.workflow_status = 'PURCHASING'

    ticket.sent_to_purchasing_at = timezone.now()

    ticket.save()

    purchasing_users = User.objects.filter(
        groups__name='Purchasing'
    )

    for user in purchasing_users:

        Notification.objects.create(
            recipient=user,
            ticket=ticket,
            message=f'Materials requested for {ticket.machine}'
        )

    return redirect(
        '/tickets/maintenance-dashboard/'
    )

@login_required
@user_passes_test(is_purchasing)
def submit_to_boss(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    ticket.workflow_status = 'APPROVAL'

    ticket.sent_to_approval_at = timezone.now()

    ticket.save()

    return redirect(
        f'/tickets/{ticket.id}/'
    )


@login_required
def approval_dashboard(request):

    if not is_boss(request.user):

        return redirect('/tickets/')

    tickets = Ticket.objects.filter(
        workflow_status='APPROVAL'
    )

    return render(
        request,
        'tickets/approval_dashboard.html',
        {
            'tickets': tickets
        }
    )

@login_required
def approve_ticket(request, ticket_id):

    if not is_boss(request.user):

        return redirect('/tickets/')

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    ticket.workflow_status = 'APPROVED'

    ticket.approved_at = timezone.now()

    ticket.save()

    return redirect(
        '/tickets/approval-dashboard/'
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
def is_boss(user):

    return (
        user.is_superuser
        or
        user.groups.filter(
            name='Boss'
        ).exists()
    )

