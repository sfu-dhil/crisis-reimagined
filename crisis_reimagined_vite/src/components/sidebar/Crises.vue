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
  <h1 class="h3 text-center">Crises</h1>
  <div class="alert alert-info mt-3" role="alert" v-if="!responsesEnabled">
    New responses are currently not being collected
  </div>

  <h2 class="h4 mt-5">Crisis of Knowledge</h2>
  <p>What is knowledge, and what roles does the university play in shaping and sustaining it?</p>
  <div class="d-flex">
    <button type="button" class="btn btn-primary"
      @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.knowledge)"
      :disabled="!responsesEnabled"
      title="Respond to this crisis"
    ><i class="bi bi-pencil-square"></i> Respond</button>
    <button type="button" class="btn btn-primary ms-3"
      @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.knowledge)"
      :disabled="!hasKnowledgeObjects"
      title="View responses for this crisis"
    ><i class="bi bi-card-text"></i> View Responses</button>
  </div>

  <h2 class="h4 mt-5">Crisis of Geopolitics</h2>
  <p>How does the university both respond to and shape the economic, political, and environmental forces that define society?</p>
  <div class="d-flex">
    <button type="button" class="btn btn-primary"
      @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.geopolitics)"
      :disabled="!responsesEnabled"
      title="Respond to this crisis"
    ><i class="bi bi-pencil-square"></i> Respond</button>
    <button type="button" class="btn btn-primary ms-3"
      @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.geopolitics)"
      :disabled="!hasGeopoliticsObjects"
      title="View responses for this crisis"
    ><i class="bi bi-card-text"></i> View Responses</button>
  </div>

  <h2 class="h4 mt-5">Crisis of Restitution</h2>
  <p>How does the university redress historic forms of discrimination and exclusion?</p>
  <div class="d-flex">
    <button type="button" class="btn btn-primary"
      @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.restitution)"
      :disabled="!responsesEnabled"
      title="Respond to this crisis"
    ><i class="bi bi-pencil-square"></i> Respond</button>
    <button type="button" class="btn btn-primary ms-3"
      @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.restitution)"
      :disabled="!hasRestitutionObjects"
      title="View responses for this crisis"
    ><i class="bi bi-card-text"></i> View Responses</button>
  </div>

  <h2 class="h4 mt-5">Crisis of Technology</h2>
  <p>How do information and communication technologies enable and constrain the university?</p>
  <div class="d-flex">
    <button type="button" class="btn btn-primary"
      @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.technology)"
      :disabled="!responsesEnabled"
      title="Respond to this crisis"
    ><i class="bi bi-pencil-square"></i> Respond</button>
    <button type="button" class="btn btn-primary ms-3"
      @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.technology)"
      :disabled="!hasTechnologyObjects"
      title="View responses for this crisis"
    ><i class="bi bi-card-text"></i> View Responses</button>
  </div>

  <h2 class="h4 mt-5">Crisis of Massification</h2>
  <p>Who is the university for? Who should have access to it?</p>
  <div class="d-flex">
    <button type="button" class="btn btn-primary"
      @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.massification)"
      :disabled="!responsesEnabled"
      :title="responsesEnabled ? 'Respond to this crisis' : 'New responses are currently not being collected at this time'"
    ><i class="bi bi-pencil-square"></i> Respond</button>
    <button type="button" class="btn btn-primary ms-3"
      @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.massification)"
      :disabled="!hasMassificationObjects"
      title="View responses for this crisis"
    ><i class="bi bi-card-text"></i> View Responses</button>
  </div>

  <h2 class="h4 mt-5">Crisis of Marketization</h2>
  <p>How are the university's intellectual freedoms threatened by creeping managerialism?</p>
  <div class="d-flex">
    <button type="button" class="btn btn-primary"
      @click="() => useDisplayStore().showQuestionnaireModal(ResponseResourceTypes.marketization)"
      :disabled="!responsesEnabled"
      title="Respond to this crisis"
    ><i class="bi bi-pencil-square"></i> Respond</button>
    <button type="button" class="btn btn-primary ms-3"
      @click="() => useDisplayStore().showResponsesModal(ResponseResourceTypes.marketization)"
      :disabled="!hasMarketizationObjects"
      title="View responses for this crisis"
    ><i class="bi bi-card-text"></i> View Responses</button>
  </div>
</template>

<style scoped>
</style>