from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Spending(models.Model):
    date = models.DateField(default=timezone.now)
    amount = models.CharField(max_length=7, null=False)
    comment = models.TextField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}: {self.amount} for {self.category}, {self.comment}"

    class Meta:
        ordering = ['-date']


class Source(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Earning(models.Model):
    date = models.DateField(default=timezone.now)
    amount = models.CharField(max_length=7, null=False)
    comment = models.TextField(max_length=400)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}: {self.amount} from {self.source}, {self.comment}"

    class Meta:
        ordering = ['-date']
