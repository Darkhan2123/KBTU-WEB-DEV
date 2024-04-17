import { Component, OnInit } from '@angular/core';
import {Company, CompanyService, Vacancy} from '../company-vacancy.service';

@Component({
  selector: 'app-vacancy',
  templateUrl: './vacancy.component.html',
  styleUrls: ['./vacancy.component.css']
})
export class VacancyComponent implements OnInit {
  companies: Company[] = [];
  vacancies: Vacancy[] = [];
  selectedVacancy: Vacancy | null = null;
  isEditing: boolean = false;

  constructor(private companyService: CompanyService) { }

  ngOnInit() {
    this.loadVacancies();
    this.loadCompanies();
  }

  loadCompanies(): void {
    this.companyService.getCompanies().subscribe(data => {
      this.companies = data;
    }, error => {
      console.error('Error loading companies', error);
    });
  }

  loadVacancies(): void {
    this.companyService.getAllVacancies().subscribe(data => {
      this.vacancies = data;
    }, error => {
      console.error('Error loading vacancies', error);
    });
  }

  selectVacancy(vacancy: Vacancy): void {
    this.selectedVacancy = { ...vacancy };
    this.isEditing = true;
  }

  saveVacancy(): void {
    if (!this.selectedVacancy) return;
    const action = this.selectedVacancy.id
      ? this.companyService.updateVacancy(this.selectedVacancy.id, this.selectedVacancy)
      : this.companyService.createVacancy(this.selectedVacancy);

    action.subscribe({
      next: () => {
        this.loadVacancies();
        this.resetForm();
      },
      error: error => console.error('Error saving vacancy', error)
    });
  }

  deleteVacancy(id: number | undefined): void {
    this.companyService.deleteVacancy(id).subscribe(() => {
      this.vacancies = this.vacancies.filter(vacancy => vacancy.id !== id);
      this.resetForm();
    }, error => {
      console.error('Error deleting vacancy', error);
    });
  }

  resetForm(): void {
    this.selectedVacancy = null;
    this.isEditing = false;
  }

  addNewVacancy(): void {
    this.selectedVacancy = { id: 0, name: '', description: '', salary: 0, company: null };
    this.isEditing = false;
  }
}
