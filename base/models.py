from django.db import models

# Create your models here.



class Enquiry(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    email= models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message= models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
