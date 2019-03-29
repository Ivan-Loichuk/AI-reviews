import { Component, OnInit } from '@angular/core';
import { Hotel } from '../dto/hotel';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  hotels: Array<Hotel> = [];

  constructor(private http: HttpClient, private activeRoute: ActivatedRoute) {}

  ngOnInit() {
    this.activeRoute.params.subscribe((params: Params) => {

    });
  }

  searchHotel(city) {
    this.http.get<Array<Hotel>>('api/hotels/' + city).subscribe(data => this.hotels = data);
  }
}
