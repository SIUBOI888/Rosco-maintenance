from django.db import models

from django.contrib.auth.models import User

from tickets.models import Ticket

class Notification(models.Model):


    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.message

