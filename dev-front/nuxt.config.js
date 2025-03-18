export default {
    // Target: https://go.nuxtjs.dev/config-target
    target: 'static',
  
    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
      title: 'Fromagerie du Baou - Fromages artisanaux à Peypin',
      htmlAttrs: {
        lang: 'fr'
      },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { hid: 'description', name: 'description', content: 'Fromagerie artisanale à Peypin proposant des fromages du terroir français, plateaux et charcuterie artisanale.' },
        { name: 'format-detection', content: 'telephone=no' },
        { name: 'keywords', content: 'fromagerie artisanale Peypin, plateaux fromages Alpes-Maritimes, fromages AOP, fromages terroir' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Open+Sans:wght@300;400;600&display=swap' }
      ]
    },
  
    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
      '~/assets/scss/main.scss'
    ],
  
    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
    ],
  
    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,
  
    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
      // https://go.nuxtjs.dev/typescript
      '@nuxt/typescript-build'
    ],
  
    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
      // https://go.nuxtjs.dev/bootstrap
      'bootstrap-vue-3/nuxt',
      // https://go.nuxtjs.dev/axios
      '@nuxtjs/axios',
      // https://auth.nuxtjs.org/
      '@nuxtjs/auth-next',
      // https://i18n.nuxtjs.org/
      '@nuxtjs/i18n'
    ],
  
    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {
      baseURL: 'http://localhost:8000/api/v1'
    },
  
    // Auth module configuration
    auth: {
      strategies: {
        local: {
          token: {
            property: 'access_token',
            global: true,
            type: 'Bearer'
          },
          user: {
            property: false
          },
          endpoints: {
            login: { url: '/auth/login', method: 'post' },
            logout: false,
            user: { url: '/users/me', method: 'get' }
          }
        }
      },
      redirect: {
        login: '/connexion',
        logout: '/',
        home: '/'
      }
    },
  
    // i18n module configuration
    i18n: {
      locales: [
        { code: 'fr', iso: 'fr-FR', file: 'fr.json', name: 'Français' },
        { code: 'en', iso: 'en-US', file: 'en.json', name: 'English' }
      ],
      defaultLocale: 'fr',
      langDir: 'locales/',
      strategy: 'prefix_except_default',
      vueI18n: {
        fallbackLocale: 'fr'
      }
    },
  
    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {
    }
}
  