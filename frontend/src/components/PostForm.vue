<script setup>
import { ref } from 'vue';
import { useUserStore } from '../stores/user';
const userStore = useUserStore();

const emit = defineEmits(['postSubmit'])

const body = ref('')

const handleSubmit = () => {
    userStore.posts.unshift(body.value)
}

</script>

<template>
    <div class="bg-white p-6 rounded-md">
        <form @submit.prevent="handleSubmit" class="flex flex-col space-y-4">
        <textarea rows="5" v-model="body" class="w-full resize-none bg-gray-100 p-4 rounded-md" placeholder="What are you thinking about, today?"></textarea>
        <div class="flex items-center justify-between">
            <button type="submit" class="bg-purple-500 text-white px-3 py-3 rounded-md">Post</button>
            <input type="file" id="attachment" class="hidden">
            <label for="attachment" class="bg-gray-950 text-white px-3 py-3 rounded-md">Attachments</label>
        </div>
        </form>
    </div>
</template>