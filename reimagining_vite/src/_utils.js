import { Modal } from 'bootstrap'
import Cookies from 'js-cookie'

export const _submitForm = async (request, formData) => {
  try {
    const csrftoken = Cookies.get('csrftoken')
    const response = await fetch(request, {
        headers: { 'X-CSRFToken': csrftoken },
        method: 'POST',
        mode: 'cors',
        body: formData,
      })
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`)
    }
    return await response.json()
  } catch (error) {
    console.error('Error submitting form:', error)
  }
}

export const toggleModal = (modalEl, show) => {
  if (modalEl) {
    const bsModal = Modal.getOrCreateInstance(modalEl)
    show ? bsModal.show() : bsModal.hide()
  }
}
