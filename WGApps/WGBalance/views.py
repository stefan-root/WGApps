from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import *

# Create your views here.

@login_required(login_url='/WGBalance/accounts/login/')
def create_transaction(request):
    all_persons = Person.objects.all()
    context = {
        'created_by_email': request.user.email,
        'today': datetime.today().strftime('%Y-%m-%d'),
        'persons': all_persons
    }
    return render(request, 'WGBalance/create_transaction.html', context)

@login_required(login_url='/WGBalance/accounts/login/')
def view_transactions(request):
    person = Person.objects.get(user__id=request.user.id)
    debitor_transactions = Transaction.objects.filter(debitor=person)
    creditor_transactions = Transaction.objects.filter(creditor=person)
    context = {
        'debitor_transactions': debitor_transactions,
        'creditor_transactions': creditor_transactions,
    }
    return render(request, 'WGBalance/view_transactions.html', context)

@login_required(login_url='/WGBalance/accounts/login/')
def confirm(request):
    title = request.POST['titleField']
    comment = request.POST['commentField']
    amount = request.POST['amountField']
    date = request.POST['dateField']
    debitor_id = request.POST['debitorField']
    creditor_id = request.POST['creditorField']
    new_transaction = Transaction(
        title = title,
        comment = comment,
        amount = amount,
        date = date,
        debitor = Person.objects.get(id=debitor_id),
        creditor = Person.objects.get(id=creditor_id),
        created_by = Person.objects.get(user__id=request.user.id)
    )
    new_transaction.save()
    context = {
        'title': title
    }
    return render(request, 'WGBalance/confirmation.html', context)