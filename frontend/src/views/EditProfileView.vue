<script setup>
import axios from 'axios';
import { onMounted, reactive, ref } from 'vue';
import{ useRouter, useRoute } from 'vue-router'
import { useUserStore } from '../stores/user';
import { useToastStore } from '../stores/toast';

const useToast = useToastStore();
const router = useRouter();
const route = useRoute();
const userStore = useUserStore();
const errorMessage = ref('');

const form = reactive({
    name: userStore.user.name,
    email: userStore.user.email,
    avatar: ''
})


const submitForm = () => {
    errorMessage.value = '';
    if (form.name === '' || form.email === '') {
        errorMessage.value = 'Fields cannot be empty';
        return
    }

    let editForm = new FormData();
    editForm.append('name', form.name);
    editForm.append('email', form.email);
    editForm.append('avatar', form.avatar);

    axios.post(`api/profile/edit/`, editForm, {
        headers:{
            "Content-Type": "multipart/form-data",
        }
    })
    .then(res => {
        if (res.data.status) {
            userStore.setUserInfo({
                id: userStore.user.id,
                name: res.data.info.name,
                email: res.data.info.email,
                avatar: res.data.info.avatar
            })
            useToast.showToast(res.data.message, 'bg-green-500')
            router.push({name: 'profile', params: {'id': userStore.user.id}})
        }
    })
    .catch(error => {
        console.log('error save edited profile: ',error);
    })
}

onMounted(() => {
    if (userStore.user.id !== route.params.id) {
        router.push({name: 'profile', params: {'id': userStore.user.id}})
    }
})

</script>

<template>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
        <div>
            <div class="bg-white rounded-lg flex flex-col space-y-6 p-10">
                <h2 class="font-bold text-3xl">Edit Profile</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium, natus! Officia soluta nulla voluptatibus beatae. Est debitis eaque expedita temporibus.</p>
            </div>
        </div>
        <div>
            <div class="bg-white rounded-lg p-10">
                <form @submit.prevent="submitForm" class="flex flex-col space-y-4">
                    <div class="flex flex-col space-y-2">
                        <label for="email">name</label>
                        <input type="text" 
                        v-model="form.name" 
                        class="bg-gray-100 p-4 rounded-md"
                        placeholder="email">
                    </div>
                    <div class="flex flex-col space-y-2">
                        <label for="password">email</label>
                        <input type="text" 
                        v-model="form.email" 
                        class="bg-gray-100 p-4 rounded-md"
                        placeholder="password">
                    </div>
                    <div class="flex flex-col space-y-2">
                        <label for="password">file</label>
                        <input type="file" 
                        @change="(el) => {form.avatar = el.target.files[0]}" 
                        class="bg-gray-100 p-4 rounded-md"
                        placeholder="password">
                    </div>
                    <div 
                    v-if="errorMessage"
                    class="text-sm text-red-500 mb-4">
                        <span>{{ errorMessage }}</span>
                    </div>
                    <button type="submit" class="w-fit p-3 bg-purple-500 rounded-md text-white">Save</button>
                </form>
            </div>
        </div>
    </div>
</template>