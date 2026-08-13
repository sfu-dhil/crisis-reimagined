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

export const SideBarNavTypes = Object.freeze({
  about: 'about',
  timeline: 'timeline',
  crises: 'crises',
})

export const useDisplaySidebarStore = defineStore('display-sidebar', {
  state: () => ({
    sidebarWidth: 400,
    gitRepoLink: null,
    gitRepoLinkText: null,
    activeNav: SideBarNavTypes.about
  }),
  getters: {
    aboutActive: (state) => state.activeNav === SideBarNavTypes.about,
    timelineActive: (state) => state.activeNav === SideBarNavTypes.timeline,
    crisesActive: (state) => state.activeNav === SideBarNavTypes.crises,
  },
  actions: {
    showAbout() {
      this.activeNav = SideBarNavTypes.about
    },
    showTimeline() {
      this.activeNav = SideBarNavTypes.timeline
    },
    showCrisis() {
      this.activeNav = SideBarNavTypes.crises
    },
  },
  persist: {
    storage: sessionStorage,
  },
})

export const useDisplayInstallationStore = defineStore('display-installation', {
  state: () => ({
    zoomToElementClassId: null,
  }),
  getters: {},
  actions: {
    zoomToElementByClassIds(elementClassId) {
      this.zoomToElementClassId = elementClassId
    },
  },
  persist: false,
})