<template>
  <div id="LoginPage">
    <Header />
    <LoginForm />
    <Footer />
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'LoginPage',
  components: {
    LoginForm,
    Header,
    Footer
  },
  data: () => {
    return {}
  },
  created: function () {
    this.$http.post(this.$api_url + '/api/usuario', {})
      .then(response => {
        if (response.data.status === 'success') {
          window.location.href = '/home'
        }
      })
  }
}
</script>

<style src='@/assets/styles/home_page_style.css'>
</style>
