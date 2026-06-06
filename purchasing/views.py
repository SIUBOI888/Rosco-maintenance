from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import PurchaseRequest
from .forms import PurchaseRequestForm
from .forms import PurchasingUpdateForm

from tickets.models import Ticket

def purchase_list(request):


    purchases = PurchaseRequest.objects.all()

    return render(
        request,
        'purchasing/purchase_list.html',
        {
            'purchases': purchases
        }
    )


def create_purchase(
    request,
    ticket_id
    ):


    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    form = PurchaseRequestForm(
        request.POST or None
    )

    if form.is_valid():

            purchase = form.save(
            commit=False
        )

            purchase.ticket = ticket

            purchase.save()

            return redirect(
            f'/tickets/{ticket.id}/'
        )
    return render(
            request,
            'purchasing/create_purchase.html',
            {
                'form': form,
                'ticket': ticket
            }
        )


def edit_purchase(
    request,
    purchase_id
    ):


    purchase = get_object_or_404(
        PurchaseRequest,
        id=purchase_id
    )

    form = PurchasingUpdateForm(
        request.POST or None,
        instance=purchase
    )

    if form.is_valid():

        form.save()

        return redirect(
            f'/tickets/{purchase.ticket.id}/'
        )

    return render(
        request,
        'purchasing/edit_purchase.html',
        {
            'form': form,
            'purchase': purchase
        }
    )


def submit_to_boss(
    request,
    purchase_id
    ):


    purchase = get_object_or_404(
        PurchaseRequest,
        id=purchase_id
    )

    purchase.status = 'Pending Approval'

    purchase.submitted_at = timezone.now()

    purchase.save()

    return redirect(
        f'/tickets/{purchase.ticket.id}/'
    )


def approve_purchase(
    request,
    purchase_id
    ):


    purchase = get_object_or_404(
        PurchaseRequest,
        id=purchase_id
    )

    purchase.status = 'Approved'

    purchase.approved_at = timezone.now()

    purchase.save()

    return redirect(
        f'/tickets/{purchase.ticket.id}/'
    )


def reject_purchase(
    request,
    purchase_id
    ):


    purchase = get_object_or_404(
        PurchaseRequest,
        id=purchase_id
    )

    purchase.status = 'Rejected'

    purchase.rejected_at = timezone.now()

    purchase.save()

    return redirect(
        f'/tickets/{purchase.ticket.id}/'
    )


def update_purchase_status(
    request,
    purchase_id,
    status
    ):


    purchase = get_object_or_404(
        PurchaseRequest,
        id=purchase_id
    )

    purchase.status = status

    purchase.save()

    return redirect(
        f'/tickets/{purchase.ticket.id}/'
    )
def mark_ordered(
request,
purchase_id
):


    purchase = get_object_or_404(
        PurchaseRequest,
        id=purchase_id
    )

    purchase.status = 'Ordered'

    purchase.save()

    return redirect(
        f'/tickets/{purchase.ticket.id}/'
    )


def mark_arrived(
request,
purchase_id
):


    purchase = get_object_or_404(
        PurchaseRequest,
        id=purchase_id
    )

    purchase.status = 'Arrived'

    purchase.save()

    return redirect(
        f'/tickets/{purchase.ticket.id}/'
    )


def mark_delivered(
request,
purchase_id
):


    purchase = get_object_or_404(
        PurchaseRequest,
        id=purchase_id
    )

    purchase.status = 'Delivered'

    purchase.save()

    return redirect(
        f'/tickets/{purchase.ticket.id}/'
    )


def accept_delivery(
request,
purchase_id
):


    purchase = get_object_or_404(
        PurchaseRequest,
        id=purchase_id
    )

    purchase.maintenance_accepted = True

    purchase.save()

    return redirect(
        f'/tickets/{purchase.ticket.id}/'
    )



