import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss', '../admin.component.scss']
})
export class UsersComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  counter(i: number) {
    return new Array(i);
  } 
}
