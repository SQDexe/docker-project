<script>
    import { PathBuilder } from '$lib/builders.js';

    import { goto } from '$app/navigation';

    async function goBack() {
        goto(PathBuilder.login);
        }
</script>

<div>
    <button on:click|preventDefault={goBack}>Return</button>
</div>