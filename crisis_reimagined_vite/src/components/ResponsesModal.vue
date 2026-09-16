<script setup>
import { ref, onMounted, watch, computed } from 'vue'
import { storeToRefs } from 'pinia'
import { toggleModal } from '../_utils.js'
import GeopoliticsSvg from './GeopoliticsSvg.vue'
import KnowledgeSVG from './KnowledgeSvg.vue'
import MarketizationSvg from './MarketizationSvg.vue'
import MassificationSvg from './MassificationSvg.vue'
import RestitutionSvg from './RestitutionSvg.vue'
import TechnologySvg from './TechnologySvg.vue'
import { useDisplayStore } from '../stores/display.js'
import { useResponseStore } from '../stores/responses.js'
import { ResponseResourceTypes } from '../_resourceTypes.js'

const fade = {
  initial: {
    opacity: 0,
  },
  enter: {
    opacity: 1,
  },
}
const slideLeft = {
  initial: {
    x: -500,
    opacity: 0,
  },
  enter: {
    x: 0,
    opacity: 1,
  },
}
const slideRight = {
  initial: {
    x: 500,
    opacity: 0,
  },
  enter: {
    x: 0,
    opacity: 1,
  },
}

const {
  responsesModalShown: shown,
  resourceType,
} = storeToRefs(useDisplayStore())
const {
  knowledgeObjects,
  restitutionObjects,
  technologyObjects,
  geopoliticsObjects,
  marketizationObjects,
  massificationObjects,
} = storeToRefs(useResponseStore())

const modalRef = ref(null)
const motionGroupPreset = ref(fade)
const currentObjectIndex = ref(0)
const changeIncrement = ref(0)
const objects = computed(() => {
  switch (resourceType.value) {
    case ResponseResourceTypes.knowledge: return knowledgeObjects.value
    case ResponseResourceTypes.restitution: return restitutionObjects.value
    case ResponseResourceTypes.technology: return technologyObjects.value
    case ResponseResourceTypes.geopolitics: return geopoliticsObjects.value
    case ResponseResourceTypes.marketization: return marketizationObjects.value
    case ResponseResourceTypes.massification: return massificationObjects.value
    default: return []
  }
})
const previous = () => {
  if (currentObjectIndex.value - 1 >= 0) {
    changeIncrement.value += 1
    motionGroupPreset.value = slideLeft
    currentObjectIndex.value -= 1
  }
}
const next = () => {
  if (currentObjectIndex.value + 1 < objects.value.length) {
    changeIncrement.value += 1
    motionGroupPreset.value = slideRight
    currentObjectIndex.value += 1
  }
}
const currentObject = computed(() => currentObjectIndex.value < objects.value.length ? objects.value[currentObjectIndex.value] : null)
watch(objects, (newValue, oldValue) => {
  if (newValue !== oldValue) {
    motionGroupPreset.value = fade
    currentObjectIndex.value = 0
  }
})

watch(shown, (newValue, oldValue) => {
  if (newValue !== oldValue) {
    toggleModal(modalRef.value, newValue)
    motionGroupPreset.value = fade
    currentObjectIndex.value = 0
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
          <button type="button" class="btn-close text-dark bg-white position-fixed z-3 top-0 end-0 m-3 p-2" data-bs-dismiss="modal" aria-label="Close"></button>
          <button
            class="d-none d-xxl-block control-prev position-fixed top-0 bottom-0 start-0 z-2" type="button"
            v-if="currentObjectIndex > 0"
            @click="previous"
          >
            <span class="control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <div class="takeaway-container d-flex flex-column mx-auto my-3" v-if="currentObject" :key="currentObject.id">
            <div class="alert alert-info mb-3" role="alert" v-if="currentObject.pending">
              Your response is awaiting approval
            </div>
            <Motion
              is="div" class="position-relative flex-grow-1 w-100 d-flex flex-row"
              :duration="300"
              :initial="motionGroupPreset.initial"
              :enter="motionGroupPreset.enter"
              :visible="motionGroupPreset.visible"
              :visible-once="motionGroupPreset.visibleOnce"
              :hovered="motionGroupPreset.hovered"
              :focused="motionGroupPreset.focused"
              :tapped="motionGroupPreset.tapped"
            >
              <GeopoliticsSvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.geopolitics"
                :key="currentObject.id" :object="currentObject"
              />
              <KnowledgeSVG class="w-100"
                v-if="resourceType === ResponseResourceTypes.knowledge"
                :key="currentObject.id" :object="currentObject"
              />
              <MarketizationSvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.marketization"
                :key="currentObject.id" :object="currentObject"
              />
              <MassificationSvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.massification"
                :key="currentObject.id" :object="currentObject"
              />
              <RestitutionSvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.restitution"
                :key="currentObject.id" :object="currentObject"
              />
              <TechnologySvg class="w-100"
                v-if="resourceType === ResponseResourceTypes.technology"
                :key="currentObject.id" :object="currentObject"
              />
            </Motion>
            <div class="d-xxl-none d-flex w-100 mt-2">
              <button type="button" class="btn btn-primary me-auto"
                v-if="currentObjectIndex > 0"
                @click="previous"
              ><i class="bi bi-chevron-left"></i> Previous
              </button>
              <button type="button" class="btn btn-primary ms-auto"
                v-if="currentObjectIndex < objects.length - 1"
                @click="next"
              >Next <i class="bi bi-chevron-right"></i>
              </button>
            </div>
          </div>
          <button
            class="d-none d-xxl-block control-next position-fixed top-0 bottom-0 end-0 z-2" type="button"
            v-if="currentObjectIndex < objects.length - 1"
            @click="next"
          >
            <span class="control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
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
.control-next, .control-prev {
  width: 5%;
  border: 0;
  filter: var(invert(1) grayscale(100));
}
.control-prev-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0'/%3e%3c/svg%3e");
}
.control-next-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708'/%3e%3c/svg%3e");
}
.control-prev-icon,
.control-next-icon {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  background-repeat: no-repeat;
  background-position: 50%;
  background-size: 100% 100%;
}
</style>