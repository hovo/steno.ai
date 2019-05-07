<template>
<div class="container" style="display: flex; min-height: 100vh; flex-direction: column;">
    <div class="container" style="display: flex; min-height: 100vh; flex-direction: column;">
        <section class="articles" style="flex:1">
            <div class="column is-4 is-offset-6"></div>
            <div class="column is-8 is-offset-2">
                <h1 class="title" contenteditable="true">Recording.wav</h1>
                <!-- contenteditable="true" -->
                <h6 class="subtitle is-6">Sun 5/5 - 12:40AM</h6>
                <hr class="hr">
            </div>
            <div class="column is-8 is-offset-2 doc">
                <div>
                    <div class="alternative" v-for="(result, idx) in sampleData.results" :key="idx">
                        <span v-for="(wordObj, word_idx) in result.alternatives[0].words" 
                            :key="word_idx"
                            class="word"
                            @click="seek(idx, word_idx)">
                            {{wordObj.word}}
                        </span>
                    </div>
                </div>
            </div>
        </section>
        <footer>
            <div class="content">
                <div class="column is-8 is-offset-2">
                    <vue-plyr :options="playerOptions" ref="plyr">
                        <audio>
                            <source src="https://storage.googleapis.com/steno/6323f5ea-cd55-4dad-a520-a8d265f08ce8.wav" type="audio/wav"/>
                        </audio>
                    </vue-plyr>
                </div>
            </div>
        </footer>
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
            sampleData: jsonObj
        }
    },
    computed: {
        player() {
            return this.$refs.plyr.player;
        }
    },
    methods: {
        seek: function(resIdx, wordIdx) {
            var startTime = this.sampleData.results[resIdx].alternatives[0].words[wordIdx].startTime
            startTime = startTime.substring(0, startTime.length-1) // Removes time unit (s) from the string
            startTime = parseFloat(startTime) // Cast string into float

            this.player.currentTime = startTime;
        }
    }
}
</script>

<style>
.sticky{
  position: fixed;
  top: 0;
  overflow: hidden;
  z-index: 10;
}
.title {
    color: #022144;
}
.doc {
    padding-top: 0;
}
[contenteditable="true"]:active,
[contenteditable="true"]:focus{
    border: none;
    outline: none;
}
.plyr__controls__item.plyr__progress__container {
  width: 100% !important;
}
.plyr__controls {
    background-color: #FBFBFB !important;
    border: 1px solid #EFF0F2 !important;
    border-radius: 5px !important;
}
.alternative {
    margin-bottom: 10px;
}
.word {
    color: #1B2733;
    display:inline-block;
    padding: 0px 2px;
}
.word:hover {
    background-color: #0061D5;
    border-radius: 4px;
    color: white;
}
</style>


