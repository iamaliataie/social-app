<script setup>
import { ref } from 'vue';

const emit = defineEmits(['actionCapture'])

const query = ref('')

const handleSubmit = () => {
    emit('actionCapture', query.value)
}

</script>

<template>
    <div class="bg-white rounded-md p-4">
        <form @submit.prevent="handleSubmit" class="flex items-center gap-4">
            <input type="text" v-model="query" class="bg-gray-100 w-full px-3 py-2 rounded-md focus:outline-none" placeholder="seach here">
            <button type="submit" class="bg-purple-500 text-white rounded-md px-3 py-2">Search</button>
        </form>
    </div>
</template>