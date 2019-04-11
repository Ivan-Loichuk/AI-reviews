import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-pagination',
  templateUrl: './pagination.component.html',
  styleUrls: ['./pagination.component.scss']
})
export class PaginationComponent implements OnInit {

  @Input() count_results:string;
  @Input() active_page:string;
  @Input() hotel:string;
  @Input() search_words:string;

  constructor() { }

  ngOnInit() {
  }

}
