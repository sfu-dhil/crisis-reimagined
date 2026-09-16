<script setup>
import { ref, watch, nextTick } from 'vue'
import { storeToRefs } from 'pinia'
import { useDisplaySidebarStore } from '../stores/display.js'
import About from './sidebar/About.vue'
import PrivacyPolicy from './sidebar/PrivacyPolicy.vue'
import Futures from './sidebar/Futures.vue'

const props = defineProps({
  showCloseButton: {
    type: Boolean,
    default: false,
  },
})

const sidebarRef = ref(null)
const {
  gitRepoLink,
  gitRepoLinkText,
  activeNav,
  aboutActive,
  futuresActive,
  privacyPolicyActive,
} = storeToRefs(useDisplaySidebarStore())

watch(activeNav, (oldValue, newValue) => {
  if (newValue !== oldValue) { nextTick(() => sidebarRef.value.scrollTo({top: 0, behavior: 'instant'})) }
})
</script>

<template>
  <aside ref="sidebarRef" class="overflow-y-auto d-flex flex-column" data-bs-theme="dark">
    <nav class="navbar sticky-top navbar-expand bg-body-tertiary">
      <div class="container-fluid">
        <ul class="navbar-nav">
          <li class="nav-item">
            <button class="nav-link"
              :class="{ active: aboutActive }"
              @click="() => useDisplaySidebarStore().showAbout()"
            >About</button>
          </li>
          <li class="nav-item">
            <button class="nav-link"
              :class="{ active: futuresActive }"
              @click="() => useDisplaySidebarStore().showFutures()"
            >Futures</button>
          </li>
          <li class="nav-item">
            <button class="nav-link"
              :class="{ active: privacyPolicyActive }"
              @click="() => useDisplaySidebarStore().showPrivacyPolicy()"
            >Privacy</button>
          </li>
        </ul>
        <button v-if="showCloseButton" type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
    </nav>
    <section class="flex-grow-1 mx-3 my-4" v-if="aboutActive">
      <About />
    </section>
    <section class="flex-grow-1 mx-3 my-4" v-if="futuresActive">
      <Futures />
    </section>
    <section class="flex-grow-1 mx-3 my-4" v-if="privacyPolicyActive">
      <PrivacyPolicy />
    </section>
    <footer class="flex-shrink-1 pb-3">
      <div class="container-flex">
        <hr class="mt-0" />
        <div class="flex-column align-items-center justify-content-between mx-3">
          <div class="col-auto">
              <div class="small m-0">Reimagining the Public University</div>
          </div>
          <div class="col-auto" v-if="gitRepoLink && gitRepoLinkText">
            <a class="small" target="_blank" :href="gitRepoLink">{{ gitRepoLinkText }}</a>
          </div>
        </div>
      </div>
    </footer>
  </aside>
</template>

<style scoped>
</style>