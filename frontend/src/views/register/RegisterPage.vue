<template>
  <div id="RegisterPage">
    <Header />
    <RegisterForm/>
    <Footer />
  </div>
</template>

<script>
import RegisterForm from '@/components/RegisterForm.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'RegisterPage',
  components: {
    RegisterForm,
    Header,
    Footer
  },
  data: () => {
    return {}
  },
  created () {
    this.$http.post(this.$api_url + '/api/usuario', {})
      .then(response => {
        if (response.data.status === 'success') {
          window.location.href = '/home'
        }
      })
  }
}
</script>

<style src='@/assets/styles/home_page_style.css'></style>
