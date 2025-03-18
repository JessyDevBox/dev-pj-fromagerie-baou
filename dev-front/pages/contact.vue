<template>
  <div>
    <div class="page-header bg-light py-5">
      <b-container>
        <h1>{{ $t('contact.title') }}</h1>
        <p class="lead">{{ $t('contact.description') }}</p>
      </b-container>
    </div>

    <b-container class="py-5">
      <b-row>
        <b-col lg="6" class="mb-4 mb-lg-0">
          <!-- Formulaire de contact -->
          <b-card>
            <h3 class="mb-4">{{ $t('contact.form.title') }}</h3>
            
            <b-alert v-model="showSuccess" variant="success" dismissible>
              {{ $t('contact.form.success') }}
            </b-alert>
            
            <b-form @submit.prevent="submitForm">
              <b-row>
                <b-col md="6">
                  <b-form-group :label="$t('contact.form.firstName')">
                    <b-form-input
                      v-model="form.firstName"
                      required
                      :placeholder="$t('contact.form.firstNamePlaceholder')"
                    ></b-form-input>
                  </b-form-group>
                </b-col>
                <b-col md="6">
                  <b-form-group :label="$t('contact.form.lastName')">
                    <b-form-input
                      v-model="form.lastName"
                      required
                      :placeholder="$t('contact.form.lastNamePlaceholder')"
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
              
              <b-form-group :label="$t('contact.form.email')">
                <b-form-input
                  v-model="form.email"
                  type="email"
                  required
                  :placeholder="$t('contact.form.emailPlaceholder')"
                ></b-form-input>
              </b-form-group>
              
              <b-form-group :label="$t('contact.form.phone')">
                <b-form-input
                  v-model="form.phone"
                  :placeholder="$t('contact.form.phonePlaceholder')"
                ></b-form-input>
              </b-form-group>
              
              <b-form-group :label="$t('contact.form.subject')">
                <b-form-select
                  v-model="form.subject"
                  :options="subjectOptions"
                  required
                ></b-form-select>
              </b-form-group>
              
              <b-form-group :label="$t('contact.form.message')">
                <b-form-textarea
                  v-model="form.message"
                  rows="5"
                  required
                  :placeholder="$t('contact.form.messagePlaceholder')"
                ></b-form-textarea>
              </b-form-group>
              
              <div class="d-grid gap-2">
                <b-button type="submit" variant="primary" :disabled="isSubmitting">
                  <b-spinner small v-if="isSubmitting" class="me-2"></b-spinner>
                  {{ $t('contact.form.submit') }}
                </b-button>
              </div>
            </b-form>
          </b-card>
        </b-col>
        
        <b-col lg="6">
          <!-- Informations de contact -->
          <b-card class="mb-4">
            <h3 class="mb-4">{{ $t('contact.info.title') }}</h3>
            
            <div class="contact-info">
              <div class="d-flex mb-3">
                <b-icon icon="geo-alt" variant="primary" font-scale="1.5" class="me-3 mt-1"></b-icon>
                <div>
                  <h5>{{ $t('contact.info.address') }}</h5>
                  <p class="mb-0">
                    15 Avenue des Alpes<br>
                    13124 Peypin<br>
                    France
                  </p>
                </div>
              </div>
              
              <div class="d-flex mb-3">
                <b-icon icon="telephone" variant="primary" font-scale="1.5" class="me-3 mt-1"></b-icon>
                <div>
                  <h5>{{ $t('contact.info.phone') }}</h5>
                  <p class="mb-0">
                    <a href="tel:+33442046789">+33 4 42 04 67 89</a>
                  </p>
                </div>
              </div>
              
              <div class="d-flex mb-3">
                <b-icon icon="envelope" variant="primary" font-scale="1.5" class="me-3 mt-1"></b-icon>
                <div>
                  <h5>{{ $t('contact.info.email') }}</h5>
                  <p class="mb-0">
                    <a href="mailto:contact@fromageriedubaou.fr">contact@fromageriedubaou.fr</a>
                  </p>
                </div>
              </div>
              
              <div class="d-flex">
                <b-icon icon="clock" variant="primary" font-scale="1.5" class="me-3 mt-1"></b-icon>
                <div>
                  <h5>{{ $t('contact.info.hours') }}</h5>
                  <p class="mb-0">
                    {{ $t('contact.info.monday') }}: Fermé<br>
                    {{ $t('contact.info.tuesday') }} - {{ $t('contact.info.friday') }}: 9h00 - 19h00<br>
                    {{ $t('contact.info.saturday') }}: 8h30 - 19h30<br>
                    {{ $t('contact.info.sunday') }}: 9h00 - 12h30
                  </p>
                </div>
              </div>
            </div>
          </b-card>
          
          <!-- Carte -->
          <b-card>
            <h3 class="mb-4">{{ $t('contact.map.title') }}</h3>
            <div class="map-container">
              <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2903.1234567890123!2d5.123456789012345!3d43.12345678901234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNDPCsDA3JzI0LjQiTiA1wrAwNycyNC40IkU!5e0!3m2!1sfr!2sfr!4v1234567890123!5m2!1sfr!2sfr"
                width="100%"
                height="300"
                style="border:0;"
                allowfullscreen=""
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade"
              ></iframe>
            </div>
            <div class="mt-3">
              <b-button variant="outline-primary" href="https://goo.gl/maps/example" target="_blank">
                <b-icon icon="map" class="me-2"></b-icon>
                {{ $t('contact.map.directions') }}
              </b-button>
            </div>
          </b-card>
        </b-col>
      </b-row>
      
      <!-- FAQ -->
      <b-row class="mt-5">
        <b-col lg="8" class="mx-auto">
          <h3 class="text-center mb-4">{{ $t('contact.faq.title') }}</h3>
          
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-button block variant="light" v-b-toggle.accordion-1>
                {{ $t('contact.faq.q1') }}
              </b-button>
            </b-card-header>
            <b-collapse id="accordion-1" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <p>{{ $t('contact.faq.a1') }}</p>
              </b-card-body>
            </b-collapse>
          </b-card>
          
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-button block variant="light" v-b-toggle.accordion-2>
                {{ $t('contact.faq.q2') }}
              </b-button>
            </b-card-header>
            <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <p>{{ $t('contact.faq.a2') }}</p>
              </b-card-body>
            </b-collapse>
          </b-card>
          
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-button block variant="light" v-b-toggle.accordion-3>
                {{ $t('contact.faq.q3') }}
              </b-button>
            </b-card-header>
            <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <p>{{ $t('contact.faq.a3') }}</p>
              </b-card-body>
            </b-collapse>
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
      form: {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        subject: null,
        message: ''
      },
      subjectOptions: [
        { value: null, text: this.$t('contact.form.selectSubject') },
        { value: 'information', text: this.$t('contact.form.subjects.information') },
        { value: 'order', text: this.$t('contact.form.subjects.order') },
        { value: 'complaint', text: this.$t('contact.form.subjects.complaint') },
        { value: 'partnership', text: this.$t('contact.form.subjects.partnership') },
        { value: 'other', text: this.$t('contact.form.subjects.other') }
      ],
      isSubmitting: false,
      showSuccess: false
    }
  },
  methods: {
    async submitForm() {
      try {
        this.isSubmitting = true;
        
        // Simuler une requête API
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        // Réinitialiser le formulaire
        this.form = {
          firstName: '',
          lastName: '',
          email: '',
          phone: '',
          subject: null,
          message: ''
        };
        
        // Afficher le message de succès
        this.showSuccess = true;
        
        // Faire défiler vers le haut pour voir le message
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } catch (error) {
        console.error('Erreur lors de l\'envoi du formulaire:', error);
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
.contact-info a {
  color: inherit;
  text-decoration: none;
}

.contact-info a:hover {
  color: #007bff;
  text-decoration: underline;
}

.map-container {
  position: relative;
  overflow: hidden;
  border-radius: 0.25rem;
}
</style>
