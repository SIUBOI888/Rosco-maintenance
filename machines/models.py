from django.db import models

class Machine(models.Model):


    MACHINE_TYPES = [

        ('CNC', 'CNC'),

        ('Lathe', 'Lathe'),

        ('Conveyor', 'Conveyor'),

        ('Press', 'Press'),

        ('Packaging', 'Packaging'),

    ]

    machine_code = models.CharField(
        max_length=50
    )

    machine_name = models.CharField(
        max_length=100
    )

    machine_type = models.CharField(
        max_length=50,
        choices=MACHINE_TYPES,
        default='CNC'
    )

    location = models.CharField(
        max_length=100
    )

    date_installed = models.DateField()

    machine_photo = models.ImageField(
        upload_to='machine_photos/',
        blank=True,
        null=True
    )

    def __str__(self):

        return f"{self.machine_code} - {self.machine_type}"

