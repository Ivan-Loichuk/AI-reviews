import { Component, OnInit } from '@angular/core';
import { Hotel } from '../dto/hotel';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Storage } from '../shared/storage';

@Component({
  selector: 'app-accommodation',
  templateUrl: './accommodation.component.html',
  styleUrls: ['./accommodation.component.scss']
})
export class AccommodationComponent implements OnInit {
  hotel: Hotel;
  comments: Array<Comment>;

  constructor(private http: HttpClient, private activatedRoute: ActivatedRoute, private router: Router, private storage: Storage) { }

  ngOnInit() {
    this.activatedRoute.params.subscribe((params: Params) => {
      this.getHotel(params['id']);
    });
  }

  getHotel(id) {
    this.http.get<Hotel>('api/hotel/' + id).subscribe(data => {
      this.hotel = data;
      this.storage.put('hotel', this.hotel);
    });
    
    this.http.get<Array<Comment>>('api/hotel/' + id + '/comments').subscribe(data => {
      this.comments = data;
      this.storage.put('comments', this.comments);
    });
  }

  allReviews() {
    this.router.navigate(['/reviews/' + this.hotel.id]);
  }
}
