<script>
  import { onMount } from 'svelte';
  import { exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9 } from './experiments/index.js';
  import MarkdownRenderer from './MarkdownRenderer.svelte';

  let selectedExperiment = null;
  let notFound = false;
  let language = 'en';

  const experiments = [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9];

  function experimentFromHash() {
    const slug = window.location.hash.slice(1);
    return experiments.find((exp) => `exp${exp.id}` === slug) ?? null;
  }

  function syncFromHash() {
    const slug = window.location.hash.slice(1);
    selectedExperiment = experimentFromHash();
    notFound = slug.length > 0 && !selectedExperiment;
  }

  onMount(() => {
    syncFromHash();
    window.addEventListener('hashchange', syncFromHash);
    return () => window.removeEventListener('hashchange', syncFromHash);
  });

  function clearSelection() {
    window.location.hash = '';
  }

  function toggleLanguage() {
    language = language === 'en' ? 'fa' : 'en';
  }
</script>

<main>
  <header>
    <button class="lang-toggle" class:fa={language === 'en'} on:click={toggleLanguage}>
      {language === 'en' ? 'فارسی' : 'English'}
    </button>
    <h1>Virtual Physics Olympiad Experiments</h1>
  </header>

  <div class="container">
    {#if notFound}
      <div class="not-found">
        <h2>404</h2>
        <p>Page not found.</p>
        <button on:click={clearSelection}>← Back to experiments</button>
      </div>
    {:else if !selectedExperiment}
      <p class="intro" class:fa={language === 'fa'}>
        {#if language === 'fa'}
          I don't have Persian keyboard. I'll write this later.
        {:else}
        Every year the Internationl Physics Olympiad (IPhO) has two section, theory and experiment. The theory secion, of course, has theory problems and the experimental section usually includes setting up some apparatus, some theoretical insight and measurements and data analysis. IPhO 2022, was held online for most of the countries, due to some change of the plans in the organization there was no time for sending real apparatus to students, and previously because of Covid there had already some trend of "Virtual Experiment".
        {/if}
      </p>
      <ul class="experiment-list">
        {#each experiments as exp (exp.id)}
          <li>
            <a href={`#exp${exp.id}`} class:fa={language === 'fa'}>
              {language === 'fa' ? exp.nameFa : exp.name}
            </a>
          </li>
        {/each}
      </ul>
    {:else}
      <div class="detail">
        <button on:click={clearSelection}>← Back</button>
        <MarkdownRenderer content={selectedExperiment.content} />
      </div>
    {/if}
  </div>
</main>

<style>
  @font-face {
    font-family: 'B Nazanin';
    src: url('./fonts/BNazanin.ttf') format('truetype');
    font-display: swap;
  }

  .fa {
    font-family: 'B Nazanin', Tahoma, sans-serif;
    direction: rtl;
    text-align: right;
  }

  :global(:root) {
    --color-bg: #f6f3ec;
    --color-surface: #fffefb;
    --color-text: #262420;
    --color-muted: #6f6a5e;
    --color-accent: #1f3a52;
    --color-accent-soft: #3d5a73;
    --color-border: #ddd6c4;
  }

  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    background: var(--color-bg);
    min-height: 100vh;
    color: var(--color-text);
  }

  main {
    min-height: 100vh;
    padding: 2rem;
  }

  header {
    text-align: center;
    color: var(--color-accent);
    margin-bottom: 3rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--color-border);
    position: relative;
  }

  .lang-toggle {
    position: absolute;
    top: 0;
    right: 0;
    background: transparent;
    color: var(--color-accent);
    border: 1px solid var(--color-border);
    padding: 0.5rem 1rem;
    border-radius: 3px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.2s ease, color 0.2s ease;
  }

  .lang-toggle:hover {
    background: var(--color-accent);
    color: var(--color-surface);
  }

  header h1 {
    font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', serif;
    font-size: 2.75rem;
    font-weight: normal;
    margin: 0;
    letter-spacing: 0.01em;
  }

  header p {
    font-size: 1.1rem;
    margin: 0.5rem 0 0 0;
    color: var(--color-muted);
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  .intro {
    max-width: 700px;
    margin: 0 auto 2rem;
    color: var(--color-muted);
    line-height: 1.7;
    text-align: justify;
    text-justify: inter-word;
  }

  .experiment-list {
    list-style: none;
    max-width: 700px;
    margin: 0 auto;
    padding: 0;
    border-top: 1px solid var(--color-border);
  }

  .experiment-list li {
    border-bottom: 1px solid var(--color-border);
  }

  .experiment-list a {
    display: block;
    padding: 1rem 0.25rem;
    color: var(--color-accent);
    text-decoration: none;
    font-size: 1.15rem;
    transition: color 0.2s ease, padding-left 0.2s ease;
  }

  .experiment-list a:hover {
    color: var(--color-accent-soft);
    padding-left: 0.75rem;
  }

  .detail {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 4px;
    padding: 2rem;
    max-width: 900px;
    margin: 0 auto;
  }

  .detail button {
    background: transparent;
    color: var(--color-accent);
    border: 1px solid var(--color-border);
    padding: 0.5rem 1rem;
    border-radius: 3px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.2s ease, color 0.2s ease;
  }

  .detail button:hover {
    background: var(--color-accent);
    color: var(--color-surface);
  }

  .detail h2 {
    margin: 1rem 0 0.5rem 0;
    color: var(--color-text);
  }

  .detail p {
    color: var(--color-muted);
    line-height: 1.6;
  }

  .not-found {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 4px;
    padding: 3rem 2rem;
    max-width: 600px;
    margin: 0 auto;
    text-align: center;
  }

  .not-found h2 {
    font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', serif;
    font-size: 2.75rem;
    margin: 0;
    color: var(--color-accent);
  }

  .not-found p {
    color: var(--color-muted);
    margin: 0.5rem 0 1.5rem;
  }

  .not-found button {
    background: transparent;
    color: var(--color-accent);
    border: 1px solid var(--color-border);
    padding: 0.5rem 1rem;
    border-radius: 3px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.2s ease, color 0.2s ease;
  }

  .not-found button:hover {
    background: var(--color-accent);
    color: var(--color-surface);
  }
</style>
