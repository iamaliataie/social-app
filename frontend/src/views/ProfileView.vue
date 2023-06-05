<script setup>
import FeedList from '../components/FeedList.vue';
import FriendSuggestionsVue from '../components/FriendSuggestions.vue';

</script>

<template>
    <div class="grid grid-cols-2 md:grid-cols-7 gap-4">
        <div class="md:col-span-2">
            <div class="bg-white rounded-md p-4">
                <div class="flex flex-col space-y-4 items-center">
                    <img src="../assets/images/self2.jpg" alt="user" class="rounded-full">
                    <h1 class="text-3xl font-bold">Ali Ahmad Ataie</h1>
                    <div class="flex items-center justify-between w-full text-gray-600">
                        <span>12 friends</span>
                        <span>12 posts</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="md:col-span-3">
            <FeedList />
        </div>
        <div class="md:col-span-2">
            <FriendSuggestionsVue/>
        </div>
    </div>
</template>