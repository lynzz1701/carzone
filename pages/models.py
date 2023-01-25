from django.db import models

# Create your models here.

class teamMember(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fb_link = models.URLField(max_length=100)
    twi_link = models.URLField(max_length=100)
    gp_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.last_name + ", " + self.first_name