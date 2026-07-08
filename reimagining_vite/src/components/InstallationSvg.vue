<script setup>
import { ref, watch, onUnmounted, onMounted, nextTick } from 'vue'
import { storeToRefs } from 'pinia'
import panzoom from 'panzoom'
import { useDisplayStore } from '../stores/display.js'

const svgRef = ref(null)
const svgGroupRef = ref(null)
const panZoomInstance = ref(null)
const grabbing = ref(false)

onMounted(() => {
  if (svgRef.value && svgGroupRef.value) {
    const SVG_HEIGHT = 3962.8
    const SVG_MARGIN_TOP = 650
    const SVG_MARGIN_BOTTOM = 0
    panZoomInstance.value = panzoom(svgGroupRef.value, {
      maxZoom: 5,
      minZoom: 0.1,
      bounds: true,
      // boundsPadding: 0.25,
      enableTextSelection: false,
      initialX: 0,
      initialY: SVG_MARGIN_TOP,
      initialZoom: Math.max(svgRef.value.clientHeight / (SVG_HEIGHT - SVG_MARGIN_TOP - SVG_MARGIN_BOTTOM), 0.1),
      beforeMouseDown: (e) => {
        const isText = !!e.target.closest('text')
        const isLink = !!e.target.closest('a')
        const isQuestionnaire = !!e.target.closest('.questionnaire')
        return !!isText || !!isLink
      },
    })
    panZoomInstance.value.on('panstart', (e) => grabbing.value = true)
    panZoomInstance.value.on('panend', (e) => grabbing.value = false)
    // nextTick(() => {
    //   // console.log('initialZoom.value', initialZoom.value)
    //   // console.log('Math.max(svgRef.value.clientHeight / (SVG_HEIGHT - SVG_MARGIN_TOP - SVG_MARGIN_BOTTOM), 0.1)', Math.max(svgRef.value.clientHeight / (SVG_HEIGHT - SVG_MARGIN_TOP - SVG_MARGIN_BOTTOM), 0.1))
    //   // panZoomInstance.value.zoomTo(
    //   //   initialX.value || 0,
    //   //   initialY.value || SVG_MARGIN_TOP,
    //   //   initialZoom.value || Math.max(svgRef.value.clientHeight / (SVG_HEIGHT - SVG_MARGIN_TOP - SVG_MARGIN_BOTTOM), 0.1),
    //   // )
    //   // panZoomInstance.value.on('transform', (e) => {
    //   //   const {scale, x, y} = e.getTransform()
    //   //   console.log('e.getTransform()', e.getTransform())
    //   //   initialX.value = -x
    //   //   initialY.value = -y
    //   //   initialZoom.value = scale
    //   // })
    // })
  }
})
onUnmounted(() => {
  if (panZoomInstance.value) {
    panZoomInstance.value.dispose()
  }
})
</script>

