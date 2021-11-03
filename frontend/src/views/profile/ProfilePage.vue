<template>
  <div id="ProfilePage">
    <Header />
    <ProfileInfoForm />
  </div>
</template>

<script>
import ProfileInfoForm from '@/components/ProfileInfoForm.vue'
import Header from '@/components/Header.vue'

export default {
  name: 'ProfilePage',
  components: {
    ProfileInfoForm,
    Header
  },
  data: () => {
    return {}
  },
}
</script>

<style src='@/assets/styles/home_page_style.css'>
</style>
