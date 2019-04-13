import { Component, OnInit } from '@angular/core';
import { HttpClient } from '../../../node_modules/@angular/common/http';
import { Hotel } from '../dto/hotel';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  hotels: Array<Hotel> = [];
  filters: Object = {};

  constructor(private http: HttpClient, private router: Router) {
    // jak dodasz limit do sql wyszukiwania to zamienić Zakopane na "" i dodać this.filters['limit'] = 3
    this.filters['city'] = "Zakopane";
    this.filters['types'] = [];

    this.searchHotel(this.filters);
   }

  ngOnInit() {
    this.getHotels();
  }

  getHotels() {
    //this.http.get<Array<Hotel>>('api/all').subscribe(data => this.hotels = data);
  }

  search(city, page=1) {
    if (city === '') {
      this.router.navigate(['search/all/1']);
    } else
      this.router.navigate(['search/' + city + '/' + page]);
  }

   searchHotel(filters) {
     this.http.post<Array<Hotel>>('api/hotels/search', filters).subscribe(data => this.hotels = data);
   }
   checkHotel(id) {
    this.router.navigate(['accommodation/' + id])
  }
}
