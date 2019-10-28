from django.db import models

# Create your models here.
class Account:
    email = models.CharField(max_length = 100, Unique = True)
    password= models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_add_now = True)
