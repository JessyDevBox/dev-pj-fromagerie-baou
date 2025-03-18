<template>
  <b-card class="bg-light">
    <h5 class="mb-3">{{ title }}</h5>
    
    <slot></slot>
    
    <hr v-if="showContact">
    
    <div v-if="showContact">
      <p class="mb-2">
        <b-icon icon="question-circle" class="me-2"></b-icon>
        <b-link to="/faq">{{ $t('cart.faq') }}</b-link>
      </p>
      <p class="mb-2">
        <b-icon icon="telephone" class="me-2"></b-icon>
        <b-link href="tel:+33442046789">+33 4 42 04 67 89</b-link>
      </p>
      <p class="mb-0">
        <b-icon icon="envelope" class="me-2"></b-icon>
        <b-link href="mailto:contact@fromageriedubaou.fr">contact@fromageriedubaou.fr</b-link>
      </p>
    </div>
  </b-card>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },
    showContact: {
      type: Boolean,
      default: true
    }
  }
}
</script>
