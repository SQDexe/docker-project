<script>
    import { PathBuilder } from '$lib/builders.js';
    import ReturnMain from '$lib/components/ReturnMain.svelte';

    export let data;
    const { list } = data;
</script>

<div>
    <table>
        <thead>
            <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Surname</th>
                <th>Username</th>
                <th>Password Hash</th>
                <th>Admin</th>
                <th>Phone Number</th>
                <th>E-mail</th>
            </tr>
        </thead>
        <tbody>
            {#each list as { id, name, surname, username, password_hash, admin, phone_number, email }}
                <tr>
                    <td>{id}</td>
                    <td>{name}</td>
                    <td>{surname}</td>
                    <td>{username}</td>
                    <td>{password_hash}</td>
                    <td>{admin}</td>
                    <td>{phone_number}</td>
                    <td>{email}</td>
                    <td><a href="{PathBuilder.workers.edit(id)}">Edit</a></td>
                    <td><a href="{PathBuilder.workers.delete(id)}">Delete</a></td>
                </tr>
            {/each}
        </tbody>
    </table>
    <ReturnMain/>
</div>