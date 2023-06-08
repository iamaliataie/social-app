<script setup>
import FeedList from '../components/FeedList.vue'
import FriendSuggestions from '@/components/FriendSuggestions.vue'
import { useUserStore } from '../stores/user'
import { onMounted } from 'vue';
import axios from 'axios';

const userStore = useUserStore();

const handleEmit = (post)=>{
  userStore.posts.unshift(post);
}

const getData = () => {
  axios.get('api/posts/')
  .then(res =>{
    userStore.posts = res.data;
  })
  .catch(error => {console.log(error);})
}

onMounted(() => {
  getData();
})

</script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-5 gap-6">
    <div class="md:col-span-3">
      <FeedList/>
    </div>
    <div class="md:col-span-2">
      <FriendSuggestions />
    </div>
  </div>
</template>