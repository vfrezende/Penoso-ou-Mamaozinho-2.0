<template>
  <div id="AddDisciplinaPage">
    <Header />
    <DisciplinaForm v-if="logged_in" />
    <b-container v-else>
        <p>
            É necessario fazer login para adicionar uma nova disciplina.
        </p>
        <a href="/login">Pagina de Login</a>
    </b-container>
  </div>
</template>

<script>
import DisciplinaForm from '@/components/DisciplinaForm.vue'
import Header from '@/components/Header.vue'

export default {
  name: 'AddDisciplinaPage',
  components: {
    DisciplinaForm,
    Header
  },
  data: () => {
    return {
      logged_in: false
    }
  },
  created: function () {
    this.$http.post(this.$api_url + '/api/usuario', {})
      .then(response => {
        if (response.data.status === 'success') {
          this.logged_in = true
        }
        this.logged_in = true
      })
  }
}
</script>

<style src='@/assets/styles/home_page_style.css'>
</style>
