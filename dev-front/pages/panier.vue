<template>
  <div>
    <div class="page-header bg-light py-5">
      <b-container>
        <h1>{{ $t('cart.title') }}</h1>
      </b-container>
    </div>

    <b-container class="py-5">
      <div v-if="cart.items.length > 0">
        <!-- Étapes du panier -->
        <b-row class="mb-5">
          <b-col>
            <b-nav tabs class="checkout-steps">
              <b-nav-item :active="step === 1" @click="step = 1">
                <span class="step-number">1</span>
                {{ $t('cart.steps.cart') }}
              </b-nav-item>
              <b-nav-item :active="step === 2" :disabled="!canProceedToDelivery" @click="goToStep(2)">
                <span class="step-number">2</span>
                {{ $t('cart.steps.delivery') }}
              </b-nav-item>
              <b-nav-item :active="step === 3" :disabled="!canProceedToPayment" @click="goToStep(3)">
                <span class="step-number">3</span>
                {{ $t('cart.steps.payment') }}
              </b-nav-item>
              <b-nav-item :active="step === 4" disabled>
                <span class="step-number">4</span>
                {{ $t('cart.steps.confirmation') }}
              </b-nav-item>
            </b-nav>
          </b-col>
        </b-row>

        <!-- Étape 1: Panier -->
        <CartItems 
          v-if="step === 1" 
          :cart="cart" 
          @update-cart="updateCart" 
          @remove-item="removeItem"
          @increase-quantity="increaseQuantity"
          @decrease-quantity="decreaseQuantity"
          @apply-promo-code="applyPromoCode"
          @proceed-to-delivery="goToStep(2)"
        />

        <!-- Étape 2: Livraison -->
        <DeliveryInfo 
          v-if="step === 2" 
          :cart="cart"
          v-model="delivery"
          :min-pickup-date="minPickupDate"
          :pickup-time-options="pickupTimeOptions"
          @back-to-cart="step = 1"
          @proceed-to-payment="goToStep(3)"
        />

        <!-- Étape 3: Paiement -->
        <PaymentInfo 
          v-if="step === 3" 
          :cart="cart"
          :delivery="delivery"
          v-model="payment"
          :payment-options="paymentOptions"
          @back-to-delivery="step = 2"
          @place-order="placeOrder"
        />

        <!-- Étape 4: Confirmation -->
        <OrderConfirmation 
          v-if="step === 4" 
          :order-number="orderNumber"
          :email="delivery.email"
        />
      </div>
      
      <!-- Panier vide -->
      <div v-else class="text-center py-5">
        <b-icon icon="cart" font-scale="5" class="mb-4 text-muted"></b-icon>
        <h3 class="mb-4">{{ $t('cart.emptyCart') }}</h3>
        <p class="mb-4">{{ $t('cart.emptyCartMessage') }}</p>
        <b-button variant="primary" to="/produits">
          {{ $t('cart.startShopping') }}
        </b-button>
      </div>
    </b-container>
  </div>
</template>

<script>
import CartItems from '~/components/cart/CartItems.vue'
import DeliveryInfo from '~/components/cart/DeliveryInfo.vue'
import PaymentInfo from '~/components/cart/PaymentInfo.vue'
import OrderConfirmation from '~/components/cart/OrderConfirmation.vue'

