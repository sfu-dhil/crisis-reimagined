import { defineStore } from 'pinia'

export const useDisplayStore = defineStore('display', {
  state: () => ({
    responsesEnabled: true,

    welcomeModalShown: false,
    questionnaireModalShown: false,
    responsesModalShown: false,
    resourceType: null,
  }),
  getters: {},
  actions: {
    forceShowInitialWelcomeMessage() {
      if (!document.cookie.split("; ").find((row) => row.startsWith("crisisReimaginedShowInitialWelcomeModal"))) {
        // set cookie to expire 1 day from now
        const exp = (new Date(Date.now() + 86400e3)).toUTCString()
        document.cookie = `crisisReimaginedShowInitialWelcomeModal=true; expires=${exp}; SameSite=None; Secure`
        this.welcomeModalShown = true
      }
    },
    _reset() {
      this.welcomeModalShown = false
      this.questionnaireModalShown = false
      this.responsesModalShown = false
      this.resourceType = null
    },
    showWelcomesModal() {
      this._reset()
      this.welcomeModalShown = true
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
  futures: 'futures',
  privacyPolicy: 'privacyPolicy',
})

export const useDisplaySidebarStore = defineStore('display-sidebar', {
  state: () => ({
    sidebarOffcanvasShown: false,
    sidebarWidth: 400,
    gitRepoLink: null,
    gitRepoLinkText: null,
    activeNav: SideBarNavTypes.about
  }),
  getters: {
    aboutActive: (state) => state.activeNav === SideBarNavTypes.about,
    futuresActive: (state) => state.activeNav === SideBarNavTypes.futures,
    privacyPolicyActive: (state) => state.activeNav === SideBarNavTypes.privacyPolicy,
  },
  actions: {
    showSidebarOffcanvas() {
      this.sidebarOffcanvasShown = true
    },
    showAbout() {
      this.activeNav = SideBarNavTypes.about
    },
    showFutures() {
      this.activeNav = SideBarNavTypes.futures
    },
    showPrivacyPolicy() {
      this.activeNav = SideBarNavTypes.privacyPolicy
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