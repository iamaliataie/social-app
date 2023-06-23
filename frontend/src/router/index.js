import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PostDetailView from '../views/PostDetailView.vue'
import ProfileView from '../views/ProfileView.vue'
import EditProfileView from '../views/EditProfileView.vue'
import PasswordChangeView from '../views/PasswordChangeView.vue'
import FriendsView from '../views/FriendsView.vue'
import NotificationsView from '../views/NotificationsView.vue'
import SearchView from '../views/SearchView.vue'
import ChatView from '../views/ChatView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/:id',
      name: 'detail',
      component: PostDetailView
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/profile/:id/edit',
      name: 'editprofile',
      component: EditProfileView
    },
    {
      path: '/profile/:id/edit/password_change',
      name: 'password_change',
      component: PasswordChangeView
    },
    {
      path: '/profile/:id/friends',
      name: 'friends',
      component: FriendsView
    },
    {
      path: '/notifications',
      name: 'notifications',
      component: NotificationsView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/chat',
      name: 'chat',
      component: ChatView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
  ]
})

export default router
