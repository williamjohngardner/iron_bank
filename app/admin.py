from django.contrib import admin
from app.models import Transaction

class PersonAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'amount', 'transaction_type', 'date', 'user')

admin.site.register(Transaction, PersonAdmin)