<template>
  <svg ref="svgRef" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 11389.69 3962.8" width="100%" height="100%"
    :class="{ grabbing: grabbing }"
  >
    <g ref="svgGroupRef" isolation="isolate">
      <g data-name="Layer 1">
        <g>
          <line x1="7728.93" y1="3526.81" x2="7728.93" y2="3524.81" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7728.93" y1="3514.74" x2="7728.93" y2="3421.09" fill="none" stroke="#a57e2d" stroke-dasharray="4.03 10.07" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7728.93" y1="3416.05" x2="7728.93" y2="3414.05" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="7728.93" y1="2895.83" x2="7728.93" y2="2893.83" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7728.93" y1="2883.8" x2="7728.93" y2="1919.92" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.03" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7728.93" y1="1914.91" x2="7728.93" y2="1912.91" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="7728.93" y1="3021.02" x2="7728.93" y2="3019.02" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7728.93" y1="3009.25" x2="7728.93" y2="2932.02" fill="none" stroke="#a57e2d" stroke-dasharray="3.91 9.78" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7728.93" y1="2927.13" x2="7728.93" y2="2925.13" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="2908.37" x2="7728.93" y2="2904.85" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="3044.53" x2="7728.93" y2="3041.01" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="3181.99" x2="7728.93" y2="3178.47" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="3260.45" x2="7728.93" y2="3256.92" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="3349.42" x2="7728.93" y2="3345.89" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="3365.04" x2="7728.93" y2="3361.52" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="3386.76" x2="7728.93" y2="3383.23" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="3057.94" x2="7728.93" y2="3054.41" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="3075.67" x2="7728.93" y2="3072.15" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <rect x="7727.42" y="3091.49" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3108.59" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3123.24" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3141.61" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3159.2" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3209.68" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3225.83" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3242.82" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3275.5" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3288.25" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3312.79" width="3" height="4.1" fill="#a57e2d"/>
        <rect x="7727.42" y="3328.29" width="3" height="4.1" fill="#a57e2d"/>
        <g>
          <line x1="1472.91" y1="3257.51" x2="1472.91" y2="3255.51" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="1472.91" y1="3245.53" x2="1472.91" y2="401.33" fill="none" stroke="#a57e2d" stroke-dasharray="3.99 9.98" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="1472.91" y1="396.35" x2="1472.91" y2="394.35" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="197.02" y1="3526.36" x2="197.02" y2="3524.36" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="197.02" y1="3514.37" x2="197.02" y2="401.34" fill="none" stroke="#a57e2d" stroke-dasharray="3.99 9.99" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="197.02" y1="396.35" x2="197.02" y2="394.35" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <line x1="180.24" y1="769.01" x2="680.57" y2="769.01" fill="none" mix-blend-mode="multiply" stroke="#223f9a" stroke-miterlimit="10" stroke-width="13"/>
        <line x1="180.24" y1="987.1" x2="708.45" y2="987.1" fill="none" mix-blend-mode="multiply" stroke="#223f9a" stroke-miterlimit="10" stroke-width="13"/>
        <text transform="translate(1163.1055 2132.7784)" fill="#223f9a" font-weight="300" mix-blend-mode="multiply"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="0" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">Black Death</tspan><tspan x="133.58" y="0" xml:space="preserve"> leads to </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="24">major collapse in </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="48">student enrollment.</tspan></tspan></text>
        <g>
          <line x1="359.62" y1="2737.58" x2="397.53" y2="2737.58" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="390.9 2745.76 389.54 2744.3 396.76 2737.58 389.54 2730.87 390.9 2729.4 399.7 2737.58 390.9 2745.76" fill="#21409a"/>
        </g>
        <text transform="translate(1615.897 796.7683)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300"><tspan font-size="24"><tspan x="0" y="0">Intellectuals no longer </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">need a university position </tspan></tspan><tspan font-size="24"><tspan x="0" y="68">to participate in </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">scholarship, creating a </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">university ‘brain drain.’ </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">The availability of,and </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">need for, print media of </tspan></tspan><tspan font-size="24"><tspan x="0" y="238">all kinds also becomes </tspan></tspan><tspan font-size="24"><tspan x="0" y="272">essential in universities, </tspan></tspan><tspan font-size="24"><tspan x="0" y="306">leading to a print-dominant </tspan></tspan><tspan font-size="24"><tspan x="0" y="340">culture lasting to this </tspan></tspan><tspan font-size="24"><tspan x="0" y="374">day. </tspan></tspan></text>
        <g>
          <line x1="1550.21" y1="787.45" x2="1588.11" y2="787.45" fill="none" stroke="#223f9a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="1581.49 795.63 1580.12 794.17 1587.34 787.46 1580.12 780.74 1581.49 779.28 1590.28 787.46 1581.49 795.63" fill="#223f9a"/>
        </g>
        <text transform="translate(1513.4617 744.5295)" fill="#223f9a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">PRINTING PRESS</tspan></text>
        <circle cx="1472.91" cy="3533.35" r="6.2" fill="#a57e2d"/>
        <circle cx="197.02" cy="3532.97" r="6.2" fill="#a57e2d"/>
        <g opacity=".8">
          <rect y="3344.73" width="1019" height="301.59" fill="#f7ec12"/>
        </g>
        <g opacity=".8">
          <rect x="1642.85" y="1272.33" width="586.38" height="157.56" fill="#f7ec12"/>
        </g>
        <g mix-blend-mode="multiply" opacity=".8">
          <rect x="1280.15" y="1527.94" width="703.45" height="249.77" transform="translate(-509.4192 2552.662) rotate(-68.1592)" fill="#f7ec12"/>
        </g>
        <g opacity=".8">
          <circle cx="1254.86" cy="1236.55" r="226.61" fill="#f7ec12"/>
        </g>
        <g opacity=".8">
          <path d="M624.23,2045.14h120.78s93.98-10.9,97.81,126.61c3.83,137.51,0,193.25,0,193.25l150.07,158.36,28.11,403.24-347.28-314.47,6.85-253.58h-66.48l-5.81,72.68-163.94-236.49,175.57-255.85,4.32,106.26Z" fill="#f7ec12"/>
        </g>
        <g opacity=".8">
          <path d="M1116.07,1522.13h355.31s60,2,68,92,0,159.59,0,159.59l3.56,154.41h-158.77v-154.41s.18-49.59-72.3-48.59-142.48,0-142.48,0h-53.3v-203Z" fill="#f7ec12"/>
        </g>
        <g opacity=".8">
          <polygon points="2229.23 2926.6 1020.37 2926.6 967.92 2518.03 2229.23 2518.03 2229.23 2926.6" fill="#f7ec12"/>
        </g>
        <text transform="translate(169.24 706.84)" fill="#223f9a" font-family="GroteskRemixMonospace-medium, &apos;GroteskRemix Monospace&apos;" font-size="165" font-variation-settings="&apos;wght&apos; 350" font-weight="500" mix-blend-mode="multiply"><tspan x="0" y="0">NEVER </tspan><tspan x="0" y="223">LET A </tspan><tspan x="0" y="446">GOOD CRISIS </tspan><tspan x="0" y="669">GO TO WASTE</tspan></text>
        <line x1="180.24" y1="1440.32" x2="1281.02" y2="1440.32" fill="none" mix-blend-mode="multiply" stroke="#223f9a" stroke-miterlimit="10" stroke-width="13"/>
        <g mix-blend-mode="multiply">
          <text transform="translate(638.5145 1720.3672)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">The Church’s division creates </tspan><tspan x="0" y="34">uncertainty over papal authority, </tspan><tspan x="0" y="68">making travel unsafe and limiting </tspan><tspan x="0" y="102">international study. Universities </tspan><tspan x="0" y="136">adapt by turning toward local </tspan><tspan x="0" y="170">students and serving a growing </tspan><tspan x="0" y="204">middle class.</tspan></text>
        </g>
        <g>
          <line x1="587.67" y1="1711.93" x2="625.57" y2="1711.93" fill="none" stroke="#223f9a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="618.95 1720.11 617.58 1718.65 624.8 1711.93 617.58 1705.22 618.95 1703.75 627.74 1711.93 618.95 1720.11" fill="#223f9a"/>
        </g>
        <text transform="translate(555.428 1672.7184)" fill="#223f9a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">PAPAL SCHISM</tspan></text>
        <text transform="translate(1329.263 3677.3939)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" mix-blend-mode="multiply" opacity=".75"><tspan x="0" y="0">1400</tspan></text>
        <text transform="translate(65.909 3675.7042)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" mix-blend-mode="multiply" opacity=".75"><tspan x="0" y="0">1100</tspan></text>
        <text transform="translate(415.5945 2746.1954)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan font-size="24"><tspan x="0" y="0">For two years, almost no </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">courses are taught in Paris. </tspan></tspan><tspan font-size="24"><tspan x="0" y="68">Finally, in 1231, King Louis </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">IX and Blanche de Castile  </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">recognize the independence </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">of the university and renew </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">and extend the privileges </tspan></tspan><tspan font-size="24"><tspan x="0" y="238">granted to it in 1200 by </tspan></tspan><tspan x="0" y="272" font-size="24">King Philip Augustus.</tspan><tspan x="382.53" y="272" font-size="21"> </tspan></text>
        <text transform="translate(819.43 680.3)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan fill="#223f9a"><tspan x="0" y="0">In the thirteenth century, the </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="24">university transforms into a </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="48">self-governing corporation, </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="72">successfully resisting </tspan></tspan><tspan x="0" y="96" fill="#223f9a">religious control.</tspan><tspan x="218.58" y="96" fill="#010101"> </tspan></text>
        <circle cx="805.2" cy="673.8" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <circle cx="1149.41" cy="2126.28" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(1029.8206 2348.5258)" fill="#223f9a" font-weight="300" mix-blend-mode="multiply"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="0">The production of paper </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="24">begins in Germany.</tspan></tspan></text>
        <circle cx="1016.13" cy="2342.03" r="5.96" fill="none" mix-blend-mode="multiply" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(1777.4986 1881.2416)" fill="#223f9a" font-weight="300" mix-blend-mode="multiply"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="0">Martin Luther publishes </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="24">the </tspan><tspan x="48.57" y="24" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">95 Theses </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5"><tspan x="0" y="48">(Disputation on the </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5"><tspan x="0" y="72">Power and Efficacy of </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5"><tspan x="0" y="96">Indulgences), </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="120">presenting them as </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="144">prompts for academic </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="168">debate and distributing </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="192">them widely as </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="216">pamphlets.</tspan></tspan></text>
        <circle cx="1763.81" cy="1874.74" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <g>
          <line x1="1472.91" y1="3359.47" x2="1472.91" y2="3357.47" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="1472.91" y1="3347.95" x2="1472.91" y2="3312.75" fill="none" stroke="#a57e2d" stroke-dasharray="3.81 9.51" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="1472.91" y1="3307.99" x2="1472.91" y2="3305.99" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="1472.91" y1="3527.15" x2="1472.91" y2="3525.15" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="1472.91" y1="3515.53" x2="1472.91" y2="3412.62" fill="none" stroke="#a57e2d" stroke-dasharray="3.85 9.62" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="1472.91" y1="3407.81" x2="1472.91" y2="3405.81" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <text transform="translate(525.1932 3307.9159)" fill="#223f9a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-variation-settings="&apos;wght&apos; 300" mix-blend-mode="multiply"><tspan font-size="97"><tspan x="0" y="0">an unfinished timeline</tspan></tspan><tspan font-size="97"><tspan x="161.8" y="100" xml:space="preserve"> of the canadian </tspan></tspan><tspan x="134.83" y="200" font-size="97">public university</tspan></text>
        <line x1="180.24" y1="1205.19" x2="1281.02" y2="1205.19" fill="none" mix-blend-mode="multiply" stroke="#223f9a" stroke-miterlimit="10" stroke-width="13"/>
        <text transform="translate(323.9944 2700.9956)" fill="#223f9a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">PARIS STUDENT STRIKES</tspan></text>
        <g>
          <line x1="4032.38" y1="2086.09" x2="4032.38" y2="2084.09" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="4032.38" y1="2074.09" x2="4032.38" y2="399" fill="none" stroke="#a57e2d" stroke-dasharray="4 10" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="4032.38" y1="394" x2="4032.38" y2="392" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g opacity=".8">
          <path d="M4489.86,1145.41s-64.1,27.05-136.79,90.87c-79.84,70.1-170.06,184.58-197.07,356.3h-281.84l-124.69-155.9-101.57,120.06v-476.69h449.55l-171.68,178.6,79.84,74.37,56.62-126.03s42.17-85.23,93.77-138.73c51.6-53.5,73.9-91.95,185.81-136.6s145.72-52.6,145.72-52.6l2.32,266.35Z" fill="#f7ec12"/>
        </g>
        <g mix-blend-mode="multiply">
          <g>
            <line x1="2555.91" y1="3530.65" x2="2555.91" y2="3528.65" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="2555.91" y1="3518.64" x2="2555.91" y2="2079.77" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.01" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="2555.91" y1="2074.76" x2="2555.91" y2="2072.76" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
        </g>
        <g>
          <line x1="3526.12" y1="3520.96" x2="3526.12" y2="3518.96" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="3526.12" y1="3508.98" x2="3526.12" y2="874.38" fill="none" stroke="#a57e2d" stroke-dasharray="3.99 9.98" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="3526.12" y1="869.39" x2="3526.12" y2="867.39" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="4032.38" y1="3530.15" x2="4032.38" y2="3528.15" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="4032.38" y1="3518.21" x2="4032.38" y2="2381.71" fill="none" stroke="#a57e2d" stroke-dasharray="3.98 9.94" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="4032.38" y1="2376.74" x2="4032.38" y2="2374.74" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <path d="M3746.97,1436.68c-49.44-63.39,22.72,29.13-26.72-34.26l198.65-143.77" fill="#f7ec12" mix-blend-mode="multiply" opacity=".6"/>
        <circle cx="4032.38" cy="3529.36" r="6.2" fill="#a57e2d"/>
        <text transform="translate(3371.6011 3674.2625)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" opacity=".75"><tspan x="0" y="0">1900</tspan></text>
        <text transform="translate(2444.4461 3675.0525)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" opacity=".75"><tspan x="0" y="0">1</tspan><tspan x="32.52" y="0" letter-spacing="-.04em">7</tspan><tspan x="93.48" y="0">50</tspan></text>
        <circle cx="2555.91" cy="3530.65" r="6.2" fill="#a57e2d"/>
        <circle cx="3526.12" cy="3527.16" r="6.2" fill="#a57e2d"/>
        <g opacity=".8">
          <rect x="2251.86" y="2521.02" width="1910.03" height="408.57" fill="#f7ec12"/>
        </g>
        <g opacity=".8">
          <path d="M4157.35,2532.8c0,133.38-.01,266.77-.06,400.15-.04,122.25-.09,244.5-.17,366.75l32.46,12.04v-166.31l295.18,344.89v145.35h-503.29c.87-371.55-.87-482.62,0-854.16" fill="#f7ec12"/>
        </g>
        <text transform="translate(2926.8733 2868.623)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">USEFUL KNOWLEDGE</tspan></text>
        <g mix-blend-mode="multiply">
          <g>
            <line x1="2959.88" y1="2908.9" x2="2997.78" y2="2908.9" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="2991.16 2917.08 2989.79 2915.62 2997.02 2908.91 2989.79 2902.19 2991.16 2900.73 2999.95 2908.91 2991.16 2917.08" fill="#21409a"/>
          </g>
        </g>
        <text transform="translate(2633.6126 1542.2324)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" font-variation-settings="&apos;wght&apos; 300"><tspan x="0" y="0">CONFLICT OF THE FACULTIES</tspan></text>
        <text transform="translate(2729.5674 1591.384)" fill="#21409a" font-weight="300"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="0">In response to Prussian university </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="34">censorship, Emmanuel Kant publishes </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="68" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">The Conflict of the Faculties</tspan><tspan x="528.26" y="68" xml:space="preserve"> in 1798. </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="102">Von Humbolt uses this text as inspiration </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="136">to establish the University of Berlin in </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="170">1810, providing the blueprint for the </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic"><tspan x="0" y="204">modern research university.</tspan></tspan></text>
        <g>
          <line x1="2668.05" y1="1585.1" x2="2705.95" y2="1585.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="2699.33 1593.28 2697.96 1591.82 2705.19 1585.11 2697.96 1578.39 2699.33 1576.93 2708.12 1585.11 2699.33 1593.28" fill="#21409a"/>
        </g>
        <text transform="translate(2969.9556 563.6326)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">KING’S COLLEGE </tspan><tspan x="0" y="58">LAND-GRANT</tspan></text>
        <g>
          <line x1="2999.61" y1="666.73" x2="3037.52" y2="666.73" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="3030.89 674.91 3029.53 673.45 3036.75 666.73 3029.53 660.02 3030.89 658.55 3039.69 666.73 3030.89 674.91" fill="#21409a"/>
        </g>
        <text transform="translate(3064.7486 673.0784)" fill="#21409a" mix-blend-mode="multiply"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">An Anglican bishop donates </tspan></tspan><tspan font-size="24"><tspan x="0" y="34" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300">225,944</tspan><tspan x="127.51" y="34" font-family="MyriadPro-Regular, &apos;Myriad Pro&apos;"> </tspan><tspan x="132.6" y="34" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300">acres to the future </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="68">University of Toronto to ensure </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="102">its financial viability, making </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="136">it one of the first university </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="170">land-grants in North America. The </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="204">land was previously taken from </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="238">the Mississauga Ojibwa.</tspan></tspan></text>
        <text transform="translate(3894.1168 3674.2625)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" mix-blend-mode="multiply" opacity=".75"><tspan x="0" y="0">1</tspan><tspan x="32.52" y="0" letter-spacing="-.05em">9</tspan><tspan x="106.68" y="0">45</tspan></text>
        <text transform="translate(3022.2564 2919.1541)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Inspired by Jeremy </tspan><tspan x="0" y="34">Bentham’s </tspan><tspan x="182.16" y="34" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">Chrestomathia</tspan><tspan x="418.96" y="34">, </tspan><tspan x="0" y="68">Utilitarians establish the </tspan><tspan x="0" y="102">University of London </tspan><tspan x="0" y="136">(later University College </tspan><tspan x="0" y="170">London). The project aims </tspan><tspan x="0" y="204">to teach ‘useful </tspan><tspan x="0" y="238">knowledge’ and break the </tspan><tspan x="0" y="272">Church of England’s </tspan><tspan x="0" y="306">monopoly over university </tspan><tspan x="0" y="340">education in England.</tspan><tspan x="382.53" y="340" letter-spacing="-.2em">	</tspan></text>
        <g mix-blend-mode="multiply">
          <text transform="translate(3644.2789 2738.0583)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300"><tspan font-size="24"><tspan x="0" y="0">In his 1917 </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">lecture </tspan><tspan x="145.73" y="34" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">Science as </tspan></tspan><tspan font-size="24"><tspan x="0" y="68" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">a Vocation</tspan><tspan x="182.16" y="68">, Max </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">Weber argues that </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">university </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">teaching should </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">separate fact from </tspan></tspan><tspan font-size="24"><tspan x="0" y="238">value, thereby </tspan></tspan><tspan font-size="24"><tspan x="0" y="272">establishing the </tspan></tspan><tspan font-size="24"><tspan x="0" y="306">principle of </tspan></tspan><tspan font-size="24"><tspan x="0" y="340">scientific </tspan></tspan><tspan x="0" y="381" font-size="24">neutrality.</tspan></text>
        </g>
        <g>
          <line x1="3585.94" y1="2729.62" x2="3623.85" y2="2729.62" fill="none" stroke="#223f9a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="3617.22 2737.8 3615.85 2736.34 3623.08 2729.62 3615.85 2722.91 3617.22 2721.44 3626.02 2729.62 3617.22 2737.8" fill="#223f9a"/>
        </g>
        <text transform="translate(3551.5572 2635.9026)" fill="#223f9a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">SCIENCE AS </tspan><tspan x="0" y="58">VOCATION</tspan></text>
        <text transform="translate(3749.5682 2170.9678)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">Operating revenue for Canadian </tspan><tspan x="0" y="34">universities declines by almost 30% </tspan><tspan x="0" y="68">between 1930 and 1935. Despite this, </tspan><tspan x="0" y="102">administrators at the University of </tspan><tspan x="0" y="136">Saskatchewan accept promissory notes </tspan><tspan x="0" y="170">from one-third of their students who </tspan><tspan x="0" y="204">are unable to pay fees.</tspan></text>
        <g>
          <line x1="3681.71" y1="2167.26" x2="3719.61" y2="2167.26" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="3712.98 2175.44 3711.62 2173.97 3718.84 2167.26 3711.62 2160.55 3712.98 2159.08 3721.78 2167.26 3712.98 2175.44" fill="#21409a"/>
        </g>
        <text transform="translate(3648.0435 2121.7236)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">THE GREAT DEPRESSION</tspan></text>
        <text transform="translate(3757.3406 1753.5342)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">In 1932, IBM </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="24">researcher Richard </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="48">Warren files a patent </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="72">for optical mark </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="96">sense systems for </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="120" xml:space="preserve">test scoring,  </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="144">commonly known as </tspan></tspan><tspan x="0" y="168" fill="#223f9a">Scantron.</tspan><tspan x="109.29" y="168" fill="#21409a" letter-spacing="1.41em">	</tspan><tspan x="144" y="168" fill="#21409a" letter-spacing="1.49em">	</tspan></text>
        <circle cx="3743.6" cy="1749.54" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <circle cx="3597.9" cy="1000.56" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <g>
          <text transform="translate(2391.1143 2222.5309)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">The Republic of Letters</tspan><tspan x="279.3" y="0" xml:space="preserve"> fosters a </tspan><tspan x="0" y="24">bloom of new ideas in the public </tspan><tspan x="0" y="48">domain, drawing the middle class </tspan><tspan x="0" y="72">into academic discourse and calling </tspan><tspan x="0" y="96">antiquated university practices </tspan><tspan x="0" y="120">into question.</tspan></text>
          <circle cx="2379.37" cy="2216.03" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        </g>
        <text transform="translate(3228.0894 1094.1672)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">The 1867 </tspan><tspan x="0" y="24">Constitution Act </tspan><tspan x="0" y="48">designates </tspan><tspan x="0" y="72">education to be </tspan><tspan x="0" y="96">regulated </tspan><tspan x="0" y="120">exclusively at the </tspan><tspan x="0" y="144">provincial level.</tspan></text>
        <circle cx="3208.95" cy="1089.69" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(4063.1434 2657.9629)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Vannevar Bush publishes </tspan><tspan stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5"><tspan x="0" y="24">Science: The Endless </tspan></tspan><tspan x="0" y="48" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">Frontier</tspan><tspan x="97.15" y="48">, proposing a linear </tspan><tspan x="0" y="72">model of innovation—basic </tspan><tspan x="0" y="96">research → applied research → </tspan><tspan x="0" y="120">development → innovation—and </tspan><tspan x="0" y="144">arguing that the government </tspan><tspan x="0" y="168">should fund basic research as </tspan><tspan x="0" y="192">the foundation for future </tspan><tspan x="0" y="216">gains in wealth, health, and </tspan><tspan x="0" y="240">national security.</tspan></text>
        <circle cx="4050.46" cy="2651.46" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <g mix-blend-mode="multiply">
          <g>
            <line x1="2555.91" y1="2007.06" x2="2555.91" y2="2005.06" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="2555.91" y1="1995.02" x2="2555.91" y2="399.02" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.03" stroke-miterlimit="10" stroke-width="3"/>
            <line x1="2555.91" y1="394" x2="2555.91" y2="392" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          </g>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="2555.91" y1="2039.93" x2="2555.91" y2="2036.4" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="2555.91" y1="2017.92" x2="2555.91" y2="2014.39" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="2555.91" y1="2063.47" x2="2555.91" y2="2059.94" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="3526.12" y1="655.47" x2="3526.12" y2="653.47" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="3526.12" y1="643.57" x2="3526.12" y2="398.96" fill="none" stroke="#a57e2d" stroke-dasharray="3.96 9.9" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="3526.12" y1="394" x2="3526.12" y2="392" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="3526.12" y1="682.69" x2="3526.12" y2="679.17" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="3526.12" y1="694.37" x2="3526.12" y2="690.84" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="3526.12" y1="711.63" x2="3526.12" y2="708.11" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="3526.12" y1="747.24" x2="3526.12" y2="743.72" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="3526.12" y1="763.23" x2="3526.12" y2="759.71" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="3526.12" y1="855.26" x2="3526.12" y2="851.74" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="3526.12" y1="822.67" x2="3526.12" y2="819.14" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="3526.12" y1="794.32" x2="3526.12" y2="790.79" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="3526.12" y1="729.14" x2="3526.12" y2="725.62" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="3526.12" y1="779.89" x2="3526.12" y2="776.37" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="4032.38" y1="2171.28" x2="4032.38" y2="2169.28" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="4032.38" y1="2159.29" x2="4032.38" y2="2122.31" fill="none" stroke="#a57e2d" stroke-dasharray="4 9.99" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="4032.38" y1="2117.31" x2="4032.38" y2="2115.31" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="4032.46" y1="2186.51" x2="4032.46" y2="2182.98" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="4032.46" y1="2209.43" x2="4032.46" y2="2205.9" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="4032.46" y1="2226" x2="4032.46" y2="2222.48" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="4032.46" y1="2252.39" x2="4032.46" y2="2248.87" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="4032.46" y1="2276.9" x2="4032.46" y2="2273.38" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="4032.46" y1="2292.21" x2="4032.46" y2="2288.68" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="4032.46" y1="2318.82" x2="4032.46" y2="2315.3" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="4032.38" y1="2352.75" x2="4032.38" y2="2349.23" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <rect x="2251.82" y="1269.99" width="484.56" height="157.56" fill="#f7ec12" opacity=".8"/>
        <text transform="translate(4009.5731 1217.7068)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">VETERANS </tspan><tspan x="0" y="58">REHABILITATION</tspan><tspan x="0" y="116">ACT</tspan></text>
        <text transform="translate(3613.6983 1004.5388)" fill="#223f9a" font-weight="300" mix-blend-mode="multiply"><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="0">American eugenicist Lewis </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="24">Terman publishes his revision </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="48">of the Binet-Simon Intelligence </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="72">Test in 1916, which will become </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="96">colloquially known as the IQ </tspan></tspan><tspan font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic"><tspan x="0" y="120">test.</tspan></tspan></text>
        <g mix-blend-mode="multiply">
          <text transform="translate(4099.6873 1385.5217)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">Economic </tspan><tspan x="0" y="34">development </tspan><tspan x="0" y="68">following WWII </tspan><tspan x="0" y="102">leads to </tspan><tspan x="0" y="136">unprecedented </tspan><tspan x="0" y="170">investment in </tspan><tspan x="0" y="204">higher education, </tspan><tspan x="0" y="238">dramatically </tspan><tspan x="0" y="272">expanding the </tspan><tspan x="0" y="306">country&apos;s </tspan><tspan x="0" y="340">academic </tspan><tspan x="0" y="374">infrastructure. </tspan><tspan x="0" y="408">By 1949-50 </tspan><tspan x="0" y="442">veterans account </tspan><tspan x="0" y="476">for 21% of all </tspan><tspan x="0" y="510">Canadian </tspan><tspan x="0" y="544">university </tspan><tspan x="0" y="578">students.</tspan></text>
        </g>
        <g>
          <line x1="4039.85" y1="1377.46" x2="4077.76" y2="1377.46" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="4071.13 1385.64 4069.77 1384.18 4076.99 1377.47 4069.77 1370.75 4071.13 1369.29 4079.93 1377.47 4071.13 1385.64" fill="#21409a"/>
        </g>
        <text transform="translate(5772.6409 3680.576)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300"><tspan x="0" y="0">1</tspan><tspan x="32.52" y="0" letter-spacing="-.03em">9</tspan><tspan x="108.84" y="0" letter-spacing="0em">88</tspan></text>
        <g>
          <line x1="5138.43" y1="537.36" x2="5138.43" y2="535.36" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="5138.43" y1="525.43" x2="5138.43" y2="405.28" fill="none" stroke="#a57e2d" stroke-dasharray="3.97 9.93" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="5138.43" y1="400.32" x2="5138.43" y2="398.32" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="5138.43" y1="2386" x2="5138.43" y2="2384" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="5138.43" y1="2374" x2="5138.43" y2="767.83" fill="none" stroke="#a57e2d" stroke-dasharray="4 10.01" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="5138.43" y1="762.83" x2="5138.43" y2="760.83" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="5138.43" y1="3536.47" x2="5138.43" y2="3534.47" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="5138.43" y1="3524.44" x2="5138.43" y2="2504.74" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.03" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="5138.43" y1="2499.73" x2="5138.43" y2="2497.73" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <circle cx="5138.43" cy="3535.67" r="6.2" fill="#a57e2d"/>
        <circle cx="5911.17" cy="3536.47" r="6.2" fill="#a57e2d"/>
        <g opacity=".8">
          <path d="M5033.39,2172.93c-88.69-68.05-165.37-59.57-206.44-51.63-66.63,12.89-115.87,57.13-144.44,119.68-33.54,72.91-27.88,156.18-27.28,234.62l-1.83,1.93c.6-.02,1.22-.03,1.85-.05,0,.58,0,1.16.01,1.74l1.71-1.8c80.03-2.68,307.54-30.96,408.67-29.99,5.54.05,13.08,1.18,14.25-1.11.8-1.57-.12-13.35,0-20.7.91-55.19,4.92-114.59,6.62-165.61.91-18.47,7.93-2.34,11.65,4.6,15.61,32.57,32.47,70.27,48.15,104.26,12.71,28.57,25.96,56.43,42.4,83.25,21.7,35.83,47.94,69.64,81.72,94.6,31.29,24.37,69.18,40.11,108.12,46.86,21.36,3.77,43,4.96,64.34,1.69,19.65-2.61,38.21-7,56.4-15.48,15.15-6.95,30.08-14.82,43.86-24.15,22.88-15.78,43.95-35.49,61.18-57.35,19.28-24.05,31.96-52.8,41-82.13,8.9-26.94,15.47-54.16,19.03-82.46,3.59-20.51,3.9-59.25,20.37-67.49,6.06-3.34,14.29-3.91,21.81-4.22,51.48-.59,123.81,0,170.43-.26,6.03-.08,11.67-.04,16.67-.5,2.25-.23,3.35-.57,3.37-1.07-76.54-29.49-309.13-104.81-393.64-134.54-7.21-2.37-14.07-4.67-20.75-4.28h-.07c-7.12.63-14.89,4.13-22.75,7.42-73.74,32.21-233.25,99.47-303.21,131.14-9.26,5.16,11.17,3.92,21.54,4.11,34.03-.32,80.38-1,116.46-1.39,20.6.58,47.93-4.11,59.62,9.58,10.05,14.28-1.5,36.27-13.05,48.96-6.73,7.45-15.18,12.78-24.81,15.66-27.79,8.88-57.27-.9-82.97-12.47-27.58-13.22-54.85-27.5-78.82-46.73" fill="#f7ec12"/>
        </g>
        <g opacity=".8">
          <rect x="4499.72" y="878.74" width="484.56" height="266.35" fill="#f7ec12"/>
        </g>
        <g opacity=".8">
          <path d="M6733.72,1400.69c-32.54.15-96.54.29-119.2.5-16.35.82-35.61,9.12-41.97,25.42-3.16,8.53-3.71,19.61-4.25,29.36-.6,11.39-1.49,24.52-1.83,35.54-.03,4.32-.11,7.57,4.97,7.5,30.02,1.7,94.17,5.24,113.52,6.32,4.45.26,5.96.3,6.13.76-10.56,24.99-223.53,498.58-232.71,519.59-.19.42-.31.64-.42.67-.21.06-.49-.79-1.27-2.5-4.13-9.35-19.51-44.18-40.49-91.69-64.22-146.52-181.9-409.87-187.74-426.25.55-.33,2.69-.43,7.49-.78,21-1.5,82.37-5.75,111.54-7.88,1.15-.15,2.51-.24,3.23-1.19.87-1.13.78-3.69.69-8.45-.4-17.71-.96-41.57-1.34-59.6-.39-6.39,1.54-11.3,4.16-17.02,4.65-10.63,10.61-19.99,18.76-28.41,7.14-7.36,14.32-12.94,24.1-17.34,6.78-2.98,15.26-6.51,21.89-8.9,77.72-1.34,286.51-.03,314.73-.47" fill="#f7ec12"/>
        </g>
        <g opacity=".8">
          <polygon points="5079.9 3387.13 4651.52 3387.13 4651.52 2379.26 5079.9 2446.02 5079.9 3387.13" fill="#f7ec12"/>
        </g>
        <g opacity=".8">
          <path d="M6723.22,3493.46c-263.68,0-430.06-4.69-430.06-311.3s170.28-298.97,433.96-298.97" fill="#f7ec12"/>
        </g>
        <g mix-blend-mode="multiply" opacity=".8">
          <polyline points="6537.94 2893.93 6723.22 2893.93 6723.22 3493.46 6684.83 3500.87" fill="#f7ec12"/>
        </g>
        <text transform="translate(5375.2972 1811.2278)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">The perception that rapid </tspan><tspan x="0" y="34">technological change is eroding the </tspan><tspan x="0" y="68">power of institutions like Church and </tspan><tspan x="0" y="102">State leads the Higher Education </tspan><tspan x="0" y="136">Council of Quebec to commision </tspan><tspan x="0" y="170">philosopher J-F Lyotard to write a </tspan><tspan x="0" y="204">report on the state of knowledge and </tspan><tspan x="0" y="238">the new postmodern condition.</tspan></text>
        <text transform="translate(5279.7759 1693.5232)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">THE POSTMODERN</tspan><tspan x="0" y="58">CONDITION</tspan></text>
        <g>
          <line x1="5316" y1="1801.24" x2="5353.91" y2="1801.24" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="5347.28 1809.42 5345.92 1807.96 5353.14 1801.25 5345.92 1794.53 5347.28 1793.07 5356.08 1801.25 5347.28 1809.42" fill="#21409a"/>
        </g>
        <text/>
        <text transform="translate(5825.1929 618.0803)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">THE INDIGENOUS </tspan><tspan x="0" y="58">STUDENT WALKOUT</tspan></text>
        <text transform="translate(5254.0094 2814.506)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">Following the university&apos;s </tspan><tspan x="0" y="34">denial of a grievance about a </tspan><tspan x="0" y="68">racist professor filed by black </tspan><tspan x="0" y="102">students, 200 students begin a </tspan><tspan x="0" y="136">peaceful sit-in. Now considered </tspan><tspan x="0" y="170">one of the largest student </tspan><tspan x="0" y="204">protests in Canadian history, it </tspan><tspan x="0" y="238">coincides with a global student </tspan><tspan x="0" y="272">movement for university reforms </tspan><tspan x="0" y="306">in the late 1960s.</tspan></text>
        <text transform="translate(5155.7916 2692.265)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">SIR GEORGE </tspan><tspan x="0" y="58">WILLIAMS AFFAIR</tspan></text>
        <g>
          <line x1="5189.34" y1="2808.94" x2="5227.25" y2="2808.94" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="5220.62 2817.12 5219.26 2815.65 5226.48 2808.94 5219.26 2802.22 5220.62 2800.76 5229.42 2808.94 5220.62 2817.12" fill="#21409a"/>
        </g>
        <g>
          <line x1="4608.32" y1="1209.68" x2="4646.23" y2="1209.68" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="4639.6 1217.86 4638.24 1216.39 4645.46 1209.68 4638.24 1202.97 4639.6 1201.5 4648.4 1209.68 4639.6 1217.86" fill="#21409a"/>
        </g>
        <text transform="translate(4997.3282 3680.576)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">1</tspan><tspan x="32.52" y="0" letter-spacing="0em">9</tspan><tspan x="111.24" y="0">68</tspan></text>
        <text transform="translate(5935.4109 740.3206)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">A coalition of Indigenous students </tspan><tspan x="0" y="34">organizes walk-outs and sit-ins at </tspan><tspan x="0" y="68">York University and the University of </tspan><tspan x="0" y="102">Toronto. Their demands include </tspan><tspan x="0" y="136">creating a dedicated Aboriginal </tspan><tspan x="0" y="170">Studies department and the formal </tspan><tspan x="0" y="204">recognition of Indigenous land rights </tspan><tspan x="0" y="238">on campus.</tspan></text>
        <text transform="translate(4577.6334 1107.593)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">SECURING ACADEMIC </tspan><tspan x="0" y="58">FREEDOM</tspan></text>
        <text transform="translate(4676.1871 1213.3889)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">After its founding in </tspan><tspan x="0" y="34">1951, the Canadian </tspan><tspan x="0" y="68">Association of </tspan><tspan x="0" y="102">University Teachers </tspan><tspan x="0" y="136">begins advocating for </tspan><tspan x="0" y="170">the right of Canadian </tspan><tspan x="0" y="204">professors to publicly </tspan><tspan x="0" y="238">challenge their </tspan><tspan x="0" y="272">institutions’ policies </tspan><tspan x="0" y="306">without reprimand or </tspan><tspan x="0" y="340">termination. </tspan></text>
        <text transform="translate(4833.5838 1736.3334)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan x="0" y="0">The National </tspan><tspan x="0" y="24">Association of </tspan><tspan x="0" y="48">Educational </tspan><tspan x="0" y="72">Broadcasters </tspan><tspan x="0" y="96">recommends that </tspan><tspan x="0" y="120">television be made </tspan><tspan x="0" y="144">the major form of </tspan><tspan x="0" y="168">instruction in </tspan><tspan x="0" y="192">American Somoa to </tspan><tspan x="0" y="216">fix its educational </tspan><tspan x="0" y="240">system.</tspan></text>
        <text transform="translate(6030.0115 2542.3734)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">Marc Lépine kills fourteen </tspan><tspan x="0" y="34">women, most of them </tspan><tspan x="0" y="68">engineering students, at </tspan><tspan x="0" y="102">Montreal&apos;s École </tspan><tspan x="0" y="136">Polytechnique. The massacre </tspan><tspan x="0" y="170">leads to a National Action </tspan><tspan x="0" y="204">Plan to promote gender </tspan><tspan x="0" y="238">equality and reduce violence </tspan><tspan x="0" y="272">against women.</tspan></text>
        <g>
          <line x1="5971.57" y1="2535.43" x2="6009.48" y2="2535.43" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="6002.85 2543.6 6001.49 2542.14 6008.71 2535.43 6001.49 2528.71 6002.85 2527.25 6011.65 2535.43 6002.85 2543.6" fill="#21409a"/>
        </g>
        <text transform="translate(5947.1475 2443.2216)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">ÉCOLE POLYTECHNIQUE </tspan><tspan x="0" y="58">MASSACRE</tspan></text>
        <g>
          <line x1="6209.88" y1="3102.16" x2="6247.79" y2="3102.16" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="6241.16 3110.34 6239.79 3108.88 6247.02 3102.16 6239.79 3095.45 6241.16 3093.99 6249.95 3102.16 6241.16 3110.34" fill="#21409a"/>
        </g>
        <g>
          <line x1="5984.2" y1="1298.66" x2="6022.1" y2="1298.66" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="6015.48 1306.84 6014.11 1305.37 6021.34 1298.66 6014.11 1291.95 6015.48 1290.48 6024.27 1298.66 6015.48 1306.84" fill="#21409a"/>
        </g>
        <text transform="translate(5952.9166 1201.1389)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">BIRTH OF </tspan><tspan x="0" y="58">WORLD WIDE WEB</tspan></text>
        <text transform="translate(4584.712 2920.8263)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0">THE</tspan><tspan x="0" y="58">‘TWO CULTURES’ </tspan><tspan x="0" y="116">PROBLEM</tspan></text>
        <g mix-blend-mode="multiply">
          <text transform="translate(4681.8883 3088.6415)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300"><tspan font-size="24"><tspan x="0" y="0">In a now-famous 1959 </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">lecture, the British </tspan></tspan><tspan font-size="24"><tspan x="0" y="68">novelist and chemist </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">C.P. Snow decries a </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">deepening divide </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">between scholarly </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">training in the </tspan></tspan><tspan font-size="24"><tspan x="0" y="238">humanities and </tspan></tspan><tspan font-size="24"><tspan x="0" y="272">training in scientific </tspan></tspan><tspan x="0" y="306" font-size="24">fields.</tspan></text>
        </g>
        <g mix-blend-mode="multiply">
          <g>
            <line x1="4622.61" y1="3080.92" x2="4660.52" y2="3080.92" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
            <polygon points="4653.89 3089.1 4652.53 3087.63 4659.75 3080.92 4652.53 3074.21 4653.89 3072.74 4662.69 3080.92 4653.89 3089.1" fill="#21409a"/>
          </g>
        </g>
        <circle cx="4821.66" cy="1730.61" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <circle cx="4901.45" cy="2392.71" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(5170.9676 1019.0315)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan x="0" y="0">Mass student action </tspan><tspan x="0" y="24">globally in 1968 </tspan><tspan x="0" y="48">advocates for shared </tspan><tspan x="0" y="72">governance models, </tspan><tspan x="0" y="96">curriculum reform, </tspan><tspan x="0" y="120">minority population </tspan><tspan x="0" y="144">incusion, and </tspan><tspan x="0" y="168">increased student </tspan><tspan x="0" y="192">agency.</tspan></text>
        <circle cx="5154.02" cy="1013.31" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <g>
          <circle cx="5951.72" cy="2199.2" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
          <text transform="translate(5967.7537 2205.6115)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5"><tspan x="0" y="0">November 9, 1989 – Fall of the </tspan><tspan x="0" y="24">Berlin Wall.</tspan></text>
        </g>
        <polygon points="6351.55 1493.5 6566.56 1494.96 6570.84 1570.02 6352.45 1527.29 6351.55 1493.5" fill="#f7ec12"/>
        <text transform="translate(6039.576 1309.6135)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Tim Berners-Lee proposes </tspan><tspan x="0" y="34">the World Wide Web as a </tspan><tspan x="0" y="68">way to make </tspan><tspan x="0" y="102">research information </tspan><tspan x="0" y="136">more accessible online: </tspan><tspan x="0" y="170">&quot;We should work toward a </tspan><tspan x="0" y="204">universal linked </tspan><tspan x="0" y="238">information system, in </tspan><tspan x="0" y="272">which generality and </tspan><tspan x="0" y="306">portability are more </tspan><tspan x="0" y="340">important than fancy </tspan><tspan x="0" y="374">graphics techniques and </tspan><tspan x="0" y="408">complex extra </tspan><tspan x="0" y="442">facilities.&quot;</tspan></text>
        <text transform="translate(6268.2879 3108.6639)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">Some decry the </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="35">explosion of </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="70">Cultural Studies </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="105">departments in the </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="140">1990s as a sign of </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="175">a growing societal </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="210">culture war, in </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="245">which “everything </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="280">is culturally </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="315">determined, as it </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="350">were, and culture </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="385">ceases to mean </tspan></tspan><tspan x="0" y="420" fill="#223f9a">anything as such.”</tspan></text>
        <text transform="translate(6161.943 3057.0189)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">CULTURE WAR</tspan></text>
        <text transform="translate(4913.9568 2398.4674)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan x="0" y="0">The federal government institutes the </tspan><tspan x="0" y="24">Canada Student Loan Program in 1964 to </tspan><tspan x="0" y="48">ensure financial assistance for students </tspan><tspan x="0" y="72">through a 100% guarantee for student </tspan><tspan x="0" y="96">loans made by private financial </tspan><tspan x="0" y="120">institutions.</tspan></text>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="2479.07" x2="5138.43" y2="2475.55" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="2455.5" x2="5138.43" y2="2451.97" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="2431.57" x2="5138.43" y2="2428.05" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="2408.33" x2="5138.43" y2="2404.81" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="5911.17" y1="1827" x2="5911.17" y2="1825" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="5911.17" y1="1814.99" x2="5911.17" y2="405.32" fill="none" stroke="#a57e2d" stroke-dasharray="4 10" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="5911.17" y1="400.32" x2="5911.17" y2="398.32" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="5911.17" y1="3536.47" x2="5911.17" y2="3534.47" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="5911.17" y1="3524.47" x2="5911.17" y2="2017.37" fill="none" stroke="#a57e2d" stroke-dasharray="4 10" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="5911.17" y1="2012.37" x2="5911.17" y2="2010.37" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="5881.84" y1="734.61" x2="5919.75" y2="734.61" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="5913.12 742.79 5911.75 741.33 5918.98 734.61 5911.75 727.9 5913.12 726.43 5921.91 734.61 5913.12 742.79" fill="#21409a"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5911.17" y1="1848.99" x2="5911.17" y2="1845.46" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5911.17" y1="1866.44" x2="5911.17" y2="1862.91" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5911.17" y1="1884.11" x2="5911.17" y2="1880.59" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5911.17" y1="1900.31" x2="5911.17" y2="1896.79" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5911.17" y1="1917.8" x2="5911.17" y2="1914.27" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5911.17" y1="1933.16" x2="5911.17" y2="1929.63" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5911.17" y1="1949.46" x2="5911.17" y2="1945.93" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5911.17" y1="1968.11" x2="5911.17" y2="1964.58" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5911.17" y1="1986.42" x2="5911.17" y2="1982.9" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5911.17" y1="2002.23" x2="5911.17" y2="1998.71" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <text transform="translate(5030.4568 534.5125)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan x="0" y="0">With the discontinuation </tspan><tspan x="0" y="24">of standardized exams in </tspan><tspan x="0" y="48">1967 in Ontario, failure </tspan><tspan x="0" y="72">rates fall from a </tspan><tspan x="0" y="96">ten-year average of 20% </tspan><tspan x="0" y="120">to 6–8% within a few </tspan><tspan x="0" y="144">years. Higher marks </tspan><tspan x="0" y="168">become more common, and </tspan><tspan x="0" y="192">average grades rise </tspan><tspan x="0" y="216">gradually through the </tspan><tspan x="0" y="240">1970s.</tspan></text>
        <circle cx="5013.44" cy="531.39" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="549.72" x2="5138.43" y2="546.2" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="563.99" x2="5138.43" y2="560.47" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="586.67" x2="5138.43" y2="583.14" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="610.43" x2="5138.43" y2="606.9" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="626.52" x2="5138.43" y2="623" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="643.38" x2="5138.43" y2="639.86" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="664.53" x2="5138.43" y2="661.01" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="685.84" x2="5138.43" y2="682.32" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="709.1" x2="5138.43" y2="705.58" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="732.63" x2="5138.43" y2="729.11" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="5138.43" y1="750.72" x2="5138.43" y2="747.2" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <line x1="6802.1" y1="1342.83" x2="6831.69" y2="1392.21" fill="#f7ec12"/>
        <text transform="translate(8474.0623 3677.365)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300"><tspan x="0" y="0">2025</tspan></text>
        <g opacity=".8">
          <circle cx="7206.28" cy="1068.96" r="143.5" fill="#f7ec12"/>
        </g>
        <g mix-blend-mode="multiply" opacity=".8">
          <path d="M8290.76,653.99c214.97,184.19,497.15,446.35,712.11,630.54,37.14,31.83-37.14-31.83,0,0l-.1,441.16-670.58-575.37c-13.27-136.92-26.55-273.81-39.83-410.73" fill="#f7ec12"/>
        </g>
        <g>
          <line x1="7045.53" y1="1560.4" x2="7045.53" y2="1558.4" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7045.53" y1="1548.45" x2="7045.53" y2="397.87" fill="none" stroke="#a57e2d" stroke-dasharray="3.98 9.94" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7045.53" y1="392.89" x2="7045.53" y2="390.89" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="7045.53" y1="2009.53" x2="7045.53" y2="2007.53" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7045.53" y1="1997.5" x2="7045.53" y2="1567.41" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.03" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7045.53" y1="1562.4" x2="7045.53" y2="1560.4" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="7045.53" y1="2478.38" x2="7045.53" y2="2476.38" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7045.53" y1="2466.49" x2="7045.53" y2="2083.95" fill="none" stroke="#a57e2d" stroke-dasharray="3.95 9.88" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7045.53" y1="2079" x2="7045.53" y2="2077" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="7045.53" y1="3530.17" x2="7045.53" y2="3528.17" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7045.53" y1="3518.17" x2="7045.53" y2="2710.92" fill="none" stroke="#a57e2d" stroke-dasharray="4 10" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7045.53" y1="2705.92" x2="7045.53" y2="2703.92" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <circle cx="7045.53" cy="3529.37" r="6.2" fill="#a57e2d"/>
        <text transform="translate(7577.8929 3673.1514)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300"><tspan x="0" y="0">2</tspan><tspan x="75.12" y="0" letter-spacing="-.03em">0</tspan><tspan x="180.72" y="0">10</tspan></text>
        <g>
          <line x1="7728.93" y1="585.99" x2="7728.93" y2="583.99" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7728.93" y1="574.03" x2="7728.93" y2="397.87" fill="none" stroke="#a57e2d" stroke-dasharray="3.98 9.95" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7728.93" y1="392.89" x2="7728.93" y2="390.89" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="7728.93" y1="1857.46" x2="7728.93" y2="1855.46" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7728.93" y1="1845.48" x2="7728.93" y2="774.33" fill="none" stroke="#a57e2d" stroke-dasharray="3.99 9.98" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="7728.93" y1="769.34" x2="7728.93" y2="767.34" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <circle cx="7728.93" cy="3526.01" r="6.2" fill="#a57e2d"/>
        <g>
          <line x1="8652.18" y1="811.56" x2="8652.18" y2="809.56" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="8652.18" y1="799.54" x2="8652.18" y2="397.9" fill="none" stroke="#a57e2d" stroke-dasharray="4.01 10.02" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="8652.18" y1="392.89" x2="8652.18" y2="390.89" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="8652.18" y1="2519.19" x2="8652.18" y2="2517.19" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="8652.18" y1="2507.18" x2="8652.18" y2="1124.9" fill="none" stroke="#a57e2d" stroke-dasharray="4 10.01" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="8652.18" y1="1119.9" x2="8652.18" y2="1117.9" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g>
          <line x1="8652.18" y1="3530.31" x2="8652.18" y2="3528.31" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="8652.18" y1="3518.33" x2="8652.18" y2="2754.88" fill="none" stroke="#a57e2d" stroke-dasharray="3.99 9.98" stroke-miterlimit="10" stroke-width="3"/>
          <line x1="8652.18" y1="2749.9" x2="8652.18" y2="2747.9" fill="none" stroke="#a57e2d" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <circle cx="8652.18" cy="3529.52" r="6.2" fill="#a57e2d"/>
        <g>
          <line x1="7806.98" y1="1494.15" x2="7844.88" y2="1494.15" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="7838.26 1502.33 7836.89 1500.86 7844.12 1494.15 7836.89 1487.43 7838.26 1485.97 7847.05 1494.15 7838.26 1502.33" fill="#21409a"/>
        </g>
        <g mix-blend-mode="multiply">
          <text transform="translate(8253.2781 2533.2432)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">A global pandemic forces universities </tspan><tspan x="0" y="34">to turn to online teaching. According </tspan><tspan x="0" y="68">to the Canadian Digital Learning </tspan><tspan x="0" y="102">Research Association, the average </tspan><tspan x="0" y="136">Canadian university has ‘17 times </tspan><tspan x="0" y="170">more online course enrolments in the </tspan><tspan x="0" y="204">2020 fall semester compared to the </tspan><tspan x="0" y="238">same time in 2019’.</tspan></text>
        </g>
        <g>
          <line x1="8185.58" y1="2528.58" x2="8223.48" y2="2528.58" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="8216.86 2536.76 8215.49 2535.3 8222.71 2528.58 8215.49 2521.87 8216.86 2520.4 8225.65 2528.58 8216.86 2536.76" fill="#21409a"/>
        </g>
        <text transform="translate(6868.2917 2023.9109)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">In the 1990&apos;s computer labs become </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="24">increasinly prevalent for general </tspan></tspan><tspan x="0" y="48" fill="#223f9a">student use in universities. </tspan><tspan x="352.16" y="48" fill="#21409a" letter-spacing="-.27em">	</tspan><tspan x="359.99" y="48" fill="#21409a" letter-spacing="1.49em">	</tspan></text>
        <text transform="translate(7764.2327 1093.3381)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Peter Thiel starts a</tspan><tspan x="0" y="24">fellowship in 2010 to </tspan><tspan x="0" y="48">encourage students to </tspan><tspan x="0" y="72">drop out of university and </tspan><tspan x="0" y="96">start companies instead.</tspan></text>
        <circle cx="6855.42" cy="2017.93" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <circle cx="7750.16" cy="1087.81" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(7263.9466 1533.1338)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Tarana Burke founds the </tspan><tspan x="291.45" y="0" letter-spacing="0em" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".25">Me</tspan><tspan x="315.64" y="0" letter-spacing="-.4em" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".25"> </tspan><tspan x="321.33" y="0" letter-spacing="0em" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".25">Too</tspan><tspan x="357.57" y="0" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".25"> </tspan><tspan x="0" y="24">movement in 2006 to support </tspan><tspan x="0" y="48">women and girls who survive </tspan><tspan x="0" y="72">sexual violence.</tspan></text>
        <circle cx="7251.87" cy="1527.6" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <circle cx="8298.65" cy="3080.64" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(7354.1028 2747.2942)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" stroke="#223f9a" stroke-miterlimit="10" stroke-width=".5">2008 Finacial Crash</tspan><tspan x="230.73" y="0">.</tspan></text>
        <circle cx="7336.06" cy="2741.79" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(6847.7917 801.3684)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">In 1996, </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="24">Ontario </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="48">deregulates </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="72">international </tspan></tspan><tspan x="0" y="96" fill="#223f9a">tuition fees.</tspan><tspan x="157.87" y="96" fill="#21409a" letter-spacing=".62em">	</tspan><tspan x="180" y="96" fill="#21409a" letter-spacing="1.49em">	</tspan></text>
        <circle cx="6835.92" cy="796.39" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(8150.4323 2490.8)" fill="#21409a" font-size="48" mix-blend-mode="multiply"><tspan x="0" y="0" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-variation-settings="&apos;wght&apos; 300">COVID </tspan><tspan x="160.13" y="0" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-weight="300">19</tspan></text>
        <circle cx="8114.36" cy="1932.94" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(6902.6218 2484.8794)" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">The Supreme Court </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="24">of Canada rules in </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="48">Delgamuukw v </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="72">British Columbia </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="96">that Indigenous </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="120">people have </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="144">ancestral land </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="168">rights but stops </tspan></tspan><tspan fill="#223f9a"><tspan x="0" y="192">short of declaring </tspan></tspan><tspan x="0" y="216" fill="#223f9a">Aboriginal title.</tspan><tspan x="206.44" y="216" fill="#21409a" letter-spacing="-.16em">	</tspan><tspan x="216" y="216" fill="#21409a" letter-spacing="1.49em">	</tspan></text>
        <circle cx="6888.78" cy="2478.38" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(7620.4271 598.4504)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Between 1999 and 2010, student </tspan><tspan x="0" y="24">enrolment at Canadian </tspan><tspan x="0" y="48">universities increases by 50%, </tspan><tspan x="0" y="72">partly due to natural growth </tspan><tspan x="0" y="96">and partly due to the </tspan><tspan x="0" y="120">conversion of seven colleges </tspan><tspan x="0" y="144">in British Columbia and </tspan><tspan x="0" y="168">Alberta to university status.</tspan></text>
        <circle cx="7608.35" cy="592.92" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(7596.0384 1861.9609)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">In the late 2000&apos;s </tspan><tspan x="0" y="24">mandatory retirement </tspan><tspan x="0" y="48">disappears across </tspan><tspan x="0" y="72">Canada.</tspan></text>
        <circle cx="7583.39" cy="1855.46" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(8304.1638 718.7708)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48"><tspan x="0" y="0">INTERNATIONAL </tspan><tspan x="0" y="58">STUDENT VISA CAP</tspan></text>
        <text transform="translate(8407.5067 830.3269)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">The Canadian federal </tspan><tspan x="0" y="34">government announces a </tspan><tspan x="0" y="68">two-year cap on </tspan><tspan x="0" y="102">international student </tspan><tspan x="0" y="136">permits for 2024, planning a </tspan><tspan x="0" y="170">35% reduction from 2023 </tspan><tspan x="0" y="204">figures. The actual reported </tspan><tspan x="0" y="238">figures in 2024 show a 48% </tspan><tspan x="0" y="272">drop, deepening the funding </tspan><tspan x="0" y="306">crisis for universities.</tspan></text>
        <g>
          <line x1="8350.8" y1="824.94" x2="8388.7" y2="824.94" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="8382.08 833.12 8380.71 831.65 8387.94 824.94 8380.71 818.23 8382.08 816.76 8390.87 824.94 8382.08 833.12" fill="#21409a"/>
        </g>
        <g mix-blend-mode="multiply">
          <text transform="translate(7380.5076 2262.9062)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="24" font-style="italic" font-weight="300"><tspan x="0" y="0">by 2008, most </tspan><tspan x="0" y="34">Canadian </tspan><tspan x="0" y="68">universities </tspan><tspan x="0" y="102">reduce the number </tspan><tspan x="0" y="136">of provincial </tspan><tspan x="0" y="170">exams recquired </tspan><tspan x="0" y="204">for entry from </tspan><tspan x="0" y="238">four to just one: </tspan><tspan x="0" y="272">English 12.</tspan></text>
        </g>
        <g>
          <line x1="7312.81" y1="2258.25" x2="7350.71" y2="2258.25" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="7344.09 2266.42 7342.72 2264.96 7349.94 2258.25 7342.72 2251.53 7344.09 2250.07 7352.88 2258.25 7344.09 2266.42" fill="#21409a"/>
        </g>
        <text transform="translate(7277.6604 2161.9814)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" font-variation-settings="&apos;wght&apos; 300" mix-blend-mode="multiply"><tspan x="0" y="0">RACE TO THE </tspan><tspan x="0" y="58">BOTTOM</tspan></text>
        <text transform="translate(8128.3323 1938.2673)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300"><tspan x="0" y="0">In July 2020, the </tspan><tspan x="0" y="24">amount of student loans </tspan><tspan x="0" y="48">owed to the Government </tspan><tspan x="0" y="72">of Canada surpasses </tspan><tspan x="0" y="96">$22.3 billion —more </tspan><tspan x="0" y="120">that the debt of some </tspan><tspan x="0" y="144">provinces.</tspan></text>
        <text transform="translate(7867.1766 1500.2507)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300"><tspan font-size="24"><tspan x="0" y="0">The New York Times declares 2012 the </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">year of the MOOC. A Udacity </tspan></tspan><tspan font-size="24"><tspan x="0" y="68">representative predicts that they </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">will disrupt how faculty are </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">recruited, trained, and paid, with </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">the most popular “compensated like a </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">TV actor or a movie actor.”</tspan></tspan></text>
        <text transform="translate(7772.259 1449.2043)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" font-variation-settings="&apos;wght&apos; 300"><tspan x="0" y="0">THE YEAR OF THE MOOC</tspan></text>
        <text transform="translate(6846.4857 3674.9814)" fill="#a57e2d" font-family="DazzleUnicase-Light, &apos;Dazzle Unicase&apos;" font-size="120" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">2000</tspan></text>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2497.34" x2="7045.53" y2="2493.82" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2518.89" x2="7045.53" y2="2515.37" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2541.72" x2="7045.53" y2="2538.2" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2567.16" x2="7045.53" y2="2563.64" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2585.2" x2="7045.53" y2="2581.68" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2598.54" x2="7045.53" y2="2595.02" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2613.98" x2="7045.53" y2="2610.46" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2637.78" x2="7045.53" y2="2634.25" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2664.42" x2="7045.53" y2="2660.9" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2687.91" x2="7045.53" y2="2684.39" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2032.49" x2="7045.53" y2="2028.97" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2056.71" x2="7045.53" y2="2053.18" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7045.53" y1="2068.35" x2="7045.53" y2="2064.82" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g opacity=".8">
          <path d="M6757.73,1395.4c25.77-.51,396.04-5.49,498.98-7.49,6.92.03,15.67-1.42,23.28-2.38,8.4-1.02,16.23-3.63,24.2-7.02,8.16-3.27,16.1-6.8,23.39-11.69,6.22-4.13,12.57-8.01,17.86-13,4.31-4.08,8.18-9.24,12.11-14.41,5.96-8.1,11.99-16.18,16.25-25.3,3.31-7.28,4.71-15.2,6.46-23.21,1.6-7.31,2.17-15.54,2.11-22.68-.01-3.99-.1-7.47-.45-9.13-.14-1.14-.78-1.97-2.01-1.88-28.8.06-357.87-.14-389.24.06-2.44.5-1.67,9-1.87,11.54-.2,9.14.82,19.79-1.97,28.89-3.67,12.48-16.07,25.82-27.34,31.25-2.89,1.37-6.01,2.39-9.1,3.36-8.8,2.66-18.1,5.59-26.75,8-17.59,4.06-148.11,4.41-165.9,7.74" fill="#f7ec12"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="834.39" x2="8652.18" y2="830.86" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="851.04" x2="8652.18" y2="847.52" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="868.35" x2="8652.18" y2="864.82" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="885.4" x2="8652.18" y2="881.88" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="904.48" x2="8652.18" y2="900.96" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="919.32" x2="8652.18" y2="915.79" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="972.06" x2="8652.18" y2="968.53" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="984.43" x2="8652.18" y2="980.91" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="1004.67" x2="8652.18" y2="1001.15" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="1019.07" x2="8652.18" y2="1015.55" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="1047.02" x2="8652.18" y2="1043.5" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="1073.36" x2="8652.18" y2="1069.84" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="1084.99" x2="8652.18" y2="1081.47" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="1111.01" x2="8652.18" y2="1107.49" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2535.38" x2="8652.18" y2="2531.85" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2550.9" x2="8652.18" y2="2547.38" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2566.5" x2="8652.18" y2="2562.97" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2576.96" x2="8652.18" y2="2573.43" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2588.16" x2="8652.18" y2="2584.63" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2604.25" x2="8652.18" y2="2600.73" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2618.24" x2="8652.18" y2="2614.72" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2633.79" x2="8652.18" y2="2630.27" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2652.01" x2="8652.18" y2="2648.49" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2672.83" x2="8652.18" y2="2669.31" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2704.83" x2="8652.18" y2="2701.3" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="8652.18" y1="2722.6" x2="8652.18" y2="2719.08" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="607.19" x2="7728.93" y2="603.67" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="630.47" x2="7728.93" y2="626.94" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="654.06" x2="7728.93" y2="650.54" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="678.81" x2="7728.93" y2="675.28" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="705.84" x2="7728.93" y2="702.32" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="730.53" x2="7728.93" y2="727" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="752.1" x2="7728.93" y2="748.58" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="1871.9" x2="7728.93" y2="1868.38" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <g mix-blend-mode="multiply">
          <line x1="7728.93" y1="1894.98" x2="7728.93" y2="1891.45" fill="none" stroke="#a57e2d" stroke-dasharray="3.52" stroke-miterlimit="10" stroke-width="3"/>
        </g>
        <rect x="8650.58" y="2681.02" width="3.2" height="4.1" fill="#a57e2d"/>
        <rect x="8650.67" y="938.9" width="3.01" height="4.1" fill="#a57e2d"/>
        <g>
          <g opacity=".8">
            <rect x="10623.52" y="451.43" width="493" height="177.37" transform="translate(-7.54 182.75) rotate(-.96)" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <rect x="10954.21" y="446.84" width="165.64" height="489.51" transform="translate(-10.06 185.58) rotate(-.96)" fill="#f7ec12"/>
          </g>
          <g opacity=".8">
            <rect x="10586.25" y="643.48" width="489.51" height="165.64" transform="translate(2779.9863 8007.7304) rotate(-45.9629)" fill="#f7ec12"/>
          </g>
        </g>
        <g mix-blend-mode="multiply" opacity=".8">
          <path d="M9003.21,1696.42c79.81,96.02,53.51,58.38,134.74,154.24l90.96-91.48,173.65,162.17v-519.78s-285.28,0-285.28,0l-123.54-116.96" fill="#f7ec12"/>
        </g>
        <g>
          <text transform="translate(9578.6107 3435.3311)" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="97" font-variation-settings="&apos;wght&apos; 300" mix-blend-mode="multiply"><tspan fill="#223f9a"><tspan x="0" y="0">futuring the public </tspan></tspan><tspan fill="#223f9a"><tspan x="26.97" y="100">university through </tspan></tspan><tspan x="350.56" y="200" fill="#223f9a">crisis</tspan><tspan x="674.15" y="200" fill="#21409a"> </tspan></text>
          <circle cx="10272.46" cy="3627.67" r="8.63" fill="#223f9a"/>
        </g>
        <text transform="translate(9278.5396 1979.5408)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" font-variation-settings="&apos;wght&apos; 300" mix-blend-mode="multiply"><tspan x="0" y="0">MASSIFICATION</tspan></text>
        <text transform="translate(9809.9073 2606.5845)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" font-variation-settings="&apos;wght&apos; 300" mix-blend-mode="multiply"><tspan x="0" y="0">TECHNOLOGY</tspan></text>
        <text transform="translate(10369.0743 2184.96)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" font-variation-settings="&apos;wght&apos; 300" mix-blend-mode="multiply"><tspan x="0" y="0">KNOWLEDGE</tspan></text>
        <text transform="translate(10589.8367 2916.2546)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" font-variation-settings="&apos;wght&apos; 300" mix-blend-mode="multiply"><tspan x="0" y="0">RESTITUTION</tspan></text>
        <text transform="translate(10042.5538 1467.3545)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" font-variation-settings="&apos;wght&apos; 300" mix-blend-mode="multiply"><tspan x="0" y="0">MARKETIZATION</tspan></text>
        <text transform="translate(9179.919 627.6528)" fill="#223f99" font-family="GroteskRemixMonospace-light, &apos;GroteskRemix Monospace&apos;" font-size="90" font-variation-settings="&apos;wght&apos; 200" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" xml:space="preserve">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;so many of the crises </tspan><tspan x="0" y="104">throughout the university’s </tspan><tspan x="0" y="208">history stem from the </tspan><tspan x="0" y="312">questions, “Who are we?” </tspan><tspan x="0" y="416">and “What are we for?”</tspan></text>
        <text transform="translate(9336.3904 3006.8203)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" font-variation-settings="&apos;wght&apos; 300" mix-blend-mode="multiply"><tspan x="0" y="0">GEOPOLITICS</tspan></text>
        <g mix-blend-mode="multiply">
          <g>
            <line x1="9226.65" y1="609.51" x2="9311.35" y2="609.51" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="6"/>
            <polygon points="9291.46 634.05 9287.37 629.65 9309.04 609.51 9287.37 589.37 9291.46 584.97 9317.85 609.51 9291.46 634.05" fill="#21409a"/>
          </g>
        </g>
        <circle cx="10020.6" cy="1448.51" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
        <circle cx="9252.66" cy="1959.22" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
        <circle cx="9311.54" cy="2989.84" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
        <circle cx="9787.06" cy="2589.08" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
        <circle cx="10567.88" cy="2897.51" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
        <circle cx="10348.34" cy="2165.55" r="11.1" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="4"/>
        <g>
          <path d="M10962.66,3681.99v16.91h-2.35v-16.91h2.35Z" fill="#223f9a"/>
          <path d="M10966.12,3690.29c0-2.27-.02-3.32-.05-3.88h2.22c.05.36.08,1.28.08,1.71.59-1.06,1.68-1.96,3.49-1.96,1.66,0,2.71.76,3.18,2.11.55-1.1,1.82-2.11,3.71-2.11s3.79,1,3.79,4.28v8.45h-2.24v-8.07c0-1.44-.47-2.71-2.18-2.71-1.86,0-2.64,1.52-2.64,3.49v7.29h-2.23v-8.18c0-1.46-.61-2.59-2.16-2.59-1.69,0-2.7,1.25-2.7,3.68v7.09h-2.26v-8.6Z" fill="#223f9a"/>
          <path d="M10994.81,3696.03c0,.86.08,2.16.19,2.86h-2.05c-.08-.42-.17-1.11-.18-1.85-.49,1.21-1.73,2.07-3.72,2.07-3.06,0-4.02-2.03-4.02-3.79,0-1.95,1.28-3.99,5.72-3.99h1.83v-1.15c0-1.15-.33-2.29-2.32-2.29-1.75,0-2.32.82-2.51,2.1h-2.22c.18-2.07,1.38-3.83,4.8-3.83,2.68,0,4.51,1.04,4.51,3.93v5.93ZM10992.63,3692.93h-1.89c-2.87,0-3.41,1.17-3.41,2.25,0,1.15.69,2.1,2.2,2.1,2.36,0,3.1-1.58,3.1-4.09v-.26Z" fill="#223f9a"/>
          <path d="M11008.16,3697.89c0,3.88-1.57,6.12-5.46,6.12s-4.84-2-5.02-3.79h2.26c.26,1.31,1.32,1.96,2.86,1.96,2.56,0,3.14-1.65,3.14-4.29v-.98c-.64,1.35-1.75,1.97-3.6,1.97-2.94,0-4.86-2.43-4.86-6.3s2.28-6.42,5.13-6.42c1.97,0,2.95.79,3.27,1.7,0-.49.07-1.18.11-1.45h2.22c-.02.6-.05,1.94-.05,3.65v7.83ZM10999.84,3692.55c0,2.76,1.17,4.38,3.07,4.38,2.29,0,3.09-1.41,3.09-4.43s-.62-4.38-2.99-4.38c-1.95,0-3.17,1.6-3.17,4.43Z" fill="#223f9a"/>
          <path d="M11011.61,3681.04h2.28v2.72h-2.28v-2.72ZM11011.61,3686.41h2.28v12.48h-2.28v-12.48Z" fill="#223f9a"/>
          <path d="M11017.37,3690.32c0-2.6-.02-3.37-.05-3.91h2.23c.04.23.1,1.36.08,1.89.51-1.09,1.65-2.14,3.64-2.14,2.37,0,3.97,1.38,3.97,4.65v8.08h-2.29v-7.7c0-1.74-.56-3.06-2.36-3.06-2.08,0-2.94,1.5-2.94,4.04v6.73h-2.28v-8.58Z" fill="#223f9a"/>
          <path d="M11039.51,3696.03c0,.86.08,2.16.19,2.86h-2.05c-.08-.42-.17-1.11-.18-1.85-.49,1.21-1.73,2.07-3.72,2.07-3.06,0-4.02-2.03-4.02-3.79,0-1.95,1.28-3.99,5.72-3.99h1.83v-1.15c0-1.15-.33-2.29-2.32-2.29-1.75,0-2.32.82-2.51,2.1h-2.22c.18-2.07,1.38-3.83,4.8-3.83,2.68,0,4.5,1.04,4.5,3.93v5.93ZM11037.34,3692.93h-1.89c-2.87,0-3.41,1.17-3.41,2.25,0,1.15.69,2.1,2.2,2.1,2.36,0,3.1-1.58,3.1-4.09v-.26Z" fill="#223f9a"/>
          <path d="M11041.17,3686.41h1.95v-3.58h2.27v3.58h2.46v1.85h-2.46v7.54c0,1.01.25,1.43,1.31,1.43.33,0,.64-.03.93-.08v1.67c-.51.18-1.27.22-1.71.22-1.93,0-2.79-.75-2.79-2.87v-7.92h-1.95v-1.85Z" fill="#223f9a"/>
          <path d="M11049.98,3681.04h2.28v2.72h-2.28v-2.72ZM11049.98,3686.41h2.28v12.48h-2.28v-12.48Z" fill="#223f9a"/>
          <path d="M11056.66,3686.41c1.6,5.09,2.67,8.5,3.04,10.3h.02c.28-1.55,2.22-7.25,3.16-10.3h2.26l-4.29,12.48h-2.48l-4.14-12.48h2.43Z" fill="#223f9a"/>
          <path d="M11068.52,3693.11c-.01,2.31.96,4.15,3.09,4.15,1.91,0,2.49-1.32,2.72-1.95h2.24c-.45,1.66-1.71,3.82-5.06,3.82-3.92,0-5.31-3.01-5.31-6.51,0-3.07,1.51-6.46,5.43-6.46s5.13,3.04,5.13,5.99c0,.09-.01.86-.02.96h-8.22ZM11074.52,3691.49c-.06-1.98-.86-3.51-2.93-3.51-2.35,0-2.92,2.1-3.02,3.51h5.95Z" fill="#223f9a"/>
          <path d="M10973.15,3719.24c0-3,.03-5.95.09-7.58h-.04c-.76,2.68-3.48,10.05-5.2,14.61h-1.47c-1.3-3.8-4.1-11.69-4.91-14.64h-.06c.12,1.82.17,5.39.17,8.1v6.54h-1.45v-15.8h2.27c1.83,5.03,4.21,11.83,4.79,13.92h.04c.3-1.32,3.11-8.86,5.02-13.92h2.23v15.8h-1.49v-7.03Z" fill="#223f9a"/>
          <path d="M10978.58,3720.77c-.02,2.63,1.13,4.46,3.27,4.46,2.03,0,2.65-1.47,2.89-2.1h1.43c-.31,1.25-1.34,3.36-4.41,3.36-3.56,0-4.67-2.95-4.67-6.02,0-2.81,1.37-5.91,4.77-5.91s4.5,2.83,4.5,5.36c0,.03,0,.81,0,.85h-7.78ZM10984.92,3719.62c-.06-2.2-.95-3.81-3.1-3.81-2.49,0-3.07,2.31-3.19,3.81h6.29Z" fill="#223f9a"/>
          <path d="M10987.35,3714.79h1.93v-3.42h1.44v3.42h2.42v1.24h-2.42v7.67c0,1.02.26,1.46,1.26,1.46.33,0,.74-.04.97-.08v1.15c-.39.15-.98.19-1.37.19-1.46,0-2.29-.54-2.29-2.36v-8.03h-1.93v-1.24Z" fill="#223f9a"/>
          <path d="M10996.35,3709.65v6.9c.57-1.17,1.75-1.98,3.51-1.98,1.52,0,3.61.77,3.61,4.1v7.61h-1.43v-7.33c0-1.95-.8-3.05-2.58-3.05-1.99,0-3.1,1.32-3.1,3.78v6.61h-1.44v-16.62h1.44Z" fill="#223f9a"/>
          <path d="M11015.71,3720.33c0,3.31-1.4,6.13-4.99,6.13-3.4,0-4.82-2.9-4.82-6.08s1.67-5.82,4.96-5.82c3.08,0,4.85,2.39,4.85,5.77ZM11007.41,3720.39c0,2.72,1.17,4.81,3.43,4.81,2.39,0,3.35-2.04,3.35-4.86,0-2.57-1.14-4.51-3.4-4.51s-3.37,1.91-3.37,4.56Z" fill="#223f9a"/>
          <path d="M11026.71,3709.65v13.71c0,1.02,0,2.19.05,2.91h-1.43c-.03-.3-.06-1.04-.06-1.82-.62,1.46-1.59,2.03-3.5,2.03-2.99,0-4.45-2.56-4.45-5.93s1.67-5.99,4.79-5.99c1.91,0,2.83.8,3.16,1.5v-6.42h1.44ZM11018.84,3720.48c0,3.03,1.39,4.7,3.26,4.7,2.66,0,3.22-2.08,3.22-4.94,0-3.46-1.08-4.38-3.09-4.38s-3.39,1.7-3.39,4.61Z" fill="#223f9a"/>
          <path d="M11030.3,3723.03c.25,1.45,1.33,2.25,2.81,2.25,1.79,0,2.43-1.01,2.43-2.08,0-1.15-.76-1.78-2.78-2.32-2.7-.72-3.45-1.72-3.45-3.22s1.08-3.09,3.65-3.09,3.67,1.52,3.82,3.23h-1.43c-.22-1.05-.76-2.04-2.46-2.04-1.48,0-2.13.74-2.13,1.79,0,.95.42,1.48,2.47,2.02,2.84.77,3.77,1.71,3.77,3.53,0,2.05-1.58,3.38-3.95,3.38-2.21,0-3.99-1.07-4.21-3.44h1.45Z" fill="#223f9a"/>
          <path d="M11045.07,3710.47h1.49v14.48h7.8l-.25,1.32h-9.05v-15.8Z" fill="#223f9a"/>
          <path d="M11064.06,3723.88c0,.8.08,1.86.18,2.39h-1.35c-.07-.42-.16-1.01-.16-1.92-.43,1.24-1.62,2.13-3.57,2.13-2.79,0-3.59-1.94-3.59-3.47s1-3.6,5.16-3.6h1.91v-1.22c0-1.15-.32-2.42-2.49-2.42-1.8,0-2.47.8-2.7,2.23h-1.42c.19-1.96,1.31-3.43,4.19-3.43,2.28,0,3.86.98,3.86,3.51v5.82ZM11062.66,3720.55h-1.98c-3.05,0-3.63,1.24-3.63,2.39,0,1.25.76,2.27,2.32,2.27,2.43,0,3.29-1.64,3.29-4.43v-.23Z" fill="#223f9a"/>
          <path d="M11067.29,3709.65h1.44v6.87c.5-.99,1.62-1.95,3.54-1.95,2.72,0,4.39,2.19,4.39,5.62s-1.41,6.29-4.72,6.29c-1.8,0-2.78-.78-3.23-1.79.02.5-.03,1.07-.07,1.59h-1.41c.02-.59.05-1.65.05-3.16v-13.47ZM11075.17,3720.24c0-2.63-1.06-4.36-3.17-4.36-2.45,0-3.35,1.57-3.35,4.48s.65,4.8,3.28,4.8c2.23,0,3.24-2.08,3.24-4.92Z" fill="#223f9a"/>
        </g>
        <path d="M11068.44,3600.83c-6.56,15.66-15.02,36.58-20.27,50l-12.31-7.47c-4.82-12.71-11.09-28.84-16.55-42.54h-8.35v27.43l-45.21-27.43h-5.57v69.55h5.57v-67.34l45.21,27.44v39.89h5.13v-29.51c0-2.29.01-4.74.03-7.26l13.12,7.96c4.11,10.9,8.25,21.68,11.02,28.8h5.43c1.85-4.62,3.93-9.78,6.09-15.13l19.36,11.75v3.38h5.56v-69.55h-8.24ZM11016.13,3631.4c.08-9.97.2-20.58-.18-26.56h.05c1.73,5.78,6.81,19.65,12.14,33.84l-12.01-7.29ZM11043.42,3663.47h-.2c-.97-2.98-3.27-9.27-6.27-17.21l10.51,6.38c-2.1,5.4-3.58,9.34-4.04,10.83ZM11052.49,3653.46c7.9-19.61,16.59-41.28,18.73-48.51h.3c-.3,6.97-.4,20-.4,33.57v26.25l-18.63-11.3Z" fill="#223f9a"/>
        <g opacity=".8">
          <polygon points="8344.29 3168.44 8058.67 2734.8 8056.93 2876.53 7975.35 2885.93 7975.35 2885.96 6746.7 2885.96 6746.7 3491.57 7975.49 3491.57 7975.49 3491.5 8060.41 3474.92 8060.41 3664.51 8344.29 3168.44" fill="#f7ec12"/>
        </g>
        <text transform="translate(7342.464 2956.9397)" fill="#21409a" font-family="GroteskRemixMonospace-regular, &apos;GroteskRemix Monospace&apos;" font-size="48" font-variation-settings="&apos;wght&apos; 300"><tspan x="0" y="0">DECLINING GOVERNMENT </tspan><tspan x="0" y="58">FUNDING</tspan></text>
        <g>
          <line x1="7377.18" y1="3044.61" x2="7415.09" y2="3044.61" fill="none" stroke="#21409a" stroke-miterlimit="10" stroke-width="2"/>
          <polygon points="7408.46 3052.79 7407.1 3051.33 7414.32 3044.61 7407.1 3037.9 7408.46 3036.43 7417.26 3044.61 7408.46 3052.79" fill="#21409a"/>
        </g>
        <text transform="translate(7437.3826 3049.7168)" fill="#21409a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-style="italic" font-weight="300"><tspan font-size="24"><tspan x="0" y="0">Provincial governments across </tspan></tspan><tspan font-size="24"><tspan x="0" y="34">Canada encourage universities </tspan></tspan><tspan font-size="24"><tspan x="0" y="68">to increase international </tspan></tspan><tspan font-size="24"><tspan x="0" y="102">enrolment as domestic numbers </tspan></tspan><tspan font-size="24"><tspan x="0" y="136">decline. Within seven years, </tspan></tspan><tspan font-size="24"><tspan x="0" y="170">international students rise to </tspan></tspan><tspan font-size="24"><tspan x="0" y="204">13% of total enrolment. Paying </tspan></tspan><tspan font-size="24"><tspan x="0" y="238">nearly four times the tuition </tspan></tspan><tspan font-size="24"><tspan x="0" y="272">of domestic students, they </tspan></tspan><tspan font-size="24"><tspan x="0" y="306">generate over one-third of all </tspan></tspan><tspan font-size="24"><tspan x="0" y="340">tuition revenue, approaching </tspan></tspan><tspan font-size="24"><tspan x="0" y="374">half in British Columbia.</tspan></tspan></text>
        <text transform="translate(8094.9505 3281.5894)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">In 2019 the Accessible Canada </tspan><tspan x="0" y="24">Act passes, introducing </tspan><tspan x="0" y="48">requirements for government </tspan><tspan x="0" y="72">Institutions.</tspan></text>
        <circle cx="8081.49" cy="3275.09" r="5.96" fill="none" stroke="#21409a" stroke-miterlimit="10"/>
        <text transform="translate(8316.5521 3087.1375)" fill="#223f9a" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="16" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0">Between 2001 and 2023, </tspan><tspan x="0" y="24">the Canadian average for </tspan><tspan x="0" y="48">university tuition more </tspan><tspan x="0" y="72">than doubles.</tspan></text>
      </g>
      <g
        class="questionnaire knowledge-questionnaire"
        transform="translate(1800, 2300)"
        @click="() => useDisplayStore().showKnowledgeQuestionnaireModal()"
      >
        <title>Click to fill out the knowledge questionnaire</title>
        <g class="questionnaire-paper">
          <image href="../assets/knowledge-questionnaire.svg" width="300" height="800" />
        </g>
        <g class="questionnaire-paper">
          <image href="../assets/knowledge-questionnaire.svg" width="300" height="800" />
        </g>
        <g class="questionnaire-paper">
          <image href="../assets/knowledge-questionnaire.svg" width="300" height="800" />
        </g>
        <g class="questionnaire-paper">
          <image href="../assets/knowledge-questionnaire.svg" width="300" height="800" />
        </g>
        <g class="questionnaire-paper">
          <image href="../assets/knowledge-questionnaire.svg" width="300" height="800" />
        </g>
        <g transform="translate(142, 10)" width="16" height="16" fill="red" class="bi bi-pin-angle-fill" viewBox="0 0 16 16">
          <path d="M9.828.722a.5.5 0 0 1 .354.146l4.95 4.95a.5.5 0 0 1 0 .707c-.48.48-1.072.588-1.503.588-.177 0-.335-.018-.46-.039l-3.134 3.134a6 6 0 0 1 .16 1.013c.046.702-.032 1.687-.72 2.375a.5.5 0 0 1-.707 0l-2.829-2.828-3.182 3.182c-.195.195-1.219.902-1.414.707s.512-1.22.707-1.414l3.182-3.182-2.828-2.829a.5.5 0 0 1 0-.707c.688-.688 1.673-.767 2.375-.72a6 6 0 0 1 1.013.16l3.134-3.133a3 3 0 0 1-.04-.461c0-.43.108-1.022.589-1.503a.5.5 0 0 1 .353-.146"/>
        </g>
      </g>
      <g
        class="responses knowledge-responses"
        transform="translate(10650, 1800)"
        @click="() => useDisplayStore().showKnowledgeResponsesModal()"
      >
        <title>Click to view the knowledge takeaways</title>
        <g class="responses-paper">
          <image href="../assets/knowledge-questionnaire.svg" width="300" height="800" />
        </g>
        <g class="responses-paper">
          <image href="../assets/knowledge-questionnaire.svg" width="300" height="800" />
        </g>
        <g class="responses-paper">
          <image href="../assets/knowledge-questionnaire.svg" width="300" height="800" />
        </g>
        <g class="responses-paper">
          <image href="../assets/knowledge-questionnaire.svg" width="300" height="800" />
        </g>
        <g class="responses-paper">
          <image href="../assets/knowledge-questionnaire.svg" width="300" height="800" />
        </g>
        <g transform="translate(142, 10)" width="16" height="16" fill="red" class="bi bi-pin-angle-fill" viewBox="0 0 16 16">
          <path d="M9.828.722a.5.5 0 0 1 .354.146l4.95 4.95a.5.5 0 0 1 0 .707c-.48.48-1.072.588-1.503.588-.177 0-.335-.018-.46-.039l-3.134 3.134a6 6 0 0 1 .16 1.013c.046.702-.032 1.687-.72 2.375a.5.5 0 0 1-.707 0l-2.829-2.828-3.182 3.182c-.195.195-1.219.902-1.414.707s.512-1.22.707-1.414l3.182-3.182-2.828-2.829a.5.5 0 0 1 0-.707c.688-.688 1.673-.767 2.375-.72a6 6 0 0 1 1.013.16l3.134-3.133a3 3 0 0 1-.04-.461c0-.43.108-1.022.589-1.503a.5.5 0 0 1 .353-.146"/>
        </g>
      </g>
    </g>
  </svg>
