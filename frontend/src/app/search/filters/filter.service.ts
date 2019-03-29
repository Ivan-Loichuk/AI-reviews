import { Subject, Observable } from 'rxjs';
import { Injectable } from '@angular/core';

@Injectable()
export class FilterService {
    private filtersSubject = new Subject<any>();

    filtersAsObs(): Observable<any> {
        return this.filtersSubject.asObservable();
    }

    submitFilters(filters) {
        this.filtersSubject.next(filters);
    }
}