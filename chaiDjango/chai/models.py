from django.db import models
from django.utils import timezone

class Chaiverity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('MASALA', 'Masala'),
        ('GINGER', 'Ginger'),
        ('KIWI', 'Kiwi'),
        ('PLAIN', 'Plain'),
        ('ELACHI', 'Elachi'),
    ]

    name = models.CharField(max_length=50)  # Increased length
    image = models.ImageField(upload_to='chais/', max_length=100)  # File name limit fix
    time = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=10, choices=CHAI_TYPE_CHOICE)  # Increased length
    description = models.TextField(default='', blank=True, null=True)

    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
