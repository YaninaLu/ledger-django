from django.shortcuts import render, redirect
from django.contrib import messages


from ledgerapp.models import Earning, Source, Spending, Category
from ledgerapp.forms import SpendingForm, EarningForm


def main(request):
    return render(request, 'ledgerapp/index.html', {})


def earnings(request):
    earn = Earning.objects.all()
    return render(request, 'ledgerapp/earnings.html', {'earnings': earn})


def add_earning(request):
    if request.method == 'POST':
        form = EarningForm(request.POST)
        if form.is_valid():
            chosen_source = Source.objects.get(name__exact=request.POST.get('source'))
            earning = form.save(commit=False)
            earning.source = chosen_source
            earning.save()
            messages.add_message(request, messages.INFO, 'A new earning added successfully!')
            return redirect(to='ledgerapp:earnings')
        else:
            messages.add_message(request, messages.ERROR, 'Some info is invalid. '
                                                          'Make sure that the date is not in the future.')
            return redirect(to='ledgerapp:add_earning')

    sources = Source.objects.all()
    return render(request, 'ledgerapp/add_earning.html', {"sources": sources, "form": EarningForm()})


def delete_earning(request, earning_id):
    earn = Earning.objects.get(pk=earning_id)
    earn.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully!')
    return redirect(to='ledgerapp:earnings')


def spendings(request):
    spend = Spending.objects.all()
    return render(request, 'ledgerapp/spendings.html', {'spendings': spend})


def add_spending(request):
    if request.method == 'POST':
        form = SpendingForm(request.POST)
        if form.is_valid():
            chosen_category = Category.objects.get(name__exact=request.POST.get('category'))
            spending = form.save(commit=False)
            spending.category = chosen_category
            spending.save()
            messages.add_message(request, messages.INFO, 'A new spending added successfully!')
            return redirect(to='ledgerapp:spendings')
        else:
            messages.add_message(request, messages.ERROR, 'Some info is invalid. '
                                                          'Make sure that the date is not in the future.')
            return redirect(to='ledgerapp:add_spending')

    categories = Category.objects.all()
    return render(request, 'ledgerapp/add_spending.html', {"categories": categories, "form": SpendingForm()})


def delete_spending(request, spending_id):
    Spending.objects.get(pk=spending_id).delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully!')
    return redirect(to='ledgerapp:spendings')
