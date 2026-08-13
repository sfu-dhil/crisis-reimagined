import { defineStore } from 'pinia'
import { ResponseResourceTypes } from '../_resourceTypes'

export const useResponseStore = defineStore('responses-data', {
  state: () => ({
    ownObjects: [],
    objects: [],
  }),
  getters: {
    objectMap: (state) => state.objects.reduce((result, o) => result.set(o.id, o), new Map()),

    knowledgeObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.knowledge),
    hasKnowledgeObjects: (state) => state.knowledgeObjects.length > 0,

    restitutionObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.restitution),
    hasRestitutionObjects: (state) => state.restitutionObjects.length > 0,

    technologyObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.technology),
    hasTechnologyObjects: (state) => state.technologyObjects.length > 0,

    geopoliticsObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.geopolitics),
    hasGeopoliticsObjects: (state) => state.geopoliticsObjects.length > 0,

    marketizationObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.marketization),
    hasMarketizationObjects: (state) => state.marketizationObjects.length > 0,

    massificationObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.massification),
    hasMassificationObjects: (state) => state.massificationObjects.length > 0,
  },
  actions: {
    initOwnResponses() {
      this.ownObjects.forEach((ownResponse) => {
        if (!this.objectMap.get(ownResponse.id)) {
          this.objects.unshift({ ...ownResponse, pending: true })
        }
      })
    },
    initData(responses) {
      this.objects = [...responses]
      // add own responses to be beginning of list if unapproved
      // so you can see your own submitted response within the session
      this.initOwnResponses()
    },
    addOwnResponse(object) {
      this.ownObjects.push(object)
      this.initOwnResponses()
    },
  },
  persist: {
    storage: localStorage,
    pick: ['ownObjects'],
  },
})