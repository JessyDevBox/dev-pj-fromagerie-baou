<template>
  <b-card class="mb-4">
    <h3 class="mb-4">{{ $t('cart.orderSummary') }}</h3>
    
    <div v-if="showItems" class="mb-3">
      <div v-for="(item, index) in cart.items" :key="index" class="d-flex justify-content-between mb-2">
        <span>{{ item.name }} × {{ item.quantity }}</span>
        <span>{{ formatPrice(item.price * item.quantity) }}</span>
      </div>
    </div>
    
    <hr v-if="showItems">
    
    <div class="d-flex justify-content-between mb-2">
      <span>{{ $t('cart.subtotal') }}</span>
      <span>{{ formatPrice(cart.subtotal) }}</span>
    </div>
    
    <div v-if="cart.discount > 0" class="d-flex justify-content-between mb-2 text-success">
      <span>{{ $t('cart.discount') }}</span>
      <span>-{{ formatPrice(cart.discount) }}</span>
    </div>
    
    <div class="d-flex justify-content-between mb-2">
      <span>{{ $t('cart.shipping') }}</span>
      <span v-if="cart.shippingCost > 0">{{ formatPrice(cart.shippingCost) }}</span>
      <span v-else class="text-success">{{ $t('cart.free') }}</span>
    </div>
    
    <hr>
    
    <div class="d-flex justify-content-between mb-3 fw-bold">
      <span>{{ $t('cart.total') }}</span>
      <span class="fs-5">{{ formatPrice(cart.total) }}</span>
    </div>
    
    <div v-if="showButton" class="d-grid gap-2">
      <b-button variant="primary" @click="$emit('proceed')">
        {{ buttonText }}
      </b-button>
    </div>
  </b-card>
</template>

<script>
export default {
  props: {
    cart: {
      type: Object,
      required: true
    },
    showItems: {
      type: Boolean,
      default: true
    },
    showButton: {
      type: Boolean,
      default: false
    },
    buttonText: {
      type: String,
      default: ''
    }
  },
  methods: {
    formatPrice(price) {
      return new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR' }).format(price);
    }
  }
}
</script>
