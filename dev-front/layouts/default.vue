<template>
  <div>
    <header>
      <b-navbar toggleable="lg" type="light" class="navbar">
        <b-container>
          <b-navbar-brand to="/">
            <img src="~/assets/images/logo.png" alt="Fromagerie du Baou" height="40">
          </b-navbar-brand>

          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
              <b-nav-item to="/" exact>{{ $t('nav.home') }}</b-nav-item>
              <b-nav-item to="/fromages">{{ $t('nav.cheeses') }}</b-nav-item>
              <b-nav-item to="/plateaux">{{ $t('nav.platters') }}</b-nav-item>
              <b-nav-item to="/a-propos">{{ $t('nav.about') }}</b-nav-item>
              <b-nav-item to="/techniques">{{ $t('nav.techniques') }}</b-nav-item>
              <b-nav-item to="/livraison">{{ $t('nav.delivery') }}</b-nav-item>
              <b-nav-item to="/contact">{{ $t('nav.contact') }}</b-nav-item>
            </b-navbar-nav>

            <b-navbar-nav class="ms-auto">
              <b-nav-item-dropdown right>
                <template #button-content>
                  <span>{{ currentLocale.name }}</span>
                </template>
                <b-dropdown-item 
                  v-for="locale in availableLocales" 
                  :key="locale.code"
                  @click="switchLanguage(locale.code)"
                >
                  {{ locale.name }}
                </b-dropdown-item>
              </b-nav-item-dropdown>

              <template v-if="!$auth.loggedIn">
                <b-nav-item to="/connexion">{{ $t('nav.login') }}</b-nav-item>
                <b-nav-item to="/inscription">{{ $t('nav.register') }}</b-nav-item>
              </template>
              <b-nav-item-dropdown v-else right>
                <template #button-content>
                  <span>{{ $auth.user.first_name }}</span>
                </template>
                <b-dropdown-item to="/compte">{{ $t('nav.account') }}</b-dropdown-item>
                <b-dropdown-item @click="logout">{{ $t('account.logout') }}</b-dropdown-item>
              </b-nav-item-dropdown>
            </b-navbar-nav>
          </b-collapse>
        </b-container>
      </b-navbar>
    </header>

    <main>
      <Nuxt />
    </main>

    <footer class="footer mt-5">
      <b-container>
        <b-row>
          <b-col md="4" class="mb-4">
            <h5>Fromagerie du Baou</h5>
            <p>ZA Le Terme D908<br>13124 Peypin<br>Bouches-du-Rhône</p>
            <p>
              <b-icon icon="telephone"></b-icon> 04 93 08 59 25<br>
              <b-icon icon="envelope"></b-icon> fromageriedubaou@gmail.com
            </p>
          </b-col>
          <b-col md="4" class="mb-4">
            <h5>Horaires d'ouverture</h5>
            <p>Du mardi au samedi<br>9h - 13h / 15h - 19h<br>Dimanche<br>9h - 13h</p>
          </b-col>
          <b-col md="4" class="mb-4">
            <h5>Suivez-nous</h5>
            <div class="social-links">
              <a href="https://www.facebook.com/p/Fromagerie-du-Baou-61565581314658/" target="_blank" class="me-3">
                <b-icon icon="facebook" font-scale="1.5"></b-icon>
              </a>
              <a href="https://www.instagram.com/fromageriedubaou/" target="_blank">
                <b-icon icon="instagram" font-scale="1.5"></b-icon>
              </a>
            </div>
          </b-col>
        </b-row>
        <hr class="my-4">
        <p class="text-center mb-0">
          &copy; {{ new Date().getFullYear() }} Fromagerie du Baou - Tous droits réservés
        </p>
      </b-container>
    </footer>
  </div>
</template>

<script>
export default {
  computed: {
    currentLocale() {
      return this.$i18n.locales.find(locale => locale.code === this.$i18n.locale);
    },
    availableLocales() {
      return this.$i18n.locales.filter(locale => locale.code !== this.$i18n.locale);
    }
  },
  methods: {
    switchLanguage(locale) {
      this.$i18n.setLocale(locale);
    },
    async logout() {
      await this.$auth.logout();
      this.$router.push('/');
    }
  }
}
</script>
