from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paypal_email = models.EmailField()

    def __str__(self):
        fullname = self.user.first_name + " " + self.user.last_name
        return(fullname)

class AccountingPeriod(models.Model):
    startdate = models.DateField
    enddate = models.DateField

    def __str__(self):
        title = self.startdate + " - " + self.enddate
        return(title)

class Bill(models.Model):
    accounting_period = models.ForeignKey(AccountingPeriod, on_delete=models.PROTECT)
    debitor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bill_debitor')
    creditor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bill_creditor')
    total = models.DecimalField(max_digits=7, decimal_places=2)
    settled_at = models.DateField()

    def __str__(self):
        title = self.accounting_period.startdate + " - " + self.accounting_period.enddate
        return(title)

class Transaction(models.Model):
    date = models.DateField()
    title = models.CharField(max_length = 60)
    created_by = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='transaction_creator')
    comment = models.TextField(null=True)
    debitor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='transaction_debitor')
    creditor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='transaction_creditor')
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return(self.title)

