from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Logs(models.Model):
    path = models.CharField(max_length=200, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now=True)
    get_data = models.JSONField(null=False, blank=False)
    post_data = models.JSONField(null=False, blank=False)

    class RequestMethods(models.TextChoices):
        GET = 'ge', _('GET'),
        POST = 'po', _('POST'),
        HEAD = 'he', _('HEAD'),
        PUT = 'pu', _('PUT'),
        DELETE = 'de', _('DELETE'),
        CONNECT = 'co', _('CONNECT'),
        OPTIONS = 'op', _('OPTIONS'),
        TRACE = 'tr', _('TRACE'),
        PATCH = 'pa', _('PATCH'),

    method = models.CharField(max_length=2, choices=RequestMethods.choices, blank=False, default=RequestMethods.GET,
                              help_text='request_method')

    def __str__(self):
        return self.RequestMethods(self.method).name + ' - ' + self.path

    @admin.display(
        boolean=True,
        ordering='timestamp',
        description='Has GET data?',
    )
    def has_get_data(self):
        return False if self.get_data == '{}' else True

    @admin.display(
        boolean=True,
        ordering='timestamp',
        description='Has POST data?',
    )
    def has_post_data(self):
        return False if self.post_data == '{}' else True


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

    class Meta:
        ordering = ['-id']
