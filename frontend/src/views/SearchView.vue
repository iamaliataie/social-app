<script setup>
import SearchBar from '../components/SearchBar.vue'
import SearchUsers from '../components/SeachUsers.vue'
import FeedItemVue from '../components/FeedItem.vue';
import FriendSuggestions from '../components/FriendSuggestions.vue';

const handleClick = (query) => {
    console.log('clicked: ', query);
}

</script>
<template>
    <div class="grid grid-cols-1 md:grid-cols-6 gap-4">
        <div class="md:col-span-4">
            <div class="flex flex-col space-y-4">
                <SearchBar @actionCapture="(query) => handleClick(query)" />
                <SearchUsers />
                <FeedItemVue />
            </div>
        </div>
        <div class="md:col-span-2">
            <FriendSuggestions />
        </div>
    </div>    
</template>