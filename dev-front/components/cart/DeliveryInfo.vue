<template>
  <b-row>
    <b-col lg="8">
      <!-- Options de livraison -->
      <b-card class="mb-4">
        <h3 class="mb-4">{{ $t('cart.deliveryMethod') }}</h3>
        
        <b-form-group>
          <b-form-radio-group
            v-model="localDelivery.method"
            stacked
            @change="updateMethod"
          >
            <template #first>
              <b-form-radio value="pickup" class="p-3 border rounded mb-3">
                <div class="d-flex align-items-center">
                  <b-icon icon="shop" variant="primary" font-scale="1.5" class="me-3"></b-icon>
                  <div>
                    <div class="fw-bold">{{ $t('cart.pickup.title') }}</div>
                    <div class="text-muted">{{ $t('cart.pickup.description') }}</div>
                    <div class="text-success mt-1">{{ $t('cart.free') }}</div>
                  </div>
                </div>
              </b-form-radio>
              
              <b-form-radio value="local" class="p-3 border rounded mb-3">
                <div class="d-flex align-items-center">
                  <b-icon icon="truck" variant="primary" font-scale="1.5" class="me-3"></b-icon>
                  <div>
                    <div class="fw-bold">{{ $t('cart.localDelivery.title') }}</div>
                    <div class="text-muted">{{ $t('cart.localDelivery.description') }}</div>
                    <div v-if="cart.subtotal >= 50" class="text-success mt-1">{{ $t('cart.free') }}</div>
                    <div v-else class="mt-1">5€</div>
                  </div>
                </div>
              </b-form-radio>
              
              <b-form-radio value="shipping" class="p-3 border rounded">
                <div class="d-flex align-items-center">
                  <b-icon icon="box-seam" variant="primary" font-scale="1.5" class="me-3"></b-icon>
                  <div>
                    <div class="fw-bold">{{ $t('cart.shipping.title') }}</div>
                    <div class="text-muted">{{ $t('cart.shipping.description') }}</div>
                    <div v-if="cart.subtotal >= 80" class="text-success mt-1">{{ $t('cart.free') }}</div>
                    <div v-else class="mt-1">12€</div>
                  </div>
                </div>
              </b-form-radio>
            </template>
          </b-form-radio-group>
        </b-form-group>
      </b-card>
      
      <!-- Adresse de livraison -->
      <b-card v-if="localDelivery.method !== 'pickup'" class="mb-4">
        <h3 class="mb-4">{{ $t('cart.deliveryAddress') }}</h3>
        
        <b-form>
          <b-row>
            <b-col md="6">
              <b-form-group :label="$t('cart.firstName')">
                <b-form-input v-model="localDelivery.firstName" required></b-form-input>
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group :label="$t('cart.lastName')">
                <b-form-input v-model="localDelivery.lastName" required></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
          
          <b-form-group :label="$t('cart.address')">
            <b-form-input v-model="localDelivery.address" required></b-form-input>
          </b-form-group>
          
          <b-row>
            <b-col md="4">
              <b-form-group :label="$t('cart.postalCode')">
                <b-form-input v-model="localDelivery.postalCode" required></b-form-input>
              </b-form-group>
            </b-col>
            <b-col md="8">
              <b-form-group :label="$t('cart.city')">
                <b-form-input v-model="localDelivery.city" required></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
          
          <b-form-group :label="$t('cart.phone')">
            <b-form-input v-model="localDelivery.phone" required></b-form-input>
          </b-form-group>
          
          <b-form-group :label="$t('cart.email')">
            <b-form-input v-model="localDelivery.email" type="email" required></b-form-input>
          </b-form-group>
          
          <b-form-group :label="$t('cart.instructions')">
            <b-form-textarea v-model="localDelivery.instructions" rows="3"></b-form-textarea>
          </b-form-group>
        </b-form>
      </b-card>
      
      <!-- Informations de retrait -->
      <b-card v-if="localDelivery.method === 'pickup'" class="mb-4">
        <h3 class="mb-4">{{ $t('cart.pickupDetails') }}</h3>
        
        <b-form>
          <p>
            <b-icon icon="geo-alt" class="me-2"></b-icon>
            <strong>{{ $t('cart.pickupLocation') }}:</strong> 15 Avenue des Alpes, 13124 Peypin
          </p>
          
          <b-form-group :label="$t('cart.pickupDate')">
            <b-form-datepicker v-model="localDelivery.pickupDate" :min="minPickupDate" required></b-form-datepicker>
          </b-form-group>
          
          <b-form-group :label="$t('cart.pickupTime')">
            <b-form-select v-model="localDelivery.pickupTime" :options="pickupTimeOptions" required></b-form-select>
          </b-form-group>
          
          <b-row>
            <b-col md="6">
              <b-form-group :label="$t('cart.firstName')">
                <b-form-input v-model="localDelivery.firstName" required></b-form-input>
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group :label="$t('cart.lastName')">
                <b-form-input v-model="localDelivery.lastName" required></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
          
          <b-form-group :label="$t('cart.phone')">
            <b-form-input v-model="localDelivery.phone" required></b-form-input>
          </b-form-group>
          
          <b-form-group :label="$t('cart.email')">
            <b-form-input v-model="localDelivery.email" type="email" required></b-form-input>
          </b-form-group>
        </b-form>
      </b-card>
      
      <!-- Navigation -->
      <div class="d-flex justify-content-between">
        <b-button variant="outline-secondary" @click="$emit('back-to-cart')">
          <b-icon icon="arrow-left" class="me-2"></b-icon>
          {{ $t('cart.backToCart') }}
        </b-button>
        <b-button variant="primary" @click="$emit('proceed-to-payment')" :disabled="!isFormValid">
          {{ $t('cart.proceedToPayment') }}
        </b-button>
      </div>
    </b-col>
    
    <b-col lg="4">
      <!-- Résumé de la commande -->
      <b-card class="mb-4">
        <h3 class="mb-4">{{ $t('cart.orderSummary') }}</h3>
        
        <div class="mb-3">
          <div v-for="(item, index) in cart.items" :key="index" class="d-flex justify-content-between mb-2">
            <span>{{ item.name }} × {{ item.quantity }}</span>
            <span>{{ formatPrice(item.price * item.quantity) }}</span>
          </div>
        </div>
        
        <hr>
        
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
      </b-card>
      
      <!-- Aide -->
      <b-card class="bg-light">
        <h5 class="mb-3">{{ $t('cart.deliveryInfo') }}</h5>
        
        <div v-if="localDelivery.method === 'pickup'" class="mb-3">
          <p class="mb-2">
            <b-icon icon="info-circle" class="me-2"></b-icon>
            {{ $t('cart.pickup.info') }}
          </p>
          <p class="mb-0">
            <b-icon icon="clock" class="me-2"></b-icon>
            {{ $t('cart.pickup.hours') }}
          </p>
        </div>
        
        <div v-else-if="localDelivery.method === 'local'" class="mb-3">
          <p class="mb-2">
            <b-icon icon="info-circle" class="me-2"></b-icon>
            {{ $t('cart.localDelivery.info') }}
          </p>
          <p class="mb-0">
            <b-icon icon="geo-alt" class="me-2"></b-icon>
            {{ $t('cart.localDelivery.area') }}
          </p>
        </div>
        
        <div v-else class="mb-3">
          <p class="mb-2">
            <b-icon icon="info-circle" class="me-2"></b-icon>
            {{ $t('cart.shipping.info') }}
          </p>
          <p class="mb-0">
            <b-icon icon="truck" class="me-2"></b-icon>
            {{ $t('cart.shipping.delay') }}
          </p>
        </div>
        
        <hr>
        
        <p class="mb-0">
          <b-icon icon="telephone" class="me-2"></b-icon>
          <b-link href="tel:+33442046789">+33 4 42 04 67 89</b-link>
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
    },
    value: {
      type: Object,
      required: true
    },
    minPickupDate: {
      type: String,
      required: true
    },
    pickupTimeOptions: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      localDelivery: { ...this.value }
    }
  },
  computed: {
    isFormValid() {
      if (this.localDelivery.method === 'pickup') {
        return this.localDelivery.firstName && 
               this.localDelivery.lastName && 
               this.localDelivery.phone && 
               this.localDelivery.email &&
               this.localDelivery.pickupDate &&
               this.localDelivery.pickupTime;
      } else {
        return this.localDelivery.firstName && 
               this.localDelivery.lastName && 
               this.localDelivery.address && 
               this.localDelivery.postalCode && 
               this.localDelivery.city && 
               this.localDelivery.phone && 
               this.localDelivery.email;
      }
    }
  },
  methods: {
    formatPrice(price) {
      return new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR' }).format(price);
    },
    updateMethod() {
      this.$emit('input', this.localDelivery);
    }
  },
  watch: {
    localDelivery: {
      handler(newVal) {
        this.$emit('input', newVal);
      },
      deep: true
    },
    value: {
      handler(newVal) {
        this.localDelivery = { ...newVal };
      },
      deep: true
    }
  }
}
</script>

<style scoped>
.form-check {
  transition: background-color 0.3s ease;
}

.form-check:hover {
  background-color: #f8f9fa;
}
</style>
