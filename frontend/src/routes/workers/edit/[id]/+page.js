import { redirect } from '@sveltejs/kit';

import { store } from '$lib/store.js';
import { FetchBuilder, PathBuilder } from '$lib/builders.js';

export async function load({ fetch, params}) {
    let token;
    store.subscribe(x => token = x.token);

    const id = Number(params.id);

    const response = await fetch(FetchBuilder.workers.edit(id), {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
            }
        });

    switch (response.status) {
        case 404 :
            throw redirect(303, PathBuilder.errors.notfound)
        case 403 :
            throw redirect(303, PathBuilder.errors.access);
        case 440 :
            throw redirect(303, PathBuilder.errors.expired);
        case 401 :
            throw redirect(303, PathBuilder.errors.auth);
        }

    if (! response.ok)
        throw redirect(303, PathBuilder.errors.session);

    const record = await response.json();

    return { id, record };
    }