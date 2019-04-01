import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Params } from '@angular/router';
import { Storage } from '../../shared/storage';

@Component({
  selector: 'app-modal-add-review',
  templateUrl: './add-review.component.html',
  styleUrls: ['./add-review.component.scss']
})
export class AddReviewComponent implements OnInit {

  private hotel: number;

  constructor(private http: HttpClient, private activRoute: ActivatedRoute, private storage: Storage) { }

  ngOnInit() {
    this.activRoute.params.subscribe((params: Params) => {
      this.hotel = params['id'];
    });
  }

  counter(i: number) {
    return new Array(i);
  }

  add(content) {
    const comment = {hotel: this.hotel, content: content};
    this.http.post('api/hotel/comment', comment).subscribe(
      () => {
        let comments = this.storage.get('comments');
        comments.push(comment);
      }
    );
  }
}
