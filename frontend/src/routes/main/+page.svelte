<script>
    import { goto } from '$app/navigation';

    import { store } from '$lib/store.js';
    import { PathBuilder } from '$lib/builders.js';
    import DatabaseTableRow from '$lib/components/DatabaseTableRow.svelte';


    async function logout() {
        $store.token = null;
        goto(PathBuilder.login);
        }

    const token = $store.token;
    if (Object.is(token, null))
        goto(PathBuilder.errors.session);
</script>

<div>
    <span>Tables:</span>
    <table>
        <tbody>
            <DatabaseTableRow name="adoptions"/>
            <DatabaseTableRow name="animals"/>
            <DatabaseTableRow name="donations"/>
            <DatabaseTableRow name="workers"/>
        </tbody>
    </table>
    <button on:click|preventDefault={logout}>Logout</button>
</div>