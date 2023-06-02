<template>
    <div class="bg-white p-6 rounded-xl ">
        <form action="#" class="flex flex-col space-y-4">
        <textarea rows="5" class="w-full resize-none bg-gray-100 p-4 rounded-md" placeholder="What are you thinking about, today?"></textarea>
        <div class="flex items-center justify-between">
            <button type="submit" class="bg-purple-500 text-white px-3 py-3 rounded-md">Post</button>
            <input type="file" id="attachment" class="hidden">
            <label for="attachment" class="bg-gray-950 text-white px-3 py-3 rounded-md">Attachments</label>
        </div>
        </form>
    </div>
</template>