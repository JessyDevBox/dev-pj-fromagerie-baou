<template>
  <div>
    <b-container class="py-5">
      <b-row>
        <b-col lg="8" class="mx-auto">
          <b-card title="Créer un compte" class="shadow-sm">
            <b-alert v-model="showError" variant="danger" dismissible>
              {{ errorMessage }}
            </b-alert>
            
            <b-form @submit.prevent="register">
              <b-row>
                <b-col md="6">
                  <b-form-group label="Prénom *">
                    <b-form-input
                      v-model="form.firstName"
                      required
                      placeholder="Votre prénom"
                    ></b-form-input>
                  </b-form-group>
                </b-col>
                <b-col md="6">
                  <b-form-group label="Nom *">
                    <b-form-input
                      v-model="form.lastName"
                      required
                      placeholder="Votre nom"
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
              
              <b-form-group label="Email *">
                <b-form-input
                  v-model="form.email"
                  type="email"
                  required
                  placeholder="Votre adresse email"
                ></b-form-input>
              </b-form-group>
              
              <b-form-group label="Téléphone">
                <b-form-input
                  v-model="form.phone"
                  placeholder="Votre numéro de téléphone"
                ></b-form-input>
              </b-form-group>
              
              <b-row>
                <b-col md="6">
                  <b-form-group label="Mot de passe *">
                    <b-form-input
                      v-model="form.password"
                      type="password"
                      required
                      placeholder="Votre mot de passe"
                    ></b-form-input>
                    <small class="text-muted">8 caractères minimum</small>
                  </b-form-group>
                </b-col>
                <b-col md="6">
                  <b-form-group label="Confirmer le mot de passe *">
                    <b-form-input
                      v-model="form.confirmPassword"
                      type="password"
                      required
                      placeholder="Confirmez votre mot de passe"
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
              
              <b-form-group>
                <b-form-checkbox v-model="form.acceptTerms" required>
                  J'accepte les <b-link to="/conditions-generales">conditions générales d'utilisation</b-link>
                </b-form-checkbox>
              </b-form-group>
              
              <div class="d-grid gap-2">
                <b-button type="submit" variant="primary" :disabled="isLoading || !form.acceptTerms">
                  <b-spinner small v-if="isLoading" class="me-2"></b-spinner>
                  Créer mon compte
                </b-button>
              </div>
            </b-form>
            
            <hr class="my-4">
            
            <p class="text-center mb-0">
              Déjà un compte ? 
              <b-link to="/connexion">Se connecter</b-link>
            </p>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  middleware: 'guest',
  data() {
    return {
      form: {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        password: '',
        confirmPassword: '',
        acceptTerms: false
      },
      isLoading: false,
      showError: false,
      errorMessage: ''
    }
  },
  methods: {
    async register() {
      if (this.form.password !== this.form.confirmPassword) {
        this.showError = true;
        this.errorMessage = 'Les mots de passe ne correspondent pas.';
        return;
      }
      
      try {
        this.isLoading = true;
        this.showError = false;
        
        // Appel à l'API pour créer un compte
        await this.$axios.post('/auth/register', {
          email: this.form.email,
          first_name: this.form.firstName,
          last_name: this.form.lastName,
          phone: this.form.phone,
          password: this.form.password
        });
        
        // Afficher un message de succès
        this.$bvToast.toast('Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter.', {
          title: 'Inscription réussie',
          variant: 'success',
          solid: true
        });
        
        // Rediriger vers la page de connexion
        this.$router.push('/connexion');
      } catch (error) {
        this.showError = true;
        if (error.response && error.response.data && error.response.data.detail) {
          this.errorMessage = error.response.data.detail;
        } else {
          this.errorMessage = 'Une erreur est survenue lors de l\'inscription. Veuillez réessayer.';
        }
      } finally {
        this.isLoading = false;
      }
    }
  },
  head() {
    return {
      title: 'Inscription - Fromagerie du Baou'
    }
  }
}
</script>
