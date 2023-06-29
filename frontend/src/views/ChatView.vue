<script setup>
import axios from 'axios'
import { onMounted, ref, watch } from 'vue';
import { useUserStore } from '../stores/user'

const userStore = useUserStore();
const conversations = ref([]);
const conversation = ref(null);
const activeConversation = ref(0);
const body = ref('')

const getActiveConversation = (conversationId) => {
    axios.get(`api/conversations/${conversationId}/`)
    .then(res => {
        conversation.value = res.data;
    })
    .catch(error => console.log(error))
}

const getConversatios = () => {
    axios.get('api/conversations/')
    .then(res => {
        conversations.value = res.data;
        activeConversation.value = conversations.value[0].id;
        getActiveConversation(activeConversation.value);
    })
    .catch(error => console.log(error))
}


const submitForm = () => {
    axios.post(`api/conversations/${activeConversation.value}/send_message/`, {body: body.value})
    .then(res => {
        conversation.value.messages.push(res.data.message);
        conversations.value.forEach(chat => {
            if (chat.id === activeConversation.value){
                chat.modified_at_formatted = res.data.modified;
            }
        })
        body.value = '';
    })
    .catch(error => console.log(error))
}

watch((activeConversation), () => {
    getActiveConversation(activeConversation.value);
})

onMounted(() => {
    getConversatios();
})
</script>

<template>
    <div class="grid grid-cols-1 md:grid-cols-6 gap-4">
        <div class="md:col-span-2">
            <div class="bg-white rounded-md overflow-hidden">
                <div 
                v-for="conversation in conversations"
                @click="activeConversation = conversation.id"
                class="flex items-center justify-between p-4 cursor-pointer"
                :class="conversation.id == activeConversation && 'bg-purple-500'">
                    <div 
                    v-for="user in conversation.users"
                    class="flex items-center space-x-3">
                        <img v-if="user.id !== userStore.user.id" :src="user.get_avatar" class=" w-12 rounded-full"/>
                        <h2 class="text-lg font-bold">{{ user.id !=userStore.user.id ? user.name : ''}}</h2>
                    </div>
                    <p>{{ conversation.modified_at_formatted }} ago</p>
                </div>
            </div>
        </div>
        <div class="md:col-span-4">
            <div class="flex flex-col gap-4 h-[400px]">
                <div class="bg-white rounded-md p-4 flex flex-col gap-4 max-h-[400px] overflow-scroll">
                    <div v-if="conversation && conversation.messages.length" v-for="message in conversation.messages">
                        <div 
                        v-if="message.created_by.id !== userStore.user.id"
                        class="flex gap-4">
                            <img :src="message.created_by.get_avatar" alt="user" class="w-12 h-12 rounded-full">
                            <div class="w-3/4 flex flex-col gap-2">
                                <p class="bg-gray-300 p-3 rounded-b-md rounded-tr-md">{{ message.body }}</p>
                                <span class="text-sm">{{ message.created_at_formatted }} ago</span>
                            </div>
                        </div>
                        <div v-else class="flex flex-row-reverse gap-4">
                            <img :src="message.created_by.get_avatar" alt="user" class="w-12 h-12 rounded-full">
                            <div class="md:max-w-3/4 flex flex-col gap-2">
                                <p class="bg-blue-600 p-3 rounded-b-md rounded-tl-md text-white">{{ message.body }}</p>
                                <span class="text-sm">{{ message.created_at_formatted }} ago</span>
                            </div>
                        </div>
                    </div>
                    <div v-else>
                        <h1>No messages</h1>
                    </div>
                </div>
                <div class="bg-white rounded-md p-4">
                    <form @submit.prevent="submitForm">
                        <textarea v-model="body" rows="2" class="bg-gray-200 w-full resize-none rounded-md focus:outline-none p-3" placeholder="Message..."></textarea>
                        <button type="submit" class="px-3 py-2 bg-purple-500 text-white rounded-md">Send</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>