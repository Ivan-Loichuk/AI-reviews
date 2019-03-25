import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-accommodation-reviews',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.scss']
})
export class ReviewsComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  counter(i: number) {
    return new Array(i);
  } 
}
