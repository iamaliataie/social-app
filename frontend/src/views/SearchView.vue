<script setup>

import { reactive } from 'vue';
import axios from 'axios';
import SearchBar from '../components/SearchBar.vue'
import Users from '../components/Users.vue'
import FeedItem from '../components/FeedItem.vue';
import FriendSuggestions from '../components/FriendSuggestions.vue';

const searchResults = reactive({
    people: [],
    posts: []
})

const handleClick = (query) => {
    axios.post('api/search/', {query: query})
    .then(res => {
        searchResults.people = res.data.users;
        searchResults.posts = res.data.posts;
    })
    .catch(error => {
        console.log(error);
    })
}

</script>
<template>
    <div class="grid grid-cols-1 md:grid-cols-6 gap-4">
        <div class="md:col-span-4">
            <div class="flex flex-col space-y-4">
                <SearchBar @actionCapture="(query) => handleClick(query)" />
                <Users v-if="searchResults.people.length > 0" :people="searchResults.people"/>
                <FeedItem v-for="post in searchResults.posts" :key="post.id" :post="post"/>
            </div>
        </div>
        <div class="md:col-span-2">
            <FriendSuggestions />
        </div>
    </div>    
</template>