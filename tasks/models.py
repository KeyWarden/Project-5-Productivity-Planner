from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_at = models.DateField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    class Meta:
        ordering = ['due_at']

    def __str__(self):
        return f"{self.owner.username} - {self.title}"


def create_task(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(owner=instance)


# post_save.connect(create_profile, sender=User)
