
from django.db import models
from django.contrib.auth.models import User   # ← importa el modelo de usuario

class Car(models.Model):
    MAKES = [
        ('toyota', 'Toyota'),
        ('honda', 'Honda'),
        ('nissan', 'Nissan'),
        # añade más…
    ]
    FUEL_CHOICES = [
        ('gasolina', 'Gasolina'),
        ('diesel', 'Diésel'),
        ('hibrido', 'Híbrido'),
        ('electrico', 'Eléctrico'),
    ]

    make        = models.CharField(max_length=30, choices=MAKES)
    model       = models.CharField(max_length=40)
    year        = models.PositiveIntegerField()
    mileage_km  = models.PositiveIntegerField()
    fuel_type   = models.CharField(max_length=10, choices=FUEL_CHOICES)
    price_clp   = models.IntegerField()
    image       = models.ImageField(upload_to='cars/', blank=True, null=True)
    seller      = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.make.title()} {self.model} ({self.year})"

