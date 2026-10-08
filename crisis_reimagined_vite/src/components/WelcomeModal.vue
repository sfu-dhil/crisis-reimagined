<script setup>
import { ref, onMounted, watch } from 'vue'
import { storeToRefs } from 'pinia'
import { useDisplayStore } from '../stores/display.js'
import { toggleModal } from '../_utils.js'

import FillInTakeawayImageUrl from '../assets/img/instructions/fill-in-takeaways.png'
import ViewResponsesImageUrl from '../assets/img/instructions/view-responses.png'

const {
  welcomeModalShown: shown,
} = storeToRefs(useDisplayStore())

const modalRef = ref(null)

watch(shown, (newValue, oldValue) => {
  if (newValue !== oldValue) { toggleModal(modalRef.value, newValue) }
})
onMounted(() => {
  useDisplayStore().forceShowInitialWelcomeMessage()
  toggleModal(modalRef.value, shown.value)
  modalRef.value.addEventListener('hidden.bs.modal', () => {
    shown.value = false
  })
  modalRef.value.addEventListener('shown.bs.modal', () => shown.value = true)
})
</script>

<template>
  <div ref="modalRef" class="modal fade" data-bs-backdrop="static" tabindex="-1">
    <div class="modal-dialog modal-fullscreen-lg-down modal-lg modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header align-items-start">
          <div class=w-100>
            <h1 class="modal-title text-center">Welcome to Reimagining the Public University - Digital Edition</h1>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <figure class="figure w-100">
            <img
              class="figure-img w-100 object-fit-contain m-0"
              :src="FillInTakeawayImageUrl"
              alt="Fill in Takeaways"
              loading="lazy" fetchpriority="low"
            />
            <figcaption class="figure-caption text-center">Click on one of the crisis takeaways to leave a response</figcaption>
          </figure>
          <figure class="figure w-100">
            <img
              class="figure-img w-100 object-fit-contain m-0"
              :src="ViewResponsesImageUrl"
              alt="View Responses"
              loading="lazy" fetchpriority="low"
            />
            <figcaption class="figure-caption text-center">Click on one of the crisis responses to view all responses for that crisis</figcaption>
          </figure>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary ms-auto" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
</style>