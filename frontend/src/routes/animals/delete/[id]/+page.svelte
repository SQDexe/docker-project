<script>
    import { page } from '$app/stores';
    import { goto } from '$app/navigation';

    import { store } from '$lib/store.js';
    import { FetchBuilder, PathBuilder } from '$lib/builders.js';
    import ReturnMain from '$lib/components/ReturnMain.svelte';


    export let data;
    const { id } = data;

    async function remove() {
        const token = $store.token;
        const response = await fetch(FetchBuilder.animals.delete(id), {
            method: 'DELETE',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
                }
            });

        switch (response.status) {
            case 404 :
                goto(PathBuilder.errors.notfound); return;
            case 422 :
                goto(PathBuilder.errors.valid); return;
            case 440 :
                goto(PathBuilder.errors.expired); return;
            case 401 :
                goto(PathBuilder.errors.auth); return;
            }

        if (! response.ok) {
            goto(PathBuilder.errors.session);
            return;
            }
        
        goto(PathBuilder.success);
        }
</script>

<div>
    <div>You are about to delete record with id {id}. Do you wish to proceed?</div>
    <div>
        <button on:click|preventDefault={remove}>Delete</button>
    </div>
    <ReturnMain/>
</div>