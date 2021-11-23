<template>
<div class="header">
  <div id="header-container">
    <b-navbar toggleable="lg" type="light" >
    <b-navbar-brand href="/home">
      <img class="icon" src="../assets/images/pom_logo.png" alt="PoM Logo">
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>

      <!-- <b-nav-item class='add_disciplina' href='/adicionar/disciplina'>Adicionar disciplina</b-nav-item> -->

      <a class='add_disciplina' href="/adicionar_disciplina">Adicionar disciplina</a>

      <div class="live-search-container">
        <LiveSearch
          :options="disciplinas"
          :placeholder="'Pesquise o nome da disciplina'"
        />
      </div>

      <b-navbar-nav class="ml-auto">

      <b-nav-item-dropdown v-if="user_data.logged_in" right>
        <template v-slot:button-content>
        <img class="icon" v-bind:src="user_data.profile_picture" alt="User Icon">
        </template>
        <b-dropdown-item v-bind:href="profile_page()">
          Profile
        </b-dropdown-item>
        <b-dropdown-item href="/logout">Sign Out</b-dropdown-item>
      </b-nav-item-dropdown>
      <b-nav-item-dropdown v-else right>
        <template v-slot:button-content>
          <img class="icon" src="../assets/images/anonymousUser.png" alt="Anonymous User Icon">
        </template>
        <b-dropdown-item href='/login'>Sign in</b-dropdown-item>
      </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
    </b-navbar>
  </div>
</div>
</template>

<script>
import LiveSearch from './LiveSearch.vue'

export default {
  components: {
    LiveSearch
  },
  data: function () {
    return {
      courses: [
        {
          name: 'materia 1',
          id: 1,
          sanitizedName: 'Um belo Nome'
        },
        {
          name: 'materia 2',
          id: 2,
          sanitizedName: 'Essa eh a materia 2e'
        },
        {
          name: 'materia 3',
          id: 3,
          sanitizedName: 'FEIJAOZINHO'
        }
      ],
      disciplinas: [],
      user_data: ''
    }
  },
  methods: {
    profile_page: function () {
      return '/profile'
    }
  },
  created () {
    this.$http.post(this.$api_url + '/api/usuario', {})
      .then(response => {
        if (response.data.status === 'success') {
          this.user_data = response.data
          this.user_data.logged_in = true
        } else {
          this.user_data = {
            logged_in: false
          }
        }
      })
    this.$http.get(this.$api_url + '/api/disciplinas')
      .then(response => {
        if (response.data) {
          this.disciplinas = response.data
        }
      })
  }
}
</script>

<style scoped>

  .header {
    background-color: #582525;
    margin-bottom: 2.4rem;
  }
  .live-search-container {
    width: 100%;
  }
  .icon {
    width: 50px;
    margin-left: 1.2rem;
    border-radius: 0.6rem;
  }
  .add_disciplina {
    margin-left: 1.2rem;
    color: #f7f7f7;
  }
</style>
