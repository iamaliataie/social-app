<template>
    <div class="grid grid-cols-1 md:grid-cols-6 gap-4">
        <div class="md:col-span-2">
            <div class="bg-white rounded-md overflow-hidden">
                <div class="flex items-center justify-between p-4 bg-purple-500">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 bg-gray-800 rounded-full"></div>
                        <h2 class="text-lg font-bold">Somebody in world</h2>
                    </div>
                    <span>12 minutes ago</span>
                </div>
                <div class="flex items-center justify-between p-4">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 bg-gray-800 rounded-full"></div>
                        <h2 class="text-lg font-bold">Somebody in world</h2>
                    </div>
                    <span>12 minutes ago</span>
                </div>
                <div class="flex items-center justify-between p-4">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 bg-gray-800 rounded-full"></div>
                        <h2 class="text-lg font-bold">Somebody in world</h2>
                    </div>
                    <span>12 minutes ago</span>
                </div>
            </div>
        </div>
        <div class="md:col-span-4">
            <div class="flex flex-col gap-4 h-[400px]">
                <div class="bg-white rounded-md p-4 flex flex-col gap-4 max-h-[400px] overflow-scroll">
                    <div class="flex gap-4">
                        <img src="../assets/images/self2.jpg" alt="user" class="w-12 h-12 rounded-full">
                        <div class="w-3/4 flex flex-col gap-2">
                            <p class="bg-gray-300 p-3 rounded-b-md rounded-tr-md">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Cum nulla praesentium dolores provident explicabo fuga quam magnam, odio hic accusantium officiis obcaecati modi labore nostrum, voluptate placeat maiores a odit?</p>
                            <span class="text-sm">12 minutes ago</span>
                        </div>
                    </div>
                    <div class="flex flex-row-reverse gap-4">
                        <img src="../assets/images/self2.jpg" alt="user" class="w-12 h-12 rounded-full">
                        <div class="md:max-w-3/4 flex flex-col gap-2">
                            <p class="bg-blue-600 p-3 rounded-b-md rounded-tl-md text-white">Lorem ipsum dolor</p>
                            <span class="text-sm">12 minutes ago</span>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-md p-4">
                    <form>
                        <textarea rows="2" class="bg-gray-200 w-full resize-none rounded-md focus:outline-none p-3" placeholder="Message..."></textarea>
                        <button type="submit" class="px-3 py-2 bg-purple-500 text-white rounded-md">Send</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>