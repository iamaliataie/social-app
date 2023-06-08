<script setup>

import { useToastStore } from '../stores/toast'

const toastStore = useToastStore();

</script>
<template>
    <div 
    class="fixed right-6 top-full text-white p-3 rounded-md transition duration-500 ease-in-out"
    :class="[toastStore.toastClasses ,{'-translate-y-[70px]': toastStore.visible}]"
    >
        <p>{{ toastStore.toastMessage }}</p>
    </div>
</template>