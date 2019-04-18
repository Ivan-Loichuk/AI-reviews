import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-rating-summary',
  templateUrl: './rating-summary.component.html',
  styleUrls: ['./rating-summary.component.scss']
})
export class RatingSummaryComponent implements OnInit {

  @Input()
  guestReviews;
  @Input()
  statistic;
  loading = true;
  total = 0;
  totalText = '';

  constructor() { }

  ngOnInit() {
    this.statistic.forEach(stat => this.calculateStat(stat));
    this.calculateOverAll();
  }

  calculateStat(stat) {
    stat['percentage'] = Math.floor((stat.positive / (stat.positive + stat.negative)) * 100);
  }

  calculateOverAll() {
    let sum = 0;
    let categories = 0;
    this.statistic.forEach(stat => {
      sum += stat['percentage'];
      categories += 1;
    });
    this.total = Math.floor((sum / categories));
    this.changeTotalText();
  }

  changeTotalText() {
    if (this.total < 50) {
      this.totalText = 'Bad';
    } else if (this.total < 80) {
      this.totalText = 'Good';
    } else
      this.totalText = 'Excellent';
  }
}
