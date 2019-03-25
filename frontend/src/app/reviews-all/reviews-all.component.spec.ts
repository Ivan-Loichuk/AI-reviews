import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReviewsAllComponent } from './reviews-all.component';

describe('ReviewsAllComponent', () => {
  let component: ReviewsAllComponent;
  let fixture: ComponentFixture<ReviewsAllComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReviewsAllComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReviewsAllComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
