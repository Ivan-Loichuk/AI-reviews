import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DelUserComponent } from './del-user.component';

describe('DelUserComponent', () => {
  let component: DelUserComponent;
  let fixture: ComponentFixture<DelUserComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DelUserComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DelUserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
