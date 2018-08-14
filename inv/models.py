from django.db import models
from django.utils import timezone


class Inv(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
#    published_date = models.DateTimeField(
#            blank=True, null=True)
    hostname = models.CharField(max_length=15,
            default=None) #NetBIOS name max=15
    ip4address = models.CharField(max_length=15,
            default=None) #255.255.255.255
    macaddress = models.CharField(max_length=17,
            default=None) #00-07-e9-31-4c-f9 (без -)
    loginInRDP = models.DateTimeField(
            blank=True, null=True)

    def LoginInRDP(self):
        self.LoginInRDP = timezone.now()
        self.save()

    def __str__(self):
        return self.title