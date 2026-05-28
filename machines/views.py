from django.shortcuts import render, redirect, get_object_or_404

from .models import Machine
from .forms import MachineForm

from tickets.models import Ticket
from tickets.models import Ticket
from purchasing.models import PurchaseRequest
from django.db.models import Sum


def create_machine(request):

    form = MachineForm(
    request.POST or None,
    request.FILES or None
)

    if form.is_valid():

        form.save()

        return redirect('/tickets/create/')

    return render(request, 'machines/create_machine.html', {
        'form': form
    })


def machine_detail(request, machine_id):

    machine = get_object_or_404(
        Machine,
        id=machine_id
    )

    tickets = Ticket.objects.filter(
        machine=machine
    ).order_by('-created_at')

    total_tickets = tickets.count()

    return render(request, 'machines/machine_detail.html', {
        'machine': machine,
        'tickets': tickets,
        'total_tickets': total_tickets,
    })

def machine_detail(request, machine_id):

    machine = Machine.objects.get(
        id=machine_id
    )

    tickets = Ticket.objects.filter(
        machine=machine
    )

    closed_tickets = tickets.filter(
        maintenance_closed=True
    )

    active_tickets = tickets.filter(
        maintenance_closed=False
    )

    total_cost = PurchaseRequest.objects.filter(
        ticket__machine=machine
    ).aggregate(
        Sum('estimated_cost')
    )['estimated_cost__sum']

    last_serviced = closed_tickets.order_by(
        '-closed_at'
    ).first()

    return render(
        request,
        'machines/machine_detail.html',
        {
            'machine': machine,
            'active_tickets': active_tickets,
            'closed_tickets': closed_tickets,
            'total_cost': total_cost,
            'last_serviced': last_serviced,
        }
    )
def machine_list(request):

    machines = Machine.objects.all()

    return render(
        request,
        'machines/machine_list.html',
        {
            'machines': machines
        }
    )