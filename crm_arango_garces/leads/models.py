from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    pass  


# Create your models here.

class Lead (models.Model):
    # SOURCE_CHOICES = {
    #     ('YT','Youtube'),
    #     ('Google','Google'),
    #     ('Newsletter','Newsletter'),
    #     ('Facebook','Facebook')
    # }
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.email}"

    # description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES)
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField()

class Agent (models.Model):  
        # name = models.CharField(max_length=50)
        # email = models.EmailField(max_length=50)
        # phone = models.CharField(max_length=50)
        user = models.OneToOneField(User, on_delete=models.CASCADE)

        def __str__(self):
            return self.user.username

