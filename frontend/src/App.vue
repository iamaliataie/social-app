<script setup>
import { onMounted } from 'vue';
import { useUserStore } from './stores/user'
import axios from 'axios';
import Navbar from './components/Navbar.vue';
import Toast from './components/Toast.vue';

const userStore = useUserStore();

onMounted(() => {
  
  userStore.initStore();
  if(userStore.user.access){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + userStore.user.access;
  }
  else {
    axios.defaults.headers.common['Authorization'] = '';
  }
  
})

</script>

<template>
  <div>
    <Navbar />
    <div class="container my-10">
      <RouterView />
    </div>
    <Toast />
  </div>
</template>