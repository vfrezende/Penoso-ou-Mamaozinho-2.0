<template>
<div class="fadeIn table_ranking" v-if="ready" style="display: flex">

    <div :class="class1">
        <div class="header">
            <h3>Primeiro Lugar</h3>
        </div>
        <div class="block1">
            <h2>
                <a v-bind:href="url_disciplina+primeiro_lugar.id">
                    {{primeiro_lugar.nome}}
                </a>
            </h2>
            <p><strong>Nota</strong></p>
            <p>{{(primeiro_lugar.razao * 5).toFixed(2)}}</p>
        </div>
        <div class="block2">
            <p><strong>Número de votos</strong></p>
            <p>{{primeiro_lugar.num_votos}}</p>
        </div>
        <div class="block3">
            <p><strong>Número de comentários</strong></p>
            <p>{{primeiro_lugar.num_comentarios}}</p>
        </div>
        <div class="block4">
            <div class="place">1</div>
        </div>
    </div>

    <div :class="class2">
        <div class="header">
            <h3>Segundo Lugar</h3>
        </div>
        <div class="block1">
            <h2>
                <a v-bind:href="url_disciplina+segundo_lugar.id">
                    {{segundo_lugar.nome}}
                </a>
            </h2>
            <p><strong>Nota</strong></p>
            <p>{{(segundo_lugar.razao * 5).toFixed(2)}}</p>
        </div>
        <div class="block2">
            <p><strong>Número de votos</strong></p>
            <p>{{segundo_lugar.num_votos}}</p>
        </div>
        <div class="block3">
            <p><strong>Número de comentários</strong></p>
            <p>{{segundo_lugar.num_comentarios}}</p>
        </div>
        <div class="block4">
            <div class="place">2</div>
        </div>
    </div>

    <div :class="class3">
        <div class="header">
            <h3>Terceiro Lugar</h3>
        </div>
        <div class="block1">
            <h2>
                <a v-bind:href="url_disciplina+terceiro_lugar.id">
                    {{terceiro_lugar.nome}}
                </a>
            </h2>
            <p><strong>Nota</strong></p>
            <p>{{(terceiro_lugar.razao * 5).toFixed(2)}}</p>
        </div>
        <div class="block2">
            <p><strong>Número de votos</strong></p>
            <p>{{terceiro_lugar.num_votos}}</p>
        </div>
        <div class="block3">
            <p><strong>Número de comentários</strong></p>
            <p>{{terceiro_lugar.num_comentarios}}</p>
        </div>
        <div class="block4">
            <div class="place">3</div>
        </div>
    </div>
</div>
</template>

<script>
export default {
  data: function () {
    return {
      class2: 'col-sm-4 ranking r2 animated ',
      class3: 'col-sm-4 ranking r3 animated ',
      class1: 'col-sm-4 ranking r1 animated first ',
      ready: false,
      url_disciplina: '/disciplina/'
    }
  },
  props: {
    primeiro_lugar: Object,
    segundo_lugar: Object,
    terceiro_lugar: Object
  },
  methods: {
  },
  mounted: function () {
    const time = 300
    setTimeout(() => {
      this.ready = true
    }, time)
    setTimeout(() => {
      this.class2 += 'slideInUp'
    }, time)
    setTimeout(() => {
      this.class3 += 'slideInUp'
    }, time * 2)
    setTimeout(() => {
      this.class1 += 'slideInUp'
    }, time * 3)
  }
}
</script>

<style src='@/assets/styles/ranking_courses_style.css' scoped>
    @import url(https://fonts.googleapis.com/css?family=Lato:400,300);
</style>
