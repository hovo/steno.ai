import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'Upload',
            component: () => import('@/views/upload')
        },
        {
            path: '/transcribe',
            name: 'Transcribe',
            component: () => import('@/views/transcribe')
        },
        {
            path: '*',
            component: () => import('@/views/404')
        }
    ]
})

export default router