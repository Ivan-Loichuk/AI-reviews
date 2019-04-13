import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-breadcrumbs',
  templateUrl: './breadcrumbs.component.html',
  styleUrls: ['./breadcrumbs.component.scss']
})
export class BreadcrumbsComponent implements OnInit {
  
  @Input() city:string;
  @Input() hotel:object;
  @Input() hotel_type:string;
  @Input() static_text:string;
  page:number = 1;

  constructor(private router: Router) { 
  }

  ngOnInit() {
  }

  search(city, page=1) {
    city = city.toLowerCase();
    
    if (city === '') {
      this.router.navigate(['search/all/1']);
    } else
      this.router.navigate(['search/' + city + '/' + page]);
  }

  navigateHome() {
    this.router.navigate(['/home/']);
  }
  checkHotel(id) {
    this.router.navigate(['accommodation/' + id])
  }
  allReviews(id, page = 1) {
    this.router.navigate(['/reviews/' + id + '/' + page]);
  }
}
