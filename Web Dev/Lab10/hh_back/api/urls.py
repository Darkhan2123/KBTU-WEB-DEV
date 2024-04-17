from django.urls import path
from .views import CompanyListAPIView, CompanyDetailAPIView, vacancy_list, vacancy_detail, company_vacancies

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view(), name='companies'),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view(), name='company'),
    path('companies/<int:pk>/vacancies/', company_vacancies, name='vacancies'),
    path('vacancies/', vacancy_list, name='vacancies'),
    path('vacancies/<int:pk>/', vacancy_detail, name='vacancy'),
]
