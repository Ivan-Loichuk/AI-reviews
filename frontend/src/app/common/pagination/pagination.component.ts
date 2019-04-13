import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-pagination',
  templateUrl: './pagination.component.html',
  styleUrls: ['./pagination.component.scss']
})
export class PaginationComponent implements OnInit {

  @Input() count_results:string;
  @Input() active_page:string;
  @Input() hotel:string;
  @Input() search_words:string;

  constructor(private router: Router) { }

  ngOnInit() {
  }

  search(city, page=1) {
    city = city.toLowerCase();
    
    if (city === '') {
      this.router.navigate(['search/all/1']);
    } else
      this.router.navigate(['search/' + city + '/' + page]);
  }
  
  allReviews(id, page = 1) {
    this.router.navigate(['/reviews/' + id + '/' + page]);
  }
}
