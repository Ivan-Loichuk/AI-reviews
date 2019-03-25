import { Component, OnInit } from '@angular/core';
import { HttpClient } from '../../../node_modules/@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  hotels = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.getHotels();
  }

  getHotels() {
    this.http.get('api/all').subscribe(data => console.log(data));
  }
}
