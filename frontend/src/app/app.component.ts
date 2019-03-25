import { Component } from '@angular/core';
import { environment as env } from '../environments/environment';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'ze-app';
  public env = env;
  public path = window.location.pathname;
  public isAdminPage = false;

  constructor(router: Router, route: ActivatedRoute){
    var pattern = /admin/g;
    if(this.path.match(pattern) != null){
      this.isAdminPage = true;
    }
  }
}
