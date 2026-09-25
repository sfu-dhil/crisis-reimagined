<script setup>
import BackgroundImageUrl from '../assets/img/marketization-background.png'
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
  <svg xmlns="http://www.w3.org/2000/svg" width="100%" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 288 648">
    <rect width="100%" height="100%" fill="white" stroke="black" />
    <defs>
      <clipPath id="b">
        <polyline points=".55 83.52 287.45 83.52 287.45 648 .55 648 .55 83.52" fill="none"/>
      </clipPath>
      <clipPath id="c">
        <polyline points="-280.34 83.52 933.58 83.52 933.58 648 -280.34 648 -280.34 83.52" fill="none"/>
      </clipPath>
      <clipPath id="d">
        <polyline points="287.45 83.52 .55 83.52 .55 648 287.45 648 287.45 83.52" fill="none"/>
      </clipPath>
    </defs>
    <rect y="83.52" width="288" height="564.48" fill="none"/>
    <g clip-path="url(#b)">
      <g clip-path="url(#c)">
        <g clip-path="url(#d)">
          <image width="1198" height="2354" transform="translate(.22 83.28) scale(.24)" :href="BackgroundImageUrl" />
        </g>
      </g>
    </g>
    <g>
      <g>
        <line x1="83.37" y1="77.57" x2="104.41" y2="77.57" fill="none" stroke="#231f20" stroke-miterlimit="10"/>
        <polygon points="101.09 81.66 100.41 80.93 104.02 77.57 100.41 74.21 101.09 73.48 105.49 77.57 101.09 81.66" fill="#231f20"/>
      </g>
      <g>
        <line x1="70" y1="275.6" x2="158" y2="275.6" fill="none" stroke="#231f20" stroke-dasharray="6 3" stroke-miterlimit="10" stroke-width=".75"/>
      </g>
      <g>
        <path d="M97.47,24.53h9v1.8h-7.02v10.62h6.12v1.8h-8.1v-14.22Z" fill="#231f20"/>
        <path d="M117.1,38.75h-2.38l-4.47-6.3v6.3h-1.98v-14.22h8.1v7.92h-3.84l4.56,6.3ZM110.25,30.65h4.14v-4.32h-4.14v4.32Z" fill="#231f20"/>
        <path d="M124.03,26.33v10.62h3.6v1.8h-9.18v-1.8h3.6v-10.62h-3.6v-1.8h9.18v1.8h-3.6Z" fill="#231f20"/>
        <path d="M129.87,36.97h6.12v-4.84h-6.12v-7.6h9v1.8h-7.02v4h6.12v8.44h-8.1v-1.8Z" fill="#231f20"/>
        <path d="M145.62,26.33v10.62h3.6v1.8h-9.18v-1.8h3.6v-10.62h-3.6v-1.8h9.18v1.8h-3.6Z" fill="#231f20"/>
        <path d="M151.47,36.97h6.12v-4.84h-6.12v-7.6h9v1.8h-7.02v4h6.12v8.44h-8.1v-1.8Z" fill="#231f20"/>
        <path d="M172.53,31.64c0-4.45,1.75-7.29,4.5-7.29s4.5,2.84,4.5,7.29-1.75,7.29-4.5,7.29-4.5-2.84-4.5-7.29ZM179.55,31.64c0-3.35-.99-5.49-2.52-5.49s-2.52,2.14-2.52,5.49.99,5.49,2.52,5.49,2.52-2.14,2.52-5.49Z" fill="#231f20"/>
        <path d="M183.87,24.53h8.1v1.8h-6.12v4.05h6.12v1.8h-6.12v6.57h-1.98v-14.22Z" fill="#231f20"/>
        <path d="M84.25,60.35h-1.98v-12.37l-1.51,4.45h-1.84l-1.51-4.45v12.37h-1.98v-14.22h3.17l1.24,3.65,1.24-3.65h3.17v14.22Z" fill="#231f20"/>
        <path d="M92.69,57.23h-4.1l-.81,3.11h-2l3.85-14.22h2.02l3.85,14.22h-2l-.81-3.11ZM92.24,55.43l-1.6-6.18-1.6,6.18h3.2Z" fill="#231f20"/>
        <path d="M106.3,60.35h-2.38l-4.47-6.3v6.3h-1.98v-14.22h8.1v7.92h-3.84l4.56,6.3ZM99.45,52.25h4.14v-4.32h-4.14v4.32Z" fill="#231f20"/>
        <path d="M112.56,52.25h3.82v8.1h-1.98v-6.3h-4.14v6.3h-1.98v-14.22h1.98v6.12l4.54-6.12h2.3l-4.54,6.12Z" fill="#231f20"/>
        <path d="M119.07,46.13h7.92v1.8h-5.94v4.05h5.94v1.8h-5.94v4.77h5.94v1.8h-7.92v-14.22Z" fill="#231f20"/>
        <path d="M132.84,47.93h-4.05v-1.8h10.08v1.8h-4.05v12.42h-1.98v-12.42Z" fill="#231f20"/>
        <path d="M145.62,47.93v10.62h3.6v1.8h-9.18v-1.8h3.6v-10.62h-3.6v-1.8h9.18v1.8h-3.6Z" fill="#231f20"/>
        <path d="M151.65,58.53l5.47-10.61h-5.47v-1.8h7.56v1.82l-5.47,10.6h5.47v1.8h-7.56v-1.82Z" fill="#231f20"/>
        <path d="M168.29,57.23h-4.11l-.81,3.11h-2l3.85-14.22h2.02l3.85,14.22h-2l-.81-3.11ZM167.84,55.43l-1.6-6.18-1.6,6.18h3.21Z" fill="#231f20"/>
        <path d="M176.04,47.93h-4.05v-1.8h10.08v1.8h-4.05v12.42h-1.98v-12.42Z" fill="#231f20"/>
        <path d="M188.82,47.93v10.62h3.6v1.8h-9.18v-1.8h3.6v-10.62h-3.6v-1.8h9.18v1.8h-3.6Z" fill="#231f20"/>
        <path d="M194.13,53.24c0-4.45,1.75-7.29,4.5-7.29s4.5,2.84,4.5,7.29-1.75,7.29-4.5,7.29-4.5-2.85-4.5-7.29ZM201.15,53.24c0-3.35-.99-5.49-2.52-5.49s-2.52,2.14-2.52,5.49.99,5.49,2.52,5.49,2.52-2.14,2.52-5.49Z" fill="#231f20"/>
        <path d="M205.47,46.13h2.81l3.13,10.88v-10.88h1.98v14.22h-2.81l-3.13-10.88v10.88h-1.98v-14.22Z" fill="#231f20"/>
      </g>
      <text transform="translate(115.15 78.96)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="8" font-weight="300" letter-spacing="-.03em"><tspan x="0" y="0">How are the university&apos;s </tspan><tspan x="0" y="9.5">intellectual freedoms </tspan><tspan x="0" y="19">threatened by creeping </tspan><tspan x="0" y="28.5">managerialism?</tspan></text>
      <text transform="translate(24.63 127.46)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="9" font-style="italic" font-weight="300" letter-spacing="-.13em"><tspan x="0" y="0">The university is under ever-increasing </tspan><tspan x="0" y="10.8">pressure to shift towards ensuring ‘value’ </tspan><tspan x="0" y="21.6">or ‘excellence’ to justify its allocation </tspan><tspan x="0" y="32.4">of resources. Is this crisis forcing the </tspan><tspan x="0" y="43.2">university to exist within its means or is </tspan><tspan x="0" y="54">it slowly undermining its ability to </tspan><tspan x="0" y="64.8">pursue knowledge?</tspan></text>
      <text transform="translate(28.19 234.64)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300"><tspan x="0" y="0" letter-spacing="-.04em">i</tspan><tspan x="6.48" y="0" letter-spacing="-.03em">n </tspan><tspan x="19.69" y="0" letter-spacing="-.04em">t</tspan><tspan x="26.12" y="0" letter-spacing="-.01em">h</tspan><tspan x="32.86" y="0" letter-spacing="-.03em">e </tspan><tspan x="46.07" y="0" letter-spacing="-.03em">y</tspan><tspan x="52.61" y="0" letter-spacing="-.01em">e</tspan><tspan x="59.34" y="0" letter-spacing="-.03em">a</tspan><tspan x="65.87" y="0" letter-spacing="-.03em">r</tspan></text>
      <text transform="translate(24.63 297.62)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300"><tspan x="0" y="0" letter-spacing="-.12em">H</tspan><tspan x="5.76" y="0" letter-spacing="-.1em">o</tspan><tspan x="11.65" y="0" letter-spacing="-.12em">w </tspan><tspan x="23.06" y="0" letter-spacing="-.11em">w</tspan><tspan x="28.91" y="0" letter-spacing="-.12em">i</tspan><tspan x="34.62" y="0" letter-spacing="-.12em">ll </tspan><tspan x="51.74" y="0" letter-spacing="-.14em">t</tspan><tspan x="57.27" y="0" letter-spacing="-.11em">h</tspan><tspan x="63.11" y="0" letter-spacing="-.12em">e </tspan><tspan x="74.52" y="0" letter-spacing="-.13em">u</tspan><tspan x="80.2" y="0" letter-spacing="-.13em">n</tspan><tspan x="85.84" y="0" letter-spacing="-.21em">i</tspan><tspan x="90.8" y="0" letter-spacing="-.13em">v</tspan><tspan x="96.43" y="0" letter-spacing="-.14em">e</tspan><tspan x="101.98" y="0" letter-spacing="-.13em">r</tspan><tspan x="107.63" y="0" letter-spacing="-.14em">s</tspan><tspan x="113.22" y="0" letter-spacing="-.2em">i</tspan><tspan x="118.24" y="0" letter-spacing="-.12em">t</tspan><tspan x="124.02" y="0" letter-spacing="-.12em">y </tspan><tspan x="135.44" y="0" letter-spacing="-.14em">r</tspan><tspan x="140.98" y="0" letter-spacing="-.11em">e</tspan><tspan x="146.79" y="0" letter-spacing="-.13em">s</tspan><tspan x="152.43" y="0" letter-spacing="-.11em">p</tspan><tspan x="158.31" y="0" letter-spacing="-.12em">o</tspan><tspan x="164.09" y="0" letter-spacing="-.11em">n</tspan><tspan x="169.91" y="0" letter-spacing="-.12em">d </tspan><tspan x="181.32" y="0" letter-spacing="-.15em">t</tspan><tspan x="186.78" y="0" letter-spacing="-.12em">o </tspan><tspan x="198.19" y="0" letter-spacing="-.14em">t</tspan><tspan x="203.73" y="0" letter-spacing="-.11em">h</tspan><tspan x="209.56" y="0" letter-spacing="-.12em">e </tspan><tspan x="0" y="10.8" letter-spacing="-.11em">p</tspan><tspan x="5.81" y="10.8" letter-spacing="-.13em">u</tspan><tspan x="11.46" y="10.8" letter-spacing="-.13em">s</tspan><tspan x="17.1" y="10.8" letter-spacing="-.12em">h </tspan><tspan x="28.52" y="10.8" letter-spacing="-.14em">f</tspan><tspan x="34.1" y="10.8" letter-spacing="-.14em">o</tspan><tspan x="39.69" y="10.8" letter-spacing="-.12em">r </tspan><tspan x="51.11" y="10.8" letter-spacing="-.23em">&apos;</tspan><tspan x="55.89" y="10.8" letter-spacing="-.12em">e</tspan><tspan x="61.61" y="10.8" letter-spacing="-.14em">x</tspan><tspan x="67.14" y="10.8" letter-spacing="-.1em">c</tspan><tspan x="73.08" y="10.8" letter-spacing="-.12em">e</tspan><tspan x="78.83" y="10.8" letter-spacing="-.12em">l</tspan><tspan x="84.53" y="10.8" letter-spacing="-.15em">l</tspan><tspan x="90.03" y="10.8" letter-spacing="-.12em">e</tspan><tspan x="95.77" y="10.8" letter-spacing="-.11em">n</tspan><tspan x="101.61" y="10.8" letter-spacing="-.1em">c</tspan><tspan x="107.55" y="10.8" letter-spacing="-.23em">e</tspan><tspan x="112.29" y="10.8" letter-spacing="-.22em">&apos;</tspan><tspan x="117.17" y="10.8" letter-spacing="-.12em">?</tspan></text>
      <text transform="translate(44.63 324.21)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="8" font-style="italic" font-weight="300"><tspan x="0" y="0" letter-spacing="-.12em">w</tspan><tspan x="5.1" y="0" letter-spacing="-.14em">i</tspan><tspan x="10.04" y="0" letter-spacing="-.14em">l</tspan><tspan x="14.98" y="0" letter-spacing="-.15em">l </tspan><tspan x="24.73" y="0" letter-spacing="-.15em">t</tspan><tspan x="29.56" y="0" letter-spacing="-.13em">h</tspan><tspan x="34.58" y="0" letter-spacing="-.15em">e </tspan><tspan x="44.33" y="0" letter-spacing="-.14em">u</tspan><tspan x="49.31" y="0" letter-spacing="-.15em">n</tspan><tspan x="54.21" y="0" letter-spacing="-.22em">i</tspan><tspan x="58.48" y="0" letter-spacing="-.13em">v</tspan><tspan x="63.55" y="0" letter-spacing="-.15em">e</tspan><tspan x="68.46" y="0" letter-spacing="-.13em">r</tspan><tspan x="73.51" y="0" letter-spacing="-.15em">s</tspan><tspan x="78.36" y="0" letter-spacing="-.22em">i</tspan><tspan x="82.64" y="0" letter-spacing="-.13em">t</tspan><tspan x="87.63" y="0" letter-spacing="-.15em">y </tspan><tspan x="97.38" y="0" letter-spacing="-.11em">e</tspan><tspan x="102.56" y="0" letter-spacing="-.12em">m</tspan><tspan x="107.69" y="0" letter-spacing="-.14em">b</tspan><tspan x="112.61" y="0" letter-spacing="-.16em">r</tspan><tspan x="117.44" y="0" letter-spacing="-.13em">a</tspan><tspan x="122.47" y="0" letter-spacing="-.1em">c</tspan><tspan x="127.71" y="0" letter-spacing="-.15em">e </tspan><tspan x="137.46" y="0" letter-spacing="-.15em">t</tspan><tspan x="142.29" y="0" letter-spacing="-.15em">h</tspan><tspan x="147.19" y="0" letter-spacing="-.17em">i</tspan><tspan x="151.93" y="0" letter-spacing="-.15em">s </tspan><tspan x="161.67" y="0" letter-spacing="-.12em">v</tspan><tspan x="166.75" y="0" letter-spacing="-.15em">a</tspan><tspan x="171.6" y="0" letter-spacing="-.17em">l</tspan><tspan x="176.29" y="0" letter-spacing="-.13em">u</tspan><tspan x="181.3" y="0" letter-spacing="-.15em">e </tspan><tspan x="191.04" y="0" letter-spacing="-.15em">o</tspan><tspan x="195.92" y="0" letter-spacing="-.15em">r </tspan><tspan x="0" y="9.6" letter-spacing="-.12em">w</tspan><tspan x="5.1" y="9.6" letter-spacing="-.14em">i</tspan><tspan x="10.04" y="9.6" letter-spacing="-.14em">l</tspan><tspan x="14.98" y="9.6" letter-spacing="-.15em">l </tspan><tspan x="24.73" y="9.6" letter-spacing="-.22em">i</tspan><tspan x="29" y="9.6" letter-spacing="-.15em">t </tspan><tspan x="38.75" y="9.6" letter-spacing="-.14em">f</tspan><tspan x="43.7" y="9.6" letter-spacing="-.15em">i</tspan><tspan x="48.55" y="9.6" letter-spacing="-.13em">n</tspan><tspan x="53.6" y="9.6" letter-spacing="-.15em">d </tspan><tspan x="63.34" y="9.6" letter-spacing="-.13em">a</tspan><tspan x="68.34" y="9.6" letter-spacing="-.15em">n </tspan><tspan x="78.08" y="9.6" letter-spacing="-.15em">a</tspan><tspan x="82.93" y="9.6" letter-spacing="-.22em">l</tspan><tspan x="87.2" y="9.6" letter-spacing="-.15em">t</tspan><tspan x="92.05" y="9.6" letter-spacing="-.15em">e</tspan><tspan x="96.96" y="9.6" letter-spacing="-.14em">r</tspan><tspan x="101.9" y="9.6" letter-spacing="-.13em">n</tspan><tspan x="106.95" y="9.6" letter-spacing="-.15em">a</tspan><tspan x="111.86" y="9.6" letter-spacing="-.15em">t</tspan><tspan x="116.72" y="9.6" letter-spacing="-.22em">i</tspan><tspan x="121" y="9.6" letter-spacing="-.13em">v</tspan><tspan x="126.07" y="9.6" letter-spacing="-.15em">e </tspan><tspan x="135.81" y="9.6" letter-spacing="-.12em">v</tspan><tspan x="140.89" y="9.6" letter-spacing="-.15em">a</tspan><tspan x="145.73" y="9.6" letter-spacing="-.17em">l</tspan><tspan x="150.43" y="9.6" letter-spacing="-.13em">u</tspan><tspan x="155.43" y="9.6" letter-spacing="-.15em">e to </tspan><tspan x="179.79" y="9.6" letter-spacing="-.13em">p</tspan><tspan x="184.86" y="9.6" letter-spacing="-.15em">u</tspan><tspan x="189.71" y="9.6" letter-spacing="-.13em">r</tspan><tspan x="194.76" y="9.6" letter-spacing="-.13em">s</tspan><tspan x="199.78" y="9.6" letter-spacing="-.13em">u</tspan><tspan x="204.79" y="9.6" letter-spacing="-.2em">e</tspan><tspan x="209.25" y="9.6" letter-spacing="-.15em">?</tspan></text>
      <text transform="translate(44.63 493.82)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="8" font-style="italic" font-weight="300"><tspan x="0" y="0" letter-spacing="-.11em">w</tspan><tspan x="5.21" y="0" letter-spacing="-.13em">h</tspan><tspan x="10.26" y="0" letter-spacing="-.15em">a</tspan><tspan x="15.17" y="0" letter-spacing="-.15em">t </tspan><tspan x="24.91" y="0" letter-spacing="-.11em">g</tspan><tspan x="30.07" y="0" letter-spacing="-.16em">o</tspan><tspan x="34.88" y="0" letter-spacing="-.13em">v</tspan><tspan x="39.95" y="0" letter-spacing="-.15em">e</tspan><tspan x="44.86" y="0" letter-spacing="-.14em">r</tspan><tspan x="49.8" y="0" letter-spacing="-.13em">n</tspan><tspan x="54.84" y="0" letter-spacing="-.13em">a</tspan><tspan x="59.84" y="0" letter-spacing="-.13em">n</tspan><tspan x="64.88" y="0" letter-spacing="-.1em">c</tspan><tspan x="70.12" y="0" letter-spacing="-.15em">e </tspan><tspan x="79.86" y="0" letter-spacing="-.12em">m</tspan><tspan x="85.01" y="0" letter-spacing="-.12em">e</tspan><tspan x="90.14" y="0" letter-spacing="-.14em">a</tspan><tspan x="95.09" y="0" letter-spacing="-.13em">s</tspan><tspan x="100.12" y="0" letter-spacing="-.15em">u</tspan><tspan x="104.97" y="0" letter-spacing="-.14em">r</tspan><tspan x="109.89" y="0" letter-spacing="-.13em">e</tspan><tspan x="114.9" y="0" letter-spacing="-.15em">s </tspan><tspan x="124.64" y="0" letter-spacing="-.15em">a</tspan><tspan x="129.5" y="0" letter-spacing="-.14em">r</tspan><tspan x="134.42" y="0" letter-spacing="-.15em">e </tspan><tspan x="144.17" y="0" letter-spacing="-.15em">i</tspan><tspan x="149.02" y="0" letter-spacing="-.15em">n </tspan><tspan x="158.77" y="0" letter-spacing="-.14em">p</tspan><tspan x="163.69" y="0" letter-spacing="-.17em">l</tspan><tspan x="168.4" y="0" letter-spacing="-.13em">a</tspan><tspan x="173.43" y="0" letter-spacing="-.1em">c</tspan><tspan x="178.67" y="0" letter-spacing="-.15em">e to </tspan><tspan x="0" y="9.6" letter-spacing="-.11em">m</tspan><tspan x="5.17" y="9.6" letter-spacing="-.13em">a</tspan><tspan x="10.19" y="9.6" letter-spacing="-.15em">k</tspan><tspan x="15.1" y="9.6" letter-spacing="-.15em">e </tspan><tspan x="24.84" y="9.6" letter-spacing="-.15em">t</tspan><tspan x="29.68" y="9.6" letter-spacing="-.15em">h</tspan><tspan x="34.57" y="9.6" letter-spacing="-.17em">i</tspan><tspan x="39.31" y="9.6" letter-spacing="-.15em">s a </tspan><tspan x="58.8" y="9.6" letter-spacing="-.14em">r</tspan><tspan x="63.72" y="9.6" letter-spacing="-.12em">e</tspan><tspan x="68.85" y="9.6" letter-spacing="-.15em">a</tspan><tspan x="73.69" y="9.6" letter-spacing="-.14em">l</tspan><tspan x="78.64" y="9.6" letter-spacing="-.22em">i</tspan><tspan x="82.92" y="9.6" letter-spacing="-.13em">t</tspan><tspan x="87.91" y="9.6" letter-spacing="-.2em">y</tspan><tspan x="92.37" y="9.6" letter-spacing="-.15em">?</tspan></text>
      <text transform="translate(24.63 467.4)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300"><tspan x="0" y="0" letter-spacing="-.09em">W</tspan><tspan x="6.01" y="0" letter-spacing="-.11em">h</tspan><tspan x="11.89" y="0" letter-spacing="-.13em">a</tspan><tspan x="17.59" y="0" letter-spacing="-.1em">t </tspan><tspan x="29.36" y="0" letter-spacing="-.09em">w</tspan><tspan x="35.38" y="0" letter-spacing="-.1em">i</tspan><tspan x="41.28" y="0" letter-spacing="-.11em">ll </tspan><tspan x="58.93" y="0" letter-spacing="-.12em">t</tspan><tspan x="64.65" y="0" letter-spacing="-.11em">h</tspan><tspan x="70.47" y="0" letter-spacing="-.11em">i</tspan><tspan x="76.35" y="0" letter-spacing="-.11em">s </tspan><tspan x="88.12" y="0" letter-spacing="-.12em">r</tspan><tspan x="93.83" y="0" letter-spacing="-.09em">e</tspan><tspan x="99.83" y="0" letter-spacing="-.11em">s</tspan><tspan x="105.65" y="0" letter-spacing="-.09em">p</tspan><tspan x="111.71" y="0" letter-spacing="-.1em">o</tspan><tspan x="117.67" y="0" letter-spacing="-.11em">n</tspan><tspan x="123.54" y="0" letter-spacing="-.1em">s</tspan><tspan x="129.49" y="0" letter-spacing="-.11em">e </tspan><tspan x="141.27" y="0" letter-spacing="-.08em">m</tspan><tspan x="147.4" y="0" letter-spacing="-.09em">e</tspan><tspan x="153.41" y="0" letter-spacing="-.09em">a</tspan><tspan x="159.41" y="0" letter-spacing="-.11em">n </tspan><tspan x="171.18" y="0" letter-spacing="-.12em">f</tspan><tspan x="176.94" y="0" letter-spacing="-.12em">o</tspan><tspan x="182.72" y="0" letter-spacing="-.1em">r </tspan><tspan x="0" y="10.8" letter-spacing="-.1em">a</tspan><tspan x="5.94" y="10.8" letter-spacing="-.08em">c</tspan><tspan x="12.08" y="10.8" letter-spacing="-.1em">a</tspan><tspan x="18.04" y="10.8" letter-spacing="-.09em">d</tspan><tspan x="24.02" y="10.8" letter-spacing="-.09em">e</tspan><tspan x="30.07" y="10.8" letter-spacing="-.1em">m</tspan><tspan x="35.98" y="10.8" letter-spacing="-.13em">i</tspan><tspan x="41.66" y="10.8" letter-spacing="-.11em">c </tspan><tspan x="53.43" y="10.8" letter-spacing="-.13em">f</tspan><tspan x="59.1" y="10.8" letter-spacing="-.12em">r</tspan><tspan x="64.81" y="10.8" letter-spacing="-.09em">e</tspan><tspan x="70.82" y="10.8" letter-spacing="-.09em">e</tspan><tspan x="76.82" y="10.8" letter-spacing="-.1em">d</tspan><tspan x="82.79" y="10.8" letter-spacing="-.08em">o</tspan><tspan x="88.87" y="10.8" letter-spacing="-.16em">m</tspan><tspan x="94.25" y="10.8" letter-spacing="-.1em">?</tspan></text>
      <circle cx="33.54" cy="322.04" r="3.06" fill="none" stroke="#231f20" stroke-miterlimit="10" stroke-width=".5"/>
      <circle cx="33.54" cy="491.84" r="3.06" fill="none" stroke="#231f20" stroke-miterlimit="10" stroke-width=".5"/>
    </g>
    <foreignObject transform="translate(60 243)" width="110" height="45" v-if="showContent">
      <input
        name="year" type="number" min="2027" max="2199"
        class="form-control" required
        v-maska="{ mask: '2c##', tokens: { c: { pattern: /[01]/ } } }" placeholder="2027" inputmode="numeric"
        v-model="object.year"
        :disabled="!editMode"
        aria-describedby="yearHelp"
      />
    </foreignObject>
    <foreignObject transform="translate(28.19 234.64)" width="200" height="50" v-if="showContent && editMode">
      <div id="yearHelp" class="form-text"><i class="bi bi-info-circle"></i> Enter a year between 2027 - 2199</div>
    </foreignObject>
    <foreignObject transform="translate(9 338)" width="270" height="120" v-if="showContent">
      <textarea
        class="form-control w-100 h-100"
        name="question_1" required placeholder="Leave your response here"
        v-model="object.question_1"
        :disabled="!editMode"
      ></textarea>
    </foreignObject>
    <foreignObject transform="translate(9 505)" width="270" :height="editMode ? 125 : 135" v-if="showContent">
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