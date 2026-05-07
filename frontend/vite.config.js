import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000,
    open: true,
    proxy: {
      '/api': {
        target: 'target: 'https://mirofish-api-sufiyan.azurewebsites.net',
        changeOrigin: true,
        secure: false
      }
    }
  }
})
