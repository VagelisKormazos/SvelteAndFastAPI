<script>
    import Layout from "$lib/Layout.svelte";

    let gameElement="Αυτή είναι η αρχική σελίδα του site μας.";
    let title2 = '';
    
    const changeTitle = () => {
        if (gameElement) {
            gameElement.textContent = "Raches Home Page";
        }
    };

</script>
<Layout >
<div class="index">
    <img src="images/raches_home.jpg" alt="Home Page">
    <p id="game"  bind:this={gameElement}>Αυτή είναι η αρχική σελίδα του site μας.</p>
    <button on:click={changeTitle}>Press</button>
    <input type="text" bind:value={title2}>
    <br>
    <a href="/history">History of our village</a>
</div>

</Layout>

<style>
    .index{
        text-align: center;
        display: block;
    }
</style>



