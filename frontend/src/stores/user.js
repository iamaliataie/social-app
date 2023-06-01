import { reactive } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const user = reactive({
    id: null,
    name: null,
    email: null,
    access: null,
    refresh: null,
    isAuthenticated: false
  })

  const initStore = () => {
    if (localStorage.getItem('user.access')) {
      user.id = localStorage.getItem('user.id');
      user.name = localStorage.getItem('user.name');
      user.email = localStorage.getItem('user.email');
      user.access = localStorage.getItem('user.access');
      user.refresh = localStorage.getItem('user.refresh');
      user.isAuthenticated = true;
      refreshToken();
    }
  }

  const setToken = (data) => {
    user.access = data.access;
    user.refresh = data.refresh;
    localStorage.setItem('user.access', user.access);
    localStorage.setItem('user.refresh', user.refresh);
    user.isAuthenticated = true;
  }

  const setUserInfo = (data) => {
    user.id = data.id;
    user.name = data.name;
    user.email = data.email;
    localStorage.setItem('user.id', user.id);
    localStorage.setItem('user.name', user.name);
    localStorage.setItem('user.email', user.email);
  }

  const removeToken = () => {
    user.id= null;
    user.name= null;
    user.email= null;
    user.access= null;
    user.refresh= null;
    user.isAuthenticated= false;

    localStorage.removeItem('user.id');
    localStorage.removeItem('user.name');
    localStorage.removeItem('user.email');
    localStorage.removeItem('user.access');
    localStorage.removeItem('user.refresh');
  }

  const refreshToken = () => {
    axios.post('/api/refresh/', {
        refresh: user.refresh
    })
        .then((response) => {
            user.access = response.data.access
            localStorage.setItem('user.access', response.data.access)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
        })
        .catch((error) => {
            removeToken();
        })
  }

  return { user, initStore, setToken, setUserInfo, removeToken }
})
