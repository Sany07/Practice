from django.db import models

# Create your models here.



class AddImage(models.Model):
    name=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='img')
    publish=models.BooleanField(default=True)
    


    def __str__(self):
        return self.name

