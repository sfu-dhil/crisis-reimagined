<script setup>
import { ref, onMounted, watch, computed, nextTick } from 'vue'
import { storeToRefs } from 'pinia'
import { useDisplaySidebarStore } from '../stores/display.js'
import { toggleOffcanvas } from '../_utils.js'
import SideBar from './SideBar.vue'

const {
  sidebarOffcanvasShown: shown,
} = storeToRefs(useDisplaySidebarStore())

const offCanvasRef = ref(null)

watch(shown, (newValue, oldValue) => {
  if (newValue !== oldValue) { toggleOffcanvas(offCanvasRef.value, newValue) }
})
onMounted(() => {
  toggleOffcanvas(offCanvasRef.value, shown.value)
  offCanvasRef.value.addEventListener('hidden.bs.offcanvas', () => shown.value = false)
  offCanvasRef.value.addEventListener('shown.bs.offcanvas', () => shown.value = true)
})
</script>

<template>
  <div ref="offCanvasRef" class="offcanvas offcanvas-start" data-bs-scroll="true" data-bs-backdrop="false" tabindex="-1">
    <SideBar :showCloseButton="true" class="w-100"  v-if="shown" />
  </div>
</template>

<style scoped>
.offcanvas {
  width: 100vmax !important;
}
</style>