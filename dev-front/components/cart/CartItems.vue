<template>
  <b-row>
    <b-col lg="8">
      <!-- Liste des produits -->
      <b-card class="mb-4">
        <h3 class="mb-4">{{ $t('cart.yourItems') }}</h3>
        
        <div v-for="(item, index) in cart.items" :key="index" class="cart-item mb-3 p-3 border-bottom">
          <b-row align-v="center">
            <b-col cols="3" sm="2">
              <b-img :src="item.image" fluid alt="Product image" class="cart-item-image"></b-img>
            </b-col>
            <b-col cols="9" sm="4">
              <h5 class="mb-1">{{ item.name }}</h5>
              <div class="text-muted small">{{ item.weight }}g</div>
              <div class="product-price">{{ formatPrice(item.price) }}</div>
            </b-col>
            <b-col cols="6" sm="3" class="mt-3 mt-sm-0">
              <b-input-group>
                <b-button variant="outline-secondary" @click="decreaseQuantity(index)">
                  <b-icon icon="dash"></b-icon>
                </b-button>
                <b-form-input
                  v-model.number="item.quantity"
                  type="number"
                  min="1"
                  class="text-center"
                  @change="updateCart"
                ></b-form-input>
                <b-button variant="outline-secondary" @click="increaseQuantity(index)">
                  <b-icon icon="plus"></b-icon>
                </b-button>
              </b-input-group>
            </b-col>
            <b-col cols="6" sm="2" class="text-end mt-3 mt-sm-0">
              <div class="fw-bold mb-2">{{ formatPrice(item.price * item.quantity) }}</div>
              <b-button variant="link" class="p-0 text-danger" @click="removeItem(index)">
                <b-icon icon="trash"></b-icon> {{ $t('cart.remove') }}
              </b-button>
            </b-col>
          </b-row>
        </div>
        
        <div class="d-flex justify-content-between align-items-center mt-4">
          <b-button variant="outline-secondary" to="/produits">
            <b-icon icon="arrow-left" class="me-2"></b-icon>
            {{ $t('cart.continueShopping') }}
          </b-button>
          <b-button variant="outline-primary" @click="updateCart">
            <b-icon icon="arrow-clockwise" class="me-2"></b-icon>
            {{ $t('cart.updateCart') }}
          </b-button>
        </div>
      </b-card>
      
      <!-- Code promo -->
      <b-card class="mb-4">
        <h5 class="mb-3">{{ $t('cart.promoCode') }}</h5>
        <b-form @submit.prevent="applyPromoCode" inline>
          <b-form-input
            v-model="promoCodeInput"
            :placeholder="$t('cart.enterPromoCode')"
            class="me-2 mb-2"
          ></b-form-input>
          <b-button type="submit" variant="outline-primary" class="mb-2">
            {{ $t('cart.apply') }}
          </b-button>
        </b-form>
      </b-card>
    </b-col>
    
    <b-col lg="4">
      <!-- Résumé de la commande -->
      <b-card class="mb-4">
        <h3 class="mb-4">{{ $t('cart.orderSummary') }}</h3>
        
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
        
        <div class="d-grid gap-2">
          <b-button variant="primary" @click="$emit('proceed-to-delivery')">
            {{ $t('cart.proceedToDelivery') }}
          </b-button>
        </div>
      </b-card>
      
      <!-- Aide -->
      <b-card class="bg-light">
        <h5 class="mb-3">{{ $t('cart.needHelp') }}</h5>
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
      </b-card>
    </b-col>
  </b-row>
</template>

<script>
export default {
  props: {
    cart: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      promoCodeInput: ''
    }
  },
  methods: {
    formatPrice(price) {
      return new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR' }).format(price);
    },
    updateCart() {
      this.$emit('update-cart');
    },
    removeItem(index) {
      this.$emit('remove-item', index);
    },
    increaseQuantity(index) {
      this.$emit('increase-quantity', index);
    },
    decreaseQuantity(index) {
      this.$emit('decrease-quantity', index);
    },
    applyPromoCode() {
      this.$emit('apply-promo-code', this.promoCodeInput);
      this.promoCodeInput = '';
    }
  }
}
</script>

<style scoped>
.cart-item {
  transition: background-color 0.3s ease;
}

.cart-item:hover {
  background-color: #f8f9fa;
}

.cart-item-image {
  max-height: 80px;
  object-fit: contain;
}
</style>
