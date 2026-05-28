from django.db import models
from machines.models import Machine


PURCHASING_STATUS = [

    ('Pending', 'Pending'),

    ('Received', 'Received'),

    ('Ordered', 'Ordered'),

    ('In Transit', 'In Transit'),

    ('Delivered', 'Delivered'),

]


class Ticket(models.Model):

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE
    )

    issue = models.TextField()

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

    def __str__(self):

        return f"{self.machine} - {self.issue}"