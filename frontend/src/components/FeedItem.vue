<script setup>
import axios from "axios";
import { useUserStore } from "../stores/user";

const userStore = useUserStore(); 
const props = defineProps(['post'])

const handleLike = (postId) => {
    axios.post(`api/posts/${postId}/like_post/`)
    .then(res => {
        props.post.likes = res.data.likes;
    })
    .catch()
}

</script>
<template>
    <div class="bg-white p-6 rounded-md">
        <div class="flex flex-col space-y-6">
        <div class="flex flex-row items-center justify-between">
            <div class="flex items-center gap-4">
            <img :src="post.created_by.get_avatar" alt="user" class="w-12 rounded-full">
            <RouterLink :to="{name: 'profile', params:{'id': post.created_by.id}}" class="text-xl font-semibold">{{ post.created_by.name }}</RouterLink>
            </div>
            <span>{{ post.created_at_formatted }} ago</span>
        </div>
        <div class="flex-col space-y-4">
            <img
            :src="post.get_image" alt="" class="w-full">
            <p class="text-justify">{{ post.body }}</p>
        </div>
        <div class="flex gap-4 items-center">
            <button 
            @click="handleLike(post.id)"
            class="flex gap-2 items-center">
                <div :class="['w-4 h-4 border border-purple-400', {'bg-purple-400': post.likes.includes(userStore.user.id)}]"></div>
                <span>{{ post.likes.length }} - {{ post.likes.includes(userStore.user.id) ? 'liked': 'likes' }}</span>
            </button>
            <RouterLink 
            :to="{name: 'detail', params:{'id': post.id}}"
            class="flex gap-2 items-center">
                <div class="w-4 h-4 bg-purple-400"></div>
                <span>{{ post.comments.length }} comments</span>
            </RouterLink>
        </div>
        </div>
    </div>
</template>