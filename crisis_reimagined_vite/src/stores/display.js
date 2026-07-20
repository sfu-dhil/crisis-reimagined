import { defineStore } from 'pinia'

export const useDisplayStore = defineStore('display', {
  state: () => ({
    responsesEnabled: true,

    questionnaireModalShown: false,
    responsesModalShown: false,
    resourceType: null,
  }),
  getters: {},
  actions: {
    _reset() {
      this.questionnaireModalShown = false
      this.responsesModalShown = false
      this.resourceType = null
    },
    showQuestionnaireModal(resourceType) {
      this._reset()
      this.questionnaireModalShown = true
      this.resourceType = resourceType
    },
    showResponsesModal(resourceType) {
      this._reset()
      this.responsesModalShown = true
      this.resourceType = resourceType
    },
  },
  persist: false,
})