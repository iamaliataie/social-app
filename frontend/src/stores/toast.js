import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useToastStore = defineStore('toast', () => {

    const toastMessage = ref('')
    const toastClasses = ref('')
    const visible = ref(false)

    const showToast = (message, classes) => {
        visible.value = true;
        toastMessage.value = message;
        toastClasses.value = classes + ' ';
        
        setTimeout(()=>{
            visible.value = false;
        }, 2000)
    }

  return { visible, toastMessage, toastClasses, showToast }
})
