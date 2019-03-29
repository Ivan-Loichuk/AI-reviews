import { Component, OnInit } from '@angular/core';
import { FilterService } from './filter.service';

@Component({
  selector: 'app-search-filters',
  templateUrl: './filters.component.html',
  styleUrls: ['./filters.component.scss']
})
export class FiltersComponent implements OnInit {
  search = {types: [], city: ''}

  constructor(private filterService: FilterService) { }

  ngOnInit() {
  }

  submitFilters() {
    this.filterService.submitFilters(this.search);
  }

  addType(type) {
    if (this.search.types.includes(type)) {
      this.search.types = this.search.types.filter(t => t !== type);
    } else
      this.search.types.push(type);
  }
}
