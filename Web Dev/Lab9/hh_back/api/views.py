from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Company, Vacancy
# Create your views here.

#/api/companies - List of all Companies
#/api/companies/<int:id>/ - Get one Company
#/api/companies/<int:id>/vacancies/ - List of Vacancies by Company
#/api/vacancies/ - List of all Vacancies
#/api/vacancies/<int:id>/ - Get one Vacancy
#/api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary

def company_list(request):
   companies = Company.objects.all()
   data = {'companies': list(companies.values())}
   return JsonResponse(data)

def company_detail(request, id):
    company = get_object_or_404(Company, pk=id)
    data = {'company': model_to_dict(company)}
    return JsonResponse(data)

def company_vacancies(request, id):
    company = get_object_or_404(Company, pk=id)
    vacancies = Vacancy.objects.filter(company=company)
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)

def vacancies(request):
    vacancy = Vacancy.objects.all()
    data = {'vacancy': list(vacancy.values())}
    return JsonResponse(data)

def vacancy_details(request, id):
    vacancy = get_object_or_404(Vacancy, pk=id)
    data = {'vacancy': model_to_dict(vacancy)}
    return JsonResponse(data)

def vacancy_top_ten(request):
    top_vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = {'vacancies': list(top_vacancies.values())}
    return JsonResponse(data)