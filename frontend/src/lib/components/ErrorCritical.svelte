<script>
    import ReturnLogin from '$lib/components/ReturnLogin.svelte';   

    const { errorMessage } = $props();
</script>

<div>
    <h3>{errorMessage}</h3>
    <ReturnLogin/>
</div>