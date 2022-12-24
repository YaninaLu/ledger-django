from django.forms import ModelForm, CharField, Textarea, DateField, ValidationError, TextInput, SelectDateWidget
from django.utils import timezone

from datetime import datetime

from ledgerapp import models


def validate_date(date):
    if date > timezone.now().date():
        raise ValidationError("Date cannot be later than today.")
    return date


class SpendingForm(ModelForm):
    date = DateField(required=True, validators=[validate_date], widget=SelectDateWidget)
    amount = CharField(max_length=7, required=True, widget=TextInput)
    comment = CharField(widget=Textarea, max_length=400)

    class Meta:
        model = models.Spending
        fields = ['date', 'amount', 'comment']
        exclude = ['category']


class EarningForm(ModelForm):
    date = DateField(required=True, validators=[validate_date], widget=SelectDateWidget)
    amount = CharField(max_length=7, required=True, widget=TextInput)
    comment = CharField(widget=Textarea, max_length=400)

    class Meta:
        model = models.Earning
        fields = ['date', 'amount', 'comment']
        exclude = ['source']
