import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        audioFile: null
    },
    getters: {
        audioFile: state => state.audioFile
    },
    mutations: {
        SET_AUDIO_FILE: (state, file) => {
            state.audioFile = file
        }
    }
})

export default store