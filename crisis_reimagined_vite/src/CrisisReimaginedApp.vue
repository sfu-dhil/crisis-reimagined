<script setup>
import { ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useResponseStore } from './stores/responses.js'
import { useDisplayStore, useDisplaySidebarStore } from './stores/display.js'
import SideBar from './components/SideBar.vue'
import InstallationSvg from './components/InstallationSvg.vue'

const props = defineProps({
  responses: {
    type: Array,
    required: true,
  },
  config: {
    type: Object,
    required: true,
  },
})

const {
  responsesEnabled,
} = storeToRefs(useDisplayStore())
const {
  sidebarWidth,
  gitRepoLink,
  gitRepoLinkText,
} = storeToRefs(useDisplaySidebarStore())

useResponseStore().initData(props.responses)
responsesEnabled.value = props.config.responses_enabled
gitRepoLink.value = props.config.git_repo_link
gitRepoLinkText.value = props.config.git_repo_link_text

const resizeRef = ref(null)
const dragging = ref(false)
const dragStart = () => dragging.value = true
const dragMove = (event) => {
  if (dragging.value) {
    sidebarWidth.value = event.x - (resizeRef.value.getBoundingClientRect().width / 2)
    event.preventDefault()
  }
}
const dragEnd = () => dragging.value = false
</script>

<template>
  <div class="d-flex align-items-stretch w-100 h-100"
    @mousemove="dragMove" @touchmove="dragMove"
    @mouseup="dragEnd" @touchend="dragEnd"
  >
    <SideBar class="sidebar vh-100"
      :style="{ width: `${sidebarWidth}px`}"
    />
    <div ref="resizeRef" class="resize"
      @mousedown="dragStart" @touchstart="dragStart"
    />
    <InstallationSvg class="flex-grow-1 h-100" />
  </div>
</template>

<style scoped>
.sidebar {
  min-width: 320px;
  max-width: 40%;
}
.resize {
   background: #444857;
   height: 100%;
   width: 14px;
   cursor: col-resize;
   flex-shrink: 0;
   position: relative;
   z-index: 10;
   user-select: none;
}
.resize::before {
   content: "";
   position: absolute;
   top: 50%;
   left: 50%;
   transform: translate(-50%, -50%);
   width: 3px;
   height: 15px;
   border-inline: 1px solid #fff;
}
</style>