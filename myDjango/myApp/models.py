from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Chai_Variety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','Masala'),
        ('PL','Plain'),
        ('SP','Spiced'),
        ('LM','Lemon'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description=models.TextField(default='')

    def __str__(self):
        return self.name
    
# One to Many
class ChaiReview(models.Model):
    RATING_CHOICES = [('1',1),('2',2),('3',3),('4',4),('5',5)]
    chai=models.ForeignKey(Chai_Variety,on_delete=models.CASCADE,related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Chai Review {{self.user.username}} for chai {{self.chai.name}}"
    
#Many to Many 
class ChaiStore(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varieties= models.ManyToManyField(Chai_Variety,related_name='stores')

    def __str__(self):
        return self.name

#one to one
class ChaiCertificate(models.Model):
    chai= models.OneToOneField(Chai_Variety,on_delete=models.CASCADE,related_name="certificate")
    certificate_number=models.CharField(max_length=100)
    issued_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Certificate for {self.chai.name}'
