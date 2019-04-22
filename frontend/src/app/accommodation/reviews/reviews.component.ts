import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-accommodation-reviews',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.scss']
})
export class ReviewsComponent implements OnInit {
  @Input()
  comments: Array<Comment>;
  @Input()
  mappings: Array<any>;

  constructor() { }

  ngOnInit() {
  }

  counter(i: number) {
    return new Array(i);
  } 
}
