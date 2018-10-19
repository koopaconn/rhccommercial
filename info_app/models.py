from django.db import models

# Create your models here.
# Create your models here.
class model_testimonial(models.Model):
    person = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    quote = models.CharField(max_length=512,blank=True)
    personpic = models.ImageField()

    def __str__(self):
        return self.person

class model_job(models.Model):
    title = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    quote = models.CharField(max_length=512,blank=True)
    mainpic = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("info_app:jobdetails",kwargs={'pk':self.pk})

class model_jobpic(models.Model):
    pic = models.ImageField()
    job = models.ForeignKey(model_job,models.CASCADE,related_name='jobpic')

class model_jobnum(models.Model):
    number = models.CharField(max_length=128)

    def __str__(self):
        return self.number
