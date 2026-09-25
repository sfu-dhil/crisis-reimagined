<script setup>
import BackgroundImageUrl from '../assets/img/technology-background.png'
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
        <polyline points="-.95 83.52 288.95 83.52 288.95 648 -.95 648 -.95 83.52" fill="none"/>
      </clipPath>
      <clipPath id="c">
        <polyline points="-575.2 83.52 638.72 83.52 638.72 648 -575.2 648 -575.2 83.52" fill="none"/>
      </clipPath>
      <clipPath id="d">
        <polyline points="288.95 83.52 -.95 83.52 -.95 648 288.95 648 288.95 83.52" fill="none"/>
      </clipPath>
    </defs>
    <g clip-path="url(#b)">
      <g clip-path="url(#c)">
        <g clip-path="url(#d)">
          <image width="1210" height="2354" transform="translate(-1.12 83.28) scale(.24)" :href="BackgroundImageUrl" />
        </g>
      </g>
    </g>
    <rect y="83.52" width="288" height="564.48" fill="none"/>
    <line x1="70" y1="275.65" x2="158" y2="275.65" fill="none" stroke="#231f20" stroke-dasharray="6 3" stroke-miterlimit="10" stroke-width=".75"/>
    <g>
      <path d="M105.85,27.74h7v1.4h-5.46v8.26h4.76v1.4h-6.3v-11.07Z" fill="#231f20"/>
      <path d="M121.12,38.8h-1.85l-3.47-4.9v4.9h-1.54v-11.07h6.3v6.16h-2.98l3.54,4.9ZM115.79,32.5h3.22v-3.36h-3.22v3.36Z" fill="#231f20"/>
      <path d="M126.5,29.14v8.26h2.8v1.4h-7.14v-1.4h2.8v-8.26h-2.8v-1.4h7.14v1.4h-2.8Z" fill="#231f20"/>
      <path d="M131.05,37.42h4.76v-3.77h-4.76v-5.91h7v1.4h-5.46v3.11h4.76v6.57h-6.3v-1.4Z" fill="#231f20"/>
      <path d="M143.3,29.14v8.26h2.8v1.4h-7.14v-1.4h2.8v-8.26h-2.8v-1.4h7.14v1.4h-2.8Z" fill="#231f20"/>
      <path d="M147.85,37.42h4.76v-3.77h-4.76v-5.91h7v1.4h-5.46v3.11h4.76v6.57h-6.3v-1.4Z" fill="#231f20"/>
      <path d="M164.23,33.27c0-3.46,1.36-5.67,3.5-5.67s3.5,2.21,3.5,5.67-1.36,5.67-3.5,5.67-3.5-2.21-3.5-5.67ZM169.69,33.27c0-2.6-.77-4.27-1.96-4.27s-1.96,1.67-1.96,4.27.77,4.27,1.96,4.27,1.96-1.67,1.96-4.27Z" fill="#231f20"/>
      <path d="M173.05,27.74h6.3v1.4h-4.76v3.15h4.76v1.4h-4.76v5.11h-1.54v-11.07Z" fill="#231f20"/>
      <path d="M92.94,47.98h-4.05v-1.8h10.08v1.8h-4.05v12.42h-1.98v-12.42Z" fill="#231f20"/>
      <path d="M100.77,46.18h7.92v1.8h-5.94v4.05h5.94v1.8h-5.94v4.77h5.94v1.8h-7.92v-14.22Z" fill="#231f20"/>
      <path d="M111.57,46.18h9v1.8h-7.02v10.62h6.12v1.8h-8.1v-14.22Z" fill="#231f20"/>
      <path d="M122.37,46.18h1.98v5.85h3.96v-5.85h1.98v14.22h-1.98v-6.57h-3.96v6.57h-1.98v-14.22Z" fill="#231f20"/>
      <path d="M133.17,46.18h2.81l3.13,10.88v-10.88h1.98v14.22h-2.81l-3.13-10.88v10.88h-1.98v-14.22Z" fill="#231f20"/>
      <path d="M143.43,53.29c0-4.45,1.75-7.29,4.5-7.29s4.5,2.84,4.5,7.29-1.75,7.29-4.5,7.29-4.5-2.85-4.5-7.29ZM150.45,53.29c0-3.35-.99-5.49-2.52-5.49s-2.52,2.14-2.52,5.49.99,5.49,2.52,5.49,2.52-2.14,2.52-5.49Z" fill="#231f20"/>
      <path d="M154.77,46.18h1.98v12.42h6.66v1.8h-8.64v-14.22Z" fill="#231f20"/>
      <path d="M165.03,53.29c0-4.45,1.75-7.29,4.5-7.29s4.5,2.84,4.5,7.29-1.75,7.29-4.5,7.29-4.5-2.85-4.5-7.29ZM172.05,53.29c0-3.35-.99-5.49-2.52-5.49s-2.52,2.14-2.52,5.49.99,5.49,2.52,5.49,2.52-2.14,2.52-5.49Z" fill="#231f20"/>
      <path d="M176.37,46.18h9v1.8h-7.02v10.62h4.32v-4.5h-2.88v-1.8h4.68v8.1h-8.1v-14.22Z" fill="#231f20"/>
      <path d="M190.14,53.83l-3.87-7.65h2.2l2.67,5.55,2.67-5.55h2.2l-3.87,7.65v6.57h-1.98v-6.57Z" fill="#231f20"/>
    </g>
    <text transform="translate(113.61 79.01)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="8" font-weight="300" letter-spacing="-.03em"><tspan x="0" y="0">How do information and </tspan><tspan x="0" y="9.5">communication technologies </tspan><tspan x="0" y="19">enable and constrain the </tspan><tspan x="0" y="28.5">university?</tspan></text>
    <text transform="translate(22.53 133.14)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="9" font-style="italic" font-weight="300" letter-spacing="-.13em"><tspan x="0" y="0">While the pace of technological change </tspan><tspan x="0" y="10.8">seems to be increasing, the university has </tspan><tspan x="0" y="21.6">always struggled to cope with the arrival </tspan><tspan x="0" y="32.4">of new techniques for creating and sharing </tspan><tspan x="0" y="43.2">knowledge. The technological crisis </tspan><tspan x="0" y="54">promises new possibilities while also </tspan><tspan x="0" y="64.8">imposing complex limitations.</tspan></text>
    <text transform="translate(22.61 234.69)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300"><tspan x="0" y="0" letter-spacing="-.04em">i</tspan><tspan x="6.48" y="0" letter-spacing="-.03em">n </tspan><tspan x="19.69" y="0" letter-spacing="-.04em">t</tspan><tspan x="26.12" y="0" letter-spacing="-.01em">h</tspan><tspan x="32.86" y="0" letter-spacing="-.03em">e </tspan><tspan x="46.07" y="0" letter-spacing="-.03em">y</tspan><tspan x="52.61" y="0" letter-spacing="-.01em">e</tspan><tspan x="59.34" y="0" letter-spacing="-.03em">a</tspan><tspan x="65.87" y="0" letter-spacing="-.03em">r</tspan></text>
    <text transform="translate(22.49 297.68)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300"><tspan x="0" y="0" letter-spacing="-.09em">W</tspan><tspan x="5.99" y="0" letter-spacing="-.11em">h</tspan><tspan x="11.85" y="0" letter-spacing="-.13em">a</tspan><tspan x="17.53" y="0" letter-spacing="-.11em">t </tspan><tspan x="29.27" y="0" letter-spacing="-.09em">n</tspan><tspan x="35.27" y="0" letter-spacing="-.09em">e</tspan><tspan x="41.27" y="0" letter-spacing="-.11em">w </tspan><tspan x="53.01" y="0" letter-spacing="-.13em">t</tspan><tspan x="58.66" y="0" letter-spacing="-.1em">e</tspan><tspan x="64.62" y="0" letter-spacing="-.09em">c</tspan><tspan x="70.6" y="0" letter-spacing="-.1em">h</tspan><tspan x="76.5" y="0" letter-spacing="-.09em">n</tspan><tspan x="82.48" y="0" letter-spacing="-.13em">o</tspan><tspan x="88.11" y="0" letter-spacing="-.13em">l</tspan><tspan x="93.73" y="0" letter-spacing="-.09em">og</tspan><tspan x="105.71" y="0" letter-spacing="-.13em">i</tspan><tspan x="111.36" y="0" letter-spacing="-.08em">c</tspan><tspan x="117.48" y="0" letter-spacing="-.08em">a</tspan><tspan x="123.6" y="0" letter-spacing="-.11em">l </tspan><tspan x="135.33" y="0" letter-spacing="-.12em">c</tspan><tspan x="141.13" y="0" letter-spacing="-.11em">r</tspan><tspan x="146.97" y="0" letter-spacing="-.11em">i</tspan><tspan x="152.83" y="0" letter-spacing="-.12em">s</tspan><tspan x="158.58" y="0" letter-spacing="-.11em">i</tspan><tspan x="164.44" y="0" letter-spacing="-.11em">s </tspan><tspan x="176.18" y="0" letter-spacing="-.09em">w</tspan><tspan x="182.18" y="0" letter-spacing="-.11em">i</tspan><tspan x="188.06" y="0" letter-spacing="-.11em">ll </tspan><tspan x="205.66" y="0" letter-spacing="-.13em">t</tspan><tspan x="211.36" y="0" letter-spacing="-.09em">h</tspan><tspan x="217.36" y="0" letter-spacing="-.11em">e </tspan><tspan x="0" y="10.8" letter-spacing="-.11em">u</tspan><tspan x="5.84" y="10.8" letter-spacing="-.11em">n</tspan><tspan x="11.64" y="10.8" letter-spacing="-.19em">i</tspan><tspan x="16.77" y="10.8" letter-spacing="-.12em">v</tspan><tspan x="22.56" y="10.8" letter-spacing="-.12em">e</tspan><tspan x="28.28" y="10.8" letter-spacing="-.11em">r</tspan><tspan x="34.08" y="10.8" letter-spacing="-.12em">s</tspan><tspan x="39.83" y="10.8" letter-spacing="-.18em">i</tspan><tspan x="45.02" y="10.8" letter-spacing="-.1em">t</tspan><tspan x="50.97" y="10.8" letter-spacing="-.11em">y </tspan><tspan x="62.7" y="10.8" letter-spacing="-.1em">f</tspan><tspan x="68.64" y="10.8" letter-spacing="-.1em">a</tspan><tspan x="74.56" y="10.8" letter-spacing="-.08em">c</tspan><tspan x="80.66" y="10.8" letter-spacing="-.16em">e</tspan><tspan x="86.02" y="10.8" letter-spacing="-.11em">?</tspan></text>
    <text transform="translate(42.61 497.45)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="8" font-style="italic" font-weight="300"><tspan x="0" y="0" letter-spacing="-.13em">h</tspan><tspan x="5.03" y="0" letter-spacing="-.12em">o</tspan><tspan x="10.15" y="0" letter-spacing="-.15em">w </tspan><tspan x="19.9" y="0" letter-spacing="-.12em">w</tspan><tspan x="24.99" y="0" letter-spacing="-.14em">i</tspan><tspan x="29.94" y="0" letter-spacing="-.14em">l</tspan><tspan x="34.88" y="0" letter-spacing="-.15em">l </tspan><tspan x="44.62" y="0" letter-spacing="-.22em">i</tspan><tspan x="48.9" y="0" letter-spacing="-.15em">t </tspan><tspan x="58.64" y="0" letter-spacing="-.13em">a</tspan><tspan x="63.67" y="0" letter-spacing="-.13em">d</tspan><tspan x="68.71" y="0" letter-spacing="-.13em">a</tspan><tspan x="73.72" y="0" letter-spacing="-.16em">p</tspan><tspan x="78.49" y="0" letter-spacing="-.15em">t </tspan><tspan x="88.24" y="0" letter-spacing="-.22em">i</tspan><tspan x="92.51" y="0" letter-spacing="-.14em">t</tspan><tspan x="97.47" y="0" letter-spacing="-.15em">s </tspan><tspan x="107.21" y="0" letter-spacing="-.14em">p</tspan><tspan x="112.13" y="0" letter-spacing="-.16em">r</tspan><tspan x="116.96" y="0" letter-spacing="-.13em">a</tspan><tspan x="121.99" y="0" letter-spacing="-.16em">c</tspan><tspan x="126.77" y="0" letter-spacing="-.15em">t</tspan><tspan x="131.64" y="0" letter-spacing="-.19em">i</tspan><tspan x="136.16" y="0" letter-spacing="-.1em">c</tspan><tspan x="141.4" y="0" letter-spacing="-.13em">e</tspan><tspan x="146.41" y="0" letter-spacing="-.15em">s </tspan><tspan x="156.16" y="0" letter-spacing="-.25em">(</tspan><tspan x="160.21" y="0" letter-spacing="-.15em">t</tspan><tspan x="165.06" y="0" letter-spacing="-.12em">e</tspan><tspan x="170.19" y="0" letter-spacing="-.13em">a</tspan><tspan x="175.22" y="0" letter-spacing="-.11em">c</tspan><tspan x="180.4" y="0" letter-spacing="-.15em">h</tspan><tspan x="185.3" y="0" letter-spacing="-.15em">i</tspan><tspan x="190.15" y="0" letter-spacing="-.13em">n</tspan><tspan x="195.22" y="0" letter-spacing="-.21em">g</tspan><tspan x="199.62" y="0" letter-spacing="-.15em">, </tspan><tspan x="0" y="9.6" letter-spacing="-.14em">r</tspan><tspan x="4.92" y="9.6" letter-spacing="-.13em">e</tspan><tspan x="9.93" y="9.6" letter-spacing="-.13em">s</tspan><tspan x="14.97" y="9.6" letter-spacing="-.12em">e</tspan><tspan x="20.1" y="9.6" letter-spacing="-.15em">a</tspan><tspan x="24.96" y="9.6" letter-spacing="-.14em">r</tspan><tspan x="29.92" y="9.6" letter-spacing="-.11em">c</tspan><tspan x="35.1" y="9.6" letter-spacing="-.23em">h</tspan><tspan x="39.36" y="9.6" letter-spacing="-.15em">, </tspan><tspan x="49.1" y="9.6" letter-spacing="-.12em">e</tspan><tspan x="54.18" y="9.6" letter-spacing="-.13em">n</tspan><tspan x="59.24" y="9.6" letter-spacing="-.11em">g</tspan><tspan x="64.39" y="9.6" letter-spacing="-.13em">a</tspan><tspan x="69.41" y="9.6" letter-spacing="-.11em">g</tspan><tspan x="74.57" y="9.6" letter-spacing="-.11em">e</tspan><tspan x="79.75" y="9.6" letter-spacing="-.12em">m</tspan><tspan x="84.9" y="9.6" letter-spacing="-.12em">e</tspan><tspan x="89.97" y="9.6" letter-spacing="-.16em">n</tspan><tspan x="94.74" y="9.6" letter-spacing="-.15em">t </tspan><tspan x="104.48" y="9.6" letter-spacing="-.17em">e</tspan><tspan x="109.19" y="9.6" letter-spacing="-.15em">t</tspan><tspan x="114.08" y="9.6" letter-spacing="-.24em">c</tspan><tspan x="118.21" y="9.6" letter-spacing="-.25em">)</tspan><tspan x="122.25" y="9.6" letter-spacing="-.15em">?</tspan></text>
    <text transform="translate(22.49 472.81)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300"><tspan x="0" y="0" letter-spacing="-.1em">H</tspan><tspan x="5.92" y="0" letter-spacing="-.09em">o</tspan><tspan x="11.97" y="0" letter-spacing="-.11em">w </tspan><tspan x="23.71" y="0" letter-spacing="-.09em">w</tspan><tspan x="29.72" y="0" letter-spacing="-.11em">i</tspan><tspan x="35.59" y="0" letter-spacing="-.11em">ll </tspan><tspan x="53.2" y="0" letter-spacing="-.13em">t</tspan><tspan x="58.89" y="0" letter-spacing="-.09em">h</tspan><tspan x="64.89" y="0" letter-spacing="-.11em">e </tspan><tspan x="76.63" y="0" letter-spacing="-.11em">u</tspan><tspan x="82.47" y="0" letter-spacing="-.11em">n</tspan><tspan x="88.27" y="0" letter-spacing="-.19em">i</tspan><tspan x="93.39" y="0" letter-spacing="-.12em">v</tspan><tspan x="99.18" y="0" letter-spacing="-.12em">e</tspan><tspan x="104.9" y="0" letter-spacing="-.11em">r</tspan><tspan x="110.71" y="0" letter-spacing="-.12em">s</tspan><tspan x="116.46" y="0" letter-spacing="-.18em">i</tspan><tspan x="121.65" y="0" letter-spacing="-.1em">t</tspan><tspan x="127.59" y="0" letter-spacing="-.11em">y </tspan><tspan x="139.33" y="0" letter-spacing="-.1em">f</tspan><tspan x="145.27" y="0" letter-spacing="-.1em">a</tspan><tspan x="151.19" y="0" letter-spacing="-.08em">c</tspan><tspan x="157.29" y="0" letter-spacing="-.11em">e </tspan><tspan x="169.02" y="0" letter-spacing="-.13em">t</tspan><tspan x="174.72" y="0" letter-spacing="-.11em">h</tspan><tspan x="180.52" y="0" letter-spacing="-.11em">i</tspan><tspan x="186.38" y="0" letter-spacing="-.11em">s </tspan><tspan x="0" y="10.8" letter-spacing="-.15em">t</tspan><tspan x="5.51" y="10.8" letter-spacing="-.1em">r</tspan><tspan x="11.43" y="10.8" letter-spacing="-.09em">a</tspan><tspan x="17.41" y="10.8" letter-spacing="-.11em">n</tspan><tspan x="23.26" y="10.8" letter-spacing="-.12em">s</tspan><tspan x="29.05" y="10.8" letter-spacing="-.12em">f</tspan><tspan x="34.79" y="10.8" letter-spacing="-.12em">o</tspan><tspan x="40.55" y="10.8" letter-spacing="-.1em">r</tspan><tspan x="46.5" y="10.8" letter-spacing="-.09em">m</tspan><tspan x="52.48" y="10.8" letter-spacing="-.13em">a</tspan><tspan x="58.16" y="10.8" letter-spacing="-.12em">t</tspan><tspan x="63.92" y="10.8" letter-spacing="-.13em">i</tspan><tspan x="69.55" y="10.8" letter-spacing="-.1em">o</tspan><tspan x="75.5" y="10.8" letter-spacing="-.18em">n</tspan><tspan x="80.75" y="10.8" letter-spacing="-.11em">?</tspan></text>
    <g>
      <line x1="85.93" y1="77.62" x2="106.97" y2="77.62" fill="none" stroke="#231f20" stroke-miterlimit="10"/>
      <polygon points="103.66 81.71 102.98 80.98 106.59 77.62 102.98 74.26 103.66 73.53 108.06 77.62 103.66 81.71" fill="#231f20"/>
    </g>
    <circle cx="32.64" cy="320.71" r="3.06" fill="none" stroke="#231f20" stroke-miterlimit="10" stroke-width=".5"/>
    <text transform="translate(42.61 323.26)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="8" font-style="italic" font-weight="300"><tspan x="0" y="0" letter-spacing="-.11em">w</tspan><tspan x="5.21" y="0" letter-spacing="-.13em">h</tspan><tspan x="10.24" y="0" letter-spacing="-.15em">o </tspan><tspan x="19.98" y="0" letter-spacing="-.17em">i</tspan><tspan x="24.72" y="0" letter-spacing="-.15em">s </tspan><tspan x="34.47" y="0" letter-spacing="-.15em">d</tspan><tspan x="39.31" y="0" letter-spacing="-.14em">r</tspan><tspan x="44.25" y="0" letter-spacing="-.22em">i</tspan><tspan x="48.53" y="0" letter-spacing="-.14em">v</tspan><tspan x="53.5" y="0" letter-spacing="-.15em">i</tspan><tspan x="58.35" y="0" letter-spacing="-.13em">n</tspan><tspan x="63.42" y="0" letter-spacing="-.15em">g </tspan><tspan x="73.16" y="0" letter-spacing="-.15em">t</tspan><tspan x="78" y="0" letter-spacing="-.15em">h</tspan><tspan x="82.89" y="0" letter-spacing="-.17em">i</tspan><tspan x="87.63" y="0" letter-spacing="-.15em">s </tspan><tspan x="97.38" y="0" letter-spacing="-.15em">t</tspan><tspan x="102.23" y="0" letter-spacing="-.12em">e</tspan><tspan x="107.36" y="0" letter-spacing="-.11em">c</tspan><tspan x="112.54" y="0" letter-spacing="-.13em">h</tspan><tspan x="117.54" y="0" letter-spacing="-.13em">n</tspan><tspan x="122.56" y="0" letter-spacing="-.14em">o</tspan><tspan x="127.54" y="0" letter-spacing="-.19em">l</tspan><tspan x="132.07" y="0" letter-spacing="-.11em">o</tspan><tspan x="137.29" y="0" letter-spacing="-.13em">g</tspan><tspan x="142.33" y="0" letter-spacing="-.19em">i</tspan><tspan x="146.84" y="0" letter-spacing="-.11em">c</tspan><tspan x="152.06" y="0" letter-spacing="-.15em">a</tspan><tspan x="156.91" y="0" letter-spacing="-.15em">l </tspan><tspan x="166.65" y="0" letter-spacing="-.11em">c</tspan><tspan x="171.83" y="0" letter-spacing="-.13em">h</tspan><tspan x="176.88" y="0" letter-spacing="-.13em">a</tspan><tspan x="181.88" y="0" letter-spacing="-.13em">n</tspan><tspan x="186.94" y="0" letter-spacing="-.11em">g</tspan><tspan x="192.1" y="0" letter-spacing="-.22em">e</tspan><tspan x="196.44" y="0" letter-spacing="-.15em">, </tspan><tspan x="0" y="9.6" letter-spacing="-.13em">a</tspan><tspan x="4.99" y="9.6" letter-spacing="-.13em">n</tspan><tspan x="10.04" y="9.6" letter-spacing="-.15em">d to </tspan><tspan x="34.4" y="9.6" letter-spacing="-.11em">w</tspan><tspan x="39.61" y="9.6" letter-spacing="-.13em">h</tspan><tspan x="44.64" y="9.6" letter-spacing="-.14em">o</tspan><tspan x="49.63" y="9.6" letter-spacing="-.13em">s</tspan><tspan x="54.67" y="9.6" letter-spacing="-.15em">e </tspan><tspan x="64.42" y="9.6" letter-spacing="-.12em">b</tspan><tspan x="69.52" y="9.6" letter-spacing="-.12em">e</tspan><tspan x="74.59" y="9.6" letter-spacing="-.13em">n</tspan><tspan x="79.61" y="9.6" letter-spacing="-.16em">e</tspan><tspan x="84.44" y="9.6" letter-spacing="-.14em">f</tspan><tspan x="89.39" y="9.6" letter-spacing="-.22em">i</tspan><tspan x="93.67" y="9.6" letter-spacing="-.22em">t</tspan><tspan x="97.98" y="9.6" letter-spacing="-.15em">?</tspan></text>
    <circle cx="32.64" cy="320.71" r="3.06" fill="none" stroke="#231f20" stroke-miterlimit="10" stroke-width=".5"/>
    <circle cx="32.64" cy="495.33" r="3.06" fill="none" stroke="#231f20" stroke-miterlimit="10" stroke-width=".5"/>
    <foreignObject transform="translate(60 243)" width="110" height="45" v-if="showContent">
      <input
        name="year" type="number" min="2027" max="2199"
        class="form-control" required
        v-maska="{ mask: '2c##', tokens: { c: { pattern: /[01]/ } } }" placeholder="2100" inputmode="numeric"
        v-model="object.year"
        :disabled="!editMode"
        aria-describedby="yearHelp"
      />
    </foreignObject>
    <foreignObject transform="translate(22.61 234.69)" width="200" height="50" v-if="showContent && editMode">
      <div id="yearHelp" class="form-text"><i class="bi bi-info-circle"></i> Enter a year between 2027 - 2199</div>
    </foreignObject>
    <foreignObject transform="translate(9 338)" width="270" height="125" v-if="showContent">
      <textarea
        class="form-control w-100 h-100"
        name="question_1" required placeholder="Leave your response here"
        v-model="object.question_1"
        :disabled="!editMode"
      ></textarea>
    </foreignObject>
    <foreignObject transform="translate(9 510)" width="270" :height="editMode ? 120 : 130" v-if="showContent">
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