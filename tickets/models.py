from django.db import models
from machines.models import Machine


PURCHASING_STATUS = [

    ('Pending', 'Pending'),

    ('Received', 'Received'),

    ('Ordered', 'Ordered'),

    ('In Transit', 'In Transit'),

    ('Delivered', 'Delivered'),

]

WORKFLOW_STATUS = [

    ('MAINTENANCE', 'Waiting for Maintenance'),

    ('PURCHASING', 'Waiting for Purchasing'),

    ('APPROVAL', 'Waiting for Approval'),

    ('APPROVED', 'Approved for Purchase'),

    ('DELIVERED', 'Materials Delivered'),

    ('CLOSED', 'Closed'),

]
class Ticket(models.Model):

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE
    )

    issue = models.TextField()

    created_by = models.CharField(
    max_length=100,
    blank=True,
    null=True
   )
    
    workflow_status = models.CharField(
    max_length=30,
    choices=WORKFLOW_STATUS,
    default='MAINTENANCE'
)
    
    maintenance_received_at = models.DateTimeField(
    blank=True,
    null=True
)

    sent_to_purchasing_at = models.DateTimeField(
        blank=True,
        null=True
    )

    purchase_request_created_at = models.DateTimeField(
        blank=True,
        null=True
    )

    approved_at = models.DateTimeField(
        blank=True,
        null=True
    )

    materials_delivered_at = models.DateTimeField(
        blank=True,
        null=True
    )

    photo = models.ImageField(
            upload_to='ticket_photos/',
            blank=True,
            null=True
        )

    purchasing_status = models.CharField(
            max_length=50,
            choices=PURCHASING_STATUS,
            default='Pending'
        )

    maintenance_accepted = models.BooleanField(
            default=False
        )

    maintenance_closed = models.BooleanField(
            default=False
        )

    created_at = models.DateTimeField(
            auto_now_add=True
        )

    closed_at = models.DateTimeField(
            blank=True,
            null=True
        )
    sent_to_approval_at = models.DateTimeField(
    null=True,
    blank=True
)
    
class MaterialRequest(models.Model):


    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='materials'
    )

    part_name = models.CharField(
        max_length=200
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

def __str__(self):

    return f"{self.part_name} x{self.quantity}"



def __str__(self):

        return f"{self.machine} - {self.issue}"