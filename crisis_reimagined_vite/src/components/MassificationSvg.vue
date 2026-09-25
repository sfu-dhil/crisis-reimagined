<script setup>
import BackgroundImageUrl from '../assets/img/massification-background.png'
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
        <polyline points="1.34 83.52 288.81 83.52 288.81 648 1.34 648 1.34 83.52" fill="none"/>
      </clipPath>
      <clipPath id="c">
        <polyline points="-862.81 83.52 351.11 83.52 351.11 648 -862.81 648 -862.81 83.52" fill="none"/>
      </clipPath>
      <clipPath id="d">
        <polyline points="288.81 83.52 1.34 83.52 1.34 648 288.81 648 288.81 83.52" fill="none"/>
      </clipPath>
    </defs>
    <rect y="83.52" width="288" height="564.48" fill="none"/>
    <g clip-path="url(#b)">
      <g clip-path="url(#c)">
        <g clip-path="url(#d)">
          <image width="1199" height="2354" transform="translate(1.19 83.28) scale(.24)" :href="BackgroundImageUrl" />
        </g>
      </g>
    </g>
    <g>
      <g>
        <line x1="75" y1="291.03" x2="160" y2="291.03" fill="none" stroke="#231f20" stroke-dasharray="6 3" stroke-miterlimit="10" stroke-width=".75"/>
      </g>
      <g>
        <path d="M108.32,43.11h7v1.4h-5.46v8.26h4.76v1.4h-6.3v-11.07Z" fill="#231f20"/>
        <path d="M123.59,54.18h-1.85l-3.47-4.9v4.9h-1.54v-11.07h6.3v6.16h-2.98l3.54,4.9ZM118.26,47.88h3.22v-3.36h-3.22v3.36Z" fill="#231f20"/>
        <path d="M128.97,44.52v8.26h2.8v1.4h-7.14v-1.4h2.8v-8.26h-2.8v-1.4h7.14v1.4h-2.8Z" fill="#231f20"/>
        <path d="M133.52,52.79h4.76v-3.77h-4.76v-5.91h7v1.4h-5.46v3.11h4.76v6.57h-6.3v-1.4Z" fill="#231f20"/>
        <path d="M145.77,44.52v8.26h2.8v1.4h-7.14v-1.4h2.8v-8.26h-2.8v-1.4h7.14v1.4h-2.8Z" fill="#231f20"/>
        <path d="M150.32,52.79h4.76v-3.77h-4.76v-5.91h7v1.4h-5.46v3.11h4.76v6.57h-6.3v-1.4Z" fill="#231f20"/>
        <path d="M166.7,48.65c0-3.46,1.36-5.67,3.5-5.67s3.5,2.21,3.5,5.67-1.36,5.67-3.5,5.67-3.5-2.21-3.5-5.67ZM172.16,48.65c0-2.6-.77-4.27-1.96-4.27s-1.96,1.67-1.96,4.27.77,4.27,1.96,4.27,1.96-1.67,1.96-4.27Z" fill="#231f20"/>
        <path d="M175.52,43.11h6.3v1.4h-4.76v3.15h4.76v1.4h-4.76v5.11h-1.54v-11.07Z" fill="#231f20"/>
        <path d="M84.61,75.78h-1.98v-12.37l-1.51,4.45h-1.84l-1.51-4.45v12.37h-1.98v-14.22h3.17l1.24,3.65,1.24-3.65h3.17v14.22Z" fill="#231f20"/>
        <path d="M93.06,72.67h-4.1l-.81,3.11h-2l3.85-14.22h2.02l3.85,14.22h-2l-.81-3.11ZM92.61,70.87l-1.6-6.18-1.6,6.18h3.2Z" fill="#231f20"/>
        <path d="M97.84,74h6.12v-4.84h-6.12v-7.6h9v1.8h-7.02v4h6.12v8.44h-8.1v-1.8Z" fill="#231f20"/>
        <path d="M108.64,74h6.12v-4.84h-6.12v-7.6h9v1.8h-7.02v4h6.12v8.44h-8.1v-1.8Z" fill="#231f20"/>
        <path d="M124.39,63.36v10.62h3.6v1.8h-9.18v-1.8h3.6v-10.62h-3.6v-1.8h9.18v1.8h-3.6Z" fill="#231f20"/>
        <path d="M130.24,61.56h8.1v1.8h-6.12v4.05h6.12v1.8h-6.12v6.57h-1.98v-14.22Z" fill="#231f20"/>
        <path d="M145.99,63.36v10.62h3.6v1.8h-9.18v-1.8h3.6v-10.62h-3.6v-1.8h9.18v1.8h-3.6Z" fill="#231f20"/>
        <path d="M151.84,61.56h9v1.8h-7.02v10.62h6.12v1.8h-8.1v-14.22Z" fill="#231f20"/>
        <path d="M168.65,72.67h-4.11l-.81,3.11h-2l3.85-14.22h2.02l3.85,14.22h-2l-.81-3.11ZM168.2,70.87l-1.6-6.18-1.6,6.18h3.21Z" fill="#231f20"/>
        <path d="M176.41,63.36h-4.05v-1.8h10.08v1.8h-4.05v12.42h-1.98v-12.42Z" fill="#231f20"/>
        <path d="M189.19,63.36v10.62h3.6v1.8h-9.18v-1.8h3.6v-10.62h-3.6v-1.8h9.18v1.8h-3.6Z" fill="#231f20"/>
        <path d="M194.5,68.67c0-4.45,1.75-7.29,4.5-7.29s4.5,2.84,4.5,7.29-1.75,7.29-4.5,7.29-4.5-2.84-4.5-7.29ZM201.52,68.67c0-3.35-.99-5.49-2.52-5.49s-2.52,2.14-2.52,5.49.99,5.49,2.52,5.49,2.52-2.14,2.52-5.49Z" fill="#231f20"/>
        <path d="M205.84,61.56h2.81l3.13,10.88v-10.88h1.98v14.22h-2.81l-3.13-10.88v10.88h-1.98v-14.22Z" fill="#231f20"/>
      </g>
      <text transform="translate(117.51 94.39)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="8" font-weight="300" letter-spacing="-.03em"><tspan x="0" y="0">Who is the university </tspan><tspan x="0" y="9.5">for? Who should have </tspan><tspan x="0" y="19">access to it?</tspan></text>
      <text transform="translate(25 142.89)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="9" font-style="italic" font-weight="300" letter-spacing="-.13em"><tspan x="0" y="0">Religion no longer dictates who may enter </tspan><tspan x="0" y="10.8">the university, yet democratization of </tspan><tspan x="0" y="21.6">access has not erased inequality. New </tspan><tspan x="0" y="32.4">forms of exclusion persist, even as the </tspan><tspan x="0" y="43.2">student body grows. The crisis of </tspan><tspan x="0" y="54">massification forces the university to </tspan><tspan x="0" y="64.8">confront the stark reality: whom does it </tspan><tspan x="0" y="75.6">truly serve, and toward what purpose?</tspan></text>
      <text transform="translate(25 250.07)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300"><tspan x="0" y="0" letter-spacing="-.04em">i</tspan><tspan x="6.48" y="0" letter-spacing="-.03em">n </tspan><tspan x="19.69" y="0" letter-spacing="-.04em">t</tspan><tspan x="26.12" y="0" letter-spacing="-.01em">h</tspan><tspan x="32.86" y="0" letter-spacing="-.03em">e </tspan><tspan x="46.07" y="0" letter-spacing="-.03em">y</tspan><tspan x="52.61" y="0" letter-spacing="-.01em">e</tspan><tspan x="59.34" y="0" letter-spacing="-.03em">a</tspan><tspan x="65.87" y="0" letter-spacing="-.03em">r</tspan></text>
      <text transform="translate(25 313.05)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300"><tspan x="0" y="0" letter-spacing="-.19em">W</tspan><tspan x="5.16" y="0" letter-spacing="-.2em">h</tspan><tspan x="10.18" y="0" letter-spacing="-.22em">a</tspan><tspan x="15.02" y="0" letter-spacing="-.2em">t </tspan><tspan x="25.08" y="0" letter-spacing="-.18em">p</tspan><tspan x="30.28" y="0" letter-spacing="-.19em">o</tspan><tspan x="35.39" y="0" letter-spacing="-.19em">p</tspan><tspan x="40.52" y="0" letter-spacing="-.22em">u</tspan><tspan x="45.42" y="0" letter-spacing="-.2em">l</tspan><tspan x="50.42" y="0" letter-spacing="-.22em">a</tspan><tspan x="55.26" y="0" letter-spacing="-.21em">t</tspan><tspan x="60.19" y="0" letter-spacing="-.23em">i</tspan><tspan x="64.98" y="0" letter-spacing="-.19em">o</tspan><tspan x="70.09" y="0" letter-spacing="-.2em">n </tspan><tspan x="80.15" y="0" letter-spacing="-.18em">w</tspan><tspan x="85.32" y="0" letter-spacing="-.2em">i</tspan><tspan x="90.36" y="0" letter-spacing="-.2em">ll </tspan><tspan x="105.45" y="0" letter-spacing="-.22em">t</tspan><tspan x="110.31" y="0" letter-spacing="-.19em">h</tspan><tspan x="115.47" y="0" letter-spacing="-.2em">e </tspan><tspan x="125.53" y="0" letter-spacing="-.2em">u</tspan><tspan x="130.54" y="0" letter-spacing="-.21em">n</tspan><tspan x="135.5" y="0" letter-spacing="-.28em">i</tspan><tspan x="139.79" y="0" letter-spacing="-.21em">v</tspan><tspan x="144.74" y="0" letter-spacing="-.22em">e</tspan><tspan x="149.62" y="0" letter-spacing="-.21em">r</tspan><tspan x="154.59" y="0" letter-spacing="-.21em">s</tspan><tspan x="159.5" y="0" letter-spacing="-.28em">i</tspan><tspan x="163.85" y="0" letter-spacing="-.19em">t</tspan><tspan x="168.96" y="0" letter-spacing="-.2em">y </tspan><tspan x="179.03" y="0" letter-spacing="-.19em">s</tspan><tspan x="184.12" y="0" letter-spacing="-.22em">e</tspan><tspan x="189" y="0" letter-spacing="-.18em">r</tspan><tspan x="194.24" y="0" letter-spacing="-.21em">v</tspan><tspan x="199.19" y="0" letter-spacing="-.26em">e</tspan><tspan x="203.72" y="0" letter-spacing="-.2em">?</tspan></text>
      <text transform="translate(45 326.93)" fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="8" font-style="italic" font-weight="300"><tspan x="0" y="0" letter-spacing="-.1em">c</tspan><tspan x="5.24" y="0" letter-spacing="-.13em">o</tspan><tspan x="10.29" y="0" letter-spacing="-.14em">n</tspan><tspan x="15.25" y="0" letter-spacing="-.15em">s</tspan><tspan x="20.1" y="0" letter-spacing="-.17em">i</tspan><tspan x="24.82" y="0" letter-spacing="-.13em">d</tspan><tspan x="29.82" y="0" letter-spacing="-.15em">e</tspan><tspan x="34.73" y="0" letter-spacing="-.15em">r </tspan><tspan x="44.47" y="0" letter-spacing="-.11em">w</tspan><tspan x="49.68" y="0" letter-spacing="-.13em">h</tspan><tspan x="54.71" y="0" letter-spacing="-.15em">o </tspan><tspan x="64.46" y="0" letter-spacing="-.17em">i</tspan><tspan x="69.2" y="0" letter-spacing="-.15em">s </tspan><tspan x="78.94" y="0" letter-spacing="-.15em">i</tspan><tspan x="83.79" y="0" letter-spacing="-.13em">n</tspan><tspan x="88.83" y="0" letter-spacing="-.13em">c</tspan><tspan x="93.85" y="0" letter-spacing="-.17em">l</tspan><tspan x="98.54" y="0" letter-spacing="-.13em">u</tspan><tspan x="103.57" y="0" letter-spacing="-.13em">d</tspan><tspan x="108.57" y="0" letter-spacing="-.12em">e</tspan><tspan x="113.7" y="0" letter-spacing="-.15em">d </tspan><tspan x="123.44" y="0" letter-spacing="-.13em">a</tspan><tspan x="128.44" y="0" letter-spacing="-.13em">n</tspan><tspan x="133.49" y="0" letter-spacing="-.15em">d </tspan><tspan x="143.23" y="0" letter-spacing="-.14em">e</tspan><tspan x="148.18" y="0" letter-spacing="-.14em">x</tspan><tspan x="153.12" y="0" letter-spacing="-.13em">c</tspan><tspan x="158.13" y="0" letter-spacing="-.17em">l</tspan><tspan x="162.83" y="0" letter-spacing="-.13em">u</tspan><tspan x="167.86" y="0" letter-spacing="-.13em">d</tspan><tspan x="172.86" y="0" letter-spacing="-.12em">e</tspan><tspan x="177.98" y="0" letter-spacing="-.15em">d </tspan><tspan x="187.73" y="0" letter-spacing="-.16em">f</tspan><tspan x="192.52" y="0" letter-spacing="-.14em">r</tspan><tspan x="197.47" y="0" letter-spacing="-.12em">o</tspan><tspan x="202.63" y="0" letter-spacing="-.15em">m </tspan><tspan x="0" y="9.6" letter-spacing="-.15em">t</tspan><tspan x="4.84" y="9.6" letter-spacing="-.15em">h</tspan><tspan x="9.73" y="9.6" letter-spacing="-.17em">i</tspan><tspan x="14.47" y="9.6" letter-spacing="-.15em">s </tspan><tspan x="24.21" y="9.6" letter-spacing="-.12em">p</tspan><tspan x="29.32" y="9.6" letter-spacing="-.13em">o</tspan><tspan x="34.36" y="9.6" letter-spacing="-.13em">p</tspan><tspan x="39.42" y="9.6" letter-spacing="-.15em">u</tspan><tspan x="44.26" y="9.6" letter-spacing="-.17em">l</tspan><tspan x="48.97" y="9.6" letter-spacing="-.15em">a</tspan><tspan x="53.88" y="9.6" letter-spacing="-.15em">t</tspan><tspan x="58.74" y="9.6" letter-spacing="-.19em">i</tspan><tspan x="63.28" y="9.6" letter-spacing="-.13em">o</tspan><tspan x="68.33" y="9.6" letter-spacing="-.21em">n</tspan><tspan x="72.71" y="9.6" letter-spacing="-.15em">?</tspan></text>
      <text fill="#231f20" font-family="DolphYY-LightItalic, &apos;Dolph YY&apos;" font-size="8" font-style="italic" font-weight="300"><tspan x="45" y="498.5" letter-spacing="-.13em">h</tspan><tspan x="50.03" y="498.5" letter-spacing="-.12em">o</tspan><tspan x="55.15" y="498.5" letter-spacing="-.15em">w </tspan><tspan x="64.9" y="498.5" letter-spacing="-.12em">w</tspan><tspan x="69.99" y="498.5" letter-spacing="-.14em">i</tspan><tspan x="74.94" y="498.5" letter-spacing="-.14em">l</tspan><tspan x="79.88" y="498.5" letter-spacing="-.15em">l </tspan><tspan x="89.62" y="498.5" letter-spacing="-.22em">i</tspan><tspan x="93.9" y="498.5" letter-spacing="-.15em">t </tspan><tspan x="103.64" y="498.5" letter-spacing="-.14em">r</tspan><tspan x="108.56" y="498.5" letter-spacing="-.13em">es</tspan><tspan x="118.58" y="498.5" letter-spacing="-.12em">p</tspan><tspan x="123.69" y="498.5" letter-spacing="-.13em">on</tspan><tspan x="133.79" y="498.5" letter-spacing="-.15em">d </tspan><tspan x="143.53" y="498.5" letter-spacing="-.15em">t</tspan><tspan x="148.37" y="498.5" letter-spacing="-.16em">h</tspan><tspan x="153.2" y="498.5" letter-spacing="-.14em">r</tspan><tspan x="158.16" y="498.5" letter-spacing="-.13em">o</tspan><tspan x="163.2" y="498.5" letter-spacing="-.13em">u</tspan><tspan x="168.22" y="498.5" letter-spacing="-.11em">g</tspan><tspan x="173.38" y="498.5" letter-spacing="-.15em">h </tspan><tspan x="183.12" y="498.5" letter-spacing="-.22em">i</tspan><tspan x="187.4" y="498.5" letter-spacing="-.14em">t</tspan><tspan x="192.35" y="498.5" letter-spacing="-.15em">s </tspan><tspan x="202.1" y="498.5" letter-spacing="-.14em">p</tspan><tspan x="207.02" y="498.5" letter-spacing="-.16em">r</tspan><tspan x="211.84" y="498.5" letter-spacing="-.13em">a</tspan><tspan x="216.88" y="498.5" letter-spacing="-.16em">c</tspan><tspan x="221.66" y="498.5" letter-spacing="-.15em">t</tspan><tspan x="226.52" y="498.5" letter-spacing="-.19em">i</tspan><tspan x="231.05" y="498.5" letter-spacing="-.1em">c</tspan><tspan x="236.29" y="498.5" letter-spacing="-.13em">e</tspan><tspan x="241.3" y="498.5" letter-spacing="-.15em">s </tspan><tspan x="45" y="508.1" letter-spacing="-.25em">(</tspan><tspan x="49.05" y="508.1" letter-spacing="-.15em">t</tspan><tspan x="53.9" y="508.1" letter-spacing="-.12em">e</tspan><tspan x="59.03" y="508.1" letter-spacing="-.13em">a</tspan><tspan x="64.06" y="508.1" letter-spacing="-.11em">c</tspan><tspan x="69.25" y="508.1" letter-spacing="-.15em">h</tspan><tspan x="74.14" y="508.1" letter-spacing="-.15em">i</tspan><tspan x="78.99" y="508.1" letter-spacing="-.13em">n</tspan><tspan x="84.06" y="508.1" letter-spacing="-.21em">g</tspan><tspan x="88.46" y="508.1" letter-spacing="-.15em">, </tspan><tspan x="98.2" y="508.1" letter-spacing="-.14em">r</tspan><tspan x="103.13" y="508.1" letter-spacing="-.13em">e</tspan><tspan x="108.14" y="508.1" letter-spacing="-.13em">s</tspan><tspan x="113.18" y="508.1" letter-spacing="-.12em">e</tspan><tspan x="118.3" y="508.1" letter-spacing="-.15em">a</tspan><tspan x="123.16" y="508.1" letter-spacing="-.14em">r</tspan><tspan x="128.12" y="508.1" letter-spacing="-.11em">c</tspan><tspan x="133.3" y="508.1" letter-spacing="-.23em">h</tspan><tspan x="137.56" y="508.1" letter-spacing="-.15em">, </tspan><tspan x="147.31" y="508.1" letter-spacing="-.12em">e</tspan><tspan x="152.38" y="508.1" letter-spacing="-.13em">n</tspan><tspan x="157.45" y="508.1" letter-spacing="-.11em">g</tspan><tspan x="162.6" y="508.1" letter-spacing="-.13em">a</tspan><tspan x="167.62" y="508.1" letter-spacing="-.11em">g</tspan><tspan x="172.78" y="508.1" letter-spacing="-.11em">e</tspan><tspan x="177.96" y="508.1" letter-spacing="-.12em">m</tspan><tspan x="183.11" y="508.1" letter-spacing="-.12em">e</tspan><tspan x="188.18" y="508.1" letter-spacing="-.16em">n</tspan><tspan x="192.95" y="508.1" letter-spacing="-.15em">t </tspan><tspan x="202.69" y="508.1" letter-spacing="-.17em">e</tspan><tspan x="207.4" y="508.1" letter-spacing="-.15em">t</tspan><tspan x="212.29" y="508.1" letter-spacing="-.24em">c</tspan><tspan x="216.42" y="508.1" letter-spacing="-.25em">)</tspan><tspan x="220.46" y="508.1" letter-spacing="-.15em">?</tspan></text>
      <text transform="translate(25 473.66)" fill="#231f20" font-family="DolphYY-Light, &apos;Dolph YY&apos;" font-size="9" font-weight="300"><tspan x="0" y="0" letter-spacing="-.19em">H</tspan><tspan x="5.08" y="0" letter-spacing="-.18em">o</tspan><tspan x="10.3" y="0" letter-spacing="-.2em">w </tspan><tspan x="20.36" y="0" letter-spacing="-.18em">w</tspan><tspan x="25.53" y="0" letter-spacing="-.2em">i</tspan><tspan x="30.57" y="0" letter-spacing="-.2em">ll </tspan><tspan x="45.66" y="0" letter-spacing="-.22em">t</tspan><tspan x="50.52" y="0" letter-spacing="-.19em">h</tspan><tspan x="55.68" y="0" letter-spacing="-.2em">e </tspan><tspan x="65.74" y="0" letter-spacing="-.2em">u</tspan><tspan x="70.75" y="0" letter-spacing="-.21em">n</tspan><tspan x="75.71" y="0" letter-spacing="-.28em">i</tspan><tspan x="80" y="0" letter-spacing="-.21em">v</tspan><tspan x="84.95" y="0" letter-spacing="-.22em">e</tspan><tspan x="89.83" y="0" letter-spacing="-.21em">r</tspan><tspan x="94.8" y="0" letter-spacing="-.21em">s</tspan><tspan x="99.72" y="0" letter-spacing="-.28em">i</tspan><tspan x="104.06" y="0" letter-spacing="-.19em">t</tspan><tspan x="109.18" y="0" letter-spacing="-.2em">y </tspan><tspan x="119.24" y="0" letter-spacing="-.19em">c</tspan><tspan x="124.38" y="0" letter-spacing="-.2em">h</tspan><tspan x="129.4" y="0" letter-spacing="-.19em">a</tspan><tspan x="134.54" y="0" letter-spacing="-.19em">n</tspan><tspan x="139.66" y="0" letter-spacing="-.22em">g</tspan><tspan x="144.55" y="0" letter-spacing="-.2em">e </tspan><tspan x="154.61" y="0" letter-spacing="-.23em">t</tspan><tspan x="159.39" y="0" letter-spacing="-.2em">o </tspan><tspan x="169.46" y="0" letter-spacing="-.19em">a</tspan><tspan x="174.54" y="0" letter-spacing="-.17em">c</tspan><tspan x="179.8" y="0" letter-spacing="-.18em">c</tspan><tspan x="185.04" y="0" letter-spacing="-.18em">o</tspan><tspan x="190.27" y="0" letter-spacing="-.17em">m</tspan><tspan x="195.55" y="0" letter-spacing="-.17em">m</tspan><tspan x="200.82" y="0" letter-spacing="-.18em">o</tspan><tspan x="206.01" y="0" letter-spacing="-.2em">d</tspan><tspan x="211.01" y="0" letter-spacing="-.22em">a</tspan><tspan x="215.85" y="0" letter-spacing="-.22em">t</tspan><tspan x="220.67" y="0" letter-spacing="-.2em">e </tspan><tspan x="0" y="10.8" letter-spacing="-.22em">t</tspan><tspan x="4.86" y="10.8" letter-spacing="-.21em">h</tspan><tspan x="9.82" y="10.8" letter-spacing="-.2em">i</tspan><tspan x="14.85" y="10.8" letter-spacing="-.2em">s </tspan><tspan x="24.91" y="10.8" letter-spacing="-.18em">p</tspan><tspan x="30.11" y="10.8" letter-spacing="-.19em">o</tspan><tspan x="35.22" y="10.8" letter-spacing="-.19em">p</tspan><tspan x="40.35" y="10.8" letter-spacing="-.22em">u</tspan><tspan x="45.24" y="10.8" letter-spacing="-.2em">l</tspan><tspan x="50.24" y="10.8" letter-spacing="-.22em">a</tspan><tspan x="55.09" y="10.8" letter-spacing="-.21em">t</tspan><tspan x="60.01" y="10.8" letter-spacing="-.23em">i</tspan><tspan x="64.8" y="10.8" letter-spacing="-.19em">o</tspan><tspan x="69.91" y="10.8" letter-spacing="-.27em">n</tspan><tspan x="74.33" y="10.8" letter-spacing="-.2em">?</tspan></text>
      <g>
        <line x1="89.84" y1="93" x2="110.88" y2="93" fill="none" stroke="#231f20" stroke-miterlimit="10"/>
        <polygon points="107.56 97.09 106.88 96.36 110.49 93 106.88 89.64 107.56 88.91 111.96 93 107.56 97.09" fill="#231f20"/>
      </g>
      <circle cx="34.82" cy="324.72" r="3.06" fill="none" stroke="#231f20" stroke-miterlimit="10" stroke-width=".5"/>
      <circle cx="34.82" cy="495.73" r="3.06" fill="none" stroke="#231f20" stroke-miterlimit="10" stroke-width=".5"/>
    </g>
    <foreignObject transform="translate(63 258)" width="110" height="45" v-if="showContent">
      <input
        name="year" type="number" min="2027" max="2199"
        class="form-control" required
        v-maska="{ mask: '2c##', tokens: { c: { pattern: /[01]/ } } }" placeholder="2027" inputmode="numeric"
        v-model="object.year"
        :disabled="!editMode"
        aria-describedby="yearHelp"
      />
    </foreignObject>
    <foreignObject transform="translate(25 250.07)" width="200" height="50" v-if="showContent && editMode">
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