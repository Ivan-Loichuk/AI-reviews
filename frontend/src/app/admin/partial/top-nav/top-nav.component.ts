import { Component, OnInit } from '@angular/core';
import * as $ from 'jquery';

@Component({
  selector: 'app-admin-top-nav',
  templateUrl: './top-nav.component.html',
  styleUrls: ['./top-nav.component.scss','../../admin.component.scss']
})
export class TopNavComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  toggleMenu(){
    $('.sidebar-offcanvas').toggleClass('active')
  }
}
