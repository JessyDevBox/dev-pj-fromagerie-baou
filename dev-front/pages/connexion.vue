<template>
  <div>
    <b-container class="py-5">
      <b-row>
        <b-col md="6" class="mx-auto">
          <b-card title="Connexion" class="shadow-sm">
            <b-alert v-model="showError" variant="danger" dismissible>
              {{ errorMessage }}
            </b-alert>
            
            <b-form @submit.prevent="login">
              <b-form-group label="Email">
                <b-form-input
                  v-model="form.email"
                  type="email"
                  required
                  placeholder="Votre adresse email"
                ></b-form-input>
              </b-form-group>
              
              <b-form-group label="Mot de passe">
                <b-form-input
                  v-model="form.password"
                  type="password"
                  required
                  placeholder="Votre mot de passe"
                ></b-form-input>
              </b-form-group>
              
              <div class="d-flex justify-content-between align-items-center mb-4">
                <b-form-checkbox v-model="form.rememberMe">
                  Se souvenir de moi
                </b-form-checkbox>
                <b-link to="/mot-de-passe-oublie">Mot de passe oublié ?</b-link>
              </div>
              
              <div class="d-grid gap-2">
                <b-button type="submit" variant="primary" :disabled="isLoading">
                  <b-spinner small v-if="isLoading" class="me-2"></b-spinner>
                  Se connecter
                </b-button>
              </div>
            </b-form>
            
            <hr class="my-4">
            
            <p class="text-center mb-0">
              Pas encore de compte ? 
              <b-link to="/inscription">S'inscrire</b-link>
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
        email: '',
        password: '',
        rememberMe: false
      },
      isLoading: false,
      showError: false,
      errorMessage: ''
    }
  },
  methods: {
    async login() {
      try {
        this.isLoading = true;
        this.showError = false;
        
        await this.$auth.loginWith('local', {
          data: {
            username: this.form.email,
            password: this.form.password
          }
        });
        
        this.$router.push('/compte');
      } catch (error) {
        this.showError = true;
        this.errorMessage = 'Identifiants incorrects. Veuillez réessayer.';
      } finally {
        this.isLoading = false;
      }
    }
  },
  head() {
    return {
      title: 'Connexion - Fromagerie du Baou'
    }
  }
}
</script>
