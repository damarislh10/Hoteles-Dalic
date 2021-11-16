import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';

import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'
import Hotel from './components/Hotel.vue'

const routes = [{
        path: '/',
        name: 'root',
        component: App
   },
    {
        path: '/user/logIn',
        name: "logIn",
        component: LogIn
    },
    {
        path: '/user/signUp',
        name: "signUp",
        component: SignUp
    },
    {
        path: '/user/home',
        name: "home",
        component: Home
    },
    {
        path: '/user/hotel',
        name: "hotel",
        component: Hotel
    }
];
const router = createRouter({
 history: createWebHistory(),
 routes,
});
export default router;
