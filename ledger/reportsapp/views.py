from ledgerapp.models import Spending, Earning

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from django.shortcuts import render
from django.contrib import messages


def get_range(period):
    end = datetime.today()

    match period:
        case 'week':
            start = end - timedelta(weeks=1)
        case 'month':
            start = end - relativedelta(months=1)
        case 'year':
            start = end - relativedelta(years=1)

    return start, end


def render_reports(request):
    return render(request, 'reportsapp/report.html')


def generate_report(request):
    if request.method == 'POST':
        period = request.POST.get('period')
        if not period:
            messages.add_message(request, messages.ERROR, 'Please, choose a report period.')
            return render(request, 'reportsapp/report.html')

        start, end = get_range(period)
        spendings = Spending.objects.filter(date__range=[start, end])
        spendings_dict = {}
        for spending in spendings:
            amount_spent = spendings_dict.get(spending.category.name, 0)
            spendings_dict[spending.category.name] = float(spending.amount) + amount_spent

        earnings = Earning.objects.filter(date__range=[start, end])
        earnings_dict = {}
        for earning in earnings:
            amount_earned = earnings_dict.get(earning.source.name, 0)
            earnings_dict[earning.source.name] = float(earning.amount) + amount_earned

        total_spent = sum(spendings_dict.values())
        total_earned = sum(earnings_dict.values())
        saved = total_earned - total_spent

        return render(request, 'reportsapp/charts.html', {
            'spendings': spendings_dict,
            'earnings': earnings_dict,
            'total_spent': total_spent,
            'total_earned': total_earned,
            'saved': saved
        })
