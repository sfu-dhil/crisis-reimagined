<script setup>
import { ref } from 'vue'
import { storeToRefs } from 'pinia'
import { breakpointsBootstrapV5, useBreakpoints } from '@vueuse/core'
import { useResponseStore } from './stores/responses.js'
import { useDisplayStore, useDisplaySidebarStore } from './stores/display.js'
import SideBar from './components/SideBar.vue'
import SideBarOffcanvas from './components/SideBarOffcanvas.vue'
import InstallationSvg from './components/InstallationSvg.vue'

const breakpoints = useBreakpoints(breakpointsBootstrapV5)
const isMediumOrSmallerScreen = breakpoints.smallerOrEqual('md')
const isLargerThanMediumScreen = breakpoints.greater('md')

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
  sidebarOffcanvasShown,
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
  if (dragging.value && resizeRef.value) {
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
    <SideBar class="sidebar vh-100" v-if="isLargerThanMediumScreen"
      :style="{ width: `${sidebarWidth}px`}"
    />
    <div ref="resizeRef" class="resize" v-if="isLargerThanMediumScreen"
      @mousedown="dragStart" @touchstart="dragStart"
    />
    <SideBarOffcanvas v-if="sidebarOffcanvasShown && isMediumOrSmallerScreen" />
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