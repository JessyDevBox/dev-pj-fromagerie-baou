<template>
  <div>
    <div class="page-header bg-light py-5">
      <b-container>
        <h1>{{ $t('platters.title') }}</h1>
        <p class="lead">{{ $t('platters.description') }}</p>
      </b-container>
    </div>

    <b-container class="py-5">
      <!-- Plateaux prédéfinis -->
      <h2 class="mb-4">Nos plateaux prédéfinis</h2>
      <b-row>
        <b-col v-for="platter in platters" :key="platter.id" md="4" class="mb-4">
          <b-card 
            :title="platter.name" 
            :img-src="platter.image" 
            img-alt="Platter image" 
            img-top 
            class="h-100 cheese-card"
          >
            <b-card-text>
              {{ platter.description }}
            </b-card-text>
            <div class="d-flex justify-content-between align-items-center mt-auto">
              <span class="fw-bold">{{ platter.price.toFixed(2) }} €</span>
              <b-button variant="primary" size="sm" :to="`/plateaux/${platter.id}`">
                {{ $t('common.readMore') }}
              </b-button>
            </div>
          </b-card>
        </b-col>
      </b-row>

      <!-- Plateaux sur mesure -->
      <div class="custom-platter-section my-5 p-5 bg-light rounded">
        <b-row>
          <b-col lg="6" class="mb-4 mb-lg-0">
            <h2>{{ $t('platters.custom.title') }}</h2>
            <p>{{ $t('platters.custom.description') }}</p>
            <p>
              Que ce soit pour un apéritif entre amis, un repas de famille ou un événement professionnel, 
              nous composons des plateaux personnalisés selon vos goûts, vos préférences et votre budget.
            </p>
            <p>
              Complétez le formulaire ci-contre pour nous indiquer vos besoins, et nous vous 
              contacterons rapidement pour vous proposer une sélection adaptée.
            </p>
          </b-col>
          <b-col lg="6">
            <b-card title="Demande de devis pour plateau personnalisé">
              <b-form @submit.prevent="submitPlatterRequest">
                <b-form-group label="Nombre de personnes *">
                  <b-form-input 
                    v-model="platterRequest.guestsCount" 
                    type="number" 
                    min="1" 
                    required
                  ></b-form-input>
                </b-form-group>
                
                <b-form-group label="Budget approximatif par personne">
                  <b-form-input 
                    v-model="platterRequest.budget" 
                    type="number" 
                    min="0" 
                    step="0.5"
                  ></b-form-input>
                </b-form-group>
                
                <b-form-group label="Description de votre demande *">
                  <b-form-textarea 
                    v-model="platterRequest.description" 
                    placeholder="Précisez vos préférences, allergies, occasion..."
                    rows="4"
                    required
                  ></b-form-textarea>
                </b-form-group>
                
                <b-form-group label="Demandes particulières">
                  <b-form-textarea 
                    v-model="platterRequest.specialRequests" 
                    placeholder="Autres informations importantes..."
                    rows="2"
                  ></b-form-textarea>
                </b-form-group>
                
                <div class="d-grid gap-2">
                  <b-button type="submit" variant="primary" :disabled="isSubmitting">
                    <b-spinner small v-if="isSubmitting" class="me-2"></b-spinner>
                    {{ $t('platters.custom.button') }}
                  </b-button>
                </div>
              </b-form>
            </b-card>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isSubmitting: false,
      platterRequest: {
        guestsCount: 1,
        budget: null,
        description: '',
        specialRequests: ''
      },
      platters: [
        {
          id: 1,
          name: 'Plateau Découverte',
          description: 'Sélection de 4 fromages variés (environ 400g) pour 4-6 personnes. Idéal pour une initiation aux fromages français.',
          price: 25.90,
          image: '/images/platter-decouverte.jpg'
        },
        {
          id: 2,
          name: 'Plateau Tradition',
          description: 'Assortiment de 6 fromages traditionnels (environ 600g) pour 6-8 personnes. Les grands classiques français.',
          price: 39.90,
          image: '/images/platter-tradition.jpg'
        },
        {
          id: 3,
          name: 'Plateau Prestige',
          description: 'Sélection de 8 fromages d\'exception (environ 800g) pour 8-10 personnes. Le meilleur de nos fromages AOP.',
          price: 59.90,
          image: '/images/platter-prestige.jpg'
        }
      ]
    }
  },
  methods: {
    async submitPlatterRequest() {
      if (this.$auth.loggedIn) {
        try {
          this.isSubmitting = true;
          // Simuler une requête API
          await new Promise(resolve => setTimeout(resolve, 1000));
          
          this.$bvToast.toast('Votre demande a été envoyée avec succès. Nous vous contacterons prochainement.', {
            title: 'Demande envoyée',
            variant: 'success',
            solid: true
          });
          
          // Réinitialiser le formulaire
          this.platterRequest = {
            guestsCount: 1,
            budget: null,
            description: '',
            specialRequests: ''
          };
        } catch (error) {
          this.$bvToast.toast('Une erreur est survenue. Veuillez réessayer.', {
            title: 'Erreur',
            variant: 'danger',
            solid: true
          });
        } finally {
          this.isSubmitting = false;
        }
      } else {
        this.$bvModal.msgBoxConfirm('Vous devez être connecté pour envoyer une demande de devis. Souhaitez-vous vous connecter maintenant ?', {
          title: 'Connexion requise',
          okVariant: 'primary',
          okTitle: 'Se connecter',
          cancelTitle: 'Annuler',
          centered: true
        })
        .then(value => {
          if (value) {
            this.$router.push('/connexion');
          }
        });
      }
    }
  },
  head() {
    return {
      title: 'Nos Plateaux - Fromagerie du Baou'
    }
  }
}
</script>
