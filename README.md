# Virtual Physics Olympiad Experiments

**Live site:** https://danialht.github.io/Physics-Olympiad-Experiments/

A small Svelte + Vite site collecting virtual physics experiments. Each experiment is a problem statement rendered from Markdown with KaTeX math, often paired with a downloadable program that simulates the experiment's measurements.

## Background

Every year the IPhO has a theory section and an experimental section, the latter normally involving real apparatus, measurements, and data analysis. IPhO 2022 was held online for most countries, and with no time to ship apparatus to students, it relied on "virtual experiments" — a format that had already started gaining traction during COVID. We found it a genuinely useful way to practice experimental skills (data collection, error propagation, regression) without physical equipment, so we put together this collection.

## Experiments

1. Geometrical and Wave Optics
2. Pendulum on Another Planet
3. The Fall
4. Charged Projectile in a Rotating Field
5. Mapping a Mountain
6. Magnetic Field of an Orbiting Charge
7. Magnetic Blackbox
8. Potential of a Charged Disk
9. Acoustic Blackbox

## Development

```bash
npm install
npm run dev
```

Open the local URL Vite prints (defaults to `http://localhost:5173/Physics-Olympiad-Experiments/`).

## Building

```bash
npm run build
```

Output goes to `dist/`.

## Deployment

Pushing to `main` triggers [.github/workflows/static.yml](.github/workflows/static.yml), which builds the site with Vite and deploys it to GitHub Pages automatically — no manual `gh-pages` step needed.

## Project structure

- `src/experiments/expN.md` — problem statement for experiment N, rendered with `marked` + KaTeX
- `src/experiments/expN.js` — metadata for experiment N (English/Persian title, simulator filename)
- `public/experiments/expN/` — downloadable simulator programs, source, and answer keys for experiment N
- `src/App.svelte` — page shell, language toggle, and experiment list/detail routing
- `src/MarkdownRenderer.svelte` — renders experiment Markdown and LaTeX as HTML

## License

MIT — see [LICENSE](LICENSE).
