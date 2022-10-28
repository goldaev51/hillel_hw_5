from django.db import models


class City(models.Model):
    name = models.CharField(max_length=60, help_text='Enter city name')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=60, help_text='Enter client name')
    product = models.ManyToManyField('Product', help_text="Select a product for this client")
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60, help_text='Enter product name')

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=60, help_text='Enter provider name')
    city = models.OneToOneField("City", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
