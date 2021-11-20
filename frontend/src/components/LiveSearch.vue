<!-- src/components/LiveSearch.vue -->

<template>
  <div class="dropdown" v-if="options">

    <!-- Dropdown Input -->
    <div>
        <input class="dropdown-input"
        :name="name"
        @focus="showOptions()"
        @blur="exit()"
        @keyup="keyMonitor"
        v-model="searchFilter"
        :disabled="disabled"
        :placeholder="placeholder" />

    </div>

    <!-- Dropdown Menu -->
    <div
        class="dropdown-content-live-search text-center py-3"
        v-show="optionsShown"
      >
      <div
        @mousedown="selectOption(option)"
        v-for="(option, index) in filteredOptions"
        :key="index">
          <div  class="dropdown-item-live-search text-center">
            {{ option.nome || option.id || option.nome_limpo || '-' }}
          </div>
        <hr>
      </div >
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dropdown',
  template: 'Dropdown',
  props: {
    name: {
      type: String,
      required: false,
      default: 'dropdown',
      note: 'Input name'
    },
    options: {
      type: Array,
      required: true,
      // default: this.filteredOptions,
      note: 'Options of dropdown. An array of options with id and name'
    },
    placeholder: {
      type: String,
      required: false,
      default: 'Please select an option',
      note: 'Placeholder of dropdown'
    },
    disabled: {
      type: Boolean,
      required: false,
      default: false,
      note: 'Disable the dropdown'
    },
    maxItem: {
      type: Number,
      required: false,
      default: 6,
      note: 'Max items showing'
    }
  },
  data () {
    return {
      selected: {},
      optionsShown: false,
      searchFilter: ''
    }
  },
  created () {
    this.$emit('selected', this.selected)
  },
  computed: {
    filteredOptions () {
      const filtered = []
      // const regOption = new RegExp(this.searchFilter, 'ig');
      for (const option of this.options) {
        if (this.searchFilter.length < 1 || option.nome_limpo.match(this.searchFilter.toLowerCase())) {
          if (filtered.length < this.maxItem) {
            filtered.push(option)
          }
        }
      }
      return filtered
    }
  },
  methods: {
    selectOption (option) {
      this.selected = option
      this.optionsShown = false
      this.searchFilter = this.selected.nome
      this.$emit('selected', this.selected)
      window.location.href = '/disciplina/' + this.selected.id
    },
    showOptions () {
      if (!this.disabled) {
        // this.searchFilter = '';
        this.optionsShown = true
      }
    },
    exit () {
      this.optionsShown = false
      this.$emit('selected', this.selected)
    },
    // Selecting when pressing Enter
    keyMonitor: function (event) {
      if (event.key === 'Enter' && this.filteredOptions[0]) { this.selectOption(this.filteredOptions[0]) }
    }
  },
  watch: {
    searchFilter () {
      if (this.filteredOptions.length === 0) {
        this.selected = {}
      } else {
        this.selected = this.filteredOptions[0]
      }
      this.$emit('filter', this.searchFilter)
    }
  }
}
</script>

<style src='@/assets/styles/live_search_style.scss' lang="scss" scoped>
</style>
