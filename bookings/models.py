from django.db import models

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('Brand Shoot', 'Brand Shoot'),
        ('Advertisement Shoot', 'Advertisement Shoot'),
        ('Wedding Shoot', 'Wedding Shoot'),
        ('Film Production', 'Film Production'),
        ('Video Editing', 'Video Editing'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name