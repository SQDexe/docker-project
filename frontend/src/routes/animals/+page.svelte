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
                <th>Species</th>
                <th>Gender</th>
                <th>Birth</th>
                <th>Arrival</th>
            </tr>
        </thead>
        <tbody>
            {#each list as { id, name, species, gender, birth, arrival }}
                <tr>
                    <td>{id}</td>
                    <td>{name}</td>
                    <td>{species}</td>
                    <td>{gender}</td>
                    <td>{birth}</td>
                    <td>{arrival}</td>
                    <td><a href="{PathBuilder.animals.edit(id)}">Edit</a></td>
                    <td><a href="{PathBuilder.animals.delete(id)}">Delete</a></td>
                </tr>
            {/each}
        </tbody>
    </table>
    <ReturnMain/>
</div>