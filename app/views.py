from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from app.models import Transaction
from app.forms import TransferFunds
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

class IndexView(TemplateView):
    template_name = "index.html"


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class CreateTransactionView(CreateView):
    model = Transaction
    fields = ["amount", "vendor", "transaction_type"]
    success_url = "/accounts/profile"

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user
        return super().form_valid(form)


class TransferFundsView(CreateView):
    model = Transaction
    fields = ["amount", "vendor"]
    success_url = "/accounts/profile"

    def form_valid(self, form):
        transaction = form.save(commit=False)
        vendor_pk = form.cleaned_data["vendor"]
        transaction.user = User.objects.get(id=vendor_pk)
        Transaction.objects.create(amount=transaction.amount, vendor='', transaction_type='DB', user=self.request.user)
        return super(TransferFundsView, self).form_valid(form)


class ProfileView(ListView):
    template_name = "accounts/profile.html"

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))


    def get_context_data(self):
        context = super().get_context_data()
        balance = 0
        transactions = Transaction.objects.filter(user=self.request.user)
        for transaction in transactions:
            print(transaction.transaction_type)
            if transaction.transaction_type == 'CR':
                balance += transaction.amount
            elif transaction.transaction_type == 'DB':
                balance -= transaction.amount
        context['balance'] = balance
        return context


class TransactionView(DetailView):
    model = Transaction
    template_name = "transaction_view.html"

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
