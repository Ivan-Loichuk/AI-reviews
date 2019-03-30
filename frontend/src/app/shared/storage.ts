import { Injectable } from "@angular/core";

@Injectable()
export class Storage {
    private data = new Map();

    put(key, data) {
        this.data[key] = data;
    }

    get(key) {
        return this.data[key];
    }
}