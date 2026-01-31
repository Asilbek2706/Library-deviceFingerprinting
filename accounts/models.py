from django.db import models
from django.contrib.auth.models import User

class UserDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255, null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'device_id')
        verbose_name = "Foydalanuvchi qurilmasi"
        verbose_name_plural = "Foydalanuvchi qurilmalari"