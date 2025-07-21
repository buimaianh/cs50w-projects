from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Email(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='emails')
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name='emails_sent')
    recipients = models.ManyToManyField('User', related_name='emails_recieved')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    def serialize(self):
        return {
            'id': self.id,
            'sender': self.sender,
            'recipients': [recipient.email for recipient in self.recipients.all()],
            'subject': self.subject,
            'body': self.body,
            'timestamp': self.timestamp.isoformat(),
            'read': self.read,
            'archived': self.archived
        }
                