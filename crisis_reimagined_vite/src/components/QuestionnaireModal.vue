<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'
import { storeToRefs } from 'pinia'
import { _submitForm, toggleModal } from '../_utils.js'
import GeopoliticsSvg from './GeopoliticsSvg.vue'
import KnowledgeSvg from './KnowledgeSvg.vue'
import MarketizationSvg from './MarketizationSvg.vue'
import MassificationSvg from './MassificationSvg.vue'
import RestitutionSvg from './RestitutionSvg.vue'
import TechnologySvg from './TechnologySvg.vue'
import { useDisplayStore } from '../stores/display.js'
import { useResponseStore } from '../stores/responses.js'
import { ResponseResourceTypes } from '../_resourceTypes.js'

const {
  questionnaireModalShown: shown,
  responsesEnabled,
  resourceType,
} = storeToRefs(useDisplayStore())

const modalRef = ref(null)
const formRef = ref(null)
const popupIncrement = ref(0)

const submit = (e) => {
  if (formRef.value && formRef.value.checkValidity()) {
    e.preventDefault()
    nextTick( async () => {
      const formData = new FormData(formRef.value)
      // add resource type
      formData.append('resourcetype', resourceType.value)
      const object = await _submitForm('/api/responses', formData)
      if (object && object.id) {
        toggleModal(modalRef.value, false)
        useResponseStore().addOwnResponse(object)
      }
    })
  }
}
watch(shown, (newValue, oldValue) => {
  if (newValue !== oldValue) {
    toggleModal(modalRef.value, newValue)
    popupIncrement.value += 1
  }
})
onMounted(() => {
  toggleModal(modalRef.value, shown.value)
  modalRef.value.addEventListener('hidden.bs.modal', () => shown.value = false)
  modalRef.value.addEventListener('shown.bs.modal', () => shown.value = true)
})
</script>
<template>
  <div ref="modalRef" class="modal fade" tabindex="-1" data-bs-backdrop="static" data-bs-theme="light">
    <div class="modal-dialog modal-fullscreen modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-body p-0">
          <button type="button" class="btn-close bg-white position-fixed z-3 top-0 end-0 m-3 p-2" data-bs-dismiss="modal" aria-label="Close"></button>
          <form ref="formRef" class="takeaway-container d-flex flex-column mx-auto">
            <div class="alert alert-info mt-3" role="alert" v-if="!responsesEnabled">
              New responses are currently not being collected
            </div>
            <div class="position-relative flex-grow-1 w-100">
              <GeopoliticsSvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.geopolitics"
                :key="popupIncrement" :editMode="!!responsesEnabled"
              />
              <KnowledgeSvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.knowledge"
                :key="popupIncrement" :editMode="!!responsesEnabled"
              />
              <MarketizationSvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.marketization"
                :key="popupIncrement" :editMode="!!responsesEnabled"
              />
              <MassificationSvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.massification"
                :key="popupIncrement" :editMode="!!responsesEnabled"
              />
              <RestitutionSvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.restitution"
                :key="popupIncrement" :editMode="!!responsesEnabled"
              />
              <TechnologySvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.technology"
                :key="popupIncrement" :editMode="!!responsesEnabled"
              />
              <div class="d-none d-lg-block position-absolute bottom-0 end-0">
                <button
                  type="submit" class="btn btn-primary btn-lg px-5 me-3 ms-auto"
                  @click="submit"
                  :disabled="!responsesEnabled"
                >Save</button>
              </div>
              <div class="d-block d-lg-none text-end w-100 mt-2">
                <button
                  type="submit" class="btn btn-primary btn-lg px-5"
                  @click="submit"
                  :disabled="!responsesEnabled"
                >Save</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.takeaway-container {
  max-width: 800px;
}
.modal {
  --bs-modal-bg: transparent;
  .btn-close {
    --bs-btn-close-opacity: 1;
  }
}
</style>