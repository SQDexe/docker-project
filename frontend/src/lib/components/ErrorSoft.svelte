<script>
    import ReturnMain from '$lib/components/ReturnMain.svelte';   

    const { errorMessage } = $props();
</script>

<div>
    <h3>{errorMessage}</h3>
    <ReturnMain/>
</div>