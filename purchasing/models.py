from django.db import models

from tickets.models import Ticket


PURCHASE_STATUS = [

    ('Pending', 'Pending'),

    ('Ordered', 'Ordered'),

    ('In Transit', 'In Transit'),

    ('Delivered', 'Delivered'),

]


class PurchaseRequest(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE
    )

    part_name = models.CharField(
        max_length=100
    )

    quantity = models.IntegerField()

    supplier = models.CharField(
        max_length=100,
        blank=True
    )

    estimated_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    eta = models.DateField(
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=50,
        choices=PURCHASE_STATUS,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.part_name