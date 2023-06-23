<script setup>
import { onMounted, ref } from 'vue';
import FriendSuggestions from '../components/FriendSuggestions.vue';
import axios from 'axios';
import { RouterLink } from 'vue-router';

const notifications = ref([])

const getNotifications = () => {
    axios.get('api/posts/notifications/')
    .then(res => {
        notifications.value = res.data;
    })
    .catch()
}

onMounted(() => {
    getNotifications();
})

</script>
<template>
    <div class="grid grid-cols-1 md:grid-cols-6 gap-4">
        <div class="md:col-span-4">
            <div class="flex flex-col space-y-4 bg-white p-4 rounded-md max-h-[400px] overflow-scroll">
                <div 
                v-if="notifications.length"
                v-for="notification in notifications" :key="notification.id"
                class="bg-gray-200 p-4 rounded-md"
                >
                    <RouterLink v-if="notification.post || notification.request" 
                    :to="{name: notification.post ? 'detail': 'profile', params: {'id': notification.post ? notification.post.id : notification.request.created_by.id }}" 
                    >
                        {{ notification.body }}
                    </RouterLink>
                    <RouterLink :to="{name: 'profile', params: {'id': notification.created_by.id}}" v-else>{{ notification.body }}</RouterLink>
                </div>
                <div v-else>
                    <p>No notification</p>
                </div>
            </div>
        </div>
        <div class="md:col-span-2">
            <div>
                <FriendSuggestions />
            </div>
        </div>
    </div>    
</template>