export default {
  components: {
    CartItems,
    DeliveryInfo,
    PaymentInfo,
    OrderConfirmation
  },
  data() {
    return {
      step: 1,
      cart: {
        items: [
          {
            id: 1,
            name: 'Comté AOP 18 mois',
            price: 39.90,
            weight: 250,
            quantity: 1,
            image: '/images/products/comte.jpg'
          },
          {
            id: 2,
            name: 'Brie de Meaux AOP',
            price: 24.90,
            weight: 300,
            quantity: 1,
            image: '/images/products/brie.jpg'
          },
          {
            id: 3,
            name: 'Roquefort AOP Carles',
            price: 29.90,
            weight: 200,
            quantity: 1,
            image: '/images/products/roquefort.jpg'
          }
        ],
        subtotal: 94.70,
        discount: 0,
        shippingCost: 0,
        total: 94.70
      },
      promoCode: '',
      delivery: {
        method: 'pickup',
        firstName: '',
        lastName: '',
        address: '',
        postalCode: '',
        city: '',
        phone: '',
        email: '',
        instructions: '',
        pickupDate: '',
        pickupTime: ''
      },
      payment: {
        method: 'card',
        cardholderName: '',
        cardNumber: '',
        expiryDate: '',
        cvv: '',
        termsAccepted: false
      },
      orderNumber: 'FDB-' + Math.floor(100000 + Math.random() * 900000)
    }
  },
  computed: {
    canProceedToDelivery() {
      return this.cart.items.length > 0;
    },
    canProceedToPayment() {
      if (this.delivery.method === 'pickup') {
        return this.delivery.firstName && 
               this.delivery.lastName && 
               this.delivery.phone && 
               this.delivery.email &&
               this.delivery.pickupDate &&
               this.delivery.pickupTime;
      } else {
        return this.delivery.firstName && 
               this.delivery.lastName && 
               this.delivery.address && 
               this.delivery.postalCode && 
               this.delivery.city && 
               this.delivery.phone && 
               this.delivery.email;
      }
    },
    canPlaceOrder() {
      if (this.payment.method === 'card') {
        return this.payment.cardholderName && 
               this.payment.cardNumber && 
               this.payment.expiryDate && 
               this.payment.cvv && 
               this.payment.termsAccepted;
      } else {
        return this.payment.termsAccepted;
      }
    },
    minPickupDate() {
      const today = new Date();
      const tomorrow = new Date(today);
      tomorrow.setDate(tomorrow.getDate() + 1);
      return tomorrow.toISOString().split('T')[0];
    },
    pickupTimeOptions() {
      return [
        { value: null, text: 'Sélectionnez une heure' },
        { value: '10:00', text: '10:00' },
        { value: '11:00', text: '11:00' },
        { value: '12:00', text: '12:00' },
        { value: '14:00', text: '14:00' },
        { value: '15:00', text: '15:00' },
        { value: '16:00', text: '16:00' },
        { value: '17:00', text: '17:00' },
        { value: '18:00', text: '18:00' }
      ];
    },
    paymentOptions() {
      return [
        { value: 'card', text: this.$t('cart.creditCard') },
        { value: 'paypal', text: 'PayPal' },
        { value: 'store', text: this.$t('cart.payAtStore') }
      ];
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
    updateCart() {
      // Recalculer le sous-total
      this.cart.subtotal = this.cart.items.reduce((total, item) => {
        return total + (item.price * item.quantity);
      }, 0);
      
      // Mettre à jour les frais de livraison
      this.updateShippingCost();
      
      // Calculer le total
      this.cart.total = this.cart.subtotal - this.cart.discount + this.cart.shippingCost;
    },
    updateShippingCost() {
      if (this.delivery.method === 'pickup') {
        this.cart.shippingCost = 0;
      } else if (this.delivery.method === 'local') {
        this.cart.shippingCost = this.cart.subtotal >= 50 ? 0 : 5;
      } else if (this.delivery.method === 'shipping') {
        this.cart.shippingCost = this.cart.subtotal >= 80 ? 0 : 12;
      }
    },
    increaseQuantity(index) {
      this.cart.items[index].quantity++;
      this.updateCart();
    },
    decreaseQuantity(index) {
      if (this.cart.items[index].quantity > 1) {
        this.cart.items[index].quantity--;
        this.updateCart();
      }
    },
    removeItem(index) {
      this.cart.items.splice(index, 1);
      this.updateCart();
    },
    applyPromoCode() {
      if (this.promoCode.toUpperCase() === 'BIENVENUE') {
        this.cart.discount = this.cart.subtotal * 0.1; // 10% de réduction
        this.$bvToast.toast('Code promo appliqué avec succès !', {
          title: 'Réduction',
          variant: 'success',
          solid: true
        });
      } else {
        this.cart.discount = 0;
        this.$bvToast.toast('Code promo invalide.', {
          title: 'Erreur',
          variant: 'danger',
          solid: true
        });
      }
      
      // Recalculer le total
      this.cart.total = this.cart.subtotal - this.cart.discount + this.cart.shippingCost;
      
      // Réinitialiser le champ
      this.promoCode = '';
    },
    goToStep(step) {
      if (step === 2 && this.canProceedToDelivery) {
        this.step = 2;
      } else if (step === 3 && this.canProceedToPayment) {
        this.updateShippingCost();
        this.cart.total = this.cart.subtotal - this.cart.discount + this.cart.shippingCost;
        this.step = 3;
      }
    },
    async placeOrder() {
      if (!this.canPlaceOrder) return;
      
      try {
        // Simuler une requête API
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // Générer un numéro de commande
        this.orderNumber = 'FDB-' + Math.floor(100000 + Math.random() * 900000);
        
        // Passer à l'étape de confirmation
        this.step = 4;
        
        // Faire défiler vers le haut
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } catch (error) {
        this.$bvToast.toast('Une erreur est survenue lors de la validation de votre commande. Veuillez réessayer.', {
          title: 'Erreur',
          variant: 'danger',
          solid: true
        });
      }
    }
  },
  head() {
    return {
      title: 'Panier - Fromagerie du Baou'
    }
  }
}
</script>

<style scoped>
.checkout-steps {
  border-bottom: none;
}

.checkout-steps .nav-link {
  border: none;
  position: relative;
  padding: 1rem 0.5rem;
}

.checkout-steps .nav-link.active {
  color: #007bff;
  font-weight: bold;
}

.step-number {
  display: inline-block;
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  border-radius: 50%;
  background-color: #e9ecef;
  margin-right: 0.5rem;
}

.checkout-steps .nav-link.active .step-number {
  background-color: #007bff;
  color: white;
}

.confirmation-icon {
  animation: scale-in 0.5s ease-out;
}

@keyframes scale-in {
  0% {
    transform: scale(0);
    opacity: 0;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}
</style>
