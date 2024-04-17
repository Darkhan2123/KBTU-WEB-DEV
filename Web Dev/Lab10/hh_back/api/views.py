from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view

from .models import *
from .serializers import *

class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailAPIView(APIView):
    def get_object(self, pk=None):
        try:
            company = Company.objects.get(id=pk)
            return company
        except:
            return  Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    def put(self, request, pk=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk=None):
        company = self.get_object(pk)
        company.delete()
        return Response({'deleted': True})


@api_view(['GET'])
def company_vacancies(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company:
        return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

    vacancies = Vacancy.objects.filter(company=company)
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializers = VacancySerializer(vacancies, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = VacancySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vacancy_detail(request, pk=None):
    try:
        vacancy = Vacancy.objects.get(id=pk)
    except:
        return Response({'error': 'Vacancy does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VacancySerializer(
            instance=vacancy,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({'deleted': True})
