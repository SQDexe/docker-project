<script>
    import { goto } from '$app/navigation';

    import { store } from '$lib/store.js';
    import { FetchBuilder, PathBuilder } from '$lib/builders.js';
    import ReturnMain from '$lib/components/ReturnMain.svelte';


    export let data;    
    const { id, formData } = data;
    let { name, species, gender, birth, arrival } = data.record;

    async function edit() {
        const token = $store.token;
        const response = await fetch(FetchBuilder.animals.edit(id), {
            method: 'PATCH',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
                },
            body: JSON.stringify({ id, name, species, gender, birth, arrival })
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
                    <td><label for="name">Name:</label></td>
                    <td><input type="text" name="name" id="name" maxlength="50" required bind:value={name}/></td>
                </tr>
                <tr>
                    <td><label for="species">Species:</label></td>
                    <td>
                        <select name="species" id="species" required bind:value={species}>
                            {#each formData.species as spec}
                                <option value="{spec}">{spec}</option>
                            {/each}
                        </select>
                    </td>
                </tr>
                <tr>
                    <td><label for="gender">Gender:</label></td>
                    <td>
                        <select name="gender" id="gender" required bind:value={gender}>
                            {#each formData.gender as gend}
                                <option value="{gend}">{gend}</option>
                            {/each}
                        </select>
                    </td>
                </tr>
                <tr>
                    <td><label for="birth">Birth:</label></td>
                    <td><input type="number" name="birth" id="birth" min="1901" max="2155" step="1" required bind:value={birth}/></td>
                </tr>
                <tr>
                    <td><label for="arrival">Arrival:</label></td>
                    <td><input type="date" name="arrival" id="arrival" min="1901-01-01" max="2155-12-31" required bind:value={arrival}/></td>
                </tr>
            </tbody>
        </table>
        <input type="submit" name="submit" id="submit" value="Edit"/>
    </form>
    <ReturnMain/>
</div>