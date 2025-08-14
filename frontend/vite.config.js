import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  
  // Tell esbuild to parse .js files as JSX to allow JSX syntax in them
  optimizeDeps: {
    esbuildOptions: {
      loader: {
        '.js': 'jsx',
      },
    },
  },

  esbuild: {
    // Apply the JSX loader to .js files inside the src folder
    include: /src\/.*\.js$/,
    loader: 'jsx',
  },

  server: {
    port: 5179,
  },
});
