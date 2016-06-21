from django import forms
from app.models import Transaction


class TransferFunds(forms.ModelForm):
    amount = forms.DecimalField
    recipiant_account_number = forms.IntegerField()

    class Meta:
        model = Transaction
        fields = ["amount", "recipiant_account_number"]
