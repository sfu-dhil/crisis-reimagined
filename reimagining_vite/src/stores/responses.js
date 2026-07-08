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
    restitutionObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.restitution),
    technologyObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.technology),
    geopoliticsObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.geopolitics),
    marketizationObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.marketization),
    massificationObjects: (state) => state.objects.filter((o) => o.resourcetype === ResponseResourceTypes.massification),
  },
  actions: {
    initOwnResponses() {
      console.log('this.ownObjects', this.ownObjects)
      this.ownObjects.forEach((ownResponse) => {
        if (!this.objectMap.get(ownResponse.id)) {
          this.objects.unshift({ ...ownResponse, pending: true })
        }
      })
    },
    initData(responses) {
      this.objects = [...responses]
      console.log('this.objects', this.objects)
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