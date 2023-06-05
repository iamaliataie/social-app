<script setup>
import { useUserStore } from "../stores/user";

const userStore = useUserStore();


</script>
<template>
    <div class="bg-white p-6 rounded-md">
        <div v-for="(post, index) in userStore.posts" :key="index">{{ post }}</div>
        <div class="flex flex-col space-y-6">
        <div class="flex flex-row items-center justify-between">
            <div class="flex items-center gap-4">
            <img src="../assets/images/self2.jpg" alt="user" class="w-12 rounded-full">
            <h1 class="text-xl font-semibold">Ali Ahmad Ataie</h1>
            </div>
            <span>12 minutes ago</span>
        </div>
        <div class="flex-col space-y-4">
            <img src="../assets/images/self2.jpg" alt="" class="w-full">
            <p class="text-justify">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quidem vero, delectus quod illum natus sit nam est non nihil unde officiis sapiente, dolores eum numquam iste debitis, facere veniam ex.</p>
        </div>
        <div class="flex gap-4 items-center">
            <div class="flex gap-2 items-center">
            <div class="w-4 h-4 bg-purple-400"></div>
            <span>20 likes</span>
            </div>
            <div class="flex gap-2 items-center">
            <div class="w-4 h-4 bg-purple-400"></div>
            <span>12 comments</span>
            </div>
        </div>
        </div>
    </div>
</template>