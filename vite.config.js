import { fileURLToPath, URL } from 'node:url'

import { VitePWA } from "vite-plugin-pwa";
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig({
  base: "/",
  plugins: [
    vue(),
    vueDevTools(),
    VitePWA({
      registerType: "autoUpdate",
      manifest: {
        name: "Food Rec",
        short_name: "FoodRec",
        description: "Food Recognition",
        theme_color: "#ffffff",
        background_color: "#ffffff",
        display: "standalone",
        icons: [
          {
            src: "/uploads/images.jpeg",
            sizes: "192x192",
            type: "image/png"
          }
        ]
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    proxy: {
      '/api': {
        target: 'https://master-thesis-gyzs.onrender.com',
        changeOrigin: true,
      },
    },
  },
})

