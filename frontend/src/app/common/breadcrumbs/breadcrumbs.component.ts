import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-breadcrumbs',
  templateUrl: './breadcrumbs.component.html',
  styleUrls: ['./breadcrumbs.component.scss']
})
export class BreadcrumbsComponent implements OnInit {
  
  @Input() city:string;
  @Input() name:string;
  @Input() hotel_type:string;

  constructor(private router: Router) { 
  }

  ngOnInit() {
  }

  search(city) {
    if (city === '') {
      this.router.navigate(['search/all']);
    } else
      this.router.navigate(['search/' + city]);
  }

  navigateHome() {
    this.router.navigate(['/home/']);
  }
}
