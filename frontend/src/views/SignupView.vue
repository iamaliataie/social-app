<script setup>
import { reactive, ref } from 'vue';
import{useRouter} from 'vue-router'
import axios from 'axios';
import { useToastStore } from '../stores/toast';

const router = useRouter();
const toastStore = useToastStore();
const errorMessage = ref('');

const form = reactive({
    name: '',
    email: '',
    password1: '',
    password2: '',
})

const validateEmail = (email) => {
    return String(email)
      .toLowerCase()
      .match(
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      );  
  };

const submitForm = async() => {
    errorMessage.value = '';
    if (form.name === '' || form.email === '' || form.password1 === '' || form.password2 === '') {
        errorMessage.value = 'Fields cannot be empty';
        return
    }
    else if (!validateEmail(form.email)) {
        errorMessage.value = 'Invalid email address';
        return
    }
    else if (form.password1.length < 8) {
        errorMessage.value = 'Password must be 8 characters at least';
        return
    }
    else if (form.password1 != form.password2) {
        errorMessage.value = 'Passwords do not match';
        return
    }

    await axios.post('api/signup/', form)
    .then(res => {
        if (!res.data.status) {
            toastStore.showToast(res.data.message, 'bg-red-500');
        }
        else{
            toastStore.showToast('Registration was succussfull.', 'bg-green-400');
            router.push({name: 'login'})
        }
    })
    .catch(error => {
        toastStore.showToast(error.message, 'bg-red-500');
    })
}

</script>

<template>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
        <div class="md:col-span-1">
            <div class="bg-white rounded-lg flex flex-col space-y-6 p-10">
                <h2 class="font-bold text-3xl">Signup</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium, natus! Officia soluta nulla voluptatibus beatae. Est debitis eaque expedita temporibus.</p>
                <p class="font-semibold">Already have an account? <a href="#" class="font-bold text-lg">Login here</a></p>
            </div>
        </div>
        <div class="md:col-span-2">
            <div class="bg-white rounded-lg p-10">
                <form @submit.prevent="submitForm" class="flex flex-col space-y-4">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="flex flex-col space-y-2">
                            <label for="email">Name</label>
                            <input type="text" 
                            v-model="form.name" 
                            class="bg-gray-100 p-4 rounded-md"
                            placeholder="name">
                        </div>
                        <div class="flex flex-col space-y-2">
                            <label for="email">Email</label>
                            <input type="email" 
                            v-model="form.email" 
                            class="bg-gray-100 p-4 rounded-md"
                            placeholder="email">
                        </div>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="flex flex-col space-y-2">
                            <label for="password">Password</label>
                            <input type="password" 
                            v-model="form.password1" 
                            class="bg-gray-100 p-4 rounded-md"
                            placeholder="password">
                        </div>
                        <div class="flex flex-col space-y-2">
                            <label for="password">Confirm Password</label>
                            <input type="password" 
                            v-model="form.password2" 
                            class="bg-gray-100 p-4 rounded-md"
                            placeholder="confirm password">
                        </div>
                    </div>
                    <div class="text-sm text-red-500 mb-4">
                        <span>{{ errorMessage }}</span>
                    </div>
                    <button type="submit" class="w-fit p-3 bg-purple-500 rounded-md text-white">Signup</button>
                </form>
            </div>
        </div>
    </div>
</template>