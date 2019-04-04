import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-rating-summary',
  templateUrl: './rating-summary.component.html',
  styleUrls: ['./rating-summary.component.scss']
})
export class RatingSummaryComponent implements OnInit {

  @Input()
  guestReviews;

  constructor() { }

  ngOnInit() {
  }

}
