from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Home(models.Model):
    home_pic = models.FileField(name=None)
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    #home_pic = models.CharField(max_length_1000)

    def get_absolute_url(self):
        return reverse('index:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.street + '-' + self.city
