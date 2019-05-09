<template>
    <section class="hero is-fullheight">
        <div class="hero-body">
            <div class="container has-text-centered">
                <div class="column is-8 is-offset-2">
                    <img src="../assets/file_upload.png">
                    <h5 class="title is-5">Upload an audio file to transcribe</h5>
                    <h6 class="subtitle is-6">.wav, .mp3, .m4a, .flac – up to 25 MB</h6>
                    <b-field class="file" style="display: inline-flex">
                        <b-upload v-model="file" @input="uploadFile(file)">
                            <b-button class="is-primary" :loading="loadingState">Upload</b-button>
                        </b-upload>
                        <span class="file-name" v-if="file">
                            {{ file.name }}
                        </span>
                    </b-field>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'upload',
    data() {
        return {
            file: null,
            loadingState: false
        }
    },
    methods: {
        uploadFile(file) {
            if (file.size > 1024 * 1024 * 25) {
                this.file = null
                this.$notification.open({
                    duration: 2000,
                    message: 'File larger than 25 MB',
                    type: 'is-danger',
                    position: 'is-bottom'
                })
                return;
            } else {
                this.loadingState = true
                // TODO: MAKE API CALL
            }
        }
    }
}
</script>

