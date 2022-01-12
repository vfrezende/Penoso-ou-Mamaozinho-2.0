<template>
  <div id="ProfilePage">
    <Header />
    <ProfileInfoForm />
    <Footer />
  </div>
</template>

<script>
import ProfileInfoForm from '@/components/ProfileInfoForm.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'ProfilePage',
  components: {
    ProfileInfoForm,
    Header,
    Footer
  },
  data: () => {
    return {}
  }
}
</script>

<style src='@/assets/styles/home_page_style.css'>
</style>
