from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from app.models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class IndexView(TemplateView):
    template_name = "index.html"


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class ProfileView(ListView):
    template_name = "accounts/profile.html"

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    class Meta:
        ordering = ['-created']

    def acct_balance(self):
        self.balance = 0
        transactions = Transaction.objects.filter(user=self.request.user)
        for transaction in transactions:
            if transaction.transaction_type == 'CR':
                self.balance += transaction.amount
            elif transaction.transaction_type == 'DB':
                self.balance -= transaction.amount
        return self.balance
