<script setup>
import { reactive } from 'vue';

const form = reactive({
    username: '',
    password: ''
})

const submitForm = () => {
    console.log(form);
}

</script>

<template>
    <div>
        <form @submit.prevent="submitForm">
            <input type="text" v-model="form.username" placeholder="username">
            <input type="text" v-model="form.password" placeholder="password">
            <button type="submit">login</button>
        </form>
    </div>
</template>