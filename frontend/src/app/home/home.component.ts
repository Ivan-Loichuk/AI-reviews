import { Component, OnInit } from '@angular/core';
import { HttpClient } from '../../../node_modules/@angular/common/http';
import { Hotel } from '../dto/hotel';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  hotels: Array<Hotel> = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.getHotels();
  }

  getHotels() {
    this.http.get<Array<Hotel>>('api/all').subscribe(data => this.hotels = data);
  }
}
