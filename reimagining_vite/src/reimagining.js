// vuejs
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { MotionPlugin } from '@vueuse/motion'
import ReimaginingApp from './ReimaginingApp.vue'

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

// css
import './assets/reimagining.scss'

// bootstrap
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

const ready = (fn) => document.readyState !== 'loading' ? fn() : document.addEventListener('DOMContentLoaded', fn)
ready(() => {
  document.querySelectorAll('.reimagining-app').forEach((mountEl) => {
    const app = createApp(ReimaginingApp, {
      ...mountEl.dataset,
      responses: mountEl.dataset.responsesJson ? JSON.parse(mountEl.dataset.responsesJson) : [],
      config: mountEl.dataset.configJson ? JSON.parse(mountEl.dataset.configJson) : {},
    })
    app.use(pinia)
    app.use(MotionPlugin)
    app.mount(mountEl)
  })
})
