import { redirect } from '@sveltejs/kit';

import { store } from '$lib/store.js';
import { FetchBuilder, PathBuilder } from '$lib/builders.js';

export async function load({ fetch }) {
    let token;
    store.subscribe(x => token = x.token);

    const response = await fetch(FetchBuilder.data.adoptions, {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
            }
        });

    switch (response.status) {
        case 440 :
            throw redirect(303, PathBuilder.errors.expired);
        case 401 :
            throw redirect(303, PathBuilder.errors.auth);
        }

    if (! response.ok)
        throw redirect(303, PathBuilder.errors.session);

    const formData = await response.json()
    return { formData };
    }