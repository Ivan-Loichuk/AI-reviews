import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-rating-stars',
  templateUrl: './rating-stars.component.html',
  styleUrls: ['./rating-stars.component.scss']
})
export class RatingStarsComponent implements OnInit {

  @Input() active: string; 

  constructor() { 
    console.log(this.active);
  }

  ngOnInit() {
  }

}
