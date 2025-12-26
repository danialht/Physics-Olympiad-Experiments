<script>
  import { exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8 } from './experiments/index.js';
  import MarkdownRenderer from './MarkdownRenderer.svelte';

  let selectedExperiment = null;

  const experiments = [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8];

  function selectExperiment(exp) {
    selectedExperiment = exp;
  }

  function clearSelection() {
    selectedExperiment = null;
  }
</script>

<main>
  <header>
    <h1>Physics Olympiad Experiments</h1>
    <p>Explore various physics olympiad experiments</p>
  </header>

  <div class="container">
    {#if !selectedExperiment}
      <div class="grid">
        {#each experiments as exp (exp.id)}
          <div class="card" on:click={() => selectExperiment(exp)}>
            <h3>{exp.name}</h3>
            <p>{exp.description}</p>
          </div>
        {/each}
      </div>
    {:else}
      <div class="detail">
        <button on:click={clearSelection}>← Back</button>
        <MarkdownRenderer content={selectedExperiment.content} />
      </div>
    {/if}
  </div>
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: #333;
  }

  main {
    min-height: 100vh;
    padding: 2rem;
  }

  header {
    text-align: center;
    color: white;
    margin-bottom: 3rem;
  }

  header h1 {
    font-size: 3rem;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  }

  header p {
    font-size: 1.2rem;
    margin: 0.5rem 0 0 0;
    opacity: 0.9;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
  }

  .card {
    background: white;
    border-radius: 10px;
    padding: 2rem;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 16px rgba(0, 0, 0, 0.2);
  }

  .card h3 {
    margin: 0 0 1rem 0;
    color: #667eea;
    font-size: 1.5rem;
  }

  .card p {
    margin: 0;
    color: #666;
    line-height: 1.5;
  }

  .detail {
    background: white;
    border-radius: 10px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    max-width: 900px;
    margin: 0 auto;
  }

  .detail button {
    background: #667eea;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.3s ease;
  }

  .detail button:hover {
    background: #764ba2;
  }

  .detail h2 {
    margin: 1rem 0 0.5rem 0;
    color: #333;
  }

  .detail p {
    color: #666;
    line-height: 1.6;
  }
</style>
