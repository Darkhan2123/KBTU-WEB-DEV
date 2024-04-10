from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list, name='companies'),
    path('companies/<int:id>', views.company_detail, name='company'),
    path('companies/<int:id>/vacancies/', views.company_vacancies, name='vacancies'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('vacancies/<int:id>', views.vacancy_details, name='vacancy'),
    path('vacancies/top_ten/', views.vacancy_top_ten, name='vacancy_sort'),
]