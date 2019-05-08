<template>
<div class="container" style="min-height: 100vh;">
    <div class="container">
        <section class="articles" style="flex:1">
            <div class="column is-4 is-offset-6"></div>
            <div class="column is-8 is-offset-2">
                <h1 class="title" contenteditable="true">Recording.wav</h1>
                <h6 class="subtitle is-6">Sun 5/5 - 12:40AM</h6>
                <hr class="hr">
            </div>
            <div class="column is-8 is-offset-2 doc" style="margin-bottom: 55px;">
                <div>
                    <div class="alternative" v-for="(result, idx) in sampleData.results" :key="idx">
                        <span v-for="(wordObj, word_idx) in result.alternatives[0].words" 
                            :key="word_idx"
                            class="word" 
                            :class="{'word-active': (idx == currentWord.alt & word_idx == currentWord.word)}"
                            @click="seek(idx, word_idx)">
                            {{wordObj.word}}
                        </span>
                    </div>
                </div>
            </div>
        </section>
        <nav class="navbar is-fixed-bottom">
            <div class="container">
                <div class="column is-8 is-offset-2">
                    <vue-plyr :options="playerOptions" ref="plyr">
                        <audio>
                            <source src="https://storage.googleapis.com/steno/6323f5ea-cd55-4dad-a520-a8d265f08ce8.wav" type="audio/wav"/>
                        </audio>
                    </vue-plyr>
                </div>
            </div>
        </nav>
    </div>
</div>

</template>

<script>
import jsonObj from '@/test-response.js'
export default {
    name: 'transcribe',
    data() {
        return {
            playerOptions: {
                controls: ['play', 'progress', 'current-time']
            },
            sampleData: jsonObj,
            currentWord: {
                alt: 0,
                word: 0
            }
        }
    },
    mounted() {
        this.player.on('timeupdate', () => {
            console.log(this.currentWord)
            var words = this.sampleData.results[this.currentWord.alt].alternatives[0].words
            var wordsLen = words.length
            var currWord = words[this.currentWord.word]

            var currentWordStartTime = this.sanitizeTime(currWord.startTime)
            var currentWordEndTime = this.sanitizeTime(currWord.endTime)

            var playerTime = this.player.currentTime
            if(!(playerTime >= currentWordStartTime & playerTime <= currentWordEndTime)) {
                if(this.currentWord.word < wordsLen-1){
                    this.currentWord.word += 1
                } else {
                    this.currentWord.alt += 1
                    this.currentWord.word = 0
                }
            }
        })
    },
    computed: {
        player() {
            return this.$refs.plyr.player;
        }
    },
    methods: {
        sanitizeTime: function(timeStr) {
            timeStr.substring(0, timeStr.length-1)
            timeStr = parseFloat(timeStr)
            return timeStr
        },
        seek: function(resIdx, wordIdx) {
            var startTime = this.sampleData.results[resIdx].alternatives[0].words[wordIdx].startTime
            startTime = this.sanitizeTime(startTime)

            this.currentWord.alt = resIdx
            this.currentWord.word = wordIdx

            this.player.currentTime = startTime;
        }
    }
}
</script>

<style>
@import '../styles/doc.css';
</style>


