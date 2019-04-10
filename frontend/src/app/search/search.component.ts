import { Component, OnInit } from '@angular/core';
import { Hotel } from '../dto/hotel';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Params } from '@angular/router';
import { FilterService } from './filters/filter.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  hotels: Array<Hotel> = [];
  search_words: String = "";
  constructor(private http: HttpClient, private activeRoute: ActivatedRoute, private filterService: FilterService) {}

  ngOnInit() {
    this.activeRoute.params.subscribe((params: Params) => {
      if (params['city'] === 'all') {
        this.searchHotel({city: '', types: []})
        this.search_words = 'All';
      } else{
        this.searchHotel({city: params['city'], types: []});
        this.search_words = params['city'];
      }
        
    });
    this.filterService.filtersAsObs().subscribe(data => {
      this.searchHotel(data);
    });
  }

  searchHotel(filters) {
    this.http.post<Array<Hotel>>('api/hotels/search', filters).subscribe(data => this.hotels = data);
  }
}
