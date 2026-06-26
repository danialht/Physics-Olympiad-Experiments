<script>
  import { marked } from 'marked';
  import katex from 'katex';
  import 'katex/dist/katex.min.css';

  export let content = '';

  let htmlContent = '';

  // Configure marked
  const markedOptions = {
    breaks: true,
    gfm: true,
  };

  marked.setOptions(markedOptions);

  function renderMath(html) {
    // Handle display math ($$...$$) - must be before inline math
    html = html.replace(/\$\$([\s\S]*?)\$\$/g, (match, math) => {
      try {
        return katex.renderToString(math, { displayMode: true });
      } catch (e) {
        console.error('KaTeX error:', e);
        return match;
      }
    });

    // Handle inline math ($...$)
    html = html.replace(/\$([^\$]+)\$/g, (match, math) => {
      try {
        return katex.renderToString(math, { displayMode: false });
      } catch (e) {
        console.error('KaTeX error:', e);
        return match;
      }
    });

    return html;
  }

  function rewriteAssetPaths(html) {
    const base = import.meta.env.BASE_URL;
    return html.replace(/(src|href)="\/(?!\/)/g, `$1="${base}`);
  }

  $: if (content) {
    let html = marked(content);
    html = rewriteAssetPaths(html);
    htmlContent = renderMath(html);
  }
</script>

<div class="markdown-content">
  {@html htmlContent}
</div>

<style>
  :global(.markdown-content) {
    font-size: 1.1rem;
    line-height: 1.8;
    color: var(--color-text);
  }

  :global(.markdown-content h1) {
    font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', serif;
    font-weight: normal;
    font-size: 2.25rem;
    margin: 1.5rem 0 1rem;
    color: var(--color-accent);
    border-bottom: 1px solid var(--color-border);
    padding-bottom: 0.5rem;
  }

  :global(.markdown-content h2) {
    font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', serif;
    font-weight: normal;
    font-size: 1.75rem;
    margin: 1.5rem 0 0.8rem;
    color: var(--color-accent);
  }

  :global(.markdown-content h3) {
    font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', serif;
    font-weight: normal;
    font-size: 1.4rem;
    margin: 1.2rem 0 0.6rem;
    color: var(--color-accent-soft);
  }

  :global(.markdown-content p) {
    margin: 1rem 0;
    line-height: 1.6;
  }

  :global(.markdown-content ul, .markdown-content ol) {
    margin: 1rem 0;
    padding-left: 2rem;
  }

  :global(.markdown-content li) {
    margin: 0.5rem 0;
    line-height: 1.6;
  }

  :global(.markdown-content strong) {
    color: var(--color-accent);
    font-weight: 600;
  }

  :global(.markdown-content a) {
    color: var(--color-accent-soft);
    text-decoration: underline;
    text-decoration-color: var(--color-border);
    text-underline-offset: 2px;
  }

  :global(.markdown-content a:hover) {
    color: var(--color-accent);
    text-decoration-color: currentColor;
  }

  :global(.markdown-content blockquote) {
    margin: 1.2rem 0;
    padding: 0.6rem 1.2rem;
    border-left: 3px solid var(--color-border);
    background: var(--color-bg);
    color: var(--color-muted);
  }

  :global(.markdown-content blockquote p) {
    margin: 0.3rem 0;
  }

  :global(.markdown-content code) {
    background: var(--color-bg);
    color: var(--color-text);
    padding: 0.2rem 0.5rem;
    border-radius: 3px;
    font-family: 'Monaco', 'Menlo', 'Courier New', monospace;
  }

  :global(.markdown-content .katex) {
    font-size: 1.1em;
    direction: ltr;
    unicode-bidi: isolate;
  }

  :global(.markdown-content .katex-display) {
    margin: 1.5rem 0;
    overflow-x: auto;
    direction: ltr;
    unicode-bidi: isolate;
  }

  :global(.markdown-content img) {
    display: block;
    margin: 1.5rem auto;
    max-width: 100%;
    border: 1px solid var(--color-border);
  }

  :global(.markdown-content table) {
    border-collapse: collapse;
    margin: 1rem 0;
    width: 100%;
  }

  :global(.markdown-content th),
  :global(.markdown-content td) {
    border: 1px solid var(--color-border);
    padding: 0.9rem 1.2rem;
    text-align: center;
  }

  :global(.markdown-content th) {
    background: var(--color-bg);
    font-weight: 600;
  }
</style>
