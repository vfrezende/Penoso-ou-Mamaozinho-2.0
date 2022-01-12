<template>
  <div id="UnauthorizedPage">
    <Header />
    <b-container class="container">
      <h2> Opa opa, você não tem autorização para acessar essa página. </h2>
      <img class="main-image" src="@/assets/images/cop.png" alt="UnauthorizedCop" />
      <h3> Apenas usuários logados possuem permissão para ver informações sobre disciplinas. </h3>
      <p>
        Não possui cadastro no PoM? <a class="message" href="/register">Cadastre-se</a> agora mesmo!
        Já é cadastrado? Aproveite e faça o <a class="message" href="/login">login</a>.
      </p>
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'UnauthorizedPage',
  components: {
    Header,
    Footer
  }
}
</script>

<style src='@/assets/styles/unauthorized_page_style.css'>
</style>
