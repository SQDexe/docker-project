<script>
    import { capitalise } from '$lib/utils.js';
    import { PathBuilder } from '$lib/builders.js';

    const { name } = $props();
    const capName = capitalise(name);
    const [base, add] = [PathBuilder[name].view, PathBuilder[name].add]
</script>

<tr>
    <td>{capName}</td>
    <td><a href="{base}">View</a></td>
    <td><a href="{add}">Add</a></td>
</tr>