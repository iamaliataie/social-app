<script setup>
import { reactive } from 'vue';
import{useRouter} from 'vue-router'
import axios from 'axios';
import { useUserStore } from '../stores/user';

const router = useRouter();
const userStore = useUserStore();


const form = reactive({
    email: '',
    password: ''
})

const submitForm = async() => {
    await axios.post('api/login/', form)
    .then(res => {
        userStore.setToken(res.data)
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + res.data.access;
        
        axios.get('api/authenticated_user/')
        .then(res => {
            userStore.setUserInfo(res.data);
            router.push('/');
        })
        .catch(error => console.log('authenticated user error: ', error))
    })
    .catch(error => console.log('login error: ', error))
}

</script>

<template>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
        <div>
            <div class="bg-white rounded-lg flex flex-col space-y-6 p-10">
                <h2 class="font-bold text-3xl">Login</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium, natus! Officia soluta nulla voluptatibus beatae. Est debitis eaque expedita temporibus.</p>
                <p class="font-semibold">don't have an account? <a href="#" class="font-bold text-lg">Signup here</a></p>
            </div>
        </div>
        <div>
            <div class="bg-white rounded-lg p-10">
                <form @submit.prevent="submitForm" class="flex flex-col space-y-4">
                    <div class="flex flex-col space-y-2">
                        <label for="email">Email</label>
                        <input type="email" 
                        v-model="form.email" 
                        class="bg-gray-100 p-4 rounded-md"
                        placeholder="email">
                    </div>
                    <div class="flex flex-col space-y-2">
                        <label for="password">Password</label>
                        <input type="password" 
                        v-model="form.password" 
                        class="bg-gray-100 p-4 rounded-md"
                        placeholder="password">
                    </div>
                    <button type="submit" class="w-fit p-3 bg-purple-500 rounded-md text-white">Login</button>
                </form>
            </div>
        </div>
    </div>
</template>