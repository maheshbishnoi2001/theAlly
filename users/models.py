from django.db import models

# Create your models here.

class allyuser(models.Model):
    username= models.CharField(max_length=50, primary_key = True, default='')
    password= models.CharField(max_length=50, default='')
    referral_code= models.CharField(max_length=50, default='')
    referral_count = models.IntegerField(default=0) 

    def __str__(self) -> str:
        return self.username
