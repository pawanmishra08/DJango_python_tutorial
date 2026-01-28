from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Student(models.Model):
    # id = models.AutoField() // It is created automatically
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(null= True , blank= True)
    address = models.TextField(null= True , blank= True)
    # file = models.FileField()

class Car(models.Model):
        car_name = models.CharField(max_length = 500)
        speed = models.IntegerField(default=50)

        def __str__(self) -> str:
              return self.car_name

#signals
#pre_save , post_save , pre_delete , post_delete

@receiver(post_save, sender= Car)
def call_car_api(sender, instance, **kwargs):
      print("CAR OBJECT CREATED")
      print(sender, instance, kwargs)