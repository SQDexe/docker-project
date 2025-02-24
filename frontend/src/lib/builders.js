import { PUBLIC_API_HOST, PUBLIC_API_PORT } from '$env/static/public';


const paths = base => Object.freeze({
    view: base,
    add: base + '/add',
    edit: id => `${base}/edit/${id}`,
    delete: id => `${base}/delete/${id}`
    });

export class PathBuilder {
    static #base = Object.freeze({
        errors: '/errors',
        adoptions: '/adoptions',
        animals: '/animals',
        donations: '/donations',
        workers: '/workers'
        });
    static login = '/login';
    static main = '/main';
    static adoptions = paths(this.#base.adoptions);
    static animals = paths(this.#base.animals);
    static donations = paths(this.#base.donations);
    static workers = paths(this.#base.workers);
    static success = '/success';
    static errors = Object.freeze({
        access: this.#base.errors + '/access',
        auth: this.#base.errors + '/auth',
        expired: this.#base.errors + '/expired',
        notfound: this.#base.errors + '/notfound',
        session: this.#base.errors + '/session',
        valid: this.#base.errors + '/valid'
        });
    }

export class FetchBuilder {
    static #host = `http://${PUBLIC_API_HOST}:${PUBLIC_API_PORT}`;
    static #base = Object.freeze({
        data: this.#host + '/data',
        adoptions: this.#host + '/adoptions',
        animals: this.#host + '/animals',
        donations: this.#host + '/donations',
        workers: this.#host + '/workers'
        });
    static login = this.#host + '/login';
    static data = Object.freeze({
        adoptions: this.#base.data + '/adoptions',
        animals: this.#base.data + '/animals'
        });
    static adoptions = paths(this.#base.adoptions);
    static animals = paths(this.#base.animals);
    static donations = paths(this.#base.donations);
    static workers = paths(this.#base.workers); 
    }