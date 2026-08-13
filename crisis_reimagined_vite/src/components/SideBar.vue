<script setup>
import { storeToRefs } from 'pinia'
import { useDisplaySidebarStore } from '../stores/display.js'
import About from './sidebar/About.vue'
import Timeline from './sidebar/Timeline.vue'
import Crises from './sidebar/Crises.vue'

const {
  gitRepoLink,
  gitRepoLinkText,
  aboutActive,
  timelineActive,
  crisesActive,
} = storeToRefs(useDisplaySidebarStore())
</script>

<template>
  <aside class="overflow-y-auto d-flex flex-column" data-bs-theme="dark">
    <nav class="navbar navbar-expand bg-body-tertiary">
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
              :class="{ active: timelineActive }"
              @click="() => useDisplaySidebarStore().showTimeline()"
            >Timeline</button>
          </li>
          <li class="nav-item">
            <button class="nav-link"
              :class="{ active: crisesActive }"
              @click="() => useDisplaySidebarStore().showCrisis()"
            >Crises</button>
          </li>
          <li class="nav-item">
            <a class="nav-link" target="_blank"
              href="https://docs.dhil.lib.sfu.ca/privacy.html"
            >Privacy</a>
          </li>
        </ul>
      </div>
    </nav>
    <section class="flex-grow-1 mx-3 my-4" v-if="aboutActive">
      <About />
    </section>
    <section class="flex-grow-1 mx-3 my-4" v-if="timelineActive">
      <Timeline />
    </section>
    <section class="flex-grow-1 mx-3 my-4" v-if="crisesActive">
      <Crises />
    </section>
    <footer class="flex-shrink-1 pb-3">
      <div class="container-flex">
        <hr class="mt-0" />
        <div class="flex-column align-items-center justify-content-between mx-5">
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