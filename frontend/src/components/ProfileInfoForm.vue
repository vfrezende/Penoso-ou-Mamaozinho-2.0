<template>
<div>
<div class="container">
  <div class="info">
  <b-alert v-show="error_message" show variant="danger">{{ error_message }}</b-alert>
    <b-alert v-show="successfully_updated_message" show variant="success">{{ successfully_updated_message }}</b-alert>
    <h1>Salve, {{ getFirstName() }}!</h1>
  </div>
</div>
<div class="form">
  <div class="thumbnail"><img v-bind:src="form.picture" alt="No User Icon"/></div>
  <b-form @submit="updateProfileInfo">
      <b-form-group
        id="input-group-name"
        label="Nome:"
        label-for="input-name"
      >
        <b-form-input
          id="input-name"
          v-model="form.name"
          type="text"
          placeholder="Insira o nome"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-pic"
        label="Foto do perfil"
        label-for="input-picture"
        description="Insira a URL da imagem"
      >
        <b-form-input
          id="input-picture"
          v-model="form.picture"
          type="url"
          placeholder="Insira o link"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-password"
        label="Senha do usuário"
        label-for="input-password"
      >
        <b-form-input
          id="input-password"
          v-model="form.password"
          type="password"
          placeholder="Insira a senha"
        ></b-form-input>
      </b-form-group>

      <b-button style="margin-right: 1em"  type="submit" variant="primary">Atualizar</b-button>
      <b-button v-show="hasDataChanged" variant="danger" @click="resetProfileInfo">Desfazer</b-button>
    </b-form>

</div>
</div>
</template>
<script>

export default {
  data: () => {
    return {
      empty_password: '',
      successfully_updated_message: '',
      error_message: '',
      form: {
        name: '',
        picture: '',
        password: ''
      },
      user_data: {
        email: '',
        name: '',
        picture: ''
      }
    }
  },
  methods: {
    hasDataChanged: function () {
      return this.form.name !== this.user_data.name ||
             this.form.picture !== this.user_data.picture ||
             this.form.password !== this.empty_password
    },
    updateProfileInfo (event) {
      event.preventDefault()
      if (!this.hasDataChanged()) {
        this.error_message = 'Nenhuma informação foi alterada!'
        this.successfully_updated_message = ''
      } else {
        this.$http.post(this.$api_url + '/api/update/usuario', this.form)
          .then(response => {
            if (response.data.status === 'success') {
              this.error_message = ''
              this.successfully_updated_message = 'Perfil atualizado com sucesso!'
              this.getUserData()
            } else {
              this.error_message = response.data.message
              this.successfully_updated_message = ''
            }
          })
          .catch(error => {
            this.error_message = error
            this.successfully_updated_message = ''
          })
      }
    },
    getFirstName () {
      return this.user_data.name.split(' ')[0]
    },
    resetProfileInfo () {
      this.form.name = this.user_data.name
      this.form.picture = this.user_data.picture
      this.form.password = this.empty_password
    },
    getUserData () {
      this.$http.post(this.$api_url + '/api/usuario', {})
        .then(response => {
          if (response.data.status === 'success') {
            this.user_data = response.data
            this.resetProfileInfo()
          }
        }
        )
    }
  },
  created () {
    if (window.location.href.match('successfully_registered')) {
      this.successfully_registered_message = 'Registrado com Sucesso!'
    }
    this.getUserData()
    this.resetProfileInfo()
  }
}
</script>

<style src='@/assets/styles/login_form_style.css' scoped></style>
