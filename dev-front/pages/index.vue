<template>
  <div>
    <div class="hero-banner" style="background-image: url('/images/hero-banner.jpg')">
      <div class="container text-center">
        <h1>{{ $t('home.hero.title') }}</h1>
        <p class="lead">{{ $t('home.hero.subtitle') }}</p>
        <b-button variant="primary" size="lg" to="/fromages" class="mt-3">
          {{ $t('home.featured.more') }}
        </b-button>
      </div>
    </div>

    <b-container class="py-5">
      <!-- Welcome Section -->
      <b-row class="mb-5 align-items-center">
        <b-col md="6">
          <h2>{{ $t('home.welcome.title') }}</h2>
          <p class="lead">{{ $t('home.welcome.description') }}</p>
          <p>
            Située à Peypin dans les Bouches-du-Rhône, la Fromagerie du Baou vous propose une sélection 
            de fromages du terroir français, élaborés selon les méthodes traditionnelles. 
            Nous privilégions les circuits courts et les producteurs locaux pour vous offrir 
            des produits de qualité exceptionnelle.
          </p>
          <b-button variant="outline-primary" to="/a-propos">
            {{ $t('common.readMore') }}
          </b-button>
        </b-col>
        <b-col md="6">
          <b-img src="/images/shop-interior.jpg" fluid rounded alt="Intérieur de la fromagerie"></b-img>
        </b-col>
      </b-row>

      <!-- Featured Products -->
      <h2 class="text-center mb-4">{{ $t('home.featured.title') }}</h2>
      <b-row>
        <b-col v-for="(cheese, index) in featuredCheeses" :key="index" md="4" class="mb-4">
          <b-card 
            :title="cheese.name" 
            :img-src="cheese.image" 
            img-alt="Cheese image" 
            img-top 
            class="h-100 cheese-card"
          >
            <b-card-text>
              {{ cheese.description }}
            </b-card-text>
            <div class="d-flex justify-content-between align-items-center">
              <span class="fw-bold">{{ cheese.price }} €/kg</span>
              <b-button variant="primary" size="sm" :to="`/fromages/${cheese.id}`">
                {{ $t('common.readMore') }}
              </b-button>
            </div>
          </b-card>
        </b-col>
      </b-row>
      <div class="text-center mt-4">
        <b-button variant="secondary" to="/fromages">
          {{ $t('home.featured.more') }}
        </b-button>
      </div>

      <!-- Plateaux Section -->
      <b-row class="my-5 bg-light p-4 rounded">
        <b-col md="6">
          <b-img src="/images/cheese-platter.jpg" fluid rounded alt="Plateau de fromages"></b-img>
        </b-col>
        <b-col md="6" class="d-flex flex-column justify-content-center">
          <h2>{{ $t('platters.title') }}</h2>
          <p>{{ $t('platters.description') }}</p>
          <p>
            Que ce soit pour un apéritif entre amis, un repas de famille ou un événement professionnel, 
            nos plateaux de fromages sauront ravir vos convives. Nous les composons avec soin selon vos goûts et votre budget.
          </p>
          <b-button variant="primary" to="/plateaux">
            {{ $t('platters.custom.button') }}
          </b-button>
        </b-col>
      </b-row>

      <!-- Newsletter -->
      <b-row class="my-5">
        <b-col lg="8" class="mx-auto">
          <b-card class="newsletter-card">
            <h3 class="text-center mb-3">{{ $t('home.newsletter.title') }}</h3>
            <p class="text-center">{{ $t('home.newsletter.description') }}</p>
            <b-form @submit.prevent="subscribeNewsletter" class="d-flex">
              <b-form-input
                v-model="newsletter.email"
                :placeholder="$t('home.newsletter.placeholder')"
                required
                type="email"
                class="me-2"
              ></b-form-input>
              <b-button type="submit" variant="primary">
                {{ $t('home.newsletter.button') }}
              </b-button>
            </b-form>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newsletter: {
        email: ''
      },
      featuredCheeses: [
        {
          id: 1,
          name: 'Comté AOP 18 mois',
          description: 'Un fromage au lait cru de vache, à pâte pressée cuite, affiné pendant 18 mois pour un goût intense et fruité.',
          price: 29.90,
          image: '/images/comte.jpg'
        },
        {
          id: 2,
          name: 'Roquefort AOP',
          description: 'Le roi des fromages bleus, au lait cru de brebis, avec une texture crémeuse et un goût puissant caractéristique.',
          price: 32.50,
          image: '/images/roquefort.jpg'
        },
        {
          id: 3,
          name: 'Tomme de Savoie',
          description: 'Fromage au lait cru de vache à pâte pressée non cuite, avec une croûte grise et une saveur douce et fruitée.',
          price: 24.80,
          image: '/images/tomme.jpg'
        }
      ]
    }
  },
  methods: {
    async subscribeNewsletter() {
      try {
        // Simuler une requête API
        await new Promise(resolve => setTimeout(resolve, 1000));
        this.$bvToast.toast('Merci pour votre inscription à notre newsletter !', {
          title: 'Inscription réussie',
          variant: 'success',
          solid: true
        });
        this.newsletter.email = '';
      } catch (error) {
        this.$bvToast.toast('Une erreur est survenue. Veuillez réessayer.', {
          title: 'Erreur',
          variant: 'danger',
          solid: true
        });
      }
    }
  },
  head() {
    return {
      title: 'Fromagerie du Baou - Fromages artisanaux à Peypin'
    }
  }
}
</script>
