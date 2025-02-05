<script>
    import { goto } from '$app/navigation';

    import { store } from '$lib/store.js';
    import { FetchBuilder, PathBuilder } from '$lib/builders.js';
    import ReturnMain from '$lib/components/ReturnMain.svelte';

    import { sha256 } from 'js-sha256';


    export let data;
    const { id } = data;
    let { name, surname, username, admin, phone_number, email } = data.record;
    let password = '';

    async function edit() {
        const token = $store.token;
        const response = await fetch(FetchBuilder.workers.edit(id), {
            method: 'PATCH',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
                },
            body: password.length === 0 ?            
                JSON.stringify({ id, name, surname, username, admin, phone_number: phone_number, email }) :
                JSON.stringify({ id, name, surname, username, password_hash: sha256(password), admin, phone_number: phone_number, email })
            });

        switch (response.status) {
            case 404 :
                goto(PathBuilder.errors.notfound); return;
            case 422 :
                goto(PathBuilder.errors.valid); return;
            case 403 :
                goto(PathBuilder.errors.access); return;
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
                    <td><label for="surname">Surname:</label></td>
                    <td><input type="text" name="surname" id="surname" maxlength="50" required bind:value={surname}/></td>
                </tr>
                <tr>
                    <td><label for="username">Username:</label></td>
                    <td><input type="text" name="username" id="username" minlength="4" maxlength="16" required bind:value={username}/></td>
                </tr>
                <tr>
                    <td><label for="password">Password:</label></td>
                    <td><input type="password" name="password" id="password" bind:value={password}/></td>
                </tr>
                <tr>
                    <td><label for="admin">Admin: </label></td>
                    <td><input type="checkbox" name="admin" id="admin" bind:checked={admin}/></td>
                </tr>
                <tr>
                    <td><label for="phone-number">Phone Number: </label></td>
                    <td><input type="tel" name="phone-number" id="phone-number" required bind:value={phone_number}/></td>
                </tr>
                <tr>
                    <td><label for="email">E-mail: </label></td>
                    <td><input type="email" name="email" id="email" required bind:value={email}/></td>
                </tr>
            </tbody>
        </table>
        <input type="submit" name="submit" id="submit" value="Edit"/>
    </form>
    <ReturnMain/>
</div>