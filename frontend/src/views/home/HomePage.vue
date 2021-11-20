<template>
  <div id="HomePage">
    <Header />
    <b-container>
      <h2><b-badge>TOP 3</b-badge> Penosas e Mamaozinhas </h2>
      <b-tabs>
        <b-tab title="Penosas pra ca#$!" active>
          <RankingCourses
            :primeiro_lugar="top_penoso[0]"
            :segundo_lugar="top_penoso[1]"
            :terceiro_lugar="top_penoso[2]"
          />
        </b-tab>
        <b-tab title="Melzinho na chupeta">
          <RankingCourses
            :primeiro_lugar="top_mamao[0]"
            :segundo_lugar="top_mamao[1]"
            :terceiro_lugar="top_mamao[2]"
          />
        </b-tab>
      </b-tabs>
    </b-container>
  </div>
</template>

<script>
import RankingCourses from '@/components/RankingCourses.vue'
import Header from '@/components/Header.vue'

export default {
  name: 'HomePage',
  components: {
    RankingCourses,
    Header
  },
  data () {
    return {
      top_mamao: '',
      top_penoso: ''
    }
  },
  created () {
    this.$http.get(this.$api_url + '/api/disciplinas/top/3/mamao', {})
      .then(response => {
        if (response.data) {
          this.top_mamao = response.data
        }
      })
    this.$http.get(this.$api_url + '/api/disciplinas/top/3/penoso', {})
      .then(response => {
        if (response.data) {
          this.top_penoso = response.data
        }
      })
  }
}
</script>

<style src='@/assets/styles/home_page_style.css'>
</style>
