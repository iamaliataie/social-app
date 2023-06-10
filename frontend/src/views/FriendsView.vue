<script setup>

import axios from 'axios';
import { onMounted, ref } from 'vue';
import {useRoute} from 'vue-router';
import { useUserStore } from '../stores/user';
import FriendSuggestions from '../components/FriendSuggestions.vue';
import Users from '../components/Users.vue';

const userStore = useUserStore();
const route = useRoute();
const friends = ref([])
const requests = ref([])

const friendshipHandle = (userId, status) => {
    axios.post(`api/friendship_handle/${userId}/${status}/`)
    .then(res => {
        friends.value = res.data.friends;
        requests.value = res.data.requests;
    })
    .catch(error => {
        console.log(error);
    })
}


onMounted(() => {
    axios.get(`api/profile/${route.params.id}/friends/`)
    .then(res => {
        friends.value = res.data.friends;
        requests.value = res.data.requests;
    })
    .catch(error => {
        console.log(error);
    })
})

</script>

<template>
    <div class="grid grid-cols-1 md:grid-cols-6 gap-4">
        <div class="md:col-span-4">
            <div class="flex flex-col space-y-4">
                <Users :people="friends" :title="'Friends'"/>
                <Users v-if="userStore.user.id === route.params.id" :people="requests" :title="'Friendship requests'" :handle-request="{'status': true, 'method': friendshipHandle}"/>
            </div>
        </div>
        <div class="md:col-span-2">
            <FriendSuggestions />
        </div>
    </div>
</template>