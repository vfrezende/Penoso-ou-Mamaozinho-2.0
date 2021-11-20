<template>
<div>
<div class="container">
  <div class="info">
    <h1>Ajude o PoM a crescer &hearts; </h1>
    <b-alert v-show="error_message" show variant="danger">{{ error_message }}</b-alert>
  </div>
</div>
<div class="form">
  <div class="thumbnail"><img src="@/assets/images/pom_logo.png"/></div>
  <h4>Adicione uma nova disciplina </h4>
  <form
    id="register"
    @submit="register_user"
    method="post"
     class="login-form"
  >
    <input id="nome" v-model="form.nome" name="nome" type="text" placeholder="Nome da disciplina" required/>
    <div style="display: flex; justify-content: space-between;">
        <label for="penoso">Penosa</label>
        <input id="penoso" v-model="form.penoso_mamao" name="penoso_mamao" value="penoso" type="radio" required/>
    </div>
    <div style="display: flex; ">
        <label for="mamao">Mamaozinha</label>
        <input id="mamao" v-model="form.penoso_mamao" name="penoso_mamao" value="mamao"  type="radio" required/>
    </div>
    <button>Cadastrar</button>
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
        nome: '',
        penoso_mamao: ''
      },
      password_confirm: '',
      error_message: ''
    }
  },
  methods: {
    register_user: function (e) {
      e.preventDefault()
      if (this.form.nome.length < 3 || this.form.nome.length > 255) {
        this.error_message = 'Nome deve ter pelo menos 3 caracteres e no maximo 255.'
        this.form.nome = ''
      } else {
        this.$http.post(this.$api_url + '/api/cadastro/disciplina', this.form)
          .then(response => {
            if (response.data.status === 'error') {
              this.error_message = response.data.message
              this.form.nome = ''
              this.form.penoso_mamao = ''
            } else {
              window.location.href = '/home'
            }
          })
      }
    }
  }
}
</script>

<style scoped>
/* Form */
.form {
  position: relative;
  z-index: 1;
  background: #FFFFFF;
  max-width: 300px;
  margin: 0 auto 100px;
  /* padding: 30px; */
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  text-align: center;
}
.form .thumbnail {
  /* background: #EF3B3A; */
  width: 150px;
  height: 150px;
  margin: 0 auto 30px;
  /* padding: 50px 30px; */
  border-top-left-radius: 100%;
  border-top-right-radius: 100%;
  border-bottom-left-radius: 100%;
  border-bottom-right-radius: 100%;
  box-sizing: border-box;
}
.form .thumbnail img {
  border-radius: 1.2rem;
  display: block;
  width: 100%;
}
.form h4 {
  margin-bottom: 1.8rem;
}
.form input {
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  box-sizing: border-box;
  font-size: 14px;
}
.form button {
  outline: 0;
  background: #EF3B3A;
  width: 100%;
  border: 0;
  padding: 15px;
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  color: #FFFFFF;
  font-size: 14px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
}
.form .message {
  margin: 15px 0 0;
  color: #b3b3b3;
  font-size: 12px;
}
.form .message a {
  color: #EF3B3A;
  text-decoration: none;
}
.form .register-form {
  display: none;
}

.container {
  position: relative;
  z-index: 1;
  max-width: 300px;
  margin: 0 auto;
}
.container:before, .container:after {
  content: "";
  display: block;
  clear: both;
}
.container .info {
  margin: 50px auto;
  text-align: center;
}
.container .info h1 {
  margin: 0 0 15px;
  padding: 0;
  font-size: 36px;
  font-weight: 300;
  color: #1a1a1a;
}
.container .info span {
  color: #4d4d4d;
  font-size: 12px;
}
.container .info span a {
  color: #000000;
  text-decoration: none;
}
.container .info span .fa {
  color: #EF3B3A;
}

/* END Form */
/* Demo Purposes */
body {
  background: #ccc;
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
body:before {
  content: "";
  position: fixed;
  top: 0;
  left: 0;
  display: block;
  background: rgba(255, 255, 255, 0.8);
  width: 100%;
  height: 100%;
}

#video {
  z-index: -99;
  position: fixed;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  -webkit-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}

</style>