</template>

<style scoped>
svg {
  cursor: grab;
  user-select: none;
  &.grabbing {
    cursor: grabbing;
  }

  text {
    cursor: text;
    user-select: all;
    a {
      cursor: pointer;
    }
  }

  .questionnaire,
  .responses {
    .bi.bi-pin-angle-fill {
      filter: drop-shadow(3px 5px 2px rgb(0 0 0 / 0.4));
    }
    .responses-paper,
    .questionnaire-paper {
      cursor: pointer;
      transition: all 0.8s ease-out;
      filter: drop-shadow(3px 5px 2px rgb(0 0 0 / 0.4));
      transform-origin: center -5%;
      &:nth-child(2) {
        transform: rotate(-1.5deg);
      }
      &:nth-child(3) {
        transform: rotate(-1deg);
      }
      &:nth-child(4) {
        transform: rotate(-0.5deg);
      }
      &:nth-child(5) {
        transform: rotate(0deg);
      }
      &:nth-child(6) {
        transform: rotate(0.5deg);
      }
    }
    &:hover {
      .questionnaire-paper {
        &:nth-child(2) {
          transform: rotate(-1.6deg);
        }
        &:nth-child(3) {
          transform: rotate(-1.1deg);
        }
        &:nth-child(4) {
          transform: rotate(-0.6deg);
        }
        &:nth-child(5) {
          transform: rotate(-0.2deg);
        }
        &:nth-child(6) {
          transform: rotate(-5deg);
        }
      }
      .responses-paper {
        &:nth-child(2) {
          transform: rotate(-1.4deg);
        }
        &:nth-child(3) {
          transform: rotate(-0.9deg);
        }
        &:nth-child(4) {
          transform: rotate(-0.4deg);
        }
        &:nth-child(5) {
          transform: rotate(0.2deg);
        }
        &:nth-child(6) {
          transform: rotate(0.8deg);
        }
      }
    }
  }
}
</style>