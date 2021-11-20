<template>
<div class="card-container">
    <div class="user-container">
        <img class="icon" v-bind:src="picture">
        <p>
            <strong> {{ name }} </strong>
        </p>
    </div>
    <div class="comment-container">
      <strong> {{ titulo }} </strong>
      <p>
        <a v-bind:href="link"> {{ link }} </a>
      </p>
    </div>
</div>
</template>

<script>
export default {
  data: function () {
    return {
      count: 0,
      likesValue: this.likes,
      dislikesValue: this.dislikes
    }
  },
  props: {
    name: String,
    link: String,
    titulo: String,
    picture: String,
    id: Number
  }
}
</script>

<style src='@/assets/styles/comment_box_style.css'></style>
