<script setup>
import { storeToRefs } from 'pinia'
import { useResponseStore } from './stores/responses.js'
import { useDisplayStore } from './stores/display.js'
import InstallationSvg from './components/InstallationSvg.vue'
import QuestionnaireModal from './components/QuestionnaireModal.vue'
import ResponsesModal from './components/ResponsesModal.vue'

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

useResponseStore().initData(props.responses)
responsesEnabled.value = props.config.responses_enabled
</script>

<template>
  <InstallationSvg />
  <QuestionnaireModal />
  <ResponsesModal />
</template>

<style scoped>
</style>