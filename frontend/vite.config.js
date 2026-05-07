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
        target: 'https://mirofish-api-sufiyan-d7gfercqc0ekavb2.centralindia-01.azurewebsites.net',
        changeOrigin: true,
        secure: false
      }
    }
  }
})
