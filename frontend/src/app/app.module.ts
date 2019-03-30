import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AlertModule } from 'ngx-bootstrap';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { HomeComponent } from './home/home.component';
import { AppRoutingModule } from './app-routing.module';
import { SearchComponent } from './search/search.component';
import { FiltersComponent } from './search/filters/filters.component';
import { ResultsComponent } from './search/results/results.component';
import { RatingStarsComponent } from './common/rating-stars/rating-stars.component';
import { PaginationComponent } from './common/pagination/pagination.component';
import { AccommodationComponent } from './accommodation/accommodation.component';
import { BreadcrumbsComponent } from './common/breadcrumbs/breadcrumbs.component';
import { ReviewsComponent } from './accommodation/reviews/reviews.component';
import { RatingSummaryComponent } from './accommodation/rating-summary/rating-summary.component';
import { ReviewsAllComponent } from './reviews-all/reviews-all.component';
import { AuthorizationComponent } from './modal-windows/authorization/authorization.component';
import { AddReviewComponent } from './modal-windows/add-review/add-review.component';
import { AdminComponent } from './admin/admin.component';
import { TopNavComponent } from './admin/partial/top-nav/top-nav.component';
import { LeftNavComponent } from './admin/partial/left-nav/left-nav.component';
import { AccommodationListComponent } from './admin/accommodation-list/accommodation-list.component';
import { AddAccommodationComponent } from './modal-windows/add-accommodation/add-accommodation.component';
import { UsersComponent } from './admin/users/users.component';
import { LoginComponent } from './admin/login/login.component';
import { DelAccommodationComponent } from './modal-windows/del-accommodation/del-accommodation.component';
import { EditAccommodationComponent } from './modal-windows/edit-accommodation/edit-accommodation.component';
import { DelUserComponent } from './modal-windows/del-user/del-user.component';
import { EditUserComponent } from './modal-windows/edit-user/edit-user.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '../../node_modules/@angular/forms';
import { FilterService } from './search/filters/filter.service';
import { Storage } from './shared/storage';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    SearchComponent,
    FiltersComponent,
    ResultsComponent,
    RatingStarsComponent,
    PaginationComponent,
    AccommodationComponent,
    BreadcrumbsComponent,
    ReviewsComponent,
    RatingSummaryComponent,
    ReviewsAllComponent,
    AuthorizationComponent,
    AddReviewComponent,
    AdminComponent,
    TopNavComponent,
    LeftNavComponent,
    AccommodationListComponent,
    AddAccommodationComponent,
    UsersComponent,
    LoginComponent,
    DelAccommodationComponent,
    EditAccommodationComponent,
    DelUserComponent,
    EditUserComponent
  ],
  imports: [
    BrowserModule,
    AlertModule.forRoot(),
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [FilterService, Storage],
  bootstrap: [AppComponent]
})
export class AppModule { }
