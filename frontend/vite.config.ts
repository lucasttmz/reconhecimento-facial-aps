import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { TanStackRouterVite }  from '@tanstack/router-plugin/vite'
import path from 'path'

export default defineConfig({
  plugins: [
    react(),
    TanStackRouterVite()
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})
