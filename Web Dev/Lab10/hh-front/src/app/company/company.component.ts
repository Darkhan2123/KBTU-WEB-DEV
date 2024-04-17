import { Component, OnInit } from '@angular/core';
import { CompanyService, Company } from '../company-vacancy.service';

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {
  companies: Company[] = [];
  selectedCompany: Company | null = null;
  isEditing: boolean = false;

  constructor(private companyService: CompanyService) { }

  ngOnInit() {
    this.loadCompanies();
  }

   loadCompanies(): void {
    this.companyService.getCompanies().subscribe(data => {
      this.companies = data;
    }, error => {
      console.error('Error loading companies', error);
    });
  }

  selectCompany(company: Company): void {
    this.selectedCompany = { ...company };
    this.isEditing = true;
  }

  saveCompany(): void {
    if (!this.selectedCompany) return;
    const action = this.selectedCompany.id
      ? this.companyService.updateCompany(this.selectedCompany.id, this.selectedCompany)
      : this.companyService.createCompany(this.selectedCompany);

    action.subscribe({
      next: () => {
        this.loadCompanies();
        this.resetForm();
      },
      error: error => console.error('Error saving company', error)
    });
  }

  deleteCompany(id: number | undefined): void {
    this.companyService.deleteCompany(id).subscribe(() => {
      this.companies = this.companies.filter(company => company.id !== id);
      this.resetForm();
    }, error => {
      console.error('Error deleting company', error);
    });
  }

  resetForm(): void {
    this.selectedCompany = null;
    this.isEditing = false;
  }

  addNewCompany(): void {
    this.selectedCompany = { id: 0, name: '', description: '', city: '', address: '' };
    this.isEditing = false;
  }
}
