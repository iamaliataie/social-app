<script setup>
import PostForm from './PostForm.vue';
import FeedItem from './FeedItem.vue';

const emit = defineEmits(['clickEmit'])

const hasanClick = (body) => {
    emit('clickEmit', body)
}

</script>
<template>
    <div class="flex flex-col space-y-4">
        <PostForm @postSubmit="(body)=>hasanClick(body)"/>
        <FeedItem />
    </div>
</template>