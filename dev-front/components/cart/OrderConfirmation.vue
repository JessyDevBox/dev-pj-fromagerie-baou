<template>
  <b-row>
    <b-col lg="8" class="mx-auto text-center">
      <div class="confirmation-icon mb-4">
        <b-icon icon="check-circle" variant="success" font-scale="5"></b-icon>
      </div>
      
      <h2 class="mb-4">{{ $t('cart.orderConfirmed') }}</h2>
      
      <p class="mb-4">
        {{ $t('cart.orderConfirmationMessage', { orderNumber }) }}
      </p>
      
      <p class="mb-5">
        {{ $t('cart.emailSent', { email }) }}
      </p>
      
      <div class="order-details p-4 mb-5 bg-light rounded text-start">
        <h4 class="mb-3">{{ $t('cart.orderDetails') }}</h4>
        
        <div class="d-flex justify-content-between mb-2">
          <span>{{ $t('cart.orderNumber') }}:</span>
          <span class="fw-bold">{{ orderNumber }}</span>
        </div>
        
        <div class="d-flex justify-content-between mb-2">
          <span>{{ $t('cart.orderDate') }}:</span>
          <span>{{ formatDate(new Date()) }}</span>
        </div>
        
        <div class="d-flex justify-content-between mb-2">
          <span>{{ $t('cart.paymentMethod') }}:</span>
          <span>{{ paymentMethodText }}</span>
        </div>
        
        <div class="d-flex justify-content-between">
          <span>{{ $t('cart.deliveryMethod') }}:</span>
          <span>{{ deliveryMethodText }}</span>
        </div>
      </div>
      
      <div class="next-steps mb-5">
        <h4 class="mb-3">{{ $t('cart.whatNext') }}</h4>
        <p>{{ $t('cart.nextStepsInfo') }}</p>
        
        <div class="d-flex justify-content-center flex-wrap">
          <b-card class="m-2 text-start" style="width: 18rem;">
            <div class="d-flex align-items-center mb-3">
              <b-icon icon="envelope" variant="primary" font-scale="2" class="me-3"></b-icon>
              <h5 class="mb-0">{{ $t('cart.checkEmail') }}</h5>
            </div>
            <p class="mb-0">{{ $t('cart.emailInfo') }}</p>
          </b-card>
          
          <b-card class="m-2 text-start" style="width: 18rem;">
            <div class="d-flex align-items-center mb-3">
              <b-icon icon="person" variant="primary" font-scale="2" class="me-3"></b-icon>
              <h5 class="mb-0">{{ $t('cart.trackOrder') }}</h5>
            </div>
            <p class="mb-0">{{ $t('cart.trackOrderInfo') }}</p>
          </b-card>
        </div>
      </div>
      
      <div class="recommendations mb-5">
        <h4 class="mb-3">{{ $t('cart.youMightLike') }}</h4>
        
        <b-row>
          <b-col md="4" v-for="(product, index) in recommendedProducts" :key="index" class="mb-4">
            <b-card class="h-100 product-card">
              <b-img :src="product.image" fluid alt="Product image" class="mb-3 product-image"></b-img>
              <h5>{{ product.name }}</h5>
              <div class="text-muted mb-2">{{ product.weight }}g</div>
              <div class="fw-bold mb-3">{{ formatPrice(product.price) }}</div>
              <b-button variant="outline-primary" size="sm" :to="`/produits/${product.slug}`">
                {{ $t('cart.viewProduct') }}
              </b-button>
            </b-card>
          </b-col>
        </b-row>
      </div>
      
      <div class="d-flex justify-content-center">
        <b-button variant="primary" to="/" class="me-3">
          {{ $t('cart.backToHome') }}
        </b-button>
        <b-button variant="outline-primary" to="/compte/commandes">
          {{ $t('cart.viewOrders') }}
        </b-button>
      </div>
    </b-col>
  </b-row>
</template>

<script>
export default {
  props: {
    orderNumber: {
      type: String,
      required: true
    },
    email: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      recommendedProducts: [
        {
          id: 4,
          name: 'Tomme de Savoie',
          price: 19.90,
          weight: 250,
          image: '/images/products/tomme.jpg',
          slug: 'tomme-de-savoie'
        },
        {
          id: 5,
          name: 'Morbier AOP',
          price: 22.90,
          weight: 250,
          image: '/images/products/morbier.jpg',
          slug: 'morbier-aop'
        },
        {
          id: 6,
          name: 'Reblochon de Savoie AOP',
          price: 24.90,
          weight: 450,
          image: '/images/products/reblochon.jpg',
          slug: 'reblochon-de-savoie-aop'
        }
      ],
      paymentMethodText: this.$t('cart.creditCard'),
      deliveryMethodText: this.$t('cart.pickup.title')
    }
  },
  methods: {
    formatPrice(price) {
      return new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR' }).format(price);
    },
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return date.toLocaleDateString('fr-FR', options);
    }
  }
}
</script>

<style scoped>
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

.order-details {
  border-left: 4px solid #28a745;
}

.product-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.product-image {
  height: 150px;
  object-fit: contain;
}
</style>
