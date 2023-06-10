<script setup>
import { reactive } from 'vue';

const props = defineProps(['people', 'title', 'handleRequest'])

</script>
<template>
    <div class="bg-white p-4 rounded-lg">
        <p v-if="title" class="text-2xl mb-6">{{ title }}</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-4">
            <div 
            v-for="user in props.people"
            class="flex flex-col space-y-4 items-center shadow-md border p-2 rounded-md">
                <img src="../assets/images/self2.jpg" alt="user" class="w-36 rounded-full">
                <RouterLink :to="{name: 'profile', params:{'id': handleRequest ? user.created_by.id : user.id}}" class="text-xl md:text-sm lg:text-xl font-bold">{{ handleRequest ? user.created_by.name : user.name }}</RouterLink>
                <div class="flex items-center justify-between w-full text-gray-600 text-sm md:text-xs lg:text-sm">
                    <span>{{ handleRequest ? user.created_by.friends.length : user.friends.length }} friends</span>
                    <span>{{ handleRequest ? user.created_by.posts.length : user.posts.length }} posts</span>
                </div>
                <div v-if="handleRequest && handleRequest.status" class="flex w-full items-center gap-2">
                    <button @click="handleRequest.method(user.created_by.id, 'accept')" class="w-full text-sm text-white bg-green-500 px-3 py-2 rounded-md">Accept</button>
                    <button @click="handleRequest.method(user.created_by.id, 'reject')" class="w-full text-sm text-white bg-red-500 px-3 py-2 rounded-md">Reject</button>
                </div>
            </div>
        </div>
    </div>
</template>