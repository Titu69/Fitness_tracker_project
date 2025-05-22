from django.db import models


from django.contrib.auth.models import User
from mongoengine import Document,StringField,IntField,FloatField,EmailField

class Profile_sqll(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    username= models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()

class Profiles_mongo_data(Document):
    username = StringField(max_length=20, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(max_length=20, required=True)
    age = IntField()
    weight = FloatField()
    height = FloatField()
    def __str__(self):
        return f"{self.username} {self.email}{self.password}{self.age}{self.weight}{self.height}"