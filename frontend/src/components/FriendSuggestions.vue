<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';

const suggessions = ref([])
const getFriendSuggesstions = () => {
    axios.get('api/friend_suggesstions/')
    .then(res => {
        suggessions.value = res.data
    })
    .catch(error => {
        console.log('error : ', error);
    })
}

onMounted(() => {
    getFriendSuggesstions();
})

</script>

<template>
    <div class="bg-white flex flex-col space-y-4 p-4 rounded-md">
        <h2 class="text-xl">Friend Suggestions</h2>
        <div 
        v-for="user in suggessions"
        class="flex items-cener justify-between">
            <div class="flex items-center space-x-4">
            <img :src="user.get_avatar" alt="user" class="w-12 rounded-full">
            <h1 class="font-semibold text-xl">{{ user.name }}</h1>
            </div>
            <RouterLink :to="{name: 'profile', params: {'id': user.id}}" class="bg-purple-500 text-white p-2 rounded-md flex items-center">Show</RouterLink>
        </div>
    </div>
</template>
