<script setup>
import axios from 'axios';
import { onMounted, reactive, ref } from 'vue';
import{ useRouter, useRoute } from 'vue-router'
import { useUserStore } from '../stores/user';
import { useToastStore } from '../stores/toast';

const toastStore = useToastStore();
const router = useRouter();
const route = useRoute();
const userStore = useUserStore();
const errorMessage = ref([]);

const form = reactive({
    old_password: '',
    new_password1: '',
    new_password2: ''
})


const submitForm = () => {
    errorMessage.value = [];
    if (form.old_password === '' || form.new_password1 === '' || form.new_password2 === '') {
        errorMessage.value.push('Fields cannot be empty');
        return
    }

    let editForm = new FormData();
    editForm.append('old_password', form.old_password);
    editForm.append('new_password1', form.new_password1);
    editForm.append('new_password2', form.new_password2);

    axios.post(`api/profile/edit/password_change/`, editForm)
    .then(res => {
        if (res.data.status) {
            toastStore.showToast(res.data.message, 'bg-green-500')
            router.push({name: 'profile', params: {'id': userStore.user.id}})
        }else{
            let messages = JSON.parse(res.data.message);
            for (const key in messages) {
                for (const val in  messages[key]){
                    errorMessage.value.push(messages[key][val].message);
                }
            }
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
                <h2 class="font-bold text-3xl">Password Change</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium, natus! Officia soluta nulla voluptatibus beatae. Est debitis eaque expedita temporibus.</p>
            </div>
        </div>
        <div>
            <div class="bg-white rounded-lg p-10">
                <form @submit.prevent="submitForm" class="flex flex-col space-y-4">
                    <div class="flex flex-col space-y-2">
                        <label for="email">Old password</label>
                        <input type="text" 
                        v-model="form.old_password" 
                        class="bg-gray-100 p-4 rounded-md"
                        placeholder="email">
                    </div>
                    <div class="flex flex-col space-y-2">
                        <label for="password">New password</label>
                        <input type="text" 
                        v-model="form.new_password1" 
                        class="bg-gray-100 p-4 rounded-md"
                        placeholder="password">
                    </div>
                    <div class="flex flex-col space-y-2">
                        <label for="password">Confirm new password</label>
                        <input type="text" 
                        v-model="form.new_password2" 
                        class="bg-gray-100 p-4 rounded-md"
                        placeholder="password">
                    </div>
                    <ul 
                    v-if="errorMessage"
                    class="text-sm text-red-500 mb-4">
                        <li v-for="message in errorMessage">{{ message }}</li>
                    </ul>
                    <button type="submit" class="w-fit p-3 bg-purple-500 rounded-md text-white">Save</button>
                </form>
            </div>
        </div>
    </div>
</template>

<style scoped>

li {
    list-style-type: circle;
}

</style>