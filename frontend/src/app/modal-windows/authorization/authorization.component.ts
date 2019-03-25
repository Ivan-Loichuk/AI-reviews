import { Component, OnInit } from '@angular/core';
import { HttpClient } from '../../../../node_modules/@angular/common/http';

@Component({
  selector: 'app-modal-authorization',
  templateUrl: './authorization.component.html',
  styleUrls: ['./authorization.component.scss']
})
export class AuthorizationComponent implements OnInit {

  userData = {};

  constructor(private http: HttpClient) { }

  ngOnInit() {
  }

  signUp() {
    this.http.post('/api/registration', this.userData).subscribe(
      success => console.log(success)
    );
  }

  signIn() {
    this.http.post('/api/auth', this.userData).subscribe();
  }

}
