import uuid
from django.db import models

class User(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Auto-generates UID
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.uid})"

    class Meta:
        db_table = "blog_user"
        ordering = ["-date_joined"]
