<script setup>
import { ref, watch, onUnmounted, onMounted, nextTick } from 'vue'
import { Tooltip } from 'bootstrap'
import { storeToRefs } from 'pinia'
import { useFullscreen } from '@vueuse/core'
import panzoom from 'panzoom'
import { useResponseStore } from '../stores/responses.js'
import { useDisplayStore, useDisplayInstallationStore, useDisplaySidebarStore } from '../stores/display.js'
import { ResponseResourceTypes } from '../_resourceTypes.js'
import QuestionnaireModal from './QuestionnaireModal.vue'
import ResponsesModal from './ResponsesModal.vue'

const SVG_HEIGHT = 3456
const MAX_ZOOM = 6
const MIN_ZOOM = 0.2
const {
  hasKnowledgeObjects,
  hasRestitutionObjects,
  hasTechnologyObjects,
  hasGeopoliticsObjects,
  hasMarketizationObjects,
  hasMassificationObjects,
} = storeToRefs(useResponseStore())
const {
  zoomToElementClassId,
} = storeToRefs(useDisplayInstallationStore())

const {
  questionnaireModalShown,
  responsesModalShown,
} = storeToRefs(useDisplayStore())

const articleRef = ref(null)
const { isFullscreen, toggle: toggleFullscreen } = useFullscreen(articleRef)
const svgRef = ref(null)
const svgGroupRef = ref(null)
const panZoomInstance = ref(null)
const grabbing = ref(false)

const panUp = () => {
  const {x, y} = panZoomInstance.value.getTransform()
  panZoomInstance.value.smoothMoveTo(x, y+100)
}
const panDown = () => {
  const {x, y} = panZoomInstance.value.getTransform()
  panZoomInstance.value.smoothMoveTo(x, y-100)
}
const panLeft = () => {
  const {x, y} = panZoomInstance.value.getTransform()
  panZoomInstance.value.smoothMoveTo(x+100, y)
}
const panRight = () => {
  const {x, y} = panZoomInstance.value.getTransform()
  panZoomInstance.value.smoothMoveTo(x-100, y)
}
const zoomIn = () => {
  const { width, height } = svgRef.value.getBoundingClientRect()
  panZoomInstance.value.smoothZoom(width/2, height/2, 2)
}
const zoomOut = () => {
  const { width, height } = svgRef.value.getBoundingClientRect()
  panZoomInstance.value.smoothZoom(width/2, height/2, 0.5)
}
watch(zoomToElementClassId, (newValue, oldValue) => {
  if (newValue && newValue !== oldValue) {
    zoomToElementClassId.value = null
    panZoomInstance.value.pause()
    panZoomInstance.value.resume()
    const xValues = []
    const yValues = []
    svgGroupRef.value.querySelectorAll(`.${newValue}`).forEach((targetEl) => {
      const { x, y, width, height } = targetEl.getBBox()
      const point = svgRef.value.createSVGPoint()
      point.x = x
      point.y = y
      const { x: minX, y: minY } = point.matrixTransform(svgGroupRef.value.getScreenCTM().inverse().multiply(targetEl.getScreenCTM()))
      point.x = x + width
      point.y = y + height
      const { x: maxX, y: maxY } = point.matrixTransform(svgGroupRef.value.getScreenCTM().inverse().multiply(targetEl.getScreenCTM()))
      xValues.push(minX, maxX)
      yValues.push(minY, maxY)
    })
    const { width: svgWidth, height: svgHeight } = svgRef.value.getBoundingClientRect()
    const targetCenterX = (Math.max(...xValues) + Math.min(...xValues)) / 2
    const targetWidth = Math.max(...xValues) - Math.min(...xValues)
    const targetCenterY = (Math.max(...yValues) + Math.min(...yValues)) / 2
    const targetHeight = Math.max(...yValues) - Math.min(...yValues)
    const { scale } = panZoomInstance.value.getTransform()
    panZoomInstance.value.moveTo(svgWidth/2 - (targetCenterX * scale), svgHeight/2 - (targetCenterY * scale))
    let zoomAbs = 1
    if (svgWidth < targetWidth) {
      zoomAbs = Math.max(MIN_ZOOM, Math.min(zoomAbs, svgWidth/targetWidth))
    }
    if (svgHeight < targetHeight) {
      zoomAbs = Math.max(MIN_ZOOM, Math.min(zoomAbs, svgHeight/targetHeight))
    }
    panZoomInstance.value.smoothZoomAbs(svgWidth/2, svgHeight/2, zoomAbs)
  }
})
const resetTooltips = () => {
  nextTick(() => {
    articleRef.value.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(
      (tooltipTriggerEl) => Tooltip.getOrCreateInstance(tooltipTriggerEl, {container: articleRef.value}).hide()
    )
  })
}
watch(isFullscreen, (oldValue, newValue) => {
  if (newValue != oldValue) { resetTooltips() }
})
const fixModalBackdrop = () => {
  nextTick(() => {
    const backdrop = document.querySelector('.modal-backdrop')
    if (backdrop) { articleRef.value.appendChild(backdrop) }
  })
}
watch(questionnaireModalShown, (isShown) => {
  if (isShown && isFullscreen.value) { fixModalBackdrop() }
})
watch(responsesModalShown, (isShown) => {
  if (isShown && isFullscreen.value) { fixModalBackdrop() }
})
onMounted(() => {
  resetTooltips()
  const INITIAL_ZOOM =  svgRef.value.clientHeight / SVG_HEIGHT
  panZoomInstance.value = panzoom(svgGroupRef.value, {
    maxZoom: MAX_ZOOM,
    minZoom: MIN_ZOOM,
    bounds: true,
    boundsPadding: 0.4,
    enableTextSelection: false,
    initialX: 0,
    initialY: 0,
    initialZoom: Math.min(MAX_ZOOM, Math.max(MIN_ZOOM, INITIAL_ZOOM)),
    // transformOrigin: { x: 0.5, y: 0.5 },
    beforeMouseDown: (e) => {
      // const isText = !!e.target.closest('text')
      const isLink = !!e.target.closest('a')
      const isQuestionnaire = !!e.target.closest('.questionnaire')
      return !!isQuestionnaire || !!isLink
    },
  })
  panZoomInstance.value.on('panstart', (e) => grabbing.value = true)
  panZoomInstance.value.on('panend', (e) => grabbing.value = false)
})
onUnmounted(() => {
  if (panZoomInstance.value) {
    panZoomInstance.value.dispose()
  }
})
</script>

