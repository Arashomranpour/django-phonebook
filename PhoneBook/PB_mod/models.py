from django.db import models

# Create your models here.

class Contact(models.Model):
    username=models.CharField(max_length=40)
    phone=models.CharField(max_length=30,verbose_name="phone number")
    email=models.EmailField(max_length=30,verbose_name="email",blank=True,null=True)
    address=models.CharField(max_length=300,verbose_name="Address")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    
