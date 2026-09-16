<script setup>
import { storeToRefs } from 'pinia'
import { useResponseStore } from '../../stores/responses.js'
import { useDisplayStore } from '../../stores/display.js'
import { ResponseResourceTypes } from '../../_resourceTypes.js'

const {
  hasKnowledgeObjects,
  hasRestitutionObjects,
  hasTechnologyObjects,
  hasGeopoliticsObjects,
  hasMarketizationObjects,
  hasMassificationObjects,
} = storeToRefs(useResponseStore())
const {
  responsesEnabled,
} = storeToRefs(useDisplayStore())

</script>

<template>
  <h1 class="h3 text-center">Futures</h1>
  <div class="alert alert-info mt-3" role="alert" v-if="!responsesEnabled">
    New responses are currently not being collected
  </div>
  <p>Below is the collection of all the responses submitted to the crisis typology cards on the timeline organised according to the six key types of crises. Feel free to explore the responses to see what other university futures visitors have imagined. If you haven’t already, please explore the Unfinished Timeline and submit your own university futures. </p>

  <h2 class="h4 mt-5">Crisis of Knowledge</h2>
  <button type="button" class="btn btn-primary"
    @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.knowledge)"
    :disabled="!hasKnowledgeObjects"
    title="View responses for this crisis"
  >View Responses</button>

  <h2 class="h4 mt-5">Crisis of Geopolitics</h2>
  <button type="button" class="btn btn-primary"
    @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.geopolitics)"
    :disabled="!hasGeopoliticsObjects"
    title="View responses for this crisis"
  >View Responses</button>

  <h2 class="h4 mt-5">Crisis of Restitution</h2>
  <button type="button" class="btn btn-primary"
    @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.restitution)"
    :disabled="!hasRestitutionObjects"
    title="View responses for this crisis"
  >View Responses</button>

  <h2 class="h4 mt-5">Crisis of Technology</h2>
  <button type="button" class="btn btn-primary"
    @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.technology)"
    :disabled="!hasTechnologyObjects"
    title="View responses for this crisis"
  >View Responses</button>

  <h2 class="h4 mt-5">Crisis of Massification</h2>
  <button type="button" class="btn btn-primary"
    @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.massification)"
    :disabled="!hasMassificationObjects"
    title="View responses for this crisis"
  >View Responses</button>

  <h2 class="h4 mt-5">Crisis of Marketization</h2>
  <button type="button" class="btn btn-primary"
    @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.marketization)"
    :disabled="!hasMarketizationObjects"
    title="View responses for this crisis"
  >View Responses</button>
</template>

<style scoped>
</style>