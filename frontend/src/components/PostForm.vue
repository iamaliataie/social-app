<script setup>
import { reactive, ref } from 'vue';
import axios from 'axios';
import { useUserStore } from '../stores/user';
import { useToastStore } from '../stores/toast';

const userStore = useUserStore();
const toastStore = useToastStore();

const form = reactive({
    body: '',
    image: null
})
const imageUrl = ref('')

const setFile = (el) => {
    form.image = el.target.files[0];
    imageUrl.value = URL.createObjectURL(form.image)
}

const handleSubmit = () => {
    
    axios.post('api/posts/post_create/', form, {
        headers:{
            "Content-Type": "multipart/form-data",
        }
    })
    .then(res => {
        userStore.posts.unshift(res.data);
        userStore.profilePosts.unshift(res.data);
        form.body = ''
        form.image = null
    })
    .catch(error => {
        toastStore.showToast(error.message, 'bg-red-500');
    })
}

</script>

<template>
    <div class="bg-white p-6 rounded-md">
        <form @submit.prevent="handleSubmit" class="flex flex-col space-y-4">
        <textarea rows="5" v-model="form.body" class="w-full resize-none bg-gray-100 p-4 rounded-md focus:outline-none" placeholder="What are you thinking about, today?"></textarea>
        <div class="flex items-center justify-between">
            <button type="submit" class="bg-purple-500 text-white px-3 py-3 rounded-md">Post</button>
            <input @change="setFile" type="file" id="attachment" class="hidden">
            <label for="attachment" class="bg-gray-800 text-white px-3 py-3 rounded-md cursor-pointer hover:bg-gray-950">Attachment</label>
        </div>
        </form>
        <div v-if="form.image" class="mt-6">
            <img :src="imageUrl" alt="image" class="w-32 rounded-md">
        </div>
    </div>
</template>