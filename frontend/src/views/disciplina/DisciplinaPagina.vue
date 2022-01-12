<template>
<div id='CoursePage'>
   <Header />
  <b-container>
    <b-alert v-show="avaliacao_erro" show variant="danger">{{ avaliacao_erro }}</b-alert>
    <b-row align-v="start" class="page-header">
      <b-col class="course-name-area">{{ disciplina.nome }}</b-col>
      <b-col class="rating-area">
        <b-progress variant="danger" height="2rem">
          <b-progress-bar :value="val_penoso">
            <span><strong>{{ val_penoso }}%</strong> Penosa</span>
          </b-progress-bar>
        </b-progress>
        <b-progress variant="success" height="2rem">
          <b-progress-bar :value="val_mamao">
            <span><strong>{{ val_mamao }}%</strong> Mamão</span>
          </b-progress-bar>
        </b-progress>
      </b-col>
    </b-row>
    <div v-if="n_avaliou_disciplina" class="user-rating p-3 ">
      <b-form-group :label=" ((disciplina.num_mamao + disciplina.num_penoso) < 2) ? 'Seja um dos primeiros a avaliar' : 'Avalie essa disciplina!'">
        <b-form-radio-group
          id="btn-radios-3"
          v-model="selected"
          :options="options"
          buttons
          name="radio-btn-stacked"
        ></b-form-radio-group>
      </b-form-group>
    </div>
    <div v-else  class="user-rating p-3 ">
      <p>Você já avaliou essa disciplina!</p>
    </div>
    <b-tabs card>
      <b-tab title="Comentários" active>
        <div class="comment_button">
          <div v-if="adicionar_comentario">
            <b-alert v-show="comentario_erro" show variant="danger">{{ comentario_erro }}</b-alert>
            <b-button pill variant="danger" class="close_button" @click="adicionar_comentario = !adicionar_comentario">Fechar</b-button>
            <b-button pill variant="success" class="btn text-center" @click="cadastrar_comentario">Enviar</b-button>
          </div>
          <div v-else>
            <b-button v-if="comments.length === 0" pill variant="success" class="btn text-center" @click="adicionar_comentario = !adicionar_comentario">Seja o Primeiro a comentar</b-button>
            <b-button v-else pill variant="success" class="btn text-center" @click="adicionar_comentario = !adicionar_comentario">Adicionar Comentário</b-button>
          </div>
          <div class="comment_form" v-show="adicionar_comentario">
            <b-form-textarea
              id="textarea"
              v-model="comentario"
              placeholder="Digite seu comentário..."
              rows="3"
              max-rows="6"
            ></b-form-textarea>
          </div>
        </div>
        <CommentBox
          v-for="comment in comments"
          v-bind:key="comment.id_comentario"
          v-bind:id="comment.id_comentario"
          v-bind:name="comment.username"
          v-bind:picture="comment.picture"
          v-bind:comment="comment.texto"
          v-bind:likes="comment.num_gostei"
          v-bind:dislikes="comment.num_nao_gostei"
        />
      </b-tab>
      <b-tab title="Links úteis">
        <div class="comment_button">
          <div v-if="adicionar_link">
            <b-alert v-show="link_erro" show variant="danger">{{ link_erro }}</b-alert>
            <b-button pill variant="danger" class="close_button" @click="adicionar_link = !adicionar_link">Fechar</b-button>
            <b-button pill variant="success" class="btn text-center" @click="cadastrar_link">Enviar</b-button>
          </div>
          <div v-else>
            <b-button pill variant="success" class="btn text-center" @click="adicionar_link = !adicionar_link">Adicionar link</b-button>
          </div>

          <div class="comment_form" v-show="adicionar_link">
            <label for="link_titulo">Titulo</label>
            <b-form-input
              id="link_titulo"
              type="text"
              v-model="link_titulo"
              placeholder="Digite o titulo do seu link..."
              rows="3"
              max-rows="6"
              class="link_container"
            ></b-form-input>
            <label for="link_url">Link</label>
            <b-form-input
              id="link_url"
              type="url"
              v-model="link_url"
              placeholder="Cole sua URL..."
              rows="3"
              max-rows="6"
            ></b-form-input>
          </div>
        </div>
        <LinkBox
          v-for="link in links"
          v-bind:key="link.id_comentario"
          v-bind:name="link.username"
          v-bind:picture="link.picture"
          v-bind:link="link.link"
          v-bind:titulo="link.titulo"
        />
      </b-tab>
      <b-tab title="Arquivos relacionados">
        <div class="comment_button">
          <div v-if="adicionar_arquivo">
            <b-alert v-show="arquivo_erro" show variant="danger">{{ arquivo_erro }}</b-alert>
            <b-button pill variant="danger" class="close_button" @click="adicionar_arquivo = !adicionar_arquivo">Fechar</b-button>
            <b-button pill variant="success" class="btn text-center" @click="cadastrar_arquivo">Enviar</b-button>
          </div>
          <div v-else>
            <b-button pill variant="success" class="btn text-center" @click="adicionar_arquivo = !adicionar_arquivo">Adicionar arquivo</b-button>
          </div>

          <div class="comment_form" v-show="adicionar_arquivo">
            <label for="arquivo_titulo">Descrição do arquivo</label>
            <b-form-input
              id="arquivo_titulo"
              type="text"
              v-model="arquivo.descricao"
              placeholder="Descrição do arquivo..."
              rows="3"
              max-rows="6"
              class="comment-container"
            ></b-form-input>
            <label for="arquivo_dados">Arquivo</label>
            <b-form-file
              id="arquivo_dados"
              v-model="arquivo.dados"
              :state="Boolean(arquivo.dados)"
              placeholder="Selecione um arquivo ou o arraste aqui..."
              drop-placeholder="Arraste o arquivo..."
              rows="3"
              max-rows="6"
              class="comment-container"
            ></b-form-file>
          </div>
        </div>
        <FileBox
          v-for="arquivo in arquivos"
          v-bind:key="arquivo.id_arquivo"
          v-bind:id="arquivo.id_arquivo"
          v-bind:name="arquivo.username"
          v-bind:picture="arquivo.picture"
          v-bind:nome="arquivo.nome"
          v-bind:descricao="arquivo.descricao"
        />
      </b-tab>
    </b-tabs>
  </b-container>
