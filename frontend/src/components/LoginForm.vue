<template>
<div>
<div class="container">
  <div class="info">
    <h1>Bem vindo de volta ao PoM!</h1>
    <b-alert v-show="error_message" show variant="danger">{{ error_message }}</b-alert>
    <b-alert v-show="successfully_registered_message" show variant="success">{{ successfully_registered_message }}</b-alert>
  </div>
</div>
<div class="form">
  <div class="thumbnail"><img src="@/assets/images/pom_logo.png"/></div>
  <form @submit="validateLogin" class="login-form">
    <input type="text" id="username" v-model="form.username" name="username" placeholder="username" required/>
    <input type="password" id="password" v-model="form.password" name="password" placeholder="password" required/>
     <input
      class="button"
      type="submit"
      value="Login"
    >
    <p class="message">Não possui cadastro? <a href="/register">Crie uma conta.</a></p>
  </form>
</div>
</div>

</template>

<script>

export default {
  data: () => {
    return {
      user_rate: null,
      form: {
        name: '',
        email: '',
        username: '',
        password: ''
      },
      error_message: '',
      successfully_registered_message: ''
    }
  },
  methods: {
    validateLogin: function (e) {
      e.preventDefault()

      this.$http.post(this.$api_url + '/api/login', this.form)
        .then(response => {
          if (response.data.status === 'success') {
            window.location.href = '/home'
          } else {
            this.error_message = response.data.message
          }
        })
        .catch(error => {
          this.error_message = error
        })
    }
  },
  created () {
    if (window.location.href.match('successfully_registered')) {
      this.successfully_registered_message = 'Registrado com Sucesso!'
    }
  }
}
</script>

<style src='@/assets/styles/login_form_style.css' scoped></style>
