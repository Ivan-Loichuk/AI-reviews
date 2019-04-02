import { Component, OnInit, Input } from '@angular/core';
import { environment as env } from '../../../environments/environment';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { Hotel } from '../../dto/hotel';

@Component({
  selector: 'app-search-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.scss']
})
export class ResultsComponent implements OnInit {
  @Input()
  hotels: Array<Hotel>;

  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit() {
  }

  checkHotel(id) {
    this.router.navigate(['accommodation/' + id])
  }
}
