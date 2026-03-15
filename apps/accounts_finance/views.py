from django.shortcuts import render
from .models import Transaction


def finance_dashboard(request):

    transactions = Transaction.objects.all()

    return render(request, "finance/finance_dashboard.html", {"transactions": transactions})