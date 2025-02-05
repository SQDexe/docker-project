import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	build: {
		outDir: 'build'
		},
	plugins: [sveltekit()]
});
