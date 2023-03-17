from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User


class UserInfo(BaseModel):
    USER_TYPE = (
        ('Lawyer', 'Lawyer'),
        ('Client', 'Client'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')
    user_type = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/profile_pic', blank=True, null=True)
    phone_num = models.CharField(max_length=12, blank=True, null=True)
    billing_rate = models.IntegerField(blank=True, null=True)
    speciality = models.TextField(blank=True, null=True)

    def lawyers(self):
        return UserInfo.objects.filter(user_type="Lawyer")