</div>
</template>

<script>
import CommentBox from '@/components/CommentBox.vue'
import LinkBox from '@/components/LinkBox.vue'
import FileBox from '@/components/FileBox.vue'
import Header from '@/components/Header.vue'

export default {
  name: 'DisciplinaPagina',
  components: {
    CommentBox,
    LinkBox,
    FileBox,
    Header
  },
  data: () => {
    return {
      id_disciplina: '',
      disciplina: { num_mamao: 0, num_penoso: 0 },
      comments: [],
      links: [],
      arquivos: [],
      val_mamao: 0,
      val_penoso: 0,
      selected: '',
      options: [
        { text: 'Penosa', value: 'penoso' },
        { text: 'Mamão', value: 'mamao' }
      ],
      adicionar_comentario: false,
      adicionar_link: false,
      adicionar_arquivo: false,
      n_avaliou_disciplina: true,
      comentario: '',
      teste: '',
      avaliacao_erro: '',
      link_erro: '',
      comentario_erro: '',
      arquivo_erro: '',
      link_titulo: '',
      link_url: '',
      arquivo: {
        descricao: '',
        dados: ''
      }
    }
  },
  methods: {
    to_base64: async function (file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = () => resolve(reader.result)
        reader.onerror = error => reject(error)
      })
    },
    cadastrar_comentario: function (e) {
      e.preventDefault()
      if (!this.comentario) {
        this.comentario_erro = 'Escreva seu comentário!'
      } else {
        this.$http.post(this.$api_url + '/api/cadastro/comentario', {
          id_disciplina: this.id_disciplina,
          comentario: this.comentario
        })
          .then(response => {
            if (response.data.status === 'error') {
              this.comentario_erro = response.data.message
            } else {
              this.comentario = ''
              this.adicionar_comentario = false
              this.get_comentarios()
            }
          })
      }
    },
    cadastrar_link: function (e) {
      e.preventDefault()
      if (!this.link_url | !this.link_titulo) {
        this.link_erro = 'Escreva seu titulo e a url!'
      } else {
        this.$http.post(this.$api_url + '/api/cadastro/link', {
          id_disciplina: this.id_disciplina,
          titulo: this.link_titulo,
          link: this.link_url
        })
          .then(response => {
            if (response.data.status === 'error') {
              this.link_erro = response.data.message
            } else {
              this.link_titulo = ''
              this.link_url = ''
              this.adicionar_link = false
              this.get_links()
            }
          })
      }
    },
    cadastrar_arquivo: async function (e) {
      e.preventDefault()
      if (!this.arquivo.descricao | !this.arquivo.dados) {
        this.arquivo_erro = 'Defina o nome do arquivo e o envie!'
      } else {
        let dados = await this.to_base64(this.arquivo.dados)
        dados = dados.split(';base64,')
        this.$http.post(this.$api_url + '/api/cadastro/arquivo', {
          id_disciplina: this.id_disciplina,
          nome: this.arquivo.dados.name,
          descricao: this.arquivo.descricao,
          mimetype: dados[0].split(':')[1],
          dados: dados[1]
        })
          .then(response => {
            if (response.data.status === 'error') {
              this.arquivo_erro = response.data.message
            } else {
              this.arquivo.nome = ''
              this.arquivo.mimetype = ''
              this.arquivo.descricao = ''
              this.arquivo.dados = ''
              this.adicionar_arquivo = false
              this.get_arquivos()
            }
          })
      }
    },
    get_comentarios: function () {
      this.$http.get(this.$api_url + '/api/comentarios/' + this.id_disciplina)
        .then(response => {
          this.comments = response.data
        })
    },
    get_links: function () {
      this.$http.get(this.$api_url + '/api/links/' + this.id_disciplina)
        .then(response => {
          this.links = response.data
        })
    },
    get_arquivos: function () {
      this.$http.get(this.$api_url + '/api/arquivos/' + this.id_disciplina)
        .then(response => {
          this.arquivos = response.data
        })
    },
    get_disciplina: function () {
      this.$http.get(this.$api_url + '/api/disciplina/' + this.id_disciplina)
        .then(response => {
          this.disciplina = response.data
        })
    },
    get_avaliou_disciplina: function () {
      this.$http.get(this.$api_url + '/api/avaliou_disciplina/' + this.id_disciplina)
        .then(response => {
          if (response.data.status === 'avaliado') {
            this.n_avaliou_disciplina = false
          } else {
            this.n_avaliou_disciplina = true
          }
        })
    }
  },
  watch: {
    selected: function () {
      this.$http.post(this.$api_url + '/api/cadastro/avaliacao_disciplina', {
        id_disciplina: this.id_disciplina,
        penoso_mamao: this.selected
      })
        .then(response => {
          if (response.data.status === 'error') {
            this.avaliacao_erro = response.data.message
          } else {
            this.get_disciplina()
          }
        })
    },
    disciplina: function () {
      this.val_penoso = (this.disciplina.num_penoso / (this.disciplina.num_mamao + this.disciplina.num_penoso)).toFixed(2) * 100
      this.val_mamao = 100 - this.val_penoso
    }
  },
  created () {
    this.id_disciplina = window.location.href.split('/').pop()
    this.get_avaliou_disciplina()
    this.get_disciplina()
    this.get_comentarios()
    this.get_links()
    this.get_arquivos()
  }
}
</script>

<style src='@/assets/styles/course_page_style.css' scoped></style>
