import { Component, OnInit } from '@angular/core';
import { Hotel } from '../dto/hotel';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-accommodation',
  templateUrl: './accommodation.component.html',
  styleUrls: ['./accommodation.component.scss']
})
export class AccommodationComponent implements OnInit {
  hotel: Hotel;

  constructor(private http: HttpClient, private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    this.activatedRoute.params.subscribe((params: Params) => {
      this.getHotel(params['id']);
    });
  }

  getHotel(id) {
    this.http.get<Hotel>('api/hotel/' + id).subscribe(data => this.hotel = data);
  }
}
