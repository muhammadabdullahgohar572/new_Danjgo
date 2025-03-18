from django.db import models
from django.utils import timezone
# Create your models here.
class Chaiverity(models.Model):
    CHAI_TYPE_CHOICE = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELACHI'),
   ]
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='chais/')
    time=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description=models.TextField(default='')
    price=models.IntegerField(default=0)
    
    
    def __str__(self):
          return self.name
