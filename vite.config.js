import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  plugins: [svelte()],
  base: '/Physics-Olympiad-Experiments/',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
  }
})
