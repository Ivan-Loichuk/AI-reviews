import { Component, OnInit } from '@angular/core';
import {Subject} from 'rxjs';
import { HttpClient } from '../../../../node_modules/@angular/common/http';
import {debounceTime} from 'rxjs/operators';
import {ViewChild, ElementRef} from '@angular/core';


@Component({
  selector: 'app-modal-authorization',
  templateUrl: './authorization.component.html',
  styleUrls: ['./authorization.component.scss']
})
export class AuthorizationComponent implements OnInit {

  userData = {};
  private _success = new Subject<string>();
  staticAlertClosed = false;
  successMessage: string;
  @ViewChild('closeBtn') closeBtn: ElementRef;


  constructor(private http: HttpClient) { }

  ngOnInit() {
    setTimeout(() => this.staticAlertClosed = true, 20000);

    this._success.subscribe((message) => this.successMessage = message);
    this._success.pipe(
      debounceTime(3000)
    ).subscribe(() => this.closeModal());
  }

  signUp() {
    this.http.post('/api/registration', this.userData).subscribe(
      success => this.changeSuccessMessage()
    );
  }

  signIn() {
    this.http.post('/api/auth', this.userData).subscribe(
      success => this.closeModal()
    );
  }

  public changeSuccessMessage() {
    this._success.next("Success");
  }

  private closeModal(): void {
    this.closeBtn.nativeElement.click();
  }
}
