import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DelAccommodationComponent } from './del-accommodation.component';

describe('DelAccommodationComponent', () => {
  let component: DelAccommodationComponent;
  let fixture: ComponentFixture<DelAccommodationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DelAccommodationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DelAccommodationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
