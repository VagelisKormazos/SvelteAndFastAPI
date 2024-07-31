<script>
  import Layout from "$lib/Layout.svelte";
  import { onMount } from 'svelte';

  let businesses = [];
  let error = null;

  // Function to fetch data from the API
  async function fetchBusinesses() {
      try {
          const response = await fetch('http://127.0.0.1:8000/businesses');
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          businesses = await response.json();
      } catch (err) {
          error = err.message;
      }
  }

  // Fetch data on component mount
  onMount(() => {
      fetchBusinesses();
  });
</script>

<Layout title="Our Businesses">
  <h1>Our Businesses</h1>
  {#if error}
      <p class="error">Error: {error}</p>
  {/if}
  {#if businesses.length > 0}
      <table class="business-table">
          <thead>
              <tr>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Type</th>
                  <th>Location</th>
                  <th>Created At</th>
              </tr>
          </thead>
          <tbody>
              {#each businesses as business (business.id)}
                  <tr>
                      <td>{business.id}</td>
                      <td>{business.name}</td>
                      <td>{business.type}</td>
                      <td>{business.location}</td>
                      <td>{new Date(business.created_at).toLocaleDateString()}</td>
                  </tr>
              {/each}
          </tbody>
      </table>
  {:else}
      <p>Loading...</p>
  {/if}
</Layout>

<style>
  h1 {
      text-align: center;
      margin-bottom: 20px;
  }

  .business-table {
      width: 100%;
      border-collapse: collapse;
  }

  .business-table th, .business-table td {
      padding: 10px;
      text-align: left;
      border-bottom: 1px solid #ddd;
  }

  .business-table th {
      background-color: #f4f4f4;
  }

  .business-table tr:nth-child(even) {
      background-color: #f9f9f9;
  }

  .error {
      color: red;
      font-weight: bold;
  }
</style>
