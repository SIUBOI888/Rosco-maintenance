from django.db import models

from tickets.models import Ticket

PURCHASE_STATUS = [


('Draft', 'Draft'),

('Pending Approval', 'Pending Approval'),

('Approved', 'Approved'),

('Rejected', 'Rejected'),

('Ordered', 'Ordered'),

('Arrived', 'Arrived'),

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
        blank=True,
        null=True
    )

    estimated_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
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
        default='Draft'
    )

    submitted_at = models.DateTimeField(
        blank=True,
        null=True
    )

    approved_at = models.DateTimeField(
        blank=True,
        null=True
    )

    rejected_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    maintenance_accepted = models.BooleanField(
    default=False
    )

    def __str__(self):

        return self.part_name

