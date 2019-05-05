<template>
    <section class="hero is-fullheight">
        <div class="hero-body">
            <div class="container has-text-centered">
                <div class="column is-8 is-offset-2">
                    <h4 class="title is-4">Oops!</h4>
                    <h5 class="subtitle is-5">We can’t seem to find the page you’re looking for.</h5>
                    <router-link to="/">
                        <b-button type="is-primary">Take Me Home</b-button>
                    </router-link>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'notFound'
}
</script>

