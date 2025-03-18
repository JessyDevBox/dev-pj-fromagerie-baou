<template>
  <b-row>
    <b-col lg="8">
      <!-- Méthodes de paiement -->
      <b-card class="mb-4">
        <h3 class="mb-4">{{ $t('cart.paymentMethod') }}</h3>
        
        <b-form-group>
          <b-form-radio-group
            v-model="localPayment.method"
            stacked
            @change="updateMethod"
          >
            <template #first>
              <b-form-radio value="card" class="p-3 border rounded mb-3">
                <div class="d-flex align-items-center">
                  <b-icon icon="credit-card" variant="primary" font-scale="1.5" class="me-3"></b-icon>
                  <div>
                    <div class="fw-bold">{{ $t('cart.creditCard') }}</div>
                    <div class="text-muted">Visa, Mastercard, American Express</div>
                  </div>
                </div>
              </b-form-radio>
              
              <b-form-radio value="paypal" class="p-3 border rounded mb-3">
                <div class="d-flex align-items-center">
                  <b-icon icon="paypal" variant="primary" font-scale="1.5" class="me-3"></b-icon>
                  <div>
                    <div class="fw-bold">PayPal</div>
                    <div class="text-muted">{{ $t('cart.payWithPaypal') }}</div>
                  </div>
                </div>
              </b-form-radio>
              
              <b-form-radio value="store" class="p-3 border rounded">
                <div class="d-flex align-items-center">
                  <b-icon icon="cash" variant="primary" font-scale="1.5" class="me-3"></b-icon>
                  <div>
                    <div class="fw-bold">{{ $t('cart.payAtStore') }}</div>
                    <div class="text-muted">{{ $t('cart.payAtStoreDescription') }}</div>
                  </div>
                </div>
              </b-form-radio>
            </template>
          </b-form-radio-group>
        </b-form-group>
      </b-card>
      
      <!-- Détails de la carte -->
      <b-card v-if="localPayment.method === 'card'" class="mb-4">
        <h3 class="mb-4">{{ $t('cart.cardDetails') }}</h3>
        
        <b-form>
          <b-form-group :label="$t('cart.cardholderName')">
            <b-form-input v-model="localPayment.cardholderName" required></b-form-input>
          </b-form-group>
          
          <b-form-group :label="$t('cart.cardNumber')">
            <b-form-input 
              v-model="localPayment.cardNumber" 
              placeholder="XXXX XXXX XXXX XXXX" 
              required
              maxlength="19"
              @input="formatCardNumber"
            ></b-form-input>
          </b-form-group>
          
          <b-row>
            <b-col md="6">
              <b-form-group :label="$t('cart.expiryDate')">
                <b-form-input 
                  v-model="localPayment.expiryDate" 
                  placeholder="MM/YY" 
                  required
                  maxlength="5"
                  @input="formatExpiryDate"
                ></b-form-input>
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group :label="$t('cart.cvv')">
                <b-form-input 
                  v-model="localPayment.cvv" 
                  placeholder="XXX" 
                  required
                  maxlength="4"
                  type="password"
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
        </b-form>
      </b-card>
      
      <!-- Informations PayPal -->
      <b-card v-if="localPayment.method === 'paypal'" class="mb-4">
        <div class="text-center p-3">
          <b-img src="/images/paypal-button.png" alt="PayPal" class="mb-3"></b-img>
          <p class="mb-0 text-muted">
            {{ $t('cart.paypalInfo') }}
          </p>
        </div>
      </b-card>
      
      <!-- Paiement en magasin -->
      <b-card v-if="localPayment.method === 'store'" class="mb-4">
        <div class="p-3">
          <h5>{{ $t('cart.payAtStoreInfo.title') }}</h5>
          <p>{{ $t('cart.payAtStoreInfo.text1') }}</p>
          <p class="mb-0">{{ $t('cart.payAtStoreInfo.text2') }}</p>
        </div>
      </b-card>
      
      <!-- Conditions générales -->
      <b-card class="mb-4">
        <b-form-checkbox v-model="localPayment.termsAccepted" required>
          {{ $t('cart.termsAgreement') }}
          <b-link to="/conditions-generales">{{ $t('cart.termsLink') }}</b-link>
        </b-form-checkbox>
      </b-card>
      
      <!-- Navigation -->
      <div class="d-flex justify-content-between">
        <b-button variant="outline-secondary" @click="$emit('back-to-delivery')">
          <b-icon icon="arrow-left" class="me-2"></b-icon>
          {{ $t('cart.backToDelivery') }}
        </b-button>
        <b-button variant="primary" @click="$emit('place-order')" :disabled="!isFormValid">
          {{ $t('cart.placeOrder') }}
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
      
      <!-- Livraison -->
      <b-card class="mb-4">
        <h5 class="mb-3">{{ $t('cart.deliveryInfo') }}</h5>
        
        <div class="mb-3">
          <div class="fw-bold">{{ $t('cart.method') }}:</div>
          <div v-if="delivery.method === 'pickup'">{{ $t('cart.pickup.title') }}</div>
          <div v-else-if="delivery.method === 'local'">{{ $t('cart.localDelivery.title') }}</div>
          <div v-else>{{ $t('cart.shipping.title') }}</div>
        </div>
        
        <div v-if="delivery.method === 'pickup'">
          <div class="fw-bold">{{ $t('cart.pickupDetails') }}:</div>
          <div>{{ formatDate(delivery.pickupDate) }} à {{ delivery.pickupTime }}</div>
          <div>15 Avenue des Alpes, 13124 Peypin</div>
        </div>
        
        <div v-else>
          <div class="fw-bold">{{ $t('cart.address') }}:</div>
          <div>{{ delivery.firstName }} {{ delivery.lastName }}</div>
          <div>{{ delivery.address }}</div>
          <div>{{ delivery.postalCode }} {{ delivery.city }}</div>
        </div>
      </b-card>
      
      <!-- Sécurité -->
      <b-card class="bg-light">
        <h5 class="mb-3">{{ $t('cart.securePayment') }}</h5>
        <div class="d-flex align-items-center mb-3">
          <b-icon icon="shield-lock" variant="success" font-scale="1.5" class="me-3"></b-icon>
          <div>{{ $t('cart.secureInfo') }}</div>
        </div>
        <div class="payment-icons d-flex justify-content-between">
          <b-img src="/images/payment/visa.png" alt="Visa" height="30"></b-img>
          <b-img src="/images/payment/mastercard.png" alt="Mastercard" height="30"></b-img>
          <b-img src="/images/payment/amex.png" alt="American Express" height="30"></b-img>
          <b-img src="/images/payment/paypal.png" alt="PayPal" height="30"></b-img>
        </div>
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
    delivery: {
      type: Object,
      required: true
    },
    value: {
      type: Object,
      required: true
    },
    paymentOptions: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      localPayment: { ...this.value }
    }
  },
  computed: {
    isFormValid() {
      if (this.localPayment.method === 'card') {
        return this.localPayment.cardholderName && 
               this.localPayment.cardNumber && 
               this.localPayment.expiryDate && 
               this.localPayment.cvv && 
               this.localPayment.termsAccepted;
      } else {
        return this.localPayment.termsAccepted;
      }
    }
  },
  methods: {
    formatPrice(price) {
      return new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR' }).format(price);
    },
    formatDate(dateString) {
      const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('fr-FR', options);
    },
    updateMethod() {
      this.$emit('input', this.localPayment);
    },
    formatCardNumber(e) {
      let value = e.target.value.replace(/\s+/g, '').replace(/[^0-9]/gi, '');
      let formattedValue = '';
      
      for (let i = 0; i < value.length; i++) {
        if (i > 0 && i % 4 === 0) {
          formattedValue += ' ';
        }
        formattedValue += value[i];
      }
      
      this.localPayment.cardNumber = formattedValue;
    },
    formatExpiryDate(e) {
      let value = e.target.value.replace(/\s+/g, '').replace(/[^0-9]/gi, '');
      
      if (value.length > 2) {
        value = value.substring(0, 2) + '/' + value.substring(2);
      }
      
      this.localPayment.expiryDate = value;
    }
  },
  watch: {
    localPayment: {
      handler(newVal) {
        this.$emit('input', newVal);
      },
      deep: true
    },
    value: {
      handler(newVal) {
        this.localPayment = { ...newVal };
      },
      deep: true
    }
  }
}
</script>

<style scoped>
.payment-icons img {
  filter: grayscale(0.5);
  transition: filter 0.3s ease;
}

.payment-icons img:hover {
  filter: grayscale(0);
}
</style>
