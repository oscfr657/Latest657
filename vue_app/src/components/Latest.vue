<template>
  <div >
    <div v-if="loading" class="latest-post" >
    Loading...
    </div>
    <div v-if="error" class="latest-post" >
      {{ error }}
    </div>
    <div class="latest-post" v-if="latest_post">
        <div class="latest-post-video" v-if="latest_post.video_file">
          <video muted autoplay loop>
            <source :src="latest_post.video_file">
          </video>
        </div>
        <div class="latest-post-image" v-if="latest_post.image_file">
          <img v-if="latest_post.image_file" :src="latest_post.image_file" :alt="latest_post.title"/>
        </div>
        <div class="latest-post-audio" v-if="latest_post.audio_file">
          <audio controls>
            <source :src="latest_post.audio_file">
          </audio>
        </div>
        <div class="latest-post-title" v-if="latest_post.title">
          <h3>{{ latest_post.title }}</h3>
        </div>
        <div class="latest-post-text" v-if="latest_post.text">
          <p>{{ latest_post.text }}</p>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "latest",
  data() {
    return {
      loading: false,
      error: false,
      latest_post: false
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.loading = true;
      this.$http.get("/latest/api/latestpost/").then(
        response => {
          this.latest_post = response.body;
          this.loading = false;
        },
        response => {
          console.log("API error");
          this.error = true;
          this.loading = false;
        }
      );
    }
  }
};
</script>
