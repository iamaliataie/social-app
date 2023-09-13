<script setup>
import axios from "axios";
import { useRoute } from "vue-router";
import { onMounted, ref } from "vue";
import FriendSuggestionsVue from "../components/FriendSuggestions.vue";
import FeedItem from '../components/FeedItem.vue';
const route = useRoute();

const post = ref({})
const commentBody = ref('')

const getPost = () => {
    axios.get(`api/posts/${route.params.id}/`)
    .then(res => {
        post.value = res.data;
    })
    .catch(error => console.log(error))
}

const handleSubmit = () => {
    axios.post(`api/posts/${route.params.id}/comment_create/`, { body: commentBody.value })
    .then(res => {
        post.value.comments.push(res.data);
        commentBody.value = '';
    })
    .catch(error => console.log(error))
}

onMounted(() => {
    getPost();
})

</script>

<template>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="md:col-span-2">
            <div class="flex flex-col gap-4">
                <FeedItem v-if="post.id" :post="post"/>
                <div class="flex flex-col gap-4">
                    <div class="bg-white rounded-md">
                        <div class="flex flex-col gap-4 p-4">
                            <div 
                            v-for="comment in post.comments"
                            class="flex flex-col gap-3 border rounded-md p-4">
                                <div class="flex items-center gap-4">
                                    <img :src="comment.created_by.get_avatar" alt="user" class="rounded-full w-10">
                                    <div class="flex flex-col">
                                        <h2>{{ comment.created_by.name }}</h2>
                                        <small>{{ comment.created_at_formatted }} ago</small>
                                    </div>
                                </div>
                                <p>{{ comment.body }}</p>
                            </div>
                        </div>
                    </div>
                    <div class="bg-white rounded-md p-4">
                        <form 
                        @submit.prevent="handleSubmit"
                        class="flex flex-col gap-4 items-start">
                            <textarea 
                            v-model="commentBody"
                            rows="3" 
                            class="bg-gray-100 rounded-md focus:outline-none p-3 w-full resize-none" placeholder="what is your opinion..."></textarea>
                            <button type="submit" class="bg-purple-500 text-white px-3 py-2 rounded-md">Submit</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div class="md:col-span-1">
            <FriendSuggestionsVue/>
        </div>
    </div>
</template>
