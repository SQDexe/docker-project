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
                <th>Date</th>
                <th>Amount</th>
                <th>Signature</th>
            </tr>
        </thead>
        <tbody>
            {#each list as { id, date, amount, signature }}
                <tr>
                    <td>{id}</td>
                    <td>{date}</td>
                    <td>{amount}</td>
                    <td>{signature}</td>
                    <td><a href="{PathBuilder.donations.edit(id)}">Edit</a></td>
                    <td><a href="{PathBuilder.donations.delete(id)}">Delete</a></td>
                </tr>
            {/each}
        </tbody>
    </table>
    <ReturnMain/>
</div>