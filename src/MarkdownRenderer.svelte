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

  $: if (content) {
    let html = marked(content);
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
    color: #333;
  }

  :global(.markdown-content h1) {
    font-size: 2.5rem;
    margin: 1.5rem 0 1rem;
    color: #667eea;
    border-bottom: 3px solid #667eea;
    padding-bottom: 0.5rem;
  }

  :global(.markdown-content h2) {
    font-size: 2rem;
    margin: 1.5rem 0 0.8rem;
    color: #764ba2;
  }

  :global(.markdown-content h3) {
    font-size: 1.5rem;
    margin: 1.2rem 0 0.6rem;
    color: #555;
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
    color: #667eea;
    font-weight: 600;
  }

  :global(.markdown-content code) {
    background: #f5f5f5;
    padding: 0.2rem 0.5rem;
    border-radius: 3px;
    font-family: 'Monaco', 'Menlo', 'Courier New', monospace;
  }

  :global(.markdown-content .katex) {
    font-size: 1.1em;
  }

  :global(.markdown-content .katex-display) {
    margin: 1.5rem 0;
    overflow-x: auto;
  }
</style>
