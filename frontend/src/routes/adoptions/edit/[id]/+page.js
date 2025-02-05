import { redirect } from '@sveltejs/kit';

import { store } from '$lib/store.js';
import { FetchBuilder, PathBuilder } from '$lib/builders.js';

export async function load({ fetch, params}) {
    let token;
    store.subscribe(x => token = x.token);

    const id = Number(params.id);

    const [response1, response2] = await Promise.all([
        fetch(FetchBuilder.data.adoptions, {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
                }
            }),
        fetch(FetchBuilder.adoptions.edit(id), {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
                }
            })
        ]);

    switch (response1.status) {
        case 440 :
            throw redirect(303, PathBuilder.errors.expired);
        case 401 :
            throw redirect(303, PathBuilder.errors.auth);
        }
    
    switch (response2.status) {
        case 404 :
            throw redirect(303, PathBuilder.errors.notfound)
        case 440 :
            throw redirect(303, PathBuilder.errors.expired);
        case 401 :
            throw redirect(303, PathBuilder.errors.auth);
        }

    if (! (response1.ok && response2.ok))
        throw redirect(303, PathBuilder.errors.session);

    const [formData, record] = await Promise.all([response1.json(), response2.json()]);

    return { id, record, formData };
    }