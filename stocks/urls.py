from django.contrib import admin
from django.urls import path
from stocks import views
urlpatterns = [
    path('', views.weight_list, name='list'),
    path('companyList/', views.company_list, name='companyList'),
    path('calc/', views.calc_weights, name='calc'),

]