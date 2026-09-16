import { Offcanvas, Modal, Tooltip } from 'bootstrap'
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

export const toggleOffcanvas = (offcanvasEl, show) => {
  if (offcanvasEl) {
    const bsOffcanvas = Offcanvas.getOrCreateInstance(offcanvasEl)
    // set timeout of 25 to make sure the offcanvas content is loaded before animating
    setTimeout(() => show ? bsOffcanvas.show() : bsOffcanvas.hide(), 25)
  }
}

export const toggleModal = (modalEl, show) => {
  if (modalEl) {
    const bsModal = Modal.getOrCreateInstance(modalEl)
    show ? bsModal.show() : bsModal.hide()
  }
}

export const resetTooltips = (parentEl) => {
  if (parentEl) {
    parentEl.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(
      (tooltipTriggerEl) => Tooltip.getOrCreateInstance(tooltipTriggerEl, {container: parentEl}).hide()
    )
  }
}