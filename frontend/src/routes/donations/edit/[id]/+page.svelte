<script>
    import { goto } from '$app/navigation';

    import { store } from '$lib/store.js';
    import { FetchBuilder, PathBuilder } from '$lib/builders.js';
    import ReturnMain from '$lib/components/ReturnMain.svelte';


    export let data;
    const { id } = data;
    let { date, amount, signature } = data.record;

    async function edit() {
        const token = $store.token;
        const response = await fetch(FetchBuilder.donations.edit(id), {
            method: 'PATCH',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
                },
            body: JSON.stringify({ id, date, amount, signature })
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
    <form on:submit|preventDefault={edit}>
        <table>
            <tbody>
                <tr>
                    <td><label for="date">Date:</label></td>
                    <td><input type="date" name="date" id="date" min="1901-01-01" max="2155-12-31" required bind:value={date}/></td>
                </tr>
                <tr>
                    <td><label for="amount">Amount:</label></td>
                    <td><input type="number" name="amount" id="amount" min="0" max="999999999" step="0.01" required bind:value={amount}/></td>
                </tr>
                <tr>
                    <td><label for="signature">Signature:</label></td>
                    <td><input type="text" name="signature" id="signature" maxlength="100" required bind:value={signature}/></td>
                </tr>
            </tbody>
        </table>
        <input type="submit" name="submit" id="submit" value="Edit"/>
    </form>
    <ReturnMain/>
</div>