from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()


    def  __str__(self):
        return self.name


class Blogs(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog', blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    


class Internship(models.Model):
    fullname=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    number=models.IntegerField()
    collage_name=models.CharField(max_length=70)
    collage_REG_NO=models.CharField(max_length=70)
    offerstatus=models.CharField(max_length=70)
    startdate=models.CharField(max_length=80)
    enddate=models.CharField(max_length=90)
    proj_report=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.fullname
    
        
