from django.shortcuts import render
from .models import Report


def report_dashboard(request):

    reports = Report.objects.all()

    return render(request, "reports/report_dashboard.html", {"reports": reports})