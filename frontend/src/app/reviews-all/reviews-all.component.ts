import { Component, OnInit } from '@angular/core';
import { Storage } from '../shared/storage';
import { Hotel } from '../dto/hotel';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-reviews-all',
  templateUrl: './reviews-all.component.html',
  styleUrls: ['./reviews-all.component.scss']
})
export class ReviewsAllComponent implements OnInit {

  comments: Array<Comment>;
  hotel: Hotel;
  statistic = {};
  commentMappings = []

  constructor(private storage: Storage, private http: HttpClient, private activRoute: ActivatedRoute) { }

  ngOnInit() {
    this.comments = this.storage.get('comments');
    this.hotel = this.storage.get('hotel');
    this.commentMappings = this.storage.get('mappings');

    if (!this.comments && !this.hotel) {
      this.activRoute.params.subscribe((params: Params) => {
        this.getHotel(params['id']);
      });
    }
  }

  getHotel(id) {
    this.http.get<Hotel>('api/hotel/' + id).subscribe(data => this.hotel = data);
    this.http.get<Array<Comment>>('api/hotel/' + id + '/comments').subscribe(data => {
      this.comments = data;
      this.http.get<any>('api/hotel/' + id + '/comment-mappings').subscribe(data => {
        this.commentMappings = data;
        this.comments.forEach(comment => this.mapComment(comment));
      });
    });
  }

  mapComment(comment) {
    comment['mappings'] = [];
    for (let i = 0; i < this.commentMappings.length; i++) {
      let commentMapping = this.commentMappings[i];
      if (commentMapping.comment_id === comment.id) {
        comment['mappings'].push(commentMapping);
      }
    }
  }
}