<template>
  <article ref="articleRef" class="position-relative bg-light">
    <svg ref="svgRef" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"
      :class="{ grabbing: grabbing }" class="position-relative"
    >
      <g ref="svgGroupRef">
        <g isolation="isolate" width="11376" height="3456">
          <g>
            <line x1="1492.85" y1="2862.98" x2="1492.85" y2="2860.98" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="1492.85" y1="2851" x2="1492.85" y2="6.8" fill="none" stroke="#a57e2d" stroke-dasharray="3.99 9.98" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="1492.85" y1="1.82" x2="1492.85" y2="-.18" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="216.97" y1="3131.83" x2="216.97" y2="3129.83" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="216.97" y1="3119.84" x2="216.97" y2="6.81" fill="none" stroke="#a57e2d" stroke-dasharray="3.99 9.99" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="216.97" y1="1.82" x2="216.97" y2="-.18" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <text class="BLACK-DEATH" transform="translate(1183.0491 1738.2488)" fill="#223f9a" font-weight="300" mix-blend-mode="multiply"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="0" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">Black Death</tspan><tspan x="133.58" y="0" xml:space="preserve"> leads to </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="24">major collapse in </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="48">student enrollment.</tspan></tspan></text>
          <g>
            <line x1="379.56" y1="2343.05" x2="417.47" y2="2343.05" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="410.84 2351.23 409.48 2349.77 416.7 2343.05 409.48 2336.34 410.84 2334.87 419.64 2343.05 410.84 2351.23" fill="#21409a"/>
          </g>
          <text class="PRINTING-PRESS" transform="translate(1635.8406 402.2388)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300"><tspan font-size="24"><tspan x="0" y="0">Intellectuals no longer </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">need a university position </tspan></tspan><tspan font-size="24"><tspan x="0" y="68">to participate in </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">scholarship, creating a </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">university ‘brain drain.’ </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">The availability of,and </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">need for, print media of </tspan></tspan><tspan font-size="24"><tspan x="0" y="238">all kinds also becomes </tspan></tspan><tspan font-size="24"><tspan x="0" y="272">essential in universities, </tspan></tspan><tspan font-size="24"><tspan x="0" y="306">leading to a print-dominant </tspan></tspan><tspan font-size="24"><tspan x="0" y="340">culture lasting to this </tspan></tspan><tspan font-size="24"><tspan x="0" y="374">day. </tspan></tspan></text>
          <g>
            <line x1="1570.15" y1="392.92" x2="1608.06" y2="392.92" fill="none" stroke="#223f9a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="1601.43 401.1 1600.06 399.64 1607.29 392.93 1600.06 386.21 1601.43 384.75 1610.22 392.93 1601.43 401.1" fill="#223f9a"/>
          </g>
          <text class="PRINTING-PRESS" transform="translate(1533.4053 350)" fill="#223f9a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">PRINTING PRESS</tspan></text>
          <circle cx="1492.85" cy="3138.82" r="6.2" fill="#a57e2d"/>
          <circle cx="216.97" cy="3138.44" r="6.2" fill="#a57e2d"/>
          <g opacity=".8">
            <rect y="2950.2" width="1038.95" height="301.59" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <rect x="1662.8" y="877.8" width="586.38" height="157.56" fill="#f7ec12"/>
          </g>
          <g mix-blend-mode="multiply" opacity=".8">
            <rect x="1300.09" y="1133.41" width="703.45" height="249.77" transform="translate(-130.6845 2323.4209) rotate(-68.1592)" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <circle cx="1274.8" cy="842.02" r="226.61" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <path d="M644.18,1650.61h120.78s93.98-10.9,97.81,126.61c3.83,137.51,0,193.25,0,193.25l150.07,158.36,28.11,403.24-347.28-314.47,6.85-253.58h-66.48l-5.81,72.68-163.94-236.49,175.57-255.85,4.32,106.26Z" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <path d="M1136.02,1127.6h355.31s60,2,68,92,0,159.59,0,159.59l3.56,154.41h-158.77v-154.41s.18-49.59-72.3-48.59c-72.48,1-142.48,0-142.48,0h-53.3v-203Z" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <polygon points="2249.18 2532.07 1040.31 2532.07 987.87 2123.5 2249.18 2123.5 2249.18 2532.07" fill="#f7ec12"/>
          </g>
          <text transform="translate(230 312.31)" fill="#223f9a" font-family="GroteskRemixMonospace-medium, &apos;GroteskRemix Monospace&apos;" font-size="165" font-weight="500" mix-blend-mode="multiply"><tspan x="0" y="0">NEVER </tspan><tspan x="0" y="223">LET A </tspan><tspan x="0" y="446">GOOD CRISIS </tspan><tspan x="0" y="669">GO TO WASTE</tspan></text>
          <line x1="230" y1="374.48" x2="740" y2="374.48" fill="none" mix-blend-mode="multiply" stroke="#223f9a" stroke-miterlimit="10" stroke-width="13"/>
          <line x1="230" y1="592.57" x2="740" y2="592.57" fill="none" mix-blend-mode="multiply" stroke="#223f9a" stroke-miterlimit="10" stroke-width="13"/>
          <line x1="230" y1="810.66" x2="1340" y2="810.66" fill="none" mix-blend-mode="multiply" stroke="#223f9a" stroke-miterlimit="10" stroke-width="13"/>
          <line x1="230" y1="1045.79" x2="1340" y2="1045.79" fill="none" mix-blend-mode="multiply" stroke="#223f9a" stroke-miterlimit="10" stroke-width="13"/>
          <g mix-blend-mode="multiply">
            <text class="PAPAL-SCHISM" transform="translate(658.458 1325.8376)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">The Church’s division creates </tspan><tspan x="0" y="34">uncertainty over papal authority, </tspan><tspan x="0" y="68">making travel unsafe and limiting </tspan><tspan x="0" y="102">international study. Universities </tspan><tspan x="0" y="136">adapt by turning toward local </tspan><tspan x="0" y="170">students and serving a growing </tspan><tspan x="0" y="204">middle class.</tspan></text>
          </g>
          <g>
            <line x1="607.61" y1="1317.4" x2="645.52" y2="1317.4" fill="none" stroke="#223f9a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="638.89 1325.58 637.52 1324.12 644.75 1317.4 637.52 1310.69 638.89 1309.22 647.68 1317.4 638.89 1325.58" fill="#223f9a"/>
          </g>
          <text class="PAPAL-SCHISM" transform="translate(575.3711 1278.189)" fill="#223f9a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">PAPAL SCHISM</tspan></text>
          <text transform="translate(1349.2065 3282.8645)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" mix-blend-mode="multiply" opacity=".75"><tspan x="0" y="0">1400</tspan></text>
          <text transform="translate(85.8525 3281.1746)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" mix-blend-mode="multiply" opacity=".75"><tspan x="0" y="0">1100</tspan></text>
          <text transform="translate(435.5381 2351.6658)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan font-size="24"><tspan x="0" y="0">For two years, almost no </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">courses are taught in Paris. </tspan></tspan><tspan font-size="24"><tspan x="0" y="68">Finally, in 1231, King Louis </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">IX and Blanche de Castile  </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">recognize the independence </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">of the university and renew </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">and extend the privileges </tspan></tspan><tspan font-size="24"><tspan x="0" y="238">granted to it in 1200 by </tspan></tspan><tspan x="0" y="272" font-size="24">King Philip Augustus.</tspan><tspan x="382.53" y="272" font-size="21"> </tspan></text>
          <text transform="translate(839.37 285.77)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan fill="#223f9a"><tspan x="0" y="0">In the thirteenth century, the </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="24">university transforms into a </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="48">self-governing corporation, </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="72">successfully resisting </tspan></tspan><tspan x="0" y="96" fill="#223f9a">religious control.</tspan><tspan x="218.58" y="96" fill="#010101"> </tspan></text>
          <circle cx="825.15" cy="279.27" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <circle cx="1169.36" cy="1731.75" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(1049.7642 1953.9963)" fill="#223f9a" font-weight="300" mix-blend-mode="multiply"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="0">The production of paper </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="24">begins in Germany.</tspan></tspan></text>
          <circle cx="1036.07" cy="1947.5" r="5.96" fill="none" mix-blend-mode="multiply" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(1797.4419 1486.7122)" fill="#223f9a" font-weight="300" mix-blend-mode="multiply"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="0">Martin Luther publishes </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="24">the </tspan><tspan x="48.57" y="24" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">95 Theses </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5"><tspan x="0" y="48">(Disputation on the </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5"><tspan x="0" y="72">Power and Efficacy of </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5"><tspan x="0" y="96">Indulgences), </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="120">presenting them as </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="144">prompts for academic </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="168">debate and distributing </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="192">them widely as </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="216">pamphlets.</tspan></tspan></text>
          <circle cx="1783.75" cy="1480.21" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <g>
            <line x1="1492.85" y1="2964.94" x2="1492.85" y2="2962.94" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="1492.85" y1="2953.42" x2="1492.85" y2="2918.22" fill="none" stroke="#a57e2d" stroke-dasharray="3.81 9.51" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="1492.85" y1="2913.46" x2="1492.85" y2="2911.46" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="1492.85" y1="3132.62" x2="1492.85" y2="3130.62" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="1492.85" y1="3121" x2="1492.85" y2="3018.09" fill="none" stroke="#a57e2d" stroke-dasharray="3.85 9.62" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="1492.85" y1="3013.28" x2="1492.85" y2="3011.28" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <text transform="translate(545.1367 2913.3855)" fill="#223f9a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" mix-blend-mode="multiply"><tspan font-size="97"><tspan x="0" y="0">an unfinished timeline</tspan></tspan><tspan font-size="97"><tspan x="161.8" y="100" xml:space="preserve"> of the canadian </tspan></tspan><tspan x="134.83" y="200" font-size="97">public university</tspan></text>
          <text transform="translate(343.938 2306.4661)" fill="#223f9a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">PARIS STUDENT STRIKES</tspan></text>
          <g>
            <line x1="4052.32" y1="1691.56" x2="4052.32" y2="1689.56" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="4052.32" y1="1679.56" x2="4052.32" y2="4.47" fill="none" stroke="#a57e2d" stroke-dasharray="4 10" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g opacity=".8">
            <path d="M4509.8,750.88s-64.1,27.05-136.79,90.87c-79.84,70.1-170.06,184.58-197.07,356.3h-281.84l-124.69-155.9-101.57,120.06v-476.69h449.55l-171.68,178.6,79.84,74.37,56.62-126.03s45.96-81.81,93.77-138.73c51.18-60.93,110.57-110.17,195.03-146.89,55.63-24.19,136.5-42.32,136.5-42.32l2.32,266.35Z" fill="#f7ec12"/>
          </g>
          <g mix-blend-mode="multiply">
            <g>
              <line x1="2575.85" y1="3136.12" x2="2575.85" y2="3134.12" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
              <line x1="2575.85" y1="3124.11" x2="2575.85" y2="1685.24" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.01" stroke-miterlimit="10" stroke-width="3"/>
              <line x1="2575.85" y1="1680.23" x2="2575.85" y2="1678.23" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            </g>
          </g>
          <g>
            <line x1="3546.06" y1="3126.43" x2="3546.06" y2="3124.43" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="3546.06" y1="3114.45" x2="3546.06" y2="479.85" fill="none" stroke="#a57e2d" stroke-dasharray="3.99 9.98" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="3546.06" y1="474.86" x2="3546.06" y2="472.86" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="4052.32" y1="3135.62" x2="4052.32" y2="3133.62" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="4052.32" y1="3123.68" x2="4052.32" y2="1987.18" fill="none" stroke="#a57e2d" stroke-dasharray="3.98 9.94" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="4052.32" y1="1982.21" x2="4052.32" y2="1980.21" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <path d="M3766.91,1042.15c-49.44-63.39,22.72,29.13-26.72-34.26l198.65-143.77" fill="#f7ec12" mix-blend-mode="multiply" opacity=".6"/>
          <circle cx="4052.32" cy="3134.83" r="6.2" fill="#a57e2d"/>
          <text transform="translate(3391.5431 3279.7327)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" opacity=".75"><tspan x="0" y="0">1900</tspan></text>
          <text transform="translate(2464.3879 3280.5227)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" opacity=".75"><tspan x="0" y="0">1</tspan><tspan x="32.52" y="0" letter-spacing="-.04em">7</tspan><tspan x="93.48" y="0">50</tspan></text>
          <circle cx="2575.85" cy="3136.12" r="6.2" fill="#a57e2d"/>
          <circle cx="3546.06" cy="3132.63" r="6.2" fill="#a57e2d"/>
          <g opacity=".8">
            <polygon points="4181.84 2532.07 2211.57 2532.07 2102.91 2123.5 4181.84 2123.5 4181.84 2532.07" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <path d="M4177.29,2138.27c0,133.38-.01,266.77-.06,400.15-.04,122.25-.09,244.5-.17,366.75l32.46,12.04v-166.31l295.18,344.89v145.35h-503.29c.87-371.55-.87-482.62,0-854.16" fill="#f7ec12"/>
          </g>
          <text transform="translate(2946.8152 2474.0935)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">USEFUL KNOWLEDGE</tspan></text>
          <g mix-blend-mode="multiply">
            <g>
              <line x1="2979.82" y1="2514.37" x2="3017.73" y2="2514.37" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
              <polygon points="3011.1 2522.55 3009.73 2521.09 3016.96 2514.38 3009.73 2507.66 3011.1 2506.2 3019.89 2514.38 3011.1 2522.55" fill="#21409a"/>
            </g>
          </g>
          <text transform="translate(2653.5544 1147.7029)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">CONFLICT OF THE FACULTIES</tspan></text>
          <text transform="translate(2749.5093 1196.8545)" fill="#21409a" font-weight="300"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="0">In response to Prussian university </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="34">censorship, Emmanuel Kant publishes </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="68" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">The Conflict of the Faculties</tspan><tspan x="528.26" y="68" xml:space="preserve"> in 1798. </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="102">Von Humbolt uses this text as inspiration </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="136">to establish the University of Berlin in </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="170">1810, providing the blueprint for the </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="204">modern research university.</tspan></tspan></text>
          <g>
            <line x1="2687.99" y1="1190.57" x2="2725.9" y2="1190.57" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="2719.27 1198.75 2717.9 1197.29 2725.13 1190.58 2717.9 1183.86 2719.27 1182.4 2728.06 1190.58 2719.27 1198.75" fill="#21409a"/>
          </g>
          <text transform="translate(2989.8975 169.103)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">KING’S COLLEGE </tspan><tspan x="0" y="58">LAND-GRANT</tspan></text>
          <g>
            <line x1="3019.55" y1="272.2" x2="3057.46" y2="272.2" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="3050.83 280.38 3049.47 278.92 3056.69 272.2 3049.47 265.49 3050.83 264.02 3059.63 272.2 3050.83 280.38" fill="#21409a"/>
          </g>
          <text transform="translate(3084.6906 278.5488)" fill="#21409a" mix-blend-mode="multiply"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">An Anglican bishop donates </tspan></tspan><tspan font-size="24"><tspan x="0" y="34" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300">225,944</tspan><tspan x="127.51" y="34" font-family="MyriadPro-Regular, &apos;Myriad Pro&apos;"> </tspan><tspan x="132.6" y="34" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300">acres to the future </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="68">University of Toronto to ensure </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="102">its financial viability, making </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="136">it one of the first university </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="170">land-grants in North America. The </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="204">land was previously taken from </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="238">the Mississauga Ojibwa.</tspan></tspan></text>
          <text transform="translate(3914.0588 3279.7327)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" mix-blend-mode="multiply" opacity=".75"><tspan x="0" y="0">1</tspan><tspan x="32.52" y="0" letter-spacing="-.05em">9</tspan><tspan x="106.68" y="0">45</tspan></text>
          <text transform="translate(3042.1984 2524.6243)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Inspired by Jeremy </tspan><tspan x="0" y="34">Bentham’s </tspan><tspan x="182.16" y="34" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">Chrestomathia</tspan><tspan x="418.96" y="34">, </tspan><tspan x="0" y="68">Utilitarians establish the </tspan><tspan x="0" y="102">University of London </tspan><tspan x="0" y="136">(later University College </tspan><tspan x="0" y="170">London). The project aims </tspan><tspan x="0" y="204">to teach ‘useful </tspan><tspan x="0" y="238">knowledge’ and break the </tspan><tspan x="0" y="272">Church of England’s </tspan><tspan x="0" y="306">monopoly over university </tspan><tspan x="0" y="340">education in England.</tspan><tspan x="382.53" y="340" letter-spacing="-.2em">	</tspan></text>
          <g mix-blend-mode="multiply">
            <text transform="translate(3664.2208 2343.5286)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300"><tspan font-size="24"><tspan x="0" y="0">In his 1917 </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">lecture </tspan><tspan x="145.73" y="34" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">Science as </tspan></tspan><tspan font-size="24"><tspan x="0" y="68" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">a Vocation</tspan><tspan x="182.16" y="68">, Max </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">Weber argues that </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">university </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">teaching should </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">separate fact from </tspan></tspan><tspan font-size="24"><tspan x="0" y="238">value, thereby </tspan></tspan><tspan font-size="24"><tspan x="0" y="272">establishing the </tspan></tspan><tspan font-size="24"><tspan x="0" y="306">principle of </tspan></tspan><tspan font-size="24"><tspan x="0" y="340">scientific </tspan></tspan><tspan x="0" y="381" font-size="24">neutrality.</tspan><tspan x="200.37" y="381" font-size="21" letter-spacing="-.01em">	</tspan></text>
          </g>
          <g>
            <line x1="3605.88" y1="2335.09" x2="3643.79" y2="2335.09" fill="none" stroke="#223f9a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="3637.16 2343.27 3635.8 2341.81 3643.02 2335.09 3635.8 2328.38 3637.16 2326.92 3645.96 2335.09 3637.16 2343.27" fill="#223f9a"/>
          </g>
          <text transform="translate(3571.499 2241.3728)" fill="#223f9a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">SCIENCE AS </tspan><tspan x="0" y="58">VOCATION</tspan></text>
          <text transform="translate(3769.5101 1776.4382)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">Operating revenue for Canadian </tspan><tspan x="0" y="34">universities declines by almost 30% </tspan><tspan x="0" y="68">between 1930 and 1935. Despite this, </tspan><tspan x="0" y="102">administrators at the University of </tspan><tspan x="0" y="136">Saskatchewan accept promissory notes </tspan><tspan x="0" y="170">from one-third of their students who </tspan><tspan x="0" y="204">are unable to pay fees.</tspan></text>
          <g>
            <line x1="3701.65" y1="1772.73" x2="3739.55" y2="1772.73" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="3732.93 1780.91 3731.56 1779.44 3738.79 1772.73 3731.56 1766.02 3732.93 1764.55 3741.72 1772.73 3732.93 1780.91" fill="#21409a"/>
          </g>
          <text transform="translate(3667.9854 1727.1941)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">THE GREAT DEPRESSION</tspan></text>
          <text transform="translate(3777.2826 1359.0046)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">In 1932, IBM </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="24">researcher Richard </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="48">Warren files a patent </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="72">for optical mark </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="96">sense systems for </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="120" xml:space="preserve">test scoring,  </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="144">commonly known as </tspan></tspan><tspan x="0" y="168" fill="#223f9a">Scantron.</tspan><tspan x="109.29" y="168" fill="#21409a" letter-spacing="1.41em">	</tspan><tspan x="144" y="168" fill="#21409a" letter-spacing="1.49em">	</tspan></text>
          <circle cx="3763.55" cy="1355.01" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <circle cx="3617.84" cy="606.03" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <g>
            <text transform="translate(2411.0564 1828.0012)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">The Republic of Letters</tspan><tspan x="279.3" y="0" xml:space="preserve"> fosters a </tspan><tspan x="0" y="24">bloom of new ideas in the public </tspan><tspan x="0" y="48">domain, drawing the middle class </tspan><tspan x="0" y="72">into academic discourse and calling </tspan><tspan x="0" y="96">antiquated university practices </tspan><tspan x="0" y="120">into question.</tspan></text>
            <circle cx="2399.31" cy="1821.5" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          </g>
          <text transform="translate(3248.0314 699.6377)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">The 1867 </tspan><tspan x="0" y="24">Constitution Act </tspan><tspan x="0" y="48">designates </tspan><tspan x="0" y="72">education to be </tspan><tspan x="0" y="96">regulated </tspan><tspan x="0" y="120">exclusively at the </tspan><tspan x="0" y="144">provincial level.</tspan></text>
          <circle cx="3228.89" cy="695.16" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(4083.0854 2263.4333)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Vannevar Bush publishes </tspan><tspan stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5"><tspan x="0" y="24">Science: The Endless </tspan></tspan><tspan x="0" y="48" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">Frontier</tspan><tspan x="97.15" y="48">, proposing a linear </tspan><tspan x="0" y="72">model of innovation—basic </tspan><tspan x="0" y="96">research → applied research → </tspan><tspan x="0" y="120">development → innovation—and </tspan><tspan x="0" y="144">arguing that the government </tspan><tspan x="0" y="168">should fund basic research as </tspan><tspan x="0" y="192">the foundation for future </tspan><tspan x="0" y="216">gains in wealth, health, and </tspan><tspan x="0" y="240">national security.</tspan></text>
          <circle cx="4070.41" cy="2256.93" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <g mix-blend-mode="multiply">
            <g>
              <line x1="2575.85" y1="1612.53" x2="2575.85" y2="1610.53" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
              <line x1="2575.85" y1="1600.5" x2="2575.85" y2="4.49" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.03" stroke-miterlimit="10" stroke-width="3"/>
            </g>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="2575.85" y1="1645.4" x2="2575.85" y2="1641.87" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="2575.85" y1="1623.39" x2="2575.85" y2="1619.86" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="2575.85" y1="1668.94" x2="2575.85" y2="1665.41" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="3546.06" y1="260.94" x2="3546.06" y2="258.94" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="3546.06" y1="249.04" x2="3546.06" y2="4.43" fill="none" stroke="#a57e2d" stroke-dasharray="3.96 9.9" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="3546.06" y1="288.16" x2="3546.06" y2="284.64" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="3546.06" y1="299.84" x2="3546.06" y2="296.31" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="3546.06" y1="317.1" x2="3546.06" y2="313.58" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="3546.06" y1="352.71" x2="3546.06" y2="349.19" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="3546.06" y1="368.7" x2="3546.06" y2="365.18" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="3546.06" y1="460.73" x2="3546.06" y2="457.21" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="3546.06" y1="428.14" x2="3546.06" y2="424.61" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="3546.06" y1="399.79" x2="3546.06" y2="396.26" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="3546.06" y1="334.61" x2="3546.06" y2="331.09" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="3546.06" y1="385.36" x2="3546.06" y2="381.84" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="4052.32" y1="1776.75" x2="4052.32" y2="1774.75" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="4052.32" y1="1764.76" x2="4052.32" y2="1727.78" fill="none" stroke="#a57e2d" stroke-dasharray="4 9.99" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="4052.32" y1="1722.78" x2="4052.32" y2="1720.78" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="4052.41" y1="1791.98" x2="4052.41" y2="1788.45" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="4052.41" y1="1814.9" x2="4052.41" y2="1811.37" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="4052.41" y1="1831.47" x2="4052.41" y2="1827.95" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="4052.41" y1="1857.86" x2="4052.41" y2="1854.34" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="4052.41" y1="1882.38" x2="4052.41" y2="1878.85" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="4052.41" y1="1897.68" x2="4052.41" y2="1894.15" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="4052.41" y1="1924.29" x2="4052.41" y2="1920.77" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="4052.32" y1="1958.22" x2="4052.32" y2="1954.7" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <polygon points="2756.32 1035.36 2208.28 1035.36 2226.38 877.8 2756.32 877.8 2756.32 1035.36" fill="#f7ec12" opacity=".8"/>
          <text transform="translate(4029.5149 823.1772)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">VETERANS </tspan><tspan x="0" y="58">REHABILITATION</tspan><tspan x="0" y="116">ACT</tspan></text>
          <text transform="translate(3633.6403 610.0093)" fill="#223f9a" font-weight="300" mix-blend-mode="multiply"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="0">American eugenicist Lewis </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="24">Terman publishes his revision </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="48">of the Binet-Simon Intelligence </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="72">Test in 1916, which will become </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="96">colloquially known as the IQ </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="120">test.</tspan></tspan></text>
          <g mix-blend-mode="multiply">
            <text transform="translate(4119.6293 990.9922)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">Economic </tspan><tspan x="0" y="34">development </tspan><tspan x="0" y="68">following WWII </tspan><tspan x="0" y="102">leads to </tspan><tspan x="0" y="136">unprecedented </tspan><tspan x="0" y="170">investment in </tspan><tspan x="0" y="204">higher education, </tspan><tspan x="0" y="238">dramatically </tspan><tspan x="0" y="272">expanding the </tspan><tspan x="0" y="306">country&apos;s </tspan><tspan x="0" y="340">academic </tspan><tspan x="0" y="374">infrastructure. </tspan><tspan x="0" y="408">By 1949-50 </tspan><tspan x="0" y="442">veterans account </tspan><tspan x="0" y="476">for 21% of all </tspan><tspan x="0" y="510">Canadian </tspan><tspan x="0" y="544">university </tspan><tspan x="0" y="578">students.</tspan></text>
          </g>
          <g>
            <line x1="4059.79" y1="982.93" x2="4097.7" y2="982.93" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="4091.07 991.11 4089.71 989.65 4096.93 982.94 4089.71 976.22 4091.07 974.76 4099.87 982.94 4091.07 991.11" fill="#21409a"/>
          </g>
          <g>
            <line x1="4628.26" y1="807.15" x2="4666.17" y2="807.15" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="4659.54 815.33 4658.18 813.86 4665.4 807.15 4658.18 800.44 4659.54 798.97 4668.34 807.15 4659.54 815.33" fill="#21409a"/>
          </g>
          <circle cx="4841.6" cy="1328.08" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <g>
            <line x1="7932.51" y1="3134.31" x2="7932.51" y2="3132.31" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7932.51" y1="3122.24" x2="7932.51" y2="3028.59" fill="none" stroke="#a57e2d" stroke-dasharray="4.03 10.07" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7932.51" y1="3023.56" x2="7932.51" y2="3021.56" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="7932.51" y1="2503.33" x2="7932.51" y2="2501.33" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7932.51" y1="2491.3" x2="7932.51" y2="1527.42" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.03" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7932.51" y1="1522.41" x2="7932.51" y2="1520.41" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="7932.51" y1="2628.52" x2="7932.51" y2="2626.52" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7932.51" y1="2616.75" x2="7932.51" y2="2539.52" fill="none" stroke="#a57e2d" stroke-dasharray="3.91 9.78" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7932.51" y1="2534.63" x2="7932.51" y2="2532.63" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="2515.87" x2="7932.51" y2="2512.35" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="2652.03" x2="7932.51" y2="2648.51" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="2789.49" x2="7932.51" y2="2785.97" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="2867.95" x2="7932.51" y2="2864.43" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="2956.92" x2="7932.51" y2="2953.39" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="2972.55" x2="7932.51" y2="2969.02" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="2994.26" x2="7932.51" y2="2990.74" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="2665.44" x2="7932.51" y2="2661.91" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="2683.17" x2="7932.51" y2="2679.65" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <rect x="7931.01" y="2699" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2716.09" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2730.75" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2749.11" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2766.71" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2817.18" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2833.33" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2850.32" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2883" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2895.75" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2920.3" width="3" height="4.1" fill="#a57e2d"/>
          <rect x="7931.01" y="2935.79" width="3" height="4.1" fill="#a57e2d"/>
          <line x1="7005.68" y1="950.34" x2="7035.28" y2="999.71" fill="#f7ec12"/>
          <text transform="translate(8677.6467 3284.8676)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300"><tspan x="0" y="0">2025</tspan></text>
          <g opacity=".8">
            <circle cx="7409.87" cy="676.46" r="143.5" fill="#f7ec12"/>
          </g>
          <g mix-blend-mode="multiply" opacity=".8">
            <path d="M8494.35,261.49c214.97,184.19,497.15,446.35,712.11,630.54,37.14,31.83-37.14-31.83,0,0l-.1,441.16-670.58-575.37c-13.27-136.92-26.55-273.81-39.83-410.73" fill="#f7ec12"/>
          </g>
          <g>
            <line x1="7249.12" y1="1167.9" x2="7249.12" y2="1165.9" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7249.12" y1="1155.96" x2="7249.12" y2="5.37" fill="none" stroke="#a57e2d" stroke-dasharray="3.98 9.94" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7249.12" y1=".4" x2="7249.12" y2="-1.6" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="7249.12" y1="1617.03" x2="7249.12" y2="1615.03" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7249.12" y1="1605.01" x2="7249.12" y2="1174.91" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.03" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7249.12" y1="1169.9" x2="7249.12" y2="1167.9" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="7249.12" y1="2085.88" x2="7249.12" y2="2083.88" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7249.12" y1="2074" x2="7249.12" y2="1691.45" fill="none" stroke="#a57e2d" stroke-dasharray="3.95 9.88" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7249.12" y1="1686.51" x2="7249.12" y2="1684.51" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="7249.12" y1="3137.67" x2="7249.12" y2="3135.67" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7249.12" y1="3125.67" x2="7249.12" y2="2318.42" fill="none" stroke="#a57e2d" stroke-dasharray="4 10" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7249.12" y1="2313.42" x2="7249.12" y2="2311.42" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <circle cx="7249.12" cy="3136.87" r="6.2" fill="#a57e2d"/>
          <text transform="translate(7781.4775 3280.6537)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300"><tspan x="0" y="0">2</tspan><tspan x="75.12" y="0" letter-spacing="-.03em">0</tspan><tspan x="180.72" y="0">10</tspan></text>
          <g>
            <line x1="7932.51" y1="193.49" x2="7932.51" y2="191.49" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7932.51" y1="181.54" x2="7932.51" y2="5.37" fill="none" stroke="#a57e2d" stroke-dasharray="3.98 9.95" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7932.51" y1=".4" x2="7932.51" y2="-1.6" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="7932.51" y1="1464.97" x2="7932.51" y2="1462.97" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7932.51" y1="1452.98" x2="7932.51" y2="381.84" fill="none" stroke="#a57e2d" stroke-dasharray="3.99 9.98" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="7932.51" y1="376.85" x2="7932.51" y2="374.85" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <circle cx="7932.51" cy="3133.51" r="6.2" fill="#a57e2d"/>
          <g>
            <line x1="8855.76" y1="419.06" x2="8855.76" y2="417.06" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="8855.76" y1="407.05" x2="8855.76" y2="5.4" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.02" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="8855.76" y1=".4" x2="8855.76" y2="-1.6" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="8855.76" y1="2126.69" x2="8855.76" y2="2124.69" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="8855.76" y1="2114.69" x2="8855.76" y2="732.4" fill="none" stroke="#a57e2d" stroke-dasharray="4 10.01" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="8855.76" y1="727.4" x2="8855.76" y2="725.4" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="8855.76" y1="3137.82" x2="8855.76" y2="3135.82" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="8855.76" y1="3125.84" x2="8855.76" y2="2362.39" fill="none" stroke="#a57e2d" stroke-dasharray="3.99 9.98" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="8855.76" y1="2357.4" x2="8855.76" y2="2355.4" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <circle cx="8855.76" cy="3137.02" r="6.2" fill="#a57e2d"/>
          <g>
            <line x1="8010.56" y1="1101.65" x2="8048.47" y2="1101.65" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="8041.84 1109.83 8040.48 1108.36 8047.7 1101.65 8040.48 1094.94 8041.84 1093.47 8050.64 1101.65 8041.84 1109.83" fill="#21409a"/>
          </g>
          <g mix-blend-mode="multiply">
            <text transform="translate(8456.8628 2140.746)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">A global pandemic forces universities </tspan><tspan x="0" y="34">to turn to online teaching. According </tspan><tspan x="0" y="68">to the Canadian Digital Learning </tspan><tspan x="0" y="102">Research Association, the average </tspan><tspan x="0" y="136">Canadian university has ‘17 times </tspan><tspan x="0" y="170">more online course enrolments in the </tspan><tspan x="0" y="204">2020 fall semester compared to the </tspan><tspan x="0" y="238">same time in 2019’.</tspan></text>
          </g>
          <g>
            <line x1="8389.16" y1="2136.08" x2="8427.07" y2="2136.08" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="8420.44 2144.26 8419.08 2142.8 8426.3 2136.09 8419.08 2129.37 8420.44 2127.91 8429.24 2136.09 8420.44 2144.26" fill="#21409a"/>
          </g>
          <text transform="translate(7071.8765 1631.4135)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">In the 1990&apos;s computer labs become </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="24">increasinly prevalent for general </tspan></tspan><tspan x="0" y="48" fill="#223f9a">student use in universities. </tspan><tspan x="352.16" y="48" fill="#21409a" letter-spacing="-.27em">	</tspan><tspan x="359.99" y="48" fill="#21409a" letter-spacing="1.49em">	</tspan></text>
          <text transform="translate(7967.8174 700.8407)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" xml:space="preserve">Peter Thiel starts a  </tspan><tspan x="0" y="24">fellowship in 2010 to </tspan><tspan x="0" y="48">encourage students to </tspan><tspan x="0" y="72">drop out of university and </tspan><tspan x="0" y="96">start companies instead.</tspan></text>
          <circle cx="7059" cy="1625.44" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <circle cx="7953.74" cy="695.31" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(7467.5312 1140.6366)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Tarana Burke founds the </tspan><tspan x="291.45" y="0" letter-spacing="0em" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".25">Me</tspan><tspan x="315.64" y="0" letter-spacing="-.4em" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".25"> </tspan><tspan x="321.33" y="0" letter-spacing="0em" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".25">Too</tspan><tspan x="357.57" y="0" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".25"> </tspan><tspan x="0" y="24">movement in 2006 to support </tspan><tspan x="0" y="48">women and girls who survive </tspan><tspan x="0" y="72">sexual violence.</tspan></text>
          <circle cx="7455.46" cy="1135.11" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <circle cx="8502.23" cy="2688.14" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(7557.6875 2354.7972)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">2008 Finacial Crash</tspan><tspan x="230.73" y="0">.</tspan></text>
          <circle cx="7539.64" cy="2349.3" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(7051.3765 408.871)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">In 1996, </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="24">Ontario </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="48">deregulates </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="72">international </tspan></tspan><tspan x="0" y="96" fill="#223f9a">tuition fees.</tspan><tspan x="157.87" y="96" fill="#21409a" letter-spacing=".62em">	</tspan><tspan x="180" y="96" fill="#21409a" letter-spacing="1.49em">	</tspan></text>
          <circle cx="7039.5" cy="403.89" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(8354.017 2098.3031)" fill="#21409a" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;">COVID </tspan><tspan x="160.12" y="0" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-weight="300">19</tspan></text>
          <circle cx="8317.95" cy="1540.44" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(7106.2065 2092.3822)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">The Supreme Court </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="24">of Canada rules in </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="48">Delgamuukw v </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="72">British Columbia </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="96">that Indigenous </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="120">people have </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="144">ancestral land </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="168">rights but stops </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="192">short of declaring </tspan></tspan><tspan x="0" y="216" fill="#223f9a">Aboriginal title.</tspan><tspan x="206.44" y="216" fill="#21409a" letter-spacing="-.16em">	</tspan><tspan x="216" y="216" fill="#21409a" letter-spacing="1.49em">	</tspan></text>
          <circle cx="7092.36" cy="2085.88" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(7824.0117 205.953)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Between 1999 and 2010, student </tspan><tspan x="0" y="24">enrolment at Canadian </tspan><tspan x="0" y="48">universities increases by 50%, </tspan><tspan x="0" y="72">partly due to natural growth </tspan><tspan x="0" y="96">and partly due to the </tspan><tspan x="0" y="120">conversion of seven colleges </tspan><tspan x="0" y="144">in British Columbia and </tspan><tspan x="0" y="168">Alberta to university status.</tspan></text>
          <circle cx="7811.94" cy="200.42" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(7799.623 1469.4638)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">In the late 2000&apos;s </tspan><tspan x="0" y="24">mandatory retirement </tspan><tspan x="0" y="48">disappears across </tspan><tspan x="0" y="72">Canada.</tspan></text>
          <circle cx="7786.98" cy="1462.96" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(8507.7485 326.2733)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">INTERNATIONAL </tspan><tspan x="0" y="58">STUDENT VISA CAP</tspan></text>
          <text transform="translate(8611.0913 437.8295)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">The Canadian federal </tspan><tspan x="0" y="34">government announces a </tspan><tspan x="0" y="68">two-year cap on </tspan><tspan x="0" y="102">international student </tspan><tspan x="0" y="136">permits for 2024, planning a </tspan><tspan x="0" y="170">35% reduction from 2023 </tspan><tspan x="0" y="204">figures. The actual reported </tspan><tspan x="0" y="238">figures in 2024 show a 48% </tspan><tspan x="0" y="272">drop, deepening the funding </tspan><tspan x="0" y="306">crisis for universities.</tspan></text>
          <g>
            <line x1="8554.38" y1="432.44" x2="8592.29" y2="432.44" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="8585.66 440.62 8584.3 439.16 8591.52 432.44 8584.3 425.73 8585.66 424.26 8594.46 432.44 8585.66 440.62" fill="#21409a"/>
          </g>
          <g mix-blend-mode="multiply">
            <text transform="translate(7584.0923 1870.4091)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">by 2008, most </tspan><tspan x="0" y="34">Canadian </tspan><tspan x="0" y="68">universities </tspan><tspan x="0" y="102">reduce the number </tspan><tspan x="0" y="136">of provincial </tspan><tspan x="0" y="170">exams recquired </tspan><tspan x="0" y="204">for entry from </tspan><tspan x="0" y="238">four to just one: </tspan><tspan x="0" y="272">English 12.</tspan></text>
          </g>
          <g>
            <line x1="7516.39" y1="1865.75" x2="7554.3" y2="1865.75" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="7547.67 1873.93 7546.31 1872.46 7553.53 1865.75 7546.31 1859.04 7547.67 1857.57 7556.47 1865.75 7547.67 1873.93" fill="#21409a"/>
          </g>
          <text transform="translate(7481.2451 1769.4843)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">RACE TO THE </tspan><tspan x="0" y="58">BOTTOM</tspan></text>
          <text transform="translate(8331.917 1545.7699)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan x="0" y="0">In July 2020, the </tspan><tspan x="0" y="24">amount of student loans </tspan><tspan x="0" y="48">owed to the Government </tspan><tspan x="0" y="72">of Canada surpasses </tspan><tspan x="0" y="96">$22.3 billion —more </tspan><tspan x="0" y="120">that the debt of some </tspan><tspan x="0" y="144">provinces.</tspan></text>
          <text transform="translate(8070.7612 1107.7533)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300"><tspan font-size="24"><tspan x="0" y="0">The New York Times declares 2012 the </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">year of the MOOC. A Udacity </tspan></tspan><tspan font-size="24"><tspan x="0" y="68">representative predicts that they </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">will disrupt how faculty are </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">recruited, trained, and paid, with </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">the most popular “compensated like a </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">TV actor or a movie actor.”</tspan></tspan></text>
          <text transform="translate(7975.8436 1056.7069)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">THE YEAR OF THE MOOC</tspan></text>
          <text transform="translate(7050.0703 3282.4838)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">2000</tspan></text>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="2104.84" x2="7249.12" y2="2101.32" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="2126.4" x2="7249.12" y2="2122.87" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="2149.22" x2="7249.12" y2="2145.7" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="2174.67" x2="7249.12" y2="2171.14" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="2192.71" x2="7249.12" y2="2189.18" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="2206.04" x2="7249.12" y2="2202.52" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="2221.48" x2="7249.12" y2="2217.96" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="2245.28" x2="7249.12" y2="2241.76" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="2271.92" x2="7249.12" y2="2268.4" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="2295.41" x2="7249.12" y2="2291.89" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="1639.99" x2="7249.12" y2="1636.47" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="1664.21" x2="7249.12" y2="1660.69" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7249.12" y1="1675.85" x2="7249.12" y2="1672.33" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g opacity=".8">
            <path d="M6868.25,1004.27c25.77-.51,489.11-6.85,592.05-8.86,6.92.03,15.67-1.42,23.28-2.38,8.4-1.02,16.23-3.63,24.2-7.02,8.16-3.27,16.1-6.8,23.39-11.69,6.22-4.13,12.57-8.01,17.86-13,4.31-4.08,8.18-9.24,12.11-14.41,5.96-8.1,11.99-16.18,16.25-25.3,3.31-7.28,4.71-15.2,6.46-23.21,1.6-7.31,2.17-15.54,2.11-22.68-.01-3.99-.1-7.47-.45-9.13-.14-1.14-.78-1.97-2.01-1.88-28.8.06-357.87-.14-389.24.06,0,0-.3,8.98-.5,11.52-.2,9.14-1.54,21.11-3.33,28.91-2.92,12.67-11.22,20.42-22.69,28.64-2.6,1.87-9.17,5.61-12.76,6.91-15.54,5.61-20.76,5.95-27.75,7.07-17.82,2.86-161.25,11.38-230.28,11.53" fill="#f7ec12"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="441.89" x2="8855.76" y2="438.37" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="458.54" x2="8855.76" y2="455.02" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="475.85" x2="8855.76" y2="472.33" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="492.91" x2="8855.76" y2="489.38" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="511.98" x2="8855.76" y2="508.46" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="526.82" x2="8855.76" y2="523.3" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="579.56" x2="8855.76" y2="576.04" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="591.93" x2="8855.76" y2="588.41" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="612.17" x2="8855.76" y2="608.65" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="626.57" x2="8855.76" y2="623.05" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="654.53" x2="8855.76" y2="651" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="680.87" x2="8855.76" y2="677.34" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="692.5" x2="8855.76" y2="688.97" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="718.51" x2="8855.76" y2="714.99" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2142.88" x2="8855.76" y2="2139.36" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2158.4" x2="8855.76" y2="2154.88" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2174" x2="8855.76" y2="2170.48" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2184.46" x2="8855.76" y2="2180.93" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2195.66" x2="8855.76" y2="2192.13" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2211.76" x2="8855.76" y2="2208.23" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2225.74" x2="8855.76" y2="2222.22" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2241.3" x2="8855.76" y2="2237.77" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2259.51" x2="8855.76" y2="2255.99" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2280.34" x2="8855.76" y2="2276.81" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2312.33" x2="8855.76" y2="2308.81" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="8855.76" y1="2330.1" x2="8855.76" y2="2326.58" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="214.7" x2="7932.51" y2="211.17" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="237.97" x2="7932.51" y2="234.45" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="261.57" x2="7932.51" y2="258.04" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="286.31" x2="7932.51" y2="282.79" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="313.34" x2="7932.51" y2="309.82" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="338.03" x2="7932.51" y2="334.51" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="359.61" x2="7932.51" y2="356.08" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="1479.41" x2="7932.51" y2="1475.88" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="7932.51" y1="1502.48" x2="7932.51" y2="1498.95" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <rect x="8854.16" y="2288.52" width="3.2" height="4.1" fill="#a57e2d"/>
          <rect x="8854.26" y="546.4" width="3.01" height="4.1" fill="#a57e2d"/>
          <g>
            <g opacity=".8">
              <rect x="10827.1" y="58.94" width="493" height="177.37" transform="translate(-.92 186.11) rotate(-.96)" fill="#f7ec12"/>
            </g>
            <g opacity=".8">
              <rect x="11157.79" y="54.35" width="165.64" height="489.51" transform="translate(-3.44 188.94) rotate(-.96)" fill="#f7ec12"/>
            </g>
            <g opacity=".8">
              <rect x="10789.83" y="250.98" width="489.51" height="165.64" transform="translate(3124.2162 8034.4212) rotate(-45.9629)" fill="#f7ec12"/>
            </g>
          </g>
          <g mix-blend-mode="multiply" opacity=".8">
            <path d="M9206.8,1303.93c79.81,96.02,53.51,58.38,134.74,154.24l90.96-91.48,173.65,162.17v-519.78s-285.28,0-285.28,0l-123.54-116.96" fill="#f7ec12"/>
          </g>
          <g>
            <text transform="translate(9782.1938 3042.8339)" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="97" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">futuring the public </tspan></tspan><tspan fill="#223f9a"><tspan x="26.97" y="100">university through </tspan></tspan><tspan x="350.56" y="200" fill="#223f9a">crisis</tspan><tspan x="674.15" y="200" fill="#21409a"> </tspan></text>
            <circle cx="10476.04" cy="3235.17" r="8.63" fill="#223f9a"/>
          </g>
          <text transform="translate(9482.1228 1587.0434)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">MASSIFICATION</tspan></text>
          <text transform="translate(10013.4902 2214.0873)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">TECHNOLOGY</tspan></text>
          <text transform="translate(10572.6572 1792.4628)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">KNOWLEDGE</tspan></text>
          <text transform="translate(10793.4199 2523.7572)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">RESTITUTION</tspan></text>
          <text transform="translate(10246.1367 1074.8573)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">MARKETIZATION</tspan></text>
          <text transform="translate(9383.502 235.1557)" fill="#223f99" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="90" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" xml:space="preserve">&nbsp;&nbsp;&nbsp;&nbsp;so many of the crises </tspan><tspan x="0" y="104">throughout the university’s </tspan><tspan x="0" y="208">history stem from the </tspan><tspan x="0" y="312">questions, “Who are we?” </tspan><tspan x="0" y="416">and “What are we for?”</tspan></text>
          <text transform="translate(9539.9736 2614.3226)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">GEOPOLITICS</tspan></text>
          <g mix-blend-mode="multiply">
            <g>
              <line x1="9430.24" y1="217.01" x2="9514.93" y2="217.01" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="6"/>
              <polygon points="9495.05 241.55 9490.96 237.16 9512.63 217.02 9490.96 196.87 9495.05 192.48 9521.44 217.02 9495.05 241.55" fill="#21409a"/>
            </g>
          </g>
          <circle cx="10224.18" cy="1056.01" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
          <circle cx="9456.25" cy="1566.72" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
          <circle cx="9515.13" cy="2597.35" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
          <circle cx="9990.65" cy="2196.58" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
          <circle cx="10771.47" cy="2505.01" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
          <circle cx="10551.92" cy="1773.05" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
          <g>
            <path d="M11160.51,3287.36v16.91h-2.35v-16.91h2.35Z" fill="#223f9a"/>
            <path d="M11163.97,3295.66c0-2.27-.02-3.32-.05-3.88h2.22c.05.36.08,1.28.08,1.71.59-1.06,1.68-1.96,3.49-1.96,1.66,0,2.71.76,3.18,2.11.55-1.1,1.82-2.11,3.71-2.11s3.79,1,3.79,4.28v8.45h-2.24v-8.07c0-1.44-.47-2.71-2.18-2.71-1.86,0-2.64,1.52-2.64,3.49v7.29h-2.23v-8.18c0-1.46-.61-2.59-2.16-2.59-1.69,0-2.7,1.25-2.7,3.68v7.09h-2.26v-8.6Z" fill="#223f9a"/>
            <path d="M11192.66,3301.4c0,.86.08,2.16.19,2.86h-2.05c-.08-.42-.17-1.11-.18-1.85-.49,1.21-1.73,2.07-3.72,2.07-3.06,0-4.02-2.03-4.02-3.79,0-1.95,1.28-3.99,5.72-3.99h1.83v-1.15c0-1.15-.33-2.29-2.32-2.29-1.75,0-2.32.82-2.51,2.1h-2.22c.18-2.07,1.38-3.83,4.8-3.83,2.68,0,4.51,1.04,4.51,3.93v5.93ZM11190.48,3298.3h-1.89c-2.87,0-3.41,1.17-3.41,2.25,0,1.15.69,2.1,2.2,2.1,2.36,0,3.1-1.58,3.1-4.09v-.26Z" fill="#223f9a"/>
            <path d="M11206.01,3303.26c0,3.88-1.57,6.12-5.46,6.12s-4.84-2-5.02-3.79h2.26c.26,1.31,1.32,1.96,2.86,1.96,2.56,0,3.14-1.65,3.14-4.29v-.98c-.64,1.35-1.75,1.97-3.6,1.97-2.94,0-4.86-2.43-4.86-6.3s2.28-6.42,5.13-6.42c1.97,0,2.95.79,3.27,1.7,0-.49.07-1.18.11-1.45h2.22c-.02.6-.05,1.94-.05,3.65v7.83ZM11197.69,3297.92c0,2.76,1.17,4.38,3.07,4.38,2.29,0,3.09-1.41,3.09-4.43s-.62-4.38-2.99-4.38c-1.95,0-3.17,1.6-3.17,4.43Z" fill="#223f9a"/>
            <path d="M11209.46,3286.41h2.28v2.72h-2.28v-2.72ZM11209.46,3291.78h2.28v12.48h-2.28v-12.48Z" fill="#223f9a"/>
            <path d="M11215.22,3295.69c0-2.6-.02-3.37-.05-3.91h2.23c.04.23.1,1.36.08,1.89.51-1.09,1.65-2.14,3.64-2.14,2.37,0,3.97,1.38,3.97,4.65v8.08h-2.29v-7.7c0-1.74-.56-3.06-2.36-3.06-2.08,0-2.94,1.5-2.94,4.04v6.73h-2.28v-8.58Z" fill="#223f9a"/>
            <path d="M11237.36,3301.4c0,.86.08,2.16.19,2.86h-2.05c-.08-.42-.17-1.11-.18-1.85-.49,1.21-1.73,2.07-3.72,2.07-3.06,0-4.02-2.03-4.02-3.79,0-1.95,1.28-3.99,5.72-3.99h1.83v-1.15c0-1.15-.33-2.29-2.32-2.29-1.75,0-2.32.82-2.51,2.1h-2.22c.18-2.07,1.38-3.83,4.8-3.83,2.68,0,4.5,1.04,4.5,3.93v5.93ZM11235.19,3298.3h-1.89c-2.87,0-3.41,1.17-3.41,2.25,0,1.15.69,2.1,2.2,2.1,2.36,0,3.1-1.58,3.1-4.09v-.26Z" fill="#223f9a"/>
            <path d="M11239.02,3291.78h1.95v-3.58h2.27v3.58h2.46v1.85h-2.46v7.54c0,1.01.25,1.43,1.31,1.43.33,0,.64-.03.93-.08v1.67c-.51.18-1.27.22-1.71.22-1.93,0-2.79-.75-2.79-2.87v-7.92h-1.95v-1.85Z" fill="#223f9a"/>
            <path d="M11247.84,3286.41h2.28v2.72h-2.28v-2.72ZM11247.84,3291.78h2.28v12.48h-2.28v-12.48Z" fill="#223f9a"/>
            <path d="M11254.51,3291.78c1.6,5.09,2.67,8.5,3.04,10.3h.02c.28-1.55,2.22-7.25,3.16-10.3h2.26l-4.29,12.48h-2.48l-4.14-12.48h2.43Z" fill="#223f9a"/>
            <path d="M11266.38,3298.48c-.01,2.31.96,4.15,3.09,4.15,1.91,0,2.49-1.32,2.72-1.95h2.24c-.45,1.66-1.71,3.82-5.06,3.82-3.92,0-5.31-3.01-5.31-6.51,0-3.07,1.51-6.46,5.43-6.46s5.13,3.04,5.13,5.99c0,.09-.01.86-.02.96h-8.22ZM11272.38,3296.86c-.06-1.98-.86-3.51-2.93-3.51-2.35,0-2.92,2.1-3.02,3.51h5.95Z" fill="#223f9a"/>
            <path d="M11171,3324.61c0-3,.03-5.95.09-7.58h-.04c-.76,2.68-3.48,10.05-5.2,14.61h-1.47c-1.3-3.8-4.1-11.69-4.91-14.64h-.06c.12,1.82.17,5.39.17,8.1v6.54h-1.45v-15.8h2.27c1.83,5.03,4.21,11.83,4.79,13.92h.04c.3-1.32,3.11-8.86,5.02-13.92h2.23v15.8h-1.49v-7.03Z" fill="#223f9a"/>
            <path d="M11176.44,3326.14c-.02,2.63,1.13,4.46,3.27,4.46,2.03,0,2.65-1.47,2.89-2.1h1.43c-.31,1.25-1.34,3.36-4.41,3.36-3.56,0-4.67-2.95-4.67-6.02,0-2.81,1.37-5.91,4.77-5.91s4.5,2.83,4.5,5.36c0,.03,0,.81,0,.85h-7.78ZM11182.78,3324.99c-.06-2.2-.95-3.81-3.1-3.81-2.49,0-3.07,2.31-3.19,3.81h6.29Z" fill="#223f9a"/>
            <path d="M11185.2,3320.16h1.93v-3.42h1.44v3.42h2.42v1.24h-2.42v7.67c0,1.02.26,1.46,1.26,1.46.33,0,.74-.04.97-.08v1.15c-.39.15-.98.19-1.37.19-1.46,0-2.29-.54-2.29-2.36v-8.03h-1.93v-1.24Z" fill="#223f9a"/>
            <path d="M11194.2,3315.02v6.9c.57-1.17,1.75-1.98,3.51-1.98,1.52,0,3.61.77,3.61,4.1v7.61h-1.43v-7.33c0-1.95-.8-3.05-2.58-3.05-1.99,0-3.1,1.32-3.1,3.78v6.61h-1.44v-16.62h1.44Z" fill="#223f9a"/>
            <path d="M11213.57,3325.7c0,3.31-1.4,6.13-4.99,6.13-3.4,0-4.82-2.9-4.82-6.08s1.67-5.82,4.96-5.82c3.08,0,4.85,2.39,4.85,5.77ZM11205.27,3325.76c0,2.72,1.17,4.81,3.43,4.81,2.39,0,3.35-2.04,3.35-4.86,0-2.57-1.14-4.51-3.4-4.51s-3.37,1.91-3.37,4.56Z" fill="#223f9a"/>
            <path d="M11224.56,3315.02v13.71c0,1.02,0,2.19.05,2.91h-1.43c-.03-.3-.06-1.04-.06-1.82-.62,1.46-1.59,2.03-3.5,2.03-2.99,0-4.45-2.56-4.45-5.93s1.67-5.99,4.79-5.99c1.91,0,2.83.8,3.16,1.5v-6.42h1.44ZM11216.69,3325.85c0,3.03,1.39,4.7,3.26,4.7,2.66,0,3.22-2.08,3.22-4.94,0-3.46-1.08-4.38-3.09-4.38s-3.39,1.7-3.39,4.61Z" fill="#223f9a"/>
            <path d="M11228.15,3328.4c.25,1.45,1.33,2.25,2.81,2.25,1.79,0,2.43-1.01,2.43-2.08,0-1.15-.76-1.78-2.78-2.32-2.7-.72-3.45-1.72-3.45-3.22s1.08-3.09,3.65-3.09,3.67,1.52,3.82,3.23h-1.43c-.22-1.05-.76-2.04-2.46-2.04-1.48,0-2.13.74-2.13,1.79,0,.95.42,1.48,2.47,2.02,2.84.77,3.77,1.71,3.77,3.53,0,2.05-1.58,3.38-3.95,3.38-2.21,0-3.99-1.07-4.21-3.44h1.45Z" fill="#223f9a"/>
            <path d="M11242.93,3315.84h1.49v14.48h7.8l-.25,1.32h-9.05v-15.8Z" fill="#223f9a"/>
            <path d="M11261.91,3329.25c0,.8.08,1.86.18,2.39h-1.35c-.07-.42-.16-1.01-.16-1.92-.43,1.24-1.62,2.13-3.57,2.13-2.79,0-3.59-1.94-3.59-3.47s1-3.6,5.16-3.6h1.91v-1.22c0-1.15-.32-2.42-2.49-2.42-1.8,0-2.47.8-2.7,2.23h-1.42c.19-1.96,1.31-3.43,4.19-3.43,2.28,0,3.86.98,3.86,3.51v5.82ZM11260.52,3325.92h-1.98c-3.05,0-3.63,1.24-3.63,2.39,0,1.25.76,2.27,2.32,2.27,2.43,0,3.29-1.64,3.29-4.43v-.23Z" fill="#223f9a"/>
            <path d="M11265.15,3315.02h1.44v6.87c.5-.99,1.62-1.95,3.54-1.95,2.72,0,4.39,2.19,4.39,5.62s-1.41,6.29-4.72,6.29c-1.8,0-2.78-.78-3.23-1.79.02.5-.03,1.07-.07,1.59h-1.41c.02-.59.05-1.65.05-3.16v-13.47ZM11273.02,3325.61c0-2.63-1.06-4.36-3.17-4.36-2.45,0-3.35,1.57-3.35,4.48s.65,4.8,3.28,4.8c2.23,0,3.24-2.08,3.24-4.92Z" fill="#223f9a"/>
          </g>
          <path d="M11266.3,3206.2c-6.56,15.66-15.02,36.58-20.27,50l-12.31-7.47c-4.82-12.71-11.09-28.84-16.55-42.54h-8.35v27.43l-45.21-27.43h-5.57v69.55h5.57v-67.34l45.21,27.44v39.89h5.13v-29.51c0-2.29.01-4.74.03-7.26l13.12,7.96c4.11,10.9,8.25,21.68,11.02,28.8h5.43c1.85-4.62,3.93-9.78,6.09-15.13l19.36,11.75v3.38h5.56v-69.55h-8.24ZM11213.98,3236.77c.08-9.97.2-20.58-.18-26.56h.05c1.73,5.78,6.81,19.65,12.14,33.84l-12.01-7.29ZM11241.28,3268.85h-.2c-.97-2.98-3.27-9.27-6.27-17.21l10.51,6.38c-2.1,5.4-3.58,9.34-4.04,10.83ZM11250.34,3258.83c7.9-19.61,16.59-41.28,18.73-48.51h.3c-.3,6.97-.4,20-.4,33.57v26.25l-18.63-11.3Z" fill="#223f9a"/>
          <g opacity=".8">
            <polygon points="8547.87 2775.94 8262.26 2342.3 8260.52 2484.04 8178.94 2493.43 8178.94 2493.46 6890.34 2486.67 6886.44 3096.93 8179.07 3099.07 8179.07 3099 8264 3082.42 8264 3272.01 8547.87 2775.94" fill="#f7ec12"/>
          </g>
          <text transform="translate(7546.0488 2564.4427)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">DECLINING GOVERNMENT </tspan><tspan x="0" y="58">FUNDING</tspan></text>
          <g>
            <line x1="7580.77" y1="2652.11" x2="7618.67" y2="2652.11" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="7612.05 2660.29 7610.68 2658.83 7617.91 2652.12 7610.68 2645.4 7612.05 2643.94 7620.84 2652.12 7612.05 2660.29" fill="#21409a"/>
          </g>
          <text transform="translate(7640.9673 2657.2191)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300"><tspan font-size="24"><tspan x="0" y="0">Provincial governments across </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">Canada encourage universities </tspan></tspan><tspan font-size="24"><tspan x="0" y="68">to increase international </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">enrolment as domestic numbers </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">decline. Within seven years, </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">international students rise to </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">13% of total enrolment. Paying </tspan></tspan><tspan font-size="24"><tspan x="0" y="238">nearly four times the tuition </tspan></tspan><tspan font-size="24"><tspan x="0" y="272">of domestic students, they </tspan></tspan><tspan font-size="24"><tspan x="0" y="306">generate over one-third of all </tspan></tspan><tspan font-size="24"><tspan x="0" y="340">tuition revenue, approaching </tspan></tspan><tspan font-size="24"><tspan x="0" y="374">half in British Columbia.</tspan></tspan><tspan font-size="21" letter-spacing=".96em"></tspan></text>
          <text transform="translate(8298.5352 2889.0922)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">In 2019 the Accessible Canada </tspan><tspan x="0" y="24">Act passes, introducing </tspan><tspan x="0" y="48">requirements for government </tspan><tspan x="0" y="72">Institutions.</tspan></text>
          <circle cx="8285.08" cy="2882.59" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(8520.1367 2694.64)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Between 2001 and 2023, </tspan><tspan x="0" y="24">the Canadian average for </tspan><tspan x="0" y="48">university tuition more </tspan><tspan x="0" y="72">than doubles.</tspan></text>
          <text transform="translate(5935.8566 3284.0466)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300"><tspan x="0" y="0">1</tspan><tspan x="32.52" y="0" letter-spacing="-.03em">9</tspan><tspan x="108.84" y="0" letter-spacing="0em">88</tspan></text>
          <g>
            <line x1="5301.64" y1="140.83" x2="5301.64" y2="138.83" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="5301.64" y1="128.9" x2="5301.64" y2="8.75" fill="none" stroke="#a57e2d" stroke-dasharray="3.97 9.93" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="5301.64" y1="3.79" x2="5301.64" y2="1.79" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="5301.64" y1="1989.47" x2="5301.64" y2="1987.47" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="5301.64" y1="1977.47" x2="5301.64" y2="371.3" fill="none" stroke="#a57e2d" stroke-dasharray="4 10.01" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="5301.64" y1="366.3" x2="5301.64" y2="364.3" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="5301.64" y1="3139.94" x2="5301.64" y2="3137.94" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="5301.64" y1="3127.91" x2="5301.64" y2="2108.21" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.03" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="5301.64" y1="2103.2" x2="5301.64" y2="2101.2" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <circle cx="5301.64" cy="3139.14" r="6.2" fill="#a57e2d"/>
          <circle cx="6074.39" cy="3139.94" r="6.2" fill="#a57e2d"/>
          <g opacity=".8">
            <path d="M5196.6,1776.4c-88.69-68.05-165.37-59.57-206.44-51.63-66.63,12.89-115.87,57.13-144.44,119.68-33.54,72.91-27.88,156.18-27.28,234.62l-1.83,1.93c.6-.02,1.22-.03,1.85-.05,0,.58,0,1.16.01,1.74l1.71-1.8c80.03-2.68,307.54-30.96,408.67-29.99,5.54.05,13.08,1.18,14.25-1.11.8-1.57-.12-13.35,0-20.7.91-55.19,4.92-114.59,6.62-165.61.91-18.47,7.93-2.34,11.65,4.6,15.61,32.57,32.47,70.27,48.15,104.26,12.71,28.57,25.96,56.43,42.4,83.25,21.7,35.83,47.94,69.64,81.72,94.6,31.29,24.37,69.18,40.11,108.12,46.86,21.36,3.77,43,4.96,64.34,1.69,19.65-2.61,38.21-7,56.4-15.48,15.15-6.95,30.08-14.82,43.86-24.15,22.88-15.78,43.95-35.49,61.18-57.35,19.28-24.05,31.96-52.8,41-82.13,8.9-26.94,15.47-54.16,19.03-82.46,3.59-20.51,3.9-59.25,20.37-67.49,6.06-3.34,14.29-3.91,21.81-4.22,51.48-.59,123.81,0,170.43-.26,6.03-.08,11.67-.04,16.67-.5,2.25-.23,3.35-.57,3.37-1.07-76.54-29.49-309.13-104.81-393.64-134.54-7.21-2.37-14.07-4.67-20.75-4.28h-.07c-7.12.63-14.89,4.13-22.75,7.42-73.74,32.21-233.25,99.47-303.21,131.14-9.26,5.16,11.17,3.92,21.54,4.11,34.03-.32,80.38-1,116.46-1.39,20.6.58,47.93-4.11,59.62,9.58,10.05,14.28-1.5,36.27-13.05,48.96-6.73,7.45-15.18,12.78-24.81,15.66-27.79,8.88-57.27-.9-82.97-12.47-27.58-13.22-54.85-27.5-78.82-46.73" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <polygon points="5147.5 751.35 4432.45 751.35 4505.72 484.52 5147.5 484.52 5147.5 751.35" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <path d="M6896.94,1004.16c-32.54.15-96.54.29-119.2.5-16.35.82-35.61,9.12-41.97,25.42-3.16,8.53-3.71,19.61-4.25,29.36-.6,11.39-1.49,24.52-1.83,35.54-.03,4.32-.11,7.57,4.97,7.5,30.02,1.7,94.17,5.24,113.52,6.32,4.45.26,5.96.3,6.13.76-10.56,24.99-223.53,498.58-232.71,519.59-.19.42-.31.64-.42.67-.21.06-.49-.79-1.27-2.5-4.13-9.35-19.51-44.18-40.49-91.69-64.22-146.52-181.9-409.87-187.74-426.25.55-.33,2.69-.43,7.49-.78,21-1.5,82.37-5.75,111.54-7.88,1.15-.15,2.51-.24,3.23-1.19.87-1.13.78-3.69.69-8.45-.4-17.71-.96-41.57-1.34-59.6-.39-6.39,1.54-11.3,4.16-17.02,4.65-10.63,10.61-19.99,18.76-28.41,7.14-7.36,14.32-12.94,24.1-17.34,6.78-2.98,15.26-6.51,21.89-8.9,77.72-1.34,286.51-.03,314.73-.47" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <polygon points="5243.11 2990.6 4814.73 2990.6 4818.14 1983.26 5243.11 2049.49 5243.11 2990.6" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <path d="M6886.44,3096.93c-263.68,0-430.06-4.69-430.06-311.3s170.28-298.97,433.96-298.97" fill="#f7ec12"/>
          </g>
          <g mix-blend-mode="multiply" opacity=".8">
            <polyline points="6753.46 2487.94 6890.34 2486.67 6886.44 3096.93 6850.13 3096.85" fill="#f7ec12"/>
          </g>
          <text transform="translate(5538.5128 1414.6985)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">The perception that rapid </tspan><tspan x="0" y="34">technological change is eroding the </tspan><tspan x="0" y="68">power of institutions like Church and </tspan><tspan x="0" y="102">State leads the Higher Education </tspan><tspan x="0" y="136">Council of Quebec to commision </tspan><tspan x="0" y="170">philosopher J-F Lyotard to write a </tspan><tspan x="0" y="204">report on the state of knowledge and </tspan><tspan x="0" y="238">the new postmodern condition.</tspan></text>
          <text transform="translate(5442.9916 1296.9939)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">THE POSTMODERN</tspan><tspan x="0" y="58">CONDITION</tspan></text>
          <g>
            <line x1="5479.22" y1="1404.71" x2="5517.13" y2="1404.71" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="5510.5 1412.89 5509.14 1411.43 5516.36 1404.72 5509.14 1398 5510.5 1396.54 5519.3 1404.72 5510.5 1412.89" fill="#21409a"/>
          </g>
          <text/>
          <text transform="translate(5988.4086 221.5508)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">THE INDIGENOUS </tspan><tspan x="0" y="58">STUDENT WALKOUT</tspan></text>
          <text transform="translate(5417.225 2417.9763)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">Following the university&apos;s </tspan><tspan x="0" y="34">denial of a grievance about a </tspan><tspan x="0" y="68">racist professor filed by black </tspan><tspan x="0" y="102">students, 200 students begin a </tspan><tspan x="0" y="136">peaceful sit-in. Now considered </tspan><tspan x="0" y="170">one of the largest student </tspan><tspan x="0" y="204">protests in Canadian history, it </tspan><tspan x="0" y="238">coincides with a global student </tspan><tspan x="0" y="272">movement for university reforms </tspan><tspan x="0" y="306">in the late 1960s.</tspan></text>
          <text transform="translate(5319.0072 2295.7356)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">SIR GEORGE </tspan><tspan x="0" y="58">WILLIAMS AFFAIR</tspan></text>
          <g>
            <line x1="5352.56" y1="2412.41" x2="5390.47" y2="2412.41" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="5383.84 2420.59 5382.47 2419.12 5389.7 2412.41 5382.47 2405.69 5383.84 2404.23 5392.63 2412.41 5383.84 2420.59" fill="#21409a"/>
          </g>
          <g>
            <line x1="4771.54" y1="813.15" x2="4809.45" y2="813.15" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="4802.82 821.33 4801.46 819.86 4808.68 813.15 4801.46 806.44 4802.82 804.97 4811.62 813.15 4802.82 821.33" fill="#21409a"/>
          </g>
          <text transform="translate(5160.5439 3284.0466)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">1</tspan><tspan x="32.52" y="0" letter-spacing="0em">9</tspan><tspan x="111.24" y="0">68</tspan></text>
          <text transform="translate(6098.6266 343.791)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">A coalition of Indigenous students </tspan><tspan x="0" y="34">organizes walk-outs and sit-ins at </tspan><tspan x="0" y="68">York University and the University of </tspan><tspan x="0" y="102">Toronto. Their demands include </tspan><tspan x="0" y="136">creating a dedicated Aboriginal </tspan><tspan x="0" y="170">Studies department and the formal </tspan><tspan x="0" y="204">recognition of Indigenous land rights </tspan><tspan x="0" y="238">on campus.</tspan></text>
          <text transform="translate(4740.849 711.0635)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">SECURING ACADEMIC </tspan><tspan x="0" y="58">FREEDOM</tspan></text>
          <text transform="translate(4839.4027 816.8594)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">After its founding in </tspan><tspan x="0" y="34">1951, the Canadian </tspan><tspan x="0" y="68">Association of </tspan><tspan x="0" y="102">University Teachers </tspan><tspan x="0" y="136">begins advocating for </tspan><tspan x="0" y="170">the right of Canadian </tspan><tspan x="0" y="204">professors to publicly </tspan><tspan x="0" y="238">challenge their </tspan><tspan x="0" y="272">institutions’ policies </tspan><tspan x="0" y="306">without reprimand or </tspan><tspan x="0" y="340">termination. </tspan></text>
          <text transform="translate(4996.7988 1339.804)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan x="0" y="0">The National </tspan><tspan x="0" y="24">Association of </tspan><tspan x="0" y="48">Educational </tspan><tspan x="0" y="72">Broadcasters </tspan><tspan x="0" y="96">recommends that </tspan><tspan x="0" y="120">television be made </tspan><tspan x="0" y="144">the major form of </tspan><tspan x="0" y="168">instruction in </tspan><tspan x="0" y="192">American Somoa to </tspan><tspan x="0" y="216">fix its educational </tspan><tspan x="0" y="240">system.</tspan></text>
          <text transform="translate(6193.2272 2145.844)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">Marc Lépine kills fourteen </tspan><tspan x="0" y="34">women, most of them </tspan><tspan x="0" y="68">engineering students, at </tspan><tspan x="0" y="102">Montreal&apos;s École </tspan><tspan x="0" y="136">Polytechnique. The massacre </tspan><tspan x="0" y="170">leads to a National Action </tspan><tspan x="0" y="204">Plan to promote gender </tspan><tspan x="0" y="238">equality and reduce violence </tspan><tspan x="0" y="272">against women.</tspan></text>
          <g>
            <line x1="6134.79" y1="2138.9" x2="6172.69" y2="2138.9" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="6166.07 2147.08 6164.7 2145.61 6171.93 2138.9 6164.7 2132.18 6166.07 2130.72 6174.86 2138.9 6166.07 2147.08" fill="#21409a"/>
          </g>
          <text transform="translate(6110.3632 2046.6921)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">ÉCOLE POLYTECHNIQUE </tspan><tspan x="0" y="58">MASSACRE</tspan></text>
          <g>
            <line x1="6373.09" y1="2705.63" x2="6411" y2="2705.63" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="6404.37 2713.81 6403.01 2712.35 6410.23 2705.64 6403.01 2698.92 6404.37 2697.46 6413.17 2705.64 6404.37 2713.81" fill="#21409a"/>
          </g>
          <g>
            <line x1="6147.41" y1="902.13" x2="6185.32" y2="902.13" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="6178.69 910.31 6177.33 908.84 6184.55 902.13 6177.33 895.42 6178.69 893.95 6187.49 902.13 6178.69 910.31" fill="#21409a"/>
          </g>
          <text transform="translate(6116.1322 804.6094)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">BIRTH OF </tspan><tspan x="0" y="58">WORLD WIDE WEB</tspan></text>
          <text transform="translate(4747.9276 2524.2966)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">THE</tspan><tspan x="0" y="58">‘TWO CULTURES’ </tspan><tspan x="0" y="116">PROBLEM</tspan></text>
          <g mix-blend-mode="multiply">
            <text transform="translate(4845.1039 2692.1121)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300"><tspan font-size="24"><tspan x="0" y="0">In a now-famous 1959 </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">lecture, the British </tspan></tspan><tspan font-size="24"><tspan x="0" y="68">novelist and chemist </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">C.P. Snow decries a </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">deepening divide </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">between scholarly </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">training in the </tspan></tspan><tspan font-size="24"><tspan x="0" y="238">humanities and </tspan></tspan><tspan font-size="24"><tspan x="0" y="272">training in scientific </tspan></tspan><tspan x="0" y="306" font-size="24">fields.</tspan></text>
          </g>
          <g mix-blend-mode="multiply">
            <g>
              <line x1="4785.83" y1="2684.39" x2="4823.74" y2="2684.39" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
              <polygon points="4817.11 2692.57 4815.74 2691.11 4822.97 2684.39 4815.74 2677.68 4817.11 2676.21 4825.9 2684.39 4817.11 2692.57" fill="#21409a"/>
            </g>
          </g>
          <circle cx="4984.87" cy="1334.08" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <circle cx="5064.66" cy="1996.18" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(5334.1826 622.502)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan x="0" y="0">Mass student action </tspan><tspan x="0" y="24">globally in 1968 </tspan><tspan x="0" y="48">advocates for shared </tspan><tspan x="0" y="72">governance models, </tspan><tspan x="0" y="96">curriculum reform, </tspan><tspan x="0" y="120">minority population </tspan><tspan x="0" y="144">incusion, and </tspan><tspan x="0" y="168">increased student </tspan><tspan x="0" y="192">agency.</tspan></text>
          <circle cx="5317.23" cy="616.78" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <g>
            <circle cx="6114.93" cy="1802.67" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
            <text transform="translate(6130.9688 1809.0818)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5"><tspan x="0" y="0">November 9, 1989 – Fall of the </tspan><tspan x="0" y="24">Berlin Wall.</tspan></text>
          </g>
          <polygon points="6514.77 1096.97 6729.78 1098.43 6734.06 1173.49 6515.67 1130.76 6514.77 1096.97" fill="#f7ec12"/>
          <text transform="translate(6202.791 913.084)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Tim Berners-Lee proposes </tspan><tspan x="0" y="34">the World Wide Web as a </tspan><tspan x="0" y="68">way to make </tspan><tspan x="0" y="102">research information </tspan><tspan x="0" y="136">more accessible online: </tspan><tspan x="0" y="170">&quot;We should work toward a </tspan><tspan x="0" y="204">universal linked </tspan><tspan x="0" y="238">information system, in </tspan><tspan x="0" y="272">which generality and </tspan><tspan x="0" y="306">portability are more </tspan><tspan x="0" y="340">important than fancy </tspan><tspan x="0" y="374">graphics techniques and </tspan><tspan x="0" y="408">complex extra </tspan><tspan x="0" y="442">facilities.&quot;</tspan></text>
          <text transform="translate(6431.5029 2712.1345)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">Some decry the </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="35">explosion of </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="70">Cultural Studies </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="105">departments in the </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="140">1990s as a sign of </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="175">a growing societal </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="210">culture war, in </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="245">which “everything </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="280">is culturally </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="315">determined, as it </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="350">were, and culture </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="385">ceases to mean </tspan></tspan><tspan x="0" y="420" fill="#223f9a">anything as such.”</tspan></text>
          <text transform="translate(6325.1586 2660.4895)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">CULTURE WAR</tspan></text>
          <text transform="translate(5077.1719 2001.9377)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan x="0" y="0">The federal government institutes the </tspan><tspan x="0" y="24">Canada Student Loan Program in 1964 to </tspan><tspan x="0" y="48">ensure financial assistance for students </tspan><tspan x="0" y="72">through a 100% guarantee for student </tspan><tspan x="0" y="96">loans made by private financial </tspan><tspan x="0" y="120">institutions.</tspan></text>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="2082.54" x2="5301.64" y2="2079.02" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="2058.97" x2="5301.64" y2="2055.44" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="2035.05" x2="5301.64" y2="2031.52" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="2011.8" x2="5301.64" y2="2008.28" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="6074.39" y1="1430.47" x2="6074.39" y2="1428.47" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="6074.39" y1="1418.46" x2="6074.39" y2="8.79" fill="none" stroke="#a57e2d" stroke-dasharray="4 10" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="6074.39" y1="3.79" x2="6074.39" y2="1.79" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="6074.39" y1="3139.94" x2="6074.39" y2="3137.94" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="6074.39" y1="3127.94" x2="6074.39" y2="1620.84" fill="none" stroke="#a57e2d" stroke-dasharray="4 10" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="6074.39" y1="1615.84" x2="6074.39" y2="1613.84" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g>
            <line x1="6045.05" y1="338.08" x2="6082.96" y2="338.08" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="6076.33 346.26 6074.97 344.8 6082.19 338.08 6074.97 331.37 6076.33 329.9 6085.13 338.08 6076.33 346.26" fill="#21409a"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="6074.39" y1="1452.46" x2="6074.39" y2="1448.93" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="6074.39" y1="1469.91" x2="6074.39" y2="1466.38" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="6074.39" y1="1487.58" x2="6074.39" y2="1484.06" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="6074.39" y1="1503.78" x2="6074.39" y2="1500.26" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="6074.39" y1="1521.27" x2="6074.39" y2="1517.74" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="6074.39" y1="1536.63" x2="6074.39" y2="1533.1" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="6074.39" y1="1552.93" x2="6074.39" y2="1549.4" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="6074.39" y1="1571.58" x2="6074.39" y2="1568.05" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="6074.39" y1="1589.89" x2="6074.39" y2="1586.37" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="6074.39" y1="1605.7" x2="6074.39" y2="1602.18" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <text transform="translate(5193.6719 137.9829)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan x="0" y="0">With the discontinuation </tspan><tspan x="0" y="24">of standardized exams in </tspan><tspan x="0" y="48">1967 in Ontario, failure </tspan><tspan x="0" y="72">rates fall from a </tspan><tspan x="0" y="96">ten-year average of 20% </tspan><tspan x="0" y="120">to 6–8% within a few </tspan><tspan x="0" y="144">years. Higher marks </tspan><tspan x="0" y="168">become more common, and </tspan><tspan x="0" y="192">average grades rise </tspan><tspan x="0" y="216">gradually through the </tspan><tspan x="0" y="240">1970s.</tspan></text>
          <circle cx="5176.66" cy="134.86" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="153.19" x2="5301.64" y2="149.67" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="167.46" x2="5301.64" y2="163.94" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="190.14" x2="5301.64" y2="186.61" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="213.9" x2="5301.64" y2="210.38" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="229.99" x2="5301.64" y2="226.47" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="246.85" x2="5301.64" y2="243.33" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="268" x2="5301.64" y2="264.48" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="289.31" x2="5301.64" y2="285.79" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="312.57" x2="5301.64" y2="309.05" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="336.1" x2="5301.64" y2="332.58" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="5301.64" y1="354.19" x2="5301.64" y2="350.67" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
          </g>
        </g>
        <g
          class="questionnaire" transform="translate(1700, 1950)"
          @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.knowledge)"
        >
          <title>Click to fill out the knowledge questionnaire</title>
          <image class="takeaway" href="../assets/svg/knowledge.svg" width="355" height="800" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/knowledge.svg" width="355" height="800" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/knowledge.svg" width="355" height="800" transform="translate(2 2)" />
        </g>
        <g
          class="questionnaire" transform="translate(2500, 200)"
          @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.geopolitics)"
        >
          <title>Click to fill out the geopolitics questionnaire</title>
          <image class="takeaway" href="../assets/svg/geopolitics.svg" width="355" height="800" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/geopolitics.svg" width="355" height="800" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/geopolitics.svg" width="355" height="800" transform="translate(2 2)" />
        </g>
        <g
          class="questionnaire" transform="translate(7925, 1625)"
          @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.marketization)"
        >
          <title>Click to fill out the marketization questionnaire</title>
          <image class="takeaway" href="../assets/svg/marketization.svg" width="355" height="800" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/marketization.svg" width="355" height="800" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/marketization.svg" width="355" height="800" transform="translate(2 2)" />
        </g>
        <g
          class="questionnaire" transform="translate(7000, 725)"
          @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.massification)"
        >
          <title>Click to fill out the massification questionnaire</title>
          <image class="takeaway" href="../assets/svg/massification.svg" width="355" height="800" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/massification.svg" width="355" height="800" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/massification.svg" width="355" height="800" transform="translate(2 2)" />
        </g>
        <g
          class="questionnaire" transform="translate(3050, 1500)"
          @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.restitution)"
        >
          <title>Click to fill out the restitution questionnaire</title>
          <image class="takeaway" href="../assets/svg/restitution.svg" width="355" height="781.5" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/restitution.svg" width="355" height="781.5" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/restitution.svg" width="355" height="781.5" transform="translate(2 2)" />
        </g>
        <g
          class="questionnaire" transform="translate(5650, 350)"
          @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.technology)"
        >
          <title>Click to fill out the technology questionnaire</title>
          <image class="takeaway" href="../assets/svg/technology.svg" width="355" height="800" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/technology.svg" width="355" height="800" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/technology.svg" width="355" height="800" transform="translate(2 2)" />
        </g>
        <g
          v-if="hasKnowledgeObjects"
          class="responses" transform="translate(10900, 1375)"
          @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.knowledge)"
        >
          <title>Click to view the knowledge responses</title>
          <image class="takeaway" href="../assets/svg/knowledge.svg" width="355" height="800" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/knowledge.svg" width="355" height="800" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/knowledge.svg" width="355" height="800" transform="translate(2 2)" />
        </g>
        <g
          v-if="hasGeopoliticsObjects"
          class="responses" transform="translate(9125, 2300)"
          @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.geopolitics)"
        >
          <title>Click to view the geopolitics responses</title>
          <image class="takeaway" href="../assets/svg/geopolitics.svg" width="355" height="800" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/geopolitics.svg" width="355" height="800" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/geopolitics.svg" width="355" height="800" transform="translate(2 2)" />
        </g>
        <g
          v-if="hasMarketizationObjects"
          class="responses" transform="translate(9775, 700)"
          @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.marketization)"
        >
          <title>Click to view the marketization responses</title>
          <image class="takeaway" href="../assets/svg/marketization.svg" width="355" height="800" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/marketization.svg" width="355" height="800" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/marketization.svg" width="355" height="800" transform="translate(2 2)" />
        </g>
        <g
          v-if="hasMassificationObjects"
          class="responses" transform="translate(8950, 1200)"
          @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.massification)"
        >
          <title>Click to view the massification responses</title>
          <image class="takeaway" href="../assets/svg/massification.svg" width="355" height="800" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/massification.svg" width="355" height="800" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/massification.svg" width="355" height="800" transform="translate(2 2)" />
        </g>
        <g
          v-if="hasRestitutionObjects"
          class="responses" transform="translate(10350, 2125)"
          @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.restitution)"
        >
          <title>Click to view the restitution responses</title>
          <image class="takeaway" href="../assets/svg/restitution.svg" width="355" height="781.5" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/restitution.svg" width="355" height="781.5" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/restitution.svg" width="355" height="781.5" transform="translate(2 2)" />
        </g>
        <g
          v-if="hasTechnologyObjects"
          class="responses" transform="translate(9550, 1700)"
          @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.technology)"
        >
          <title>Click to view the technology responses</title>
          <image class="takeaway" href="../assets/svg/technology.svg" width="355" height="800" transform="translate(0 0)" />
          <image class="takeaway" href="../assets/svg/technology.svg" width="355" height="800" transform="translate(1 1)" />
          <image class="takeaway" href="../assets/svg/technology.svg" width="355" height="800" transform="translate(2 2)" />
        </g>
      </g>
    </svg>
    <div class="z-3 position-absolute bottom-0 start-50 translate-middle-x btn-group text-center">
      <button @click="panUp"
        type="button" class="btn btn-link text-light link-underline-opacity-0"
        data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-title="Pan Up"
      >
        <i class="bi bi-arrow-up"></i>
      </button>
      <button @click="panDown"
        type="button" class="btn btn-link text-light link-underline-opacity-0"
        data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-title="Pan Down"
      >
        <i class="bi bi-arrow-down"></i>
      </button>
      <button @click="panLeft"
        type="button" class="btn btn-link text-light link-underline-opacity-0"
        data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-title="Pan Left"
      >
        <i class="bi bi-arrow-left"></i>
      </button>
      <button @click="panRight"
        type="button" class="btn btn-link text-light link-underline-opacity-0"
        data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-title="Pan Right"
      >
        <i class="bi bi-arrow-right"></i>
      </button>
      <button @click="zoomIn"
        type="button" class="btn btn-link text-light link-underline-opacity-0"
        data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-title="Zoom In"
      >
        <i class="bi bi-plus-lg"></i>
      </button>
      <button @click="zoomOut"
        type="button" class="btn btn-link text-light link-underline-opacity-0"
        data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-title="Zoom Out"
      >
        <i class="bi bi-dash-lg"></i>
      </button>
    </div>
    <div class="z-3 position-absolute top-0 end-0 btn-group-vertical text-center">
      <button @click="() => { toggleFullscreen() }"
        type="button" class="btn btn-link text-light link-underline-opacity-0"
        data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-title="Toggle Fullscreen Mode"
      >
        <i v-if="!isFullscreen" class="bi bi-fullscreen"></i>
        <i v-if="isFullscreen" class="bi bi-fullscreen-exit"></i>
      </button>
    </div>
    <QuestionnaireModal />
    <ResponsesModal />
  </article>
</template>

<style scoped>
svg {
  cursor: grab;
  user-select: none;
  &.grabbing {
    cursor: grabbing;
  }

  text {
    /*
    cursor: text;
    user-select: all;
    */
    a {
      cursor: pointer;
    }
  }

  .questionnaire,
  .responses {
    .bi.bi-pin-angle-fill {
      filter: drop-shadow(3px 5px 2px rgb(0 0 0 / 0.4));
    }
    .takeaway {
      cursor: pointer;
      transition: all 0.8s ease-out;
      filter: drop-shadow(3px 5px 2px rgb(0 0 0 / 0.4));
      transform-origin: 150 20;
      &:nth-child(2) {
        transform: rotate(1deg);
      }
      &:nth-child(3) {
        transform: rotate(-1deg);
      }
      &:nth-child(4) {
        transform: rotate(0deg);
      }
    }
  }
  .questionnaire:hover {
    .takeaway {
      &:nth-child(4) {
        transform: translate(5%, 20%) rotate(-10deg);
      }
    }
  }
  .responses:hover {
    .takeaway {
      &:nth-child(4) {
        transform: translate(-5%, 20%) rotate(10deg);
      }
    }
  }
}
button.btn.btn-link {
  font-size: 1.5em;
  text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;
}
</style>