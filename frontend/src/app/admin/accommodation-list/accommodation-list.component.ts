import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-accommodation-list',
  templateUrl: './accommodation-list.component.html',
  styleUrls: ['./accommodation-list.component.scss', '../admin.component.scss']
})
export class AccommodationListComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  counter(i: number) {
    return new Array(i);
  } 
}
