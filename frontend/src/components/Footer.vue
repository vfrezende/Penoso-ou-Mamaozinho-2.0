<template>
    <div id="container">
        <div id="contacts">
          <div id="contacts--contact">
            <a href="mailto: penosomamaozinho@gmail.com?subject=HelloTest"   target="_blank">penosomamaozinho@gmail.com</a>
            <p>{{ phone }}</p>
          </div>
        <div id="contacts--social">
          <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <div>
              <a href="https://www.facebook.com/Penoso-Mamaozinho-105847831891516" class="fa fa-facebook"></a>
            </div>
            <div>
              <a href="https://twitter.com/PMamaozinho" class="fa fa-twitter"></a>
            </div>
            <div>
              <a href="https://www.instagram.com/penosomamaozinho/" class="fa fa-instagram"></a>
            </div>
          </div>
        </div>
        <div id="mentions">
          <p>{{ mention }}</p>
        </div>
   </div>
</template>

<script>
export default {
  data: function () {
    return {
      phone: 'Telefone: (31)99988-7766',
      mention: 'Copyright © 2020-2021 LTDA.'
    }
  }
}
</script>

<style src='@/assets/styles/footer_style.css'>
</style>
