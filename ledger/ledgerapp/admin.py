from django.contrib import admin
from ledgerapp.models import Spending, Earning, Category, Source


admin.site.register(Spending)
admin.site.register(Earning)
admin.site.register(Category)
admin.site.register(Source)
