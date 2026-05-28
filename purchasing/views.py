from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import PurchaseRequest

from .forms import PurchaseRequestForm


def purchase_list(request):

    purchases = PurchaseRequest.objects.all()

    return render(
        request,
        'purchasing/purchase_list.html',
        {
            'purchases': purchases
        }
    )


def create_purchase(request):

    form = PurchaseRequestForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect('/purchasing/')

    return render(
        request,
        'purchasing/create_purchase.html',
        {
            'form': form
        }
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

    return redirect('/purchasing/')