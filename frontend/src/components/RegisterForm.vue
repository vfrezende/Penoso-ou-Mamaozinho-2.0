<template>
<div>
<div class="container">
  <div class="info">
    <h1>Faça parte do PoM</h1>
    <b-alert v-show="error_message" show variant="danger">{{ error_message }}</b-alert>
  </div>
</div>
<div class="form">
  <div class="thumbnail"><img src="@/assets/images/pom_logo.png"/></div>
  <form
    id="register"
    @submit="register_user"
    method="post"
     class="login-form"
  >
    <input id="name" v-model="form.name" name="name" type="text" placeholder="name" required/>
    <input id="email" v-model="form.email" name="email" type="email" placeholder="email address" required/>
    <input id="username" v-model="form.username" name="username" type="text" placeholder="username" required/>
    <input id="picture" v-model="form.picture" name="picture" type="url" placeholder="Picture URL (can use github profile pic url)"/>
    <input id="password" v-model="form.password" name="password" type="password" placeholder="password" required/>
    <input id="confirm" v-model="password_confirm" name="confirm" type="password" placeholder="confirm password" required/>
    <button>Cadastrar</button>
    <p class="message">Já possui cadastro? <a href="/login">Sign In</a></p>
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
        password: '',
        picture: ''
      },
      password_confirm: '',
      error_message: ''
    }
  },
  methods: {
    register_user: function (e) {
      e.preventDefault()
      if (this.form.password !== this.password_confirm) {
        this.error_message = 'Senhas não combinam.'
        this.form.password = ''
        this.password_confirm = ''
      } else if (this.form.name.length < 1 || this.form.name.length > 50) {
        this.error_message = 'Nome deve ter pelo menos 1 caractere e no maximo 50.'
        this.form.name = ''
        this.form.password = ''
        this.password_confirm = ''
      } else if (this.form.username.length < 4 || this.form.username.length > 25) {
        this.error_message = 'Username deve ter pelo menos 4 caracteres e no maximo 25.'
        this.form.username = ''
        this.form.password = ''
        this.password_confirm = ''
      } else if (this.form.email.length < 6 || this.form.email.length > 50) {
        this.error_message = 'Email deve ter pelo menos 6 caracteres e no maximo 50.'
        this.form.email = ''
        this.form.password = ''
        this.password_confirm = ''
      } else if (this.form.password.length < 6 || this.form.password.length > 50) {
        this.error_message = 'Senha deve ter pelo menos 6 caractere e no maximo 50.'
        this.form.password = ''
        this.password_confirm = ''
      } else {
        this.$http.post(this.$api_url + '/api/cadastro/usuario', this.form)
          .then(response => {
            if (response.data.status === 'error') {
              this.error_message = response.data.message
              this.form.name = ''
              this.form.email = ''
              this.form.username = ''
              this.form.password = ''
              this.form.picture = ''
              this.password_confirm = ''
            } else {
              window.location.href = '/login?successfully_registered'
            }
          })
      }
    }
  }
}
</script>

<style src='@/assets/styles/register_form_style.css' scoped></style>
