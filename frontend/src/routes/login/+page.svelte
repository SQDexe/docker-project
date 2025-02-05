<script>
    import { goto } from '$app/navigation';

    import { store } from '$lib/store.js';
    import { FetchBuilder, PathBuilder } from '$lib/builders.js';

    import { sha256 } from 'js-sha256';


    let [username, password] = ['', ''];
    
    async function login() {
        const response = await fetch(FetchBuilder.login, {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
                },
            body: JSON.stringify({ username, password_hash: sha256(password) })
            });

        if (! response.ok) {
            goto(PathBuilder.errors.auth);
            return;
            }
        
        const { access_token } = await response.json();
        $store.token = access_token;
        goto(PathBuilder.main);
        }
</script>

<div>
    <form on:submit|preventDefault={login}>
        <table>
            <tbody>
                <tr>
                    <td><label for="username">Username:</label></td>
                    <td><input type="text" name="username" id="username" minlength="4" maxlength="16" required bind:value={username}/></td>
                </tr>
                <tr>
                    <td><label for="password">Password:</label></td>
                    <td><input type="password" name="password" id="password" required bind:value={password}/><br/></td>
                </tr>
            </tbody>
        </table>
        <input type="submit" name="submit" id="submit" value="Login"/>
    </form>
</div>