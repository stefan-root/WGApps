from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(AccountingPeriod)
admin.site.register(Person)
admin.site.register(Bill)
admin.site.register(Transaction)
