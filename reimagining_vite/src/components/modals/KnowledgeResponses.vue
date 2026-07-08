<script setup>
import { ref, onMounted, watch, nextTick, computed } from 'vue'
import { storeToRefs } from 'pinia'
import { _submitForm, toggleModal } from '../../_utils.js'
import { useDisplayStore } from '../../stores/display.js'
import { useResponseStore } from '../../stores/responses.js'
import { ResponseResourceTypes } from '../../_resourceTypes.js'

const {
  knowledgeResponsesModalShown: shown,
} = storeToRefs(useDisplayStore())
const {
  knowledgeObjects: objects,
} = storeToRefs(useResponseStore())


console.log('objects', objects.value)

const modalRef = ref(null)
const currentObjectIndex = ref(0)
const object = computed(() => currentObjectIndex.value < objects.value.length ? objects.value[currentObjectIndex.value] : null)

watch(objects, (newValue, oldValue) => {
  if (newValue !== oldValue) {
    currentObjectIndex.value = 0
  }
})
watch(shown, (newValue, oldValue) => {
  if (newValue !== oldValue) {
    toggleModal(modalRef.value, newValue)
  }
})
onMounted(() => {
  toggleModal(modalRef.value, shown.value)
  modalRef.value.addEventListener('hidden.bs.modal', () => shown.value = false)
  modalRef.value.addEventListener('shown.bs.modal', () => shown.value = true)
})
</script>
<template>
  <div ref="modalRef" class="modal fade" tabindex="-1" data-bs-backdrop="static">
    <div class="modal-dialog modal-fullscreen-lg-down modal-xl modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header align-items-start">
          <div class="modal-title">Knowledge Takeaways WIP</div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body py-0" v-if="!object">
          There are no Knowledge takeaways yet
        </div>
        <div class="modal-body py-0" v-if="object">
          <div class="alert alert-warning mt-3" role="alert" v-if="object.pending">
            Your response is awaiting approval
          </div>
          <p>
            In the year {{ object.year }}
          </p>
          <p>What counts as knowledge in this future?</p>
          <p>{{ object.question_1 }}</p>
          <p>What has the university become?</p>
          <p>{{ object.question_2 }}</p>
        </div>
        <div class="modal-footer" v-if="object && objects.length > 1">
          <button
            type="button" class="btn btn-primary me-auto"
            v-if="currentObjectIndex !== 0"
            @click="() => currentObjectIndex -= 1"
          >Previous</button>
          <button
            type="button" class="btn btn-primary ms-auto"
            v-if="currentObjectIndex !== objects.length - 1"
            @click="() => currentObjectIndex += 1"
          >Next</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
</style>