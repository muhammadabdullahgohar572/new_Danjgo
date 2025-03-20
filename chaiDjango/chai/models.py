from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Chaiverity(models.Model):
    CHAI_TYPE_CHOICE = [
        ("MASALA", "Masala"),
        ("GINGER", "Ginger"),
        ("KIWI", "Kiwi"),
        ("PLAIN", "Plain"),
        ("ELACHI", "Elachi"),
    ]

    name = models.CharField(max_length=50)  # Increased length
    image = models.ImageField(upload_to="chais/", max_length=100)  # File name limit fix
    time = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=10, choices=CHAI_TYPE_CHOICE)  # Increased length
    description = models.TextField(default="", blank=True, null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ChaiReview(models.Model):
    chai = models.ForeignKey(
        Chaiverity, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now())
    
    
    def __str__(self):
        return f'{self.user.username}reviews for {self.chai.name}'
    
    
class store(models.Model):
    name=models.CharField(max_length=100);
    location=models.CharField(max_length=100)
    chai_Chaiverity=models.ManyToManyField(Chaiverity,related_name='store')   
    
    def __str__(self):
        return self.name
    
    
    
class chaicertificate(models.Model):
    chai=models.OneToOneField(Chaiverity,on_delete=models.CASCADE,related_name='Certificate')
    certificate_number=models.CharField(max_length=100);
    issue_Date=models.DateTimeField(default=timezone.now)
    valid_untill=models.DateTimeField()


def __str__(self):
    return f'certificate for {self.name.chai}'
    
        
    