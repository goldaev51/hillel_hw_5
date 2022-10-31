from django.db import models
from django.urls import reverse


class Person(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('forms:person-info', args=[str(self.id)])
