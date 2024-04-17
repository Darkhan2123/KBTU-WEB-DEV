import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Router } from '@angular/router'
import { Observable } from "rxjs";

export interface Company {
  id?: number;
  name: string;
  description: string;
  city: string;
  address: string;
}
export interface Vacancy {
  id: any;
  name: string;
  description: string;
  salary: number;
  company: number | null ;
}
@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  private baseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) { }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.baseUrl}/companies/`);
  }

  getCompany(id: number): Observable<Company> {
    return this.http.get<Company>(`${this.baseUrl}/companies/${id}/`);
  }

  createCompany(company: Company): Observable<Company> {
    return this.http.post<Company>(`${this.baseUrl}/companies/`, company);
  }

  updateCompany(id: number, company: Company): Observable<Company> {
    return this.http.put<Company>(`${this.baseUrl}/companies/${id}/`, company);
  }

  deleteCompany(id: number | undefined): Observable<any> {
    return this.http.delete(`${this.baseUrl}/companies/${id}/`);
  }


  getCompanyVacancies(id: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.baseUrl}/companies/${id}/vacancies/`);
  }

  /*---------------------------------*/

  getAllVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.baseUrl}/vacancies/`);
  }

  createVacancy(vacancy: Vacancy): Observable<Vacancy> {
    return this.http.post<Vacancy>(`${this.baseUrl}/vacancies/`, vacancy);
  }

  getVacancy(id: number): Observable<Vacancy> {
    return this.http.get<Vacancy>(`${this.baseUrl}/vacancies/${id}/`);
  }

  updateVacancy(id: number, vacancy: Vacancy): Observable<Vacancy> {
    return this.http.put<Vacancy>(`${this.baseUrl}/vacancies/${id}/`, vacancy);
  }

  deleteVacancy(id: number | undefined): Observable<any> {
    return this.http.delete(`${this.baseUrl}/vacancies/${id}/`);
  }
}
