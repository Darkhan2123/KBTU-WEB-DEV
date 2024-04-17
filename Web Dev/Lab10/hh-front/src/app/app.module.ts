import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { CommonModule } from "@angular/common";
import { AppComponent } from './app.component';
import { CompanyComponent } from './company/company.component';
import { VacancyComponent } from "./vacancy/vacancy.component";
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    CompanyComponent,
    VacancyComponent,
    HomeComponent,
  ],
  imports: [
    BrowserModule,
    CommonModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
