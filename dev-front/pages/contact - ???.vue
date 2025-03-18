<template>
  <div>
    <div class="page-header bg-light py-5">
      <b-container>
        <h1>{{ $t('contact.title') }}</h1>
      </b-container>
    </div>

    <b-container class="py-5">
      <b-row>
        <b-col lg="6" class="mb-5 mb-lg-0">
          <h2>Nous contacter</h2>
          <p class="lead">
            Vous avez une question sur nos produits, nos services ou vous souhaitez passer une commande ?
            N'hésitez pas à nous contacter via le formulaire ci-contre ou directement par téléphone.
          </p>

          <div class="contact-info mt-5">
            <div class="d-flex mb-4">
              <b-icon icon="geo-alt" variant="primary" font-scale="2" class="me-3"></b-icon>
              <div>
                <h5>{{ $t('contact.info.address') }}</h5>
                <p class="mb-0">
                  Fromagerie du Baou<br>
                  ZA Le Terme D908<br>
                  13124 Peypin<br>
                  Bouches-du-Rhône
                </p>
              </div>
            </div>

            <div class="d-flex mb-4">
              <b-icon icon="telephone" variant="primary" font-scale="2" class="me-3"></b-icon>
              <div>
                <h5>{{ $t('contact.info.phone') }}</h5>
                <p class="mb-0">04 93 08 59 25</p>
              </div>
            </div>

            <div class="d-flex mb-4">
              <b-icon icon="envelope" variant="primary" font-scale="2" class="me-3"></b-icon>
              <div>
                <h5>{{ $t('contact.info.email') }}</h5>
                <p class="mb-0">fromageriedubaou@gmail.com</p>
              </div>
            </div>

            <div class="d-flex mb-4">
              <b-icon icon="clock" variant="primary" font-scale="2" class="me-3"></b-icon>
              <div>
                <h5>{{ $t('contact.info.hours') }}</h5>
                <p class="mb-0">
                  Du mardi au samedi<br>
                  9h - 13h / 15h - 19h<br>
                  Dimanche<br>
                  9h - 13h
                </p>
              </div>
            </div>
          </div>

          <div class="social-links mt-4">
            <h5>Suivez-nous</h5>
            <div class="d-flex">
              <a href="https://www.facebook.com/p/Fromagerie-du-Baou-61565581314658/" target="_blank" class="me-3">
                <b-icon icon="facebook" font-scale="1.5"></b-icon>
              </a>
              <a href="https://www.instagram.com/fromageriedubaou/" target="_blank">
                <b-icon icon="instagram" font-scale="1.5"></b-icon>
              </a>
            </div>
          </div>
        </b-col>

        <b-col lg="6">
          <b-card title="Formulaire de contact">
            <b-form @submit.prevent="submitContactForm">
              <b-form-group label="Nom *">
                <b-form-input 
                  v-model="contactForm.name" 
                  required
                ></b-form-input>
              </b-form-group>
              
              <b-form-group label="Email *">
                <b-form-input 
                  v-model="contactForm.email" 
                  type="email"
                  required
                ></b-form-input>
              </b-form-group>
              
              <b-form-group label="Sujet *">
                <b-form-input 
                  v-model="contactForm.subject" 
                  required
                ></b-form-input>
              </b-form-group>
              
              <b-form-group label="Message *">
                <b-form-textarea 
                  v-model="contactForm.message" 
                  rows="6"
                  required
                ></b-form-textarea>
              </b-form-group>
              
              <div class="d-grid gap-2">
                <b-button type="submit" variant="primary" :disabled="isSubmitting">
                  <b-spinner small v-if="isSubmitting" class="me-2"></b-spinner>
                  {{ $t('contact.form.button') }}
                </b-button>
              </div>
            </b-form>
          </b-card>
        </b-col>
      </b-row>

      <!-- Google Maps -->
      <div class="mt-5">
        <h3 class="mb-3">Nous trouver</h3>
        <div class="map-container">
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2900.5693167852!2d5.5801!3d43.3845!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNDPCsDIzJzA0LjIiTiA1wrAzNCc0OC40IkU!5e0!3m2!1sfr!2sfr!4v1616000000000!5m2!1sfr!2sfr" 
            width="100%" 
            height="450" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy"
          ></iframe>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isSubmitting: false,
      contactForm: {
        name: '',
        email: '',
        subject: '',
        message: ''
      }
    }
  },
  methods: {
    async submitContactForm() {
      try {
        this.isSubmitting = true;
        // Simuler une requête API
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        this.$bvToast.toast('Votre message a été envoyé avec succès. Nous vous répondrons dans les plus brefs délais.', {
          title: 'Message envoyé',
          variant: 'success',
          solid: true
        });
        
        // Réinitialiser le formulaire
        this.contactForm = {
          name: '',
          email: '',
          subject: '',
          message: ''
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
    }
  },
  head() {
    return {
      title: 'Contact - Fromagerie du Baou'
    }
  }
}
</script>

<style scoped>
.map-container {
  position: relative;
  width: 100%;
  height: 450px;
  overflow: hidden;
  border-radius: 8px;
}
</style>
