<script setup>
import { useRouter } from "vue-router";
import { useUserStore } from "../stores/user"

const router = useRouter();
const userStore = useUserStore();
const logout = () => {
    userStore.removeToken();
    router.push('/login')
}

</script>
<template>
    <div class="bg-white py-10">
        <div class="container flex flex-col md:flex-row items-center justify-between">
      <div>
            <h1 class="text-4xl font-bold">Social</h1>
        </div>
        <ul 
        v-if="userStore.user.isAuthenticated"
        class="flex flex-col overflow-hidden md:flex-row gap-4 md:h-full"
        id="menu"
        >
            <a href="#" class="md:hidden">Profile</a>
            <router-link :to="{name: 'home'}" class="hidden md:block">Home</router-link>
            <a href="#">Messages</a>
            <a href="#">Notifications</a>
            <a href="#">Search</a>
            <button @click="logout" class="text-left">Logout</button>
        </ul>
        <div 
        v-if="userStore.user.isAuthenticated"
        class="hidden md:flex rounded-full overflow-hidden">
            <img src="../assets/images/self2.jpg" alt="" class="w-28">
        </div>
        <div 
        v-else
        class="flex gap-4 items-center text-white">
            <RouterLink 
                :to="{name: 'login'}" 
                class="px-3 py-2 rounded-md bg-gray-950 "
            >
                Login
            </RouterLink>
            <RouterLink 
                :to="{name: 'login'}" 
                class="px-3 py-2 rounded-md bg-purple-500 "
            >
                Signup
            </RouterLink>
        </div>
    </div>
    </div>
</template>