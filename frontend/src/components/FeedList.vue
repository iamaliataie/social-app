<script setup>
import PostForm from './PostForm.vue';
import FeedItem from './FeedItem.vue';
import { useUserStore } from '../stores/user';
import { useRoute } from 'vue-router';
const route = useRoute();
const userStore = useUserStore();
const props = defineProps(['posts']);

</script>
<template>
    <div class="flex flex-col space-y-4">
        <PostForm v-if="!route.params.id || userStore.user.id == route.params.id"/>
        <FeedItem v-for="(post, index) in props.posts" :key="index" :post="post"/>
    </div>
</template>