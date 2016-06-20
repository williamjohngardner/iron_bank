from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    CREDIT = 'CR'
    DEBIT = 'DB'

    TRANSACTION_CHOICES = ((CREDIT, 'CR'),(DEBIT, 'DB'))

    amount = models.DecimalField(max_digits=6, decimal_places=2)
    vendor = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_CHOICES, default=CREDIT,)

    def __str__(self):
        return self.vendor
