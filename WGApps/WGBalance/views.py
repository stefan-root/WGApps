from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime

from .models import Transaction

# Create your views here.

def index(request):
    context = {
        'today': datetime.today().strftime('%Y-%m-%d')
    }
    return render(request, 'WGBalance/index.html', context)

def confirm(request):
    title = request.POST['titleField']
    comment = request.POST['commentField']
    amount = request.POST['amountField']
    date = request.POST['dateField']
    t = Transaction(
        title = title,
        comment = comment,
        amount = amount,
        date = date
    )
    t.save()
    context = {
        'title': title
    }
    return render(request, 'WGBalance/confirmation.html', context)