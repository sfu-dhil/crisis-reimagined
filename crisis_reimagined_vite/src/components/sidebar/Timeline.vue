<script setup>
import { useDisplayInstallationStore } from '../../stores/display.js'
</script>

<template>
  <h1 class="h3 text-center">Timeline</h1>
  <ul class="timeline">
    <li class="d-flex align-items-baseline">
      <button class="btn btn-link text-decoration-none p-0 m-0 me-1"
        @click="() => useDisplayInstallationStore().zoomToElementByClassIds('PAPAL-SCHISM')"
      ><i class="bi bi-link-45deg"></i></button>
      <div>
        <h2 class="h5 d-flex-shrink-1">PAPAL SCHISM</h2>
        <p>
          The Church’s division creates uncertainty over papal authority, making travel unsafe and limiting international study. Universities adapt by turning toward local students and serving a growing middle class.
        </p>
      </div>
    </li>
    <li class="d-flex align-items-baseline">
      <button class="btn btn-link text-decoration-none p-0 m-0 me-1"
        @click="() => useDisplayInstallationStore().zoomToElementByClassIds('BLACK-DEATH')"
      ><i class="bi bi-link-45deg"></i></button>
      <div>
        <p>
          <strong>Black Death</strong>
          leads to major collapse in student enrollment
        </p>
      </div>
    </li>
    <li class="d-flex align-items-baseline">
      <button class="btn btn-link text-decoration-none p-0 m-0 me-1"
        @click="() => useDisplayInstallationStore().zoomToElementByClassIds('PRINTING-PRESS')"
      ><i class="bi bi-link-45deg"></i></button>
      <div>
        <h2 class="h5">PRINTING PRESS</h2>
        <p>
          Intellectuals no longer need a university position to participate in scholarship, creating a university ‘brain drain.’ The availability of,and need for, print media of all kinds also becomes essential in universities, leading to a print-dominant culture lasting to this day.
        </p>
      </div>
    </li>
  </ul>
</template>

<style scoped>
ul.timeline {
  list-style-type: none;
  position: relative;
}
ul.timeline:before {
  content: ' ';
  background: var(--bs-emphasis-color);
  position: absolute;
  left: 0.7em;
  width: 0.1em;
  height: 100%;
}
ul.timeline > li {
  margin: 1em 0;
  padding-left: 0.5em;
}
ul.timeline > li:before {
  content: ' ';
  background: var(--bs-body-bg);
  position: absolute;
  border-radius: 50%;
  border: 3px solid var(--bs-emphasis-color);
  left: 0em;
  width: 1.5em;
  height: 1.5em;
}
</style>