# Physics Olympiad Experiments Website

A Svelte-based website showcasing physics olympiad experiments.

## Setup

1. Navigate to the website directory:
```bash
cd website
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

4. Open `http://localhost:5173` in your browser.

## Building for GitHub Pages

1. Build the project:
```bash
npm run build
```

2. Deploy to GitHub Pages:
```bash
npm run deploy
```

Make sure you have:
- Initialized a git repository in the parent folder
- Set the repository as a GitHub remote
- Have the `gh-pages` package installed (included in dependencies)

## Customization

- Edit [src/App.svelte](src/App.svelte) to customize the website
- Add experiment details to the `experiments` array in the component
- Modify styles to match your preference

## Deployment Steps

1. Push your code to GitHub
2. Go to repository Settings → Pages
3. Set the source to "Deploy from a branch"
4. Select the `gh-pages` branch
5. Your site will be available at `https://yourusername.github.io/Physics-Olympiad-Experiments/`
