<script setup>
import BackgroundImageUrl from '../assets/img/restitution-background.png'
import { vMaska } from 'maska/vue'
const props = defineProps({
  showContent: {
    type: Boolean,
    default: true,
  },
  editMode: {
    type: Boolean,
    default: false,
  },
  object: {
    type: Object,
    default: {},
  }
})
</script>

<template>
  <svg xmlns="http://www.w3.org/2000/svg" width="100%" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 288 634">
    <rect width="100%" height="100%" fill="white" stroke="black" />
    <defs>
      <clipPath id="b">
        <polyline points="-.68 118.56 288.68 118.56 288.68 648 -.68 648 -.68 118.56" fill="none"/>
      </clipPath>
      <clipPath id="c">
        <polyline points="-323.32 118.56 288.68 118.56 288.68 648 -323.32 648 -323.32 118.56" fill="none"/>
      </clipPath>
      <clipPath id="d">
        <polyline points="288.68 118.56 -.68 118.56 -.68 648 288.68 648 288.68 118.56" fill="none"/>
      </clipPath>
    </defs>
    <g isolation="isolate">
      <g id="a" data-name="Layer 1">
        <g clip-path="url(#b)">
          <g clip-path="url(#c)">
            <g clip-path="url(#d)">
              <image width="1208" height="2208" transform="translate(-1 118.32) scale(.24)" :href="BackgroundImageUrl" />
            </g>
          </g>
        </g>
        <rect y="118.56" width="288" height="529.44" fill="none"/>
        <g>
          <g>
            <path d="M101.55,44.06h7v1.4h-5.46v8.26h4.76v1.4h-6.3v-11.07Z" fill="#231f20"/>
            <path d="M116.82,55.13h-1.85l-3.47-4.9v4.9h-1.54v-11.07h6.3v6.16h-2.98l3.54,4.9ZM111.49,48.82h3.22v-3.36h-3.22v3.36Z" fill="#231f20"/>
            <path d="M122.21,45.46v8.26h2.8v1.4h-7.14v-1.4h2.8v-8.26h-2.8v-1.4h7.14v1.4h-2.8Z" fill="#231f20"/>
            <path d="M126.75,53.74h4.76v-3.77h-4.76v-5.91h7v1.4h-5.46v3.11h4.76v6.57h-6.3v-1.4Z" fill="#231f20"/>
            <path d="M139.01,45.46v8.26h2.8v1.4h-7.14v-1.4h2.8v-8.26h-2.8v-1.4h7.14v1.4h-2.8Z" fill="#231f20"/>
            <path d="M143.55,53.74h4.76v-3.77h-4.76v-5.91h7v1.4h-5.46v3.11h4.76v6.57h-6.3v-1.4Z" fill="#231f20"/>
            <path d="M159.93,49.59c0-3.46,1.36-5.67,3.5-5.67s3.5,2.21,3.5,5.67-1.36,5.67-3.5,5.67-3.5-2.21-3.5-5.67ZM165.39,49.59c0-2.6-.77-4.27-1.96-4.27s-1.96,1.67-1.96,4.27.77,4.27,1.96,4.27,1.96-1.67,1.96-4.27Z" fill="#231f20"/>
            <path d="M168.75,44.06h6.3v1.4h-4.76v3.15h4.76v1.4h-4.76v5.11h-1.54v-11.07Z" fill="#231f20"/>
            <path d="M89.1,76.73h-2.38l-4.47-6.3v6.3h-1.98v-14.22h8.1v7.92h-3.84l4.56,6.3ZM82.25,68.62h4.14v-4.32h-4.14v4.32Z" fill="#231f20"/>
            <path d="M91.07,62.5h7.92v1.8h-5.94v4.05h5.94v1.8h-5.94v4.77h5.94v1.8h-7.92v-14.22Z" fill="#231f20"/>
            <path d="M101.87,74.94h6.12v-4.84h-6.12v-7.6h9v1.8h-7.02v4h6.12v8.44h-8.1v-1.8Z" fill="#231f20"/>
            <path d="M115.64,64.3h-4.05v-1.8h10.08v1.8h-4.05v12.42h-1.98v-12.42Z" fill="#231f20"/>
            <path d="M128.42,64.3v10.62h3.6v1.8h-9.18v-1.8h3.6v-10.62h-3.6v-1.8h9.18v1.8h-3.6Z" fill="#231f20"/>
            <path d="M137.24,64.3h-4.05v-1.8h10.08v1.8h-4.05v12.42h-1.98v-12.42Z" fill="#231f20"/>
            <path d="M145.07,62.5h1.98v12.42h3.96v-12.42h1.98v14.22h-7.92v-14.22Z" fill="#231f20"/>
            <path d="M158.84,64.3h-4.05v-1.8h10.08v1.8h-4.05v12.42h-1.98v-12.42Z" fill="#231f20"/>
            <path d="M171.62,64.3v10.62h3.6v1.8h-9.18v-1.8h3.6v-10.62h-3.6v-1.8h9.18v1.8h-3.6Z" fill="#231f20"/>
            <path d="M176.93,69.61c0-4.45,1.75-7.29,4.5-7.29s4.5,2.84,4.5,7.29-1.75,7.29-4.5,7.29-4.5-2.84-4.5-7.29ZM183.95,69.61c0-3.35-.99-5.49-2.52-5.49s-2.52,2.14-2.52,5.49.99,5.49,2.52,5.49,2.52-2.14,2.52-5.49Z" fill="#231f20"/>
            <path d="M188.27,62.5h2.81l3.13,10.88v-10.88h1.98v14.22h-2.81l-3.13-10.88v10.88h-1.98v-14.22Z" fill="#231f20"/>
          </g>
          <text transform="translate(107.86 95.33)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="8" font-weight="300" letter-spacing="-.03em"><tspan x="0" y="0">How does the university </tspan><tspan x="0" y="9.5">redress historic forms of </tspan><tspan x="0" y="19">discrimination and </tspan><tspan x="0" y="28.5">exclusion?</tspan></text>
          <text transform="translate(18.23 149.9)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="9" font-style="italic" font-weight="300" letter-spacing="-.13em" mix-blend-mode="multiply"><tspan x="0" y="0">At times, the university must face the </tspan><tspan x="0" y="10.8">injustices it perpetuates. This crisis of </tspan><tspan x="0" y="21.6">accountability forces it to confront </tspan><tspan x="0" y="32.4">internal dissent and public scrutiny </tspan><tspan x="0" y="43.2">alike, laying bare the gap between its </tspan><tspan x="0" y="54">professed values and its actions.</tspan></text>
          <text transform="translate(18.23 247.99)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" letter-spacing="-.04em">i</tspan><tspan x="6.48" y="0" letter-spacing="-.03em">n </tspan><tspan x="19.69" y="0" letter-spacing="-.04em">t</tspan><tspan x="26.12" y="0" letter-spacing="-.01em">h</tspan><tspan x="32.86" y="0" letter-spacing="-.03em">e </tspan><tspan x="46.07" y="0" letter-spacing="-.03em">y</tspan><tspan x="52.61" y="0" letter-spacing="-.01em">e</tspan><tspan x="59.34" y="0" letter-spacing="-.03em">a</tspan><tspan x="65.87" y="0" letter-spacing="-.03em">r</tspan></text>
          <text transform="translate(18.23 311.31)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" letter-spacing="-.14em">W</tspan><tspan x="5.61" y="0" letter-spacing="-.15em">h</tspan><tspan x="11.08" y="0" letter-spacing="-.17em">a</tspan><tspan x="16.37" y="0" letter-spacing="-.15em">t </tspan><tspan x="27.33" y="0" letter-spacing="-.16em">i</tspan><tspan x="32.68" y="0" letter-spacing="-.18em">n</tspan><tspan x="37.87" y="0" letter-spacing="-.17em">j</tspan><tspan x="43.14" y="0" letter-spacing="-.16em">u</tspan><tspan x="48.57" y="0" letter-spacing="-.15em">s</tspan><tspan x="54.01" y="0" letter-spacing="-.16em">t</tspan><tspan x="59.39" y="0" letter-spacing="-.17em">i</tspan><tspan x="64.65" y="0" letter-spacing="-.12em">c</tspan><tspan x="70.37" y="0" letter-spacing="-.15em">e </tspan><tspan x="81.33" y="0" letter-spacing="-.13em">w</tspan><tspan x="86.95" y="0" letter-spacing="-.15em">i</tspan><tspan x="92.44" y="0" letter-spacing="-.15em">ll </tspan><tspan x="108.88" y="0" letter-spacing="-.17em">t</tspan><tspan x="114.19" y="0" letter-spacing="-.14em">h</tspan><tspan x="119.8" y="0" letter-spacing="-.15em">e </tspan><tspan x="130.76" y="0" letter-spacing="-.15em">u</tspan><tspan x="136.22" y="0" letter-spacing="-.16em">n</tspan><tspan x="141.63" y="0" letter-spacing="-.23em">i</tspan><tspan x="146.37" y="0" letter-spacing="-.16em">v</tspan><tspan x="151.77" y="0" letter-spacing="-.17em">e</tspan><tspan x="157.1" y="0" letter-spacing="-.16em">r</tspan><tspan x="162.52" y="0" letter-spacing="-.16em">s</tspan><tspan x="167.88" y="0" letter-spacing="-.23em">i</tspan><tspan x="172.68" y="0" letter-spacing="-.14em">t</tspan><tspan x="178.24" y="0" letter-spacing="-.15em">y </tspan><tspan x="189.2" y="0" letter-spacing="-.13em">b</tspan><tspan x="194.87" y="0" letter-spacing="-.15em">e </tspan><tspan x="205.84" y="0" letter-spacing="-.16em">f</tspan><tspan x="211.19" y="0" letter-spacing="-.16em">o</tspan><tspan x="216.56" y="0" letter-spacing="-.17em">r</tspan><tspan x="221.86" y="0" letter-spacing="-.12em">c</tspan><tspan x="227.58" y="0" letter-spacing="-.14em">e</tspan><tspan x="233.17" y="0" letter-spacing="-.15em">d </tspan><tspan x="0" y="10" letter-spacing="-.18em">t</tspan><tspan x="5.24" y="10" letter-spacing="-.15em">o </tspan><tspan x="16.2" y="10" letter-spacing="-.14em">ad</tspan><tspan x="27.31" y="10" letter-spacing="-.17em">d</tspan><tspan x="32.59" y="10" letter-spacing="-.17em">r</tspan><tspan x="37.9" y="10" letter-spacing="-.14em">e</tspan><tspan x="43.49" y="10" letter-spacing="-.15em">s</tspan><tspan x="48.96" y="10" letter-spacing="-.22em">s</tspan><tspan x="53.8" y="10" letter-spacing="-.15em">?</tspan></text>
          <g mix-blend-mode="multiply">
            <text transform="translate(38.94 336.57)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="8" font-style="italic" font-weight="300"><tspan x="0" y="0" letter-spacing="-.16em">w</tspan><tspan x="4.81" y="0" letter-spacing="-.18em">h</tspan><tspan x="9.46" y="0" letter-spacing="-.2em">a</tspan><tspan x="13.97" y="0" letter-spacing="-.2em">t </tspan><tspan x="22.91" y="0" letter-spacing="-.21em">s</tspan><tspan x="27.3" y="0" letter-spacing="-.23em">t</tspan><tspan x="31.57" y="0" letter-spacing="-.21em">r</tspan><tspan x="35.99" y="0" letter-spacing="-.2em">a</tspan><tspan x="40.5" y="0" letter-spacing="-.2em">t</tspan><tspan x="44.95" y="0" letter-spacing="-.16em">e</tspan><tspan x="49.73" y="0" letter-spacing="-.18em">g</tspan><tspan x="54.37" y="0" letter-spacing="-.24em">i</tspan><tspan x="58.49" y="0" letter-spacing="-.18em">e</tspan><tspan x="63.1" y="0" letter-spacing="-.2em">s </tspan><tspan x="72.05" y="0" letter-spacing="-.18em">a</tspan><tspan x="76.64" y="0" letter-spacing="-.18em">n</tspan><tspan x="81.29" y="0" letter-spacing="-.2em">d </tspan><tspan x="90.23" y="0" letter-spacing="-.22em">t</tspan><tspan x="94.58" y="0" letter-spacing="-.18em">a</tspan><tspan x="99.22" y="0" letter-spacing="-.21em">c</tspan><tspan x="103.6" y="0" letter-spacing="-.2em">t</tspan><tspan x="108.07" y="0" letter-spacing="-.24em">i</tspan><tspan x="112.19" y="0" letter-spacing="-.17em">c</tspan><tspan x="116.9" y="0" letter-spacing="-.2em">s </tspan><tspan x="125.85" y="0" letter-spacing="-.17em">w</tspan><tspan x="130.54" y="0" letter-spacing="-.19em">i</tspan><tspan x="135.09" y="0" letter-spacing="-.19em">l</tspan><tspan x="139.63" y="0" letter-spacing="-.2em">l </tspan><tspan x="148.58" y="0" letter-spacing="-.17em">e</tspan><tspan x="153.25" y="0" letter-spacing="-.19em">n</tspan><tspan x="157.81" y="0" letter-spacing="-.18em">s</tspan><tspan x="162.44" y="0" letter-spacing="-.2em">u</tspan><tspan x="166.88" y="0" letter-spacing="-.19em">r</tspan><tspan x="171.41" y="0" letter-spacing="-.2em">e </tspan><tspan x="180.35" y="0" letter-spacing="-.2em">t</tspan><tspan x="184.79" y="0" letter-spacing="-.18em">h</tspan><tspan x="189.44" y="0" letter-spacing="-.2em">a</tspan><tspan x="193.94" y="0" letter-spacing="-.2em">t </tspan><tspan x="202.89" y="0" letter-spacing="-.2em">t</tspan><tspan x="207.32" y="0" letter-spacing="-.18em">h</tspan><tspan x="211.94" y="0" letter-spacing="-.2em">e </tspan><tspan x="0" y="9.6" letter-spacing="-.19em">u</tspan><tspan x="4.59" y="9.6" letter-spacing="-.2em">n</tspan><tspan x="9.08" y="9.6" letter-spacing="-.27em">i</tspan><tspan x="12.96" y="9.6" letter-spacing="-.18em">v</tspan><tspan x="17.62" y="9.6" letter-spacing="-.2em">e</tspan><tspan x="22.13" y="9.6" letter-spacing="-.18em">r</tspan><tspan x="26.78" y="9.6" letter-spacing="-.2em">s</tspan><tspan x="31.23" y="9.6" letter-spacing="-.27em">i</tspan><tspan x="35.11" y="9.6" letter-spacing="-.18em">t</tspan><tspan x="39.71" y="9.6" letter-spacing="-.2em">y </tspan><tspan x="48.65" y="9.6" letter-spacing="-.22em">i</tspan><tspan x="52.99" y="9.6" letter-spacing="-.2em">s </tspan><tspan x="61.93" y="9.6" letter-spacing="-.18em">h</tspan><tspan x="66.55" y="9.6" letter-spacing="-.19em">e</tspan><tspan x="71.12" y="9.6" letter-spacing="-.22em">l</tspan><tspan x="75.43" y="9.6" letter-spacing="-.2em">d to </tspan><tspan x="97.79" y="9.6" letter-spacing="-.18em">a</tspan><tspan x="102.42" y="9.6" letter-spacing="-.15em">c</tspan><tspan x="107.27" y="9.6" letter-spacing="-.15em">c</tspan><tspan x="112.11" y="9.6" letter-spacing="-.18em">o</tspan><tspan x="116.76" y="9.6" letter-spacing="-.19em">u</tspan><tspan x="121.35" y="9.6" letter-spacing="-.21em">n</tspan><tspan x="125.71" y="9.6" letter-spacing="-.27em">t</tspan><tspan x="129.62" y="9.6" letter-spacing="-.2em">?</tspan></text>
          </g>
          <text transform="translate(18.94 483.09)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" letter-spacing="-.21em">H</tspan><tspan x="4.9" y="0" letter-spacing="-.2em">o</tspan><tspan x="9.94" y="0" letter-spacing="-.22em">w </tspan><tspan x="19.64" y="0" letter-spacing="-.2em">w</tspan><tspan x="24.63" y="0" letter-spacing="-.22em">i</tspan><tspan x="29.49" y="0" letter-spacing="-.22em">ll </tspan><tspan x="44.04" y="0" letter-spacing="-.24em">t</tspan><tspan x="48.72" y="0" letter-spacing="-.23em">h</tspan><tspan x="53.5" y="0" letter-spacing="-.22em">i</tspan><tspan x="58.35" y="0" letter-spacing="-.22em">s </tspan><tspan x="68.05" y="0" letter-spacing="-.24em">r</tspan><tspan x="72.73" y="0" letter-spacing="-.21em">e</tspan><tspan x="77.69" y="0" letter-spacing="-.22em">s</tspan><tspan x="82.51" y="0" letter-spacing="-.23em">t</tspan><tspan x="87.25" y="0" letter-spacing="-.3em">i</tspan><tspan x="91.42" y="0" letter-spacing="-.23em">t</tspan><tspan x="96.14" y="0" letter-spacing="-.23em">u</tspan><tspan x="100.94" y="0" letter-spacing="-.23em">t</tspan><tspan x="105.69" y="0" letter-spacing="-.25em">i</tspan><tspan x="110.3" y="0" letter-spacing="-.21em">o</tspan><tspan x="115.23" y="0" letter-spacing="-.22em">n </tspan><tspan x="124.93" y="0" letter-spacing="-.26em">t</tspan><tspan x="129.42" y="0" letter-spacing="-.21em">r</tspan><tspan x="134.33" y="0" letter-spacing="-.21em">a</tspan><tspan x="139.29" y="0" letter-spacing="-.22em">n</tspan><tspan x="144.13" y="0" letter-spacing="-.23em">s</tspan><tspan x="148.89" y="0" letter-spacing="-.23em">f</tspan><tspan x="153.62" y="0" letter-spacing="-.23em">o</tspan><tspan x="158.36" y="0" letter-spacing="-.21em">r</tspan><tspan x="163.29" y="0" letter-spacing="-.22em">m </tspan><tspan x="173" y="0" letter-spacing="-.24em">t</tspan><tspan x="177.68" y="0" letter-spacing="-.21em">h</tspan><tspan x="182.66" y="0" letter-spacing="-.22em">e </tspan><tspan x="192.36" y="0" letter-spacing="-.22em">u</tspan><tspan x="197.19" y="0" letter-spacing="-.23em">n</tspan><tspan x="201.97" y="0" letter-spacing="-.3em">i</tspan><tspan x="206.08" y="0" letter-spacing="-.23em">v</tspan><tspan x="210.85" y="0" letter-spacing="-.24em">e</tspan><tspan x="215.55" y="0" letter-spacing="-.23em">r</tspan><tspan x="220.34" y="0" letter-spacing="-.23em">s</tspan><tspan x="225.07" y="0" letter-spacing="-.3em">i</tspan><tspan x="229.24" y="0" letter-spacing="-.21em">t</tspan><tspan x="234.17" y="0" letter-spacing="-.28em">y</tspan><tspan x="238.51" y="0" letter-spacing="-.22em">?</tspan></text>
          <g>
            <line x1="80.19" y1="93.94" x2="101.23" y2="93.94" fill="none" stroke="#231f20" stroke-miterlimit="10"/>
            <polygon points="97.92 98.03 97.24 97.3 100.85 93.95 97.24 90.59 97.92 89.86 102.32 93.95 97.92 98.03" fill="#231f20"/>
          </g>
          <g mix-blend-mode="multiply">
            <line x1="70" y1="288.8" x2="166" y2="288.8" fill="none" stroke="#231f20" stroke-dasharray="6 3" stroke-miterlimit="10" stroke-width=".75"/>
          </g>
          <g>
            <text transform="translate(38.23 498.27)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="8" font-style="italic" font-weight="300" mix-blend-mode="multiply"><tspan x="0" y="0" letter-spacing="-.2em">i</tspan><tspan x="4.45" y="0" letter-spacing="-.2em">n </tspan><tspan x="13.4" y="0" letter-spacing="-.16em">w</tspan><tspan x="18.21" y="0" letter-spacing="-.18em">h</tspan><tspan x="22.86" y="0" letter-spacing="-.2em">a</tspan><tspan x="27.36" y="0" letter-spacing="-.2em">t </tspan><tspan x="36.31" y="0" letter-spacing="-.16em">w</tspan><tspan x="41.14" y="0" letter-spacing="-.19em">a</tspan><tspan x="45.66" y="0" letter-spacing="-.17em">y</tspan><tspan x="50.33" y="0" letter-spacing="-.2em">s </tspan><tspan x="59.28" y="0" letter-spacing="-.17em">w</tspan><tspan x="63.97" y="0" letter-spacing="-.19em">i</tspan><tspan x="68.52" y="0" letter-spacing="-.19em">l</tspan><tspan x="73.06" y="0" letter-spacing="-.2em">l </tspan><tspan x="82.01" y="0" letter-spacing="-.2em">t</tspan><tspan x="86.44" y="0" letter-spacing="-.18em">h</tspan><tspan x="91.06" y="0" letter-spacing="-.2em">e </tspan><tspan x="100.01" y="0" letter-spacing="-.19em">u</tspan><tspan x="104.59" y="0" letter-spacing="-.2em">n</tspan><tspan x="109.09" y="0" letter-spacing="-.27em">i</tspan><tspan x="112.97" y="0" letter-spacing="-.18em">v</tspan><tspan x="117.63" y="0" letter-spacing="-.2em">e</tspan><tspan x="122.14" y="0" letter-spacing="-.18em">r</tspan><tspan x="126.79" y="0" letter-spacing="-.2em">s</tspan><tspan x="131.24" y="0" letter-spacing="-.27em">i</tspan><tspan x="135.12" y="0" letter-spacing="-.18em">t</tspan><tspan x="139.72" y="0" letter-spacing="-.2em">y </tspan><tspan x="148.66" y="0" letter-spacing="-.16em">m</tspan><tspan x="153.43" y="0" letter-spacing="-.18em">a</tspan><tspan x="158.06" y="0" letter-spacing="-.2em">k</tspan><tspan x="162.56" y="0" letter-spacing="-.2em">e </tspan><tspan x="171.5" y="0" letter-spacing="-.27em">i</tspan><tspan x="175.38" y="0" letter-spacing="-.19em">t</tspan><tspan x="179.94" y="0" letter-spacing="-.18em">s</tspan><tspan x="184.58" y="0" letter-spacing="-.19em">e</tspan><tspan x="189.14" y="0" letter-spacing="-.21em">l</tspan><tspan x="193.55" y="0" letter-spacing="-.2em">f </tspan><tspan x="0" y="9.6" letter-spacing="-.18em">a</tspan><tspan x="4.63" y="9.6" letter-spacing="-.15em">c</tspan><tspan x="9.48" y="9.6" letter-spacing="-.15em">c</tspan><tspan x="14.33" y="9.6" letter-spacing="-.18em">o</tspan><tspan x="18.97" y="9.6" letter-spacing="-.19em">u</tspan><tspan x="23.56" y="9.6" letter-spacing="-.21em">n</tspan><tspan x="27.92" y="9.6" letter-spacing="-.22em">t</tspan><tspan x="32.27" y="9.6" letter-spacing="-.18em">a</tspan><tspan x="36.9" y="9.6" letter-spacing="-.19em">b</tspan><tspan x="41.42" y="9.6" letter-spacing="-.24em">l</tspan><tspan x="45.54" y="9.6" letter-spacing="-.2em">e to </tspan><tspan x="67.9" y="9.6" letter-spacing="-.2em">t</tspan><tspan x="72.33" y="9.6" letter-spacing="-.2em">h</tspan><tspan x="76.83" y="9.6" letter-spacing="-.22em">i</tspan><tspan x="81.17" y="9.6" letter-spacing="-.2em">s </tspan><tspan x="90.11" y="9.6" letter-spacing="-.2em">i</tspan><tspan x="94.57" y="9.6" letter-spacing="-.24em">n</tspan><tspan x="98.73" y="9.6" letter-spacing="-.21em">j</tspan><tspan x="103.13" y="9.6" letter-spacing="-.19em">u</tspan><tspan x="107.68" y="9.6" letter-spacing="-.21em">s</tspan><tspan x="112.07" y="9.6" letter-spacing="-.2em">t</tspan><tspan x="116.54" y="9.6" letter-spacing="-.24em">i</tspan><tspan x="120.66" y="9.6" letter-spacing="-.15em">c</tspan><tspan x="125.5" y="9.6" letter-spacing="-.25em">e</tspan><tspan x="129.56" y="9.6" letter-spacing="-.2em">? </tspan><tspan x="138.51" y="9.6" letter-spacing="-.19em">H</tspan><tspan x="143.04" y="9.6" letter-spacing="-.17em">o</tspan><tspan x="147.76" y="9.6" letter-spacing="-.2em">w </tspan><tspan x="156.71" y="9.6" letter-spacing="-.19em">m</tspan><tspan x="161.29" y="9.6" letter-spacing="-.22em">i</tspan><tspan x="165.62" y="9.6" letter-spacing="-.16em">g</tspan><tspan x="170.37" y="9.6" letter-spacing="-.21em">h</tspan><tspan x="174.74" y="9.6" letter-spacing="-.2em">t </tspan><tspan x="183.68" y="9.6" letter-spacing="-.2em">t</tspan><tspan x="188.12" y="9.6" letter-spacing="-.2em">h</tspan><tspan x="192.61" y="9.6" letter-spacing="-.22em">i</tspan><tspan x="196.95" y="9.6" letter-spacing="-.2em">s </tspan><tspan x="0" y="19.2" letter-spacing="-.2em">a</tspan><tspan x="4.46" y="19.2" letter-spacing="-.18em">f</tspan><tspan x="9.13" y="19.2" letter-spacing="-.19em">f</tspan><tspan x="13.71" y="19.2" letter-spacing="-.17em">e</tspan><tspan x="18.43" y="19.2" letter-spacing="-.21em">c</tspan><tspan x="22.82" y="19.2" letter-spacing="-.2em">t </tspan><tspan x="31.76" y="19.2" letter-spacing="-.27em">i</tspan><tspan x="35.64" y="19.2" letter-spacing="-.19em">t</tspan><tspan x="40.19" y="19.2" letter-spacing="-.2em">s </tspan><tspan x="49.14" y="19.2" letter-spacing="-.19em">p</tspan><tspan x="53.66" y="19.2" letter-spacing="-.22em">l</tspan><tspan x="57.97" y="19.2" letter-spacing="-.18em">a</tspan><tspan x="62.6" y="19.2" letter-spacing="-.15em">c</tspan><tspan x="67.44" y="19.2" letter-spacing="-.2em">e </tspan><tspan x="76.39" y="19.2" letter-spacing="-.2em">o</tspan><tspan x="80.83" y="19.2" letter-spacing="-.2em">f </tspan><tspan x="89.77" y="19.2" letter-spacing="-.19em">p</tspan><tspan x="94.29" y="19.2" letter-spacing="-.19em">r</tspan><tspan x="98.84" y="19.2" letter-spacing="-.27em">i</tspan><tspan x="102.71" y="19.2" letter-spacing="-.19em">v</tspan><tspan x="107.29" y="19.2" letter-spacing="-.19em">i</tspan><tspan x="111.84" y="19.2" letter-spacing="-.24em">l</tspan><tspan x="115.95" y="19.2" letter-spacing="-.16em">e</tspan><tspan x="120.73" y="19.2" letter-spacing="-.16em">g</tspan><tspan x="125.49" y="19.2" letter-spacing="-.25em">e</tspan><tspan x="129.56" y="19.2" letter-spacing="-.2em">?</tspan></text>
            <circle cx="28.05" cy="495.08" r="3.06" fill="none" stroke="#231f20" stroke-miterlimit="10" stroke-width=".5"/>
          </g>
        </g>
      </g>
    </g>
    <foreignObject transform="translate(63 258)" width="110" height="45" v-if="showContent">
      <input
        name="year" type="number" min="2027" max="2199"
        class="form-control" required
        v-maska="{ mask: '2c##', tokens: { c: { pattern: /[01]/ } } }" placeholder="2100" inputmode="numeric"
        v-model="object.year"
        :disabled="!editMode"
        aria-describedby="yearHelp"
      />
    </foreignObject>
    <foreignObject transform="translate(18.23 247.99)" width="200" height="50" v-if="showContent && editMode">
      <div id="yearHelp" class="form-text"><i class="bi bi-info-circle"></i> Enter a year between 2027 - 2199</div>
    </foreignObject>
    <foreignObject transform="translate(9 348)" width="270" height="125" v-if="showContent">
      <textarea
        class="form-control w-100 h-100"
        name="question_1" required placeholder="Leave your response here"
        v-model="object.question_1"
        :disabled="!editMode"
      ></textarea>
    </foreignObject>
    <foreignObject transform="translate(9 518)" width="270" :height="editMode ? 100 : 110" v-if="showContent">
      <textarea
        class="form-control w-100 h-100"
        name="question_2" required placeholder="Leave your response here"
        v-model="object.question_2"
        :disabled="!editMode"
      ></textarea>
    </foreignObject>
  </svg>
</template>

<style scoped>
textarea {
  font-size: 8px;
  overflow-y: auto;
  font-family: DolphYY-Light;
  resize: none;
  padding-top: 0;
  padding-bottom: 0;
  background: transparent !important;
  box-shadow: none !important;
  scrollbar-width: thin !important;
  &:not(:focus) {
    border-color: transparent;
  }
  &:hover {
    border-color: #86b7fe;
  }
}
input {
  font-family: DazzleUnicase-Medium;
  font-size: 24px;
  background: transparent !important;
  padding-top: 0;
  padding-bottom: 0;
  box-shadow: none !important;
  &:not(:focus) {
    border-color: transparent;
  }
  &:hover {
    border-color: #86b7fe;
  }
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
input[type=number] {
  -moz-appearance: textfield;
}
.form-text {
  font-size: 8px;
}
</style>