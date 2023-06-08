<script setup>
import PostForm from './PostForm.vue';
import FeedItem from './FeedItem.vue';
import { useUserStore } from '../stores/user';

const userStore = useUserStore();

</script>
<template>
    <div class="flex flex-col space-y-4">
        <PostForm />
        <FeedItem v-for="(post, index) in userStore.posts" :key="index" :post="post"/>
    </div>
</template>