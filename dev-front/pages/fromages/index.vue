<template>
  <div>
    <div class="page-header bg-light py-5">
      <b-container>
        <h1>{{ $t('cheeses.title') }}</h1>
        <p class="lead">{{ $t('cheeses.description') }}</p>
      </b-container>
    </div>

    <b-container class="py-5">
      <!-- Filtres -->
      <b-row class="mb-4">
        <b-col md="3">
          <b-form-group :label="$t('cheeses.origin')">
            <b-form-select v-model="filters.origin" :options="originOptions"></b-form-select>
          </b-form-group>
        </b-col>
        <b-col md="3">
          <b-form-group label="Type de lait">
            <b-form-select v-model="filters.milkType" :options="milkTypeOptions"></b-form-select>
          </b-form-group>
        </b-col>
        <b-col md="4">
          <b-form-group label="Prix">
            <b-form-input v-model="filters.maxPrice" type="range" min="0" max="50" step="5"></b-form-input>
            <div class="d-flex justify-content-between">
              <span>0€</span>
              <span>{{ filters.maxPrice }}€ et +</span>
            </div>
          </b-form-group>
        </b-col>
        <b-col md="2" class="d-flex align-items-end">
          <b-button variant="outline-secondary" @click="resetFilters" block>Réinitialiser</b-button>
        </b-col>
      </b-row>

      <!-- Liste des fromages -->
      <b-row>
        <b-col v-for="cheese in filteredCheeses" :key="cheese.id" md="4" class="mb-4">
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
            <div class="mt-auto">
              <div class="mb-2">
                <small class="text-muted">
                  {{ $t('cheeses.origin') }}: {{ cheese.origin }}
                </small>
                <br>
                <small class="text-muted">
                  {{ $t('cheeses.milk') }}: {{ cheese.milkType }}
                </small>
              </div>
              <div class="d-flex justify-content-between align-items-center">
                <span class="fw-bold">{{ cheese.price.toFixed(2) }} €/kg</span>
                <b-button variant="primary" size="sm" :to="`/fromages/${cheese.id}`">
                  {{ $t('common.readMore') }}
                </b-button>
              </div>
            </div>
          </b-card>
        </b-col>
      </b-row>

      <!-- Message si aucun résultat -->
      <b-alert v-if="filteredCheeses.length === 0" show variant="info" class="text-center">
        Aucun fromage ne correspond à vos critères. Veuillez modifier vos filtres.
      </b-alert>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      filters: {
        origin: null,
        milkType: null,
        maxPrice: 50
      },
      cheeses: [
        {
          id: 1,
          name: 'Comté AOP 18 mois',
          description: 'Un fromage au lait cru de vache, à pâte pressée cuite, affiné pendant 18 mois pour un goût intense et fruité.',
          price: 29.90,
          origin: 'Franche-Comté',
          milkType: 'Vache',
          image: '/images/comte.jpg'
        },
        {
          id: 2,
          name: 'Roquefort AOP',
          description: 'Le roi des fromages bleus, au lait cru de brebis, avec une texture crémeuse et un goût puissant caractéristique.',
          price: 32.50,
          origin: 'Aveyron',
          milkType: 'Brebis',
          image: '/images/roquefort.jpg'
        },
        {
          id: 3,
          name: 'Tomme de Savoie',
          description: 'Fromage au lait cru de vache à pâte pressée non cuite, avec une croûte grise et une saveur douce et fruitée.',
          price: 24.80,
          origin: 'Savoie',
          milkType: 'Vache',
          image: '/images/tomme.jpg'
        },
        {
          id: 4,
          name: 'Crottin de Chavignol AOP',
          description: 'Petit fromage de chèvre au lait cru, à la texture crémeuse et au goût de noisette qui s\'affirme avec l\'affinage.',
          price: 4.50,
          origin: 'Berry',
          milkType: 'Chèvre',
          image: '/images/crottin.jpg'
        },
        {
          id: 5,
          name: 'Camembert de Normandie AOP',
          description: 'Fromage emblématique à croûte fleurie et à pâte molle, au lait cru de vache, avec un goût typé et une texture fondante.',
          price: 18.90,
          origin: 'Normandie',
          milkType: 'Vache',
          image: '/images/camembert.jpg'
        },
        {
          id: 6,
          name: 'Ossau-Iraty AOP',
          description: 'Fromage basque au lait de brebis, à pâte pressée non cuite, avec des arômes de noisette et une texture fondante.',
          price: 34.80,
          origin: 'Pays Basque',
          milkType: 'Brebis',
          image: '/images/ossau-iraty.jpg'
        }
      ]
    }
  },
  computed: {
    originOptions() {
      const origins = [...new Set(this.cheeses.map(cheese => cheese.origin))];
      return [
        { value: null, text: 'Toutes les origines' },
        ...origins.map(origin => ({ value: origin, text: origin }))
      ];
    },
    milkTypeOptions() {
      const milkTypes = [...new Set(this.cheeses.map(cheese => cheese.milkType))];
      return [
        { value: null, text: 'Tous les types de lait' },
        ...milkTypes.map(type => ({ value: type, text: type }))
      ];
    },
    filteredCheeses() {
      return this.cheeses.filter(cheese => {
        // Filtre par origine
        if (this.filters.origin && cheese.origin !== this.filters.origin) {
          return false;
        }
        
        // Filtre par type de lait
        if (this.filters.milkType && cheese.milkType !== this.filters.milkType) {
          return false;
        }
        
        // Filtre par prix maximum
        if (cheese.price > this.filters.maxPrice) {
          return false;
        }
        
        return true;
      });
    }
  },
  methods: {
    resetFilters() {
      this.filters = {
        origin: null,
        milkType: null,
        maxPrice: 50
      };
    }
  },
  head() {
    return {
      title: 'Nos Fromages - Fromagerie du Baou'
    }
  }
}
</script>
