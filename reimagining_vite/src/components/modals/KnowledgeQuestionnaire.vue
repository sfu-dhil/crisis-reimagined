<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'
import { storeToRefs } from 'pinia'
import { vMaska } from 'maska/vue'
import { _submitForm, toggleModal } from '../../_utils.js'
import { useDisplayStore } from '../../stores/display.js'
import { useResponseStore } from '../../stores/responses.js'
import { ResponseResourceTypes } from '../../_resourceTypes.js'

const {
  knowledgeQuestionnaireModalShown: shown,
  responsesEnabled,
} = storeToRefs(useDisplayStore())

const modalRef = ref(null)
const formRef = ref(null)
const year = ref('00')
const question_1 = ref(null)
const question_2 = ref(null)

const submit = (e) => {
  if (formRef.value && formRef.value.checkValidity()) {
    e.preventDefault()
    nextTick( async () => {
      const formData = new FormData(formRef.value)
      // fix year
      formData.set('year', 2100 + parseInt(formData.get('year')))
      // add resource type
      formData.append('resourcetype', ResponseResourceTypes.knowledge)
      const object = await _submitForm('/api/responses', formData)
      console.log('object', object)
      if (object && object.id) {
        toggleModal(modalRef.value, false)
        useResponseStore().addOwnResponse(object)
      }
    })
  }
}
const resetForm = () => {
  year.value = '00'
  question_1.value = null
  question_2.value = null
}
watch(shown, (newValue, oldValue) => {
  if (newValue !== oldValue) {
    toggleModal(modalRef.value, newValue)
    if (!newValue) {
      resetForm()
    }
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
          <div class="modal-title">Knowledge Questionnaire WIP</div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body py-0">
          <div class="alert alert-warning mt-3" role="alert" v-if="!responsesEnabled">
            The questionnaire is currently disabled
          </div>
          <form ref="formRef">
            <div class="mb-3">
              <label for="knowledge-questionnaire-year" class="form-label">In the year</label>
              <div class="input-group">
                <label for="knowledge-questionnaire-year" class="input-group-text">21</label>
                <input
                  id="knowledge-questionnaire-year" name="year" type="text" class="form-control" required
                  v-maska="'##'" placeholder="00" inputmode="numeric"
                  v-model="year"
                  :disabled="!responsesEnabled"
                />
              </div>
            </div>
            <div class="mb-3">
              <label for="knowledge-questionnaire-question-1" class="form-label">What counts as knowledge in this future?</label>
              <textarea
                id="knowledge-questionnaire-question-1" name="question_1" class="form-control" rows="4" required
                v-model="question_1"
                :disabled="!responsesEnabled"
              ></textarea>
            </div>
            <div class="mb-3">
              <label for="knowledge-questionnaire-question-2" class="form-label">What has the university become?</label>
              <textarea
                id="knowledge-questionnaire-question-2" name="question_2" class="form-control" rows="4" required
                v-model="question_2"
                :disabled="!responsesEnabled"
              ></textarea>
            </div>
            <button
              type="submit" class="btn btn-primary mb-3"
              @click="submit"
              :disabled="!responsesEnabled"
            >Submit</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
</style>