from django.urls import path
from reportsapp import views


urlpatterns = [
    path('', views.render_reports, name='main'),
    path('generate_report/', views.generate_report, name='generate_report'),
]