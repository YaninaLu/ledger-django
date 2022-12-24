from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('add_earning/', views.add_earning, name='add_earning'),
    path('earnings/', views.earnings, name='earnings'),
    path('delete_earning/<int:earning_id>', views.delete_earning, name='delete_earning'),
    path('spendings/', views.spendings, name='spendings'),
    path('add_spending/', views.add_spending, name='add_spending'),
    path('delete_spending/<int:spending_id>', views.delete_spending, name='delete_spending'),
]
