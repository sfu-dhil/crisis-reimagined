import { defineStore } from 'pinia'

export const useDisplayStore = defineStore('display', {
  state: () => ({
    responsesEnabled: true,

    knowledgeQuestionnaireModalShown: false,
    knowledgeResponsesModalShown: false,

    restitutionQuestionnaireModalShown: false,
    restitutionResponsesModalShown: false,

    massificationQuestionnaireModalShown: false,
    massificationResponsesModalShown: false,

    technologyQuestionnaireModalShown: false,
    technologyResponsesModalShown: false,

    marketizationQuestionnaireModalShown: false,
    marketizationResponsesModalShown: false,

    geopoliticsQuestionnaireModalShown: false,
    geopoliticsResponsesModalShown: false,
  }),
  getters: {},
  actions: {
    _hideAllModals() {
      this.knowledgeQuestionnaireModalShown = false
      this.knowledgeResponsesModalShown = false

      this.restitutionQuestionnaireModalShown = false
      this.restitutionResponsesModalShown = false

      this.massificationQuestionnaireModalShown = false
      this.massificationResponsesModalShown = false

      this.technologyQuestionnaireModalShown = false
      this.technologyResponsesModalShown = false

      this.marketizationQuestionnaireModalShown = false
      this.marketizationResponsesModalShown = false

      this.geopoliticsQuestionnaireModalShown = false
      this.geopoliticsResponsesModalShown = false
    },
    showKnowledgeQuestionnaireModal() {
      this._hideAllModals()
      this.knowledgeQuestionnaireModalShown = true
    },
    showKnowledgeResponsesModal() {
      this._hideAllModals()
      this.knowledgeResponsesModalShown = true
    },
  },
  persist: false,
})