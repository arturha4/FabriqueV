from django.db import models


class Mailing(models.Model):
    started_at = models.DateTimeField()
    message_text = models.TextField()
    mailing_filter = models.CharField(max_length=30)
    ended_at = models.DateTimeField()


class Customer(models.Model):
    phone = models.CharField(max_length=11, unique=True)
    operator_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=30)
    time_zone = models.CharField(max_length=30)


class Message(models.Model):
    sent_at = models.DateTimeField()
    sent = models.BooleanField(default=False)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name="messages")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="messages")
