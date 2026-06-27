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

  function trackPageView() {
    if (typeof window.gtag !== 'function') return;
    const page_path = window.location.pathname + window.location.search + window.location.hash;
    const page_title = selectedExperiment
      ? selectedExperiment.name
      : notFound
        ? '404 Not Found'
        : 'Virtual Physics Olympiad Experiments';
    window.gtag('event', 'page_view', { page_path, page_title });
  }

  function syncFromHash() {
    const slug = window.location.hash.slice(1);
    selectedExperiment = experimentFromHash();
    notFound = slug.length > 0 && !selectedExperiment;
    trackPageView();
  }

  function languageFromQuery() {
    return new URLSearchParams(window.location.search).get('lang') === 'fa' ? 'fa' : 'en';
  }

  onMount(() => {
    language = languageFromQuery();
    syncFromHash();
    window.addEventListener('hashchange', syncFromHash);
    return () => window.removeEventListener('hashchange', syncFromHash);
  });

  function clearSelection() {
    window.location.hash = '';
  }

  function toggleLanguage() {
    language = language === 'en' ? 'fa' : 'en';
    const params = new URLSearchParams(window.location.search);
    if (language === 'fa') {
      params.set('lang', 'fa');
    } else {
      params.delete('lang');
    }
    const query = params.toString();
    const newUrl = `${window.location.pathname}${query ? `?${query}` : ''}${window.location.hash}`;
    history.replaceState(null, '', newUrl);
  }
</script>

<main>
  <header>
    <div class="header-bar">
      <button class="lang-toggle" class:fa={language === 'en'} on:click={toggleLanguage}>
        {language === 'en' ? 'فارسی' : 'English'}
      </button>
    </div>
    <h1 class:fa={language === 'fa'}>
      {language === 'fa' ? 'آزمایش های مجازی المپیاد فیزیک' : 'Virtual Physics Olympiad Experiments'}
    </h1>
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
        این نسخه اولیه توضیحات هست و بعدا تغییر می کند.<br />
این یک مجموعه از سوال های آزمایشگاه مجازی برای المپیاد فیزیک است. با اینکه آزمایشگاه مجازی بیشتر در سال های  1399 و 1400 و 1401 معروف بود ولی همچنان ما بر این باور هستیم که چیز های زیادی هست که می شود از آن ها یاد گرفت و به همین دلیل این مجموعه رو آماده کردیم.        

        {:else}
        This is the first draft and will be changed later.<br />
        This is a collection of virutal experiments for practicing eperimental physics, eventhough virtual experiments were only a thing in 2020, 2021, and 2022, we still believe that there is a lot that could be learned from them.
        <!-- Every year, the International Physics Olympiad (IPhO) consists of two sections: theory and experiment. <br />
        The theory section, as the name suggests, contains theoretical problems that participants must solve. These problems are usually well-designed and divided into multiple parts. Some parts are straightforward, while others are time-consuming. Some require clever insights and creative thinking, whereas others mainly test your ability to carry out a systematic solution accurately. As a result, the highest scores in the theory section are often very high, typically around 29 out of 30 points or even higher. <br />
        The experimental section is quite different. It usually begins with setting up an apparatus, after which participants must perform measurements and analyze the resulting data. Success requires a combination of theoretical understanding, practical skills, and efficient data analysis. Speed is often crucial, since many experiments involve a large number of measurements that must be completed within a limited time. <br />
        IPhO 2022 was held online for most countries due to last-minute organizational changes. Similarly, IPhO 2021 conducted its experimental section online, with the required apparatus shipped to participating countries. In IPhO 2022, however, the experimental section was conducted entirely virtually using a computer simulation program. Before that, virtual experiments had already been used in other competitions, such as APhO 2022, EuPhO 2020, and EuPhO 2021. <br />
        Virtual experiments are extremely interesting, and they offer several important advantages. <br />
        Perhaps the biggest advantage is accessibility to practice. Practicing a real experimental problem from a previous IPhO or other Physics Olympiad often requires specialized equipment. In some cases, the apparatus can be expensive; in others, it may be highly sophisticated, such as the custom PCB board used in IPhO 2021. The time and money required to obtain such equipment are often disproportionate to the amount that can be learned from a single experiment. <br />
        Furthermore, many students around the world have very limited access to laboratory facilities. During IPhO 2022, I spoke with a student through our Discord channel and was surprised to learn that some participants did not even have a laboratory in their schools. How can talented students from such schools develop strong experimental skills? Whether this situation is fair is a separate question, but virtual experiments provide at least part of the solution. <br />
        Although virtual experiments do not train students to physically assemble and operate real apparatus, they still develop many of the most important experimental skills. Perhaps the most significant of these is the ability to analyze data quickly and accurately. In addition, many experimental problems contain substantial theoretical components, making them useful for developing theoretical intuition as well. <br />
        Good experimental problems often provide a considerable amount of freedom. The problem introduces an apparatus, explains how it can be configured, and then asks participants to determine an unknown quantity. Participants are free to design their own procedure to obtain the answer. This aspect of experimental problem-solving is often one of the most challenging—and rewarding—parts of the competition. Fortunately, it can also be practiced effectively through virtual experiments. <br />
        So what is the goal of this website? <br />
        Simply put, it is to provide additional resources for practicing experimental Physics Olympiad problems. <br />
        There are already several excellent virtual experiments available, including those from IPhO 2022, APhO 2022, EuPhO 2020, and EuPhO 2021. However, these resources have two limitations. First, there are only a handful of them. If you attempt one before you are adequately prepared, you may not gain as much from the experience, and because the supply is limited, it is difficult to build strong experimental skills through those problems alone. Second, these problems are generally quite difficult. They are designed for top-level competitions and are therefore not always suitable for regular practice. <br />
        The resources on this website are intended for students who want to practice, improve their skills, and gradually build confidence before tackling the most challenging Olympiad-level experimental problems, so that after solving the problems offered here, the student has undergone some phase transition and would be ready for doing the harder virtual experiments that are provided from past competitions. <br />
        I hope you enjoy the hours that you put on these problems. <br />
        Danial Hosseintabar, June 25, 2026 <br /> -->


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
      <div class="detail" class:fa={language === 'fa'}>
        <button on:click={clearSelection}>{language === 'fa' ? '→ بازگشت' : '← Back'}</button>
        <MarkdownRenderer content={language === 'fa' ? selectedExperiment.contentFa : selectedExperiment.content} />
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
  }

  .header-bar {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 1rem;
  }

  .lang-toggle {
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

  header h1.fa {
    text-align: center;
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

  @media (max-width: 640px) {
    main {
      padding: 1rem;
    }

    header {
      margin-bottom: 2rem;
    }

    header h1 {
      font-size: 1.9rem;
    }

    header p {
      font-size: 1rem;
    }

    .intro {
      font-size: 0.95rem;
    }

    .experiment-list a {
      font-size: 1rem;
    }

    .detail {
      padding: 1.25rem;
    }

    .not-found {
      padding: 2rem 1.25rem;
    }

    .not-found h2 {
      font-size: 2rem;
    }
  }
</style>
