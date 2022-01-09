<template>
<div class="card-container">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <div class="user-container">
        <img class="icon" v-bind:src="picture">
        <p>
            <strong> {{ name }} </strong>
        </p>
    </div>
    <div class="comment-container">
      <h5 style="text-align: center;">
      <p>
        <a v-bind:href="arquivo_url" class="download-button"><i class="fa fa-download"></i> Download</a>
        {{ nome }}
      </p>
      </h5>
      <p>
        <a> {{ descricao }} </a>
      </p>
    </div>
</div>
</template>

<script>
export default {
  data: function () {
    return {
      arquivo_url: this.$api_url + '/api/arquivo/' + this.id
    }
  },
  props: {
    name: String,
    nome: String,
    descricao: String,
    picture: String,
    id: Number
  }
}
</script>

<style src='@/assets/styles/comment_box_style.css'></style>
