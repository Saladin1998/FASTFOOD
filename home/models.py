from django.db import models


class Aboutus(models.Model):
    title = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.IntegerField(default=0, verbose_name="Phone number")
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def str(self):
        return self.title

class Chef(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    def str(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New','Yangi'),
        ('Read', 'Read'),
        ('Closed','Yopilgan')
    )
    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=30)
    phone = models.IntegerField(default=0, verbose_name="Phone number")
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
