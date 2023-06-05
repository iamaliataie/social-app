<script setup>
import FeedList from '../components/FeedList.vue'
import FriendSuggestions from '@/components/FriendSuggestions.vue'
import { useUserStore } from '../stores/user'

const userStore = useUserStore();

const handleEmit = (post)=>{
  userStore.posts.unshift(post);
}

</script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-5 gap-6">
    <div class="md:col-span-3">
      <FeedList @clickEmit="(post)=>handleEmit(post)"/>
    </div>
    <div class="md:col-span-2">
      <FriendSuggestions />
    </div>
  </div>
</template>