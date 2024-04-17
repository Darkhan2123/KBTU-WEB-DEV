import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CompanyComponent } from './company/company.component';
import {VacancyComponent} from "./vacancy/vacancy.component";
import {HomeComponent} from "./home/home.component";

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'companies', component: CompanyComponent },
  { path: 'vacancies', component: VacancyComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
