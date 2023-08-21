<script setup>
import axios from 'axios';
import FeedList from '../components/FeedList.vue';
import FriendSuggestionsVue from '../components/FriendSuggestions.vue';
import { useRoute, useRouter } from 'vue-router';
import { onMounted, ref, watch } from 'vue';
import { useUserStore } from '../stores/user';
const userStore = useUserStore()

const route = useRoute();
const router = useRouter();
const user = ref(null);
const friendship = ref(0)

const getUser = () => {
    axios.get(`api/profile/${route.params.id}`)
    .then(res => {
        user.value = res.data.user;
        userStore.profilePosts = res.data.posts;
        friendship.value = res.data.friendship;
    })
    .catch(error => {
        console.log(error);
    })
}

onMounted(()=>{
    getUser();
})

const createFriendshipRequest = () => {
    axios.post(`api/friendship_create/${route.params.id}/`)
    .then(res => {
        friendship.value = 1;
    })
    .catch(error => {
        console.log(error);
    })
}

const friendshipHandle = (userId, status) => {
    axios.post(`api/friendship_handle/${userId}/${status}/`)
    .then(res => {
        friendship.value = res.data.friendship;
        if (res.data.friendship == 3){
            user.value.friends.push('_')
        }
        else{
            user.value.friends.pop();
        }
    })
    .catch(error => {
        console.log(error);
    })
}

const directMessage = () => {
    axios.get(`api/conversations/create_get_conversation/${user.value.id}/`)
    .then(res => {
        router.push({name: 'chat'})
    })
    .catch(error => console.log(error))
}


watch(route, () => {
    getUser();
}, { flush: 'pre', immediate: true, deep: true })

</script>

<template>
    <div class="grid grid-cols-2 md:grid-cols-7 gap-4">
        <div class="md:col-span-2">
            <div v-if="user != null" class="bg-white rounded-md p-4">
                <div class="flex flex-col space-y-4 items-center">
                    <img :src="user.get_avatar" alt="user" class="rounded-full">
                    <h1 class="text-3xl font-bold">{{ user.name }}</h1>
                    <p v-if="userStore.user.id == user.id" class="text-lg">{{ user.email }}</p>
                    <div class="flex items-center justify-between w-full text-gray-600">
                        <RouterLink :to="{name: 'friends', params: {'id': user.id}}">{{ user.friends.length }} friends</RouterLink>
                        <span>{{ userStore.profilePosts.length }} posts</span>
                    </div>
                    <div v-if="user.id !== userStore.user.id" class="w-full flex flex-col gap-2">
                        <button v-if="friendship == 0" @click="createFriendshipRequest" class="bg-purple-500 text-white w-full px-3 py-2 rounded-md">Send friendship request</button>
                        <div v-else-if="friendship == 1" class="flex gap-4 items-center w-full">
                            <button class="bg-yellow-500 text-white w-4/6 px-3 py-2 rounded-md">Request send</button>
                            <button @click="friendshipHandle(user.id, 'cancel')" class="bg-red-500 text-white w-2/6 px-3 py-2 rounded-md">Cancel</button>
                        </div>
                        <div v-else-if="friendship == 2" class="flex gap-4 items-center w-full">
                            <button @click="friendshipHandle(user.id, 'accept')" class="bg-green-500 text-white w-full px-3 py-2 rounded-md">Accept</button>
                            <button @click="friendshipHandle(user.id, 'reject')" class="bg-red-500 text-white w-full px-3 py-2 rounded-md">Reject</button>
                        </div>
                        <div v-else class="flex gap-4 items-center w-full">
                            <button class="bg-blue-500 text-white w-4/6 px-3 py-2 rounded-md">Friends</button>
                            <button @click="friendshipHandle(user.id, 'remove')" class="bg-red-500 text-white w-2/6 px-3 py-2 rounded-md">Remove</button>
                        </div>
                    </div>
                    <div v-if="user.id === userStore.user.id" class="w-full flex">
                        <RouterLink :to="{name: 'editprofile', params: {'id': user.id}}"
                        class="bg-blue-500 py-2 px-3 rounded-md w-full text-white text-center"
                        >
                            Edit Profile
                        </RouterLink>
                    </div>
                    <div v-if="user.id !== userStore.user.id" class="w-full flex">
                        <button 
                        @click="directMessage"
                        class="bg-blue-500 py-2 px-3 rounded-md w-full text-white text-center"
                        >
                            Direct Message
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="md:col-span-3">
            <FeedList :posts="userStore.profilePosts"/>
        </div>
        <div class="md:col-span-2">
            <FriendSuggestionsVue/>
        </div>
    </div>
</template>
