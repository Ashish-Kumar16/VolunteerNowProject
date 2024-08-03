from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    reset_otp = models.CharField(max_length=6, blank=True, null=True)

    def generate_reset_otp(self):
        """Generate a new OTP and save it to the profile."""
        otp = get_random_string(length=6, allowed_chars='0123456789')
        self.reset_otp = otp
        self.save()
        return otp

    def __str__(self):
        return f"Profile for {self.user.username}"
