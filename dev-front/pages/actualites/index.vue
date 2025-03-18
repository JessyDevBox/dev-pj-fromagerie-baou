<template>
  <div>
    <div class="page-header bg-light py-5">
      <b-container>
        <h1>{{ $t('news.title') }}</h1>
        <p class="lead">{{ $t('news.description') }}</p>
      </b-container>
    </div>

    <b-container class="py-5">
      <!-- Filtres -->
      <b-row class="mb-4">
        <b-col md="6" lg="4">
          <b-form-group label="Filtrer par catégorie">
            <b-form-select v-model="selectedCategory" :options="categoryOptions"></b-form-select>
          </b-form-group>
        </b-col>
        <b-col md="6" lg="4">
          <b-form-group label="Rechercher">
            <b-form-input v-model="searchQuery" placeholder="Rechercher un article..."></b-form-input>
          </b-form-group>
        </b-col>
      </b-row>

      <!-- Liste des articles -->
      <b-row>
        <b-col v-for="article in filteredArticles" :key="article.id" md="6" lg="4" class="mb-4">
          <b-card
            :title="article.title"
            :img-src="article.image"
            :img-alt="article.title"
            img-top
            class="h-100 news-card"
          >
            <b-card-text>
              <div class="d-flex justify-content-between mb-2">
                <b-badge variant="primary">{{ article.category }}</b-badge>
                <small class="text-muted">{{ formatDate(article.date) }}</small>
              </div>
              <p>{{ article.excerpt }}</p>
            </b-card-text>
            <template #footer>
              <div class="d-grid gap-2">
                <b-button variant="outline-primary" :to="`/actualites/${article.slug}`">
                  {{ $t('news.readMore') }}
                </b-button>
              </div>
            </template>
          </b-card>
        </b-col>
      </b-row>

      <!-- Pagination -->
      <b-row class="mt-4">
        <b-col class="d-flex justify-content-center">
          <b-pagination
            v-model="currentPage"
            :total-rows="filteredArticles.length"
            :per-page="perPage"
            align="center"
          ></b-pagination>
        </b-col>
      </b-row>

      <!-- Newsletter -->
      <b-row class="mt-5">
        <b-col lg="8" class="mx-auto">
          <b-card bg-variant="light" class="text-center p-4">
            <h3>{{ $t('news.newsletter.title') }}</h3>
            <p>{{ $t('news.newsletter.description') }}</p>
            <b-form @submit.prevent="subscribeNewsletter" inline class="justify-content-center">
              <b-form-input
                v-model="newsletter.email"
                type="email"
                required
                placeholder="Votre adresse email"
                class="mb-2 me-sm-2 mb-sm-0"
              ></b-form-input>
              <b-button type="submit" variant="primary" :disabled="isSubscribing">
                <b-spinner small v-if="isSubscribing" class="me-2"></b-spinner>
                {{ $t('news.newsletter.button') }}
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
      articles: [
        {
          id: 1,
          title: "Le Comté d'été vs d'hiver : quelles différences ?",
          slug: "comte-ete-vs-hiver",
          excerpt: "Découvrez les différences subtiles entre le Comté fabriqué en été et celui fabriqué en hiver, et comment la saisonnalité influence ses arômes.",
          image: "/images/news/comte-seasons.jpg",
          category: "Fromages",
          date: "2024-03-10"
        },
        {
          id: 2,
          title: "Nouveauté : arrivage de fromages corses",
          slug: "arrivage-fromages-corses",
          excerpt: "Nous sommes ravis de vous annoncer l'arrivée de nouveaux fromages corses dans notre sélection : Brocciu, Venaco et Niolo.",
          image: "/images/news/corsican-cheese.jpg",
          category: "Nouveautés",
          date: "2024-03-05"
        },
        {
          id: 3,
          title: "Atelier dégustation : les fromages de brebis",
          slug: "atelier-degustation-fromages-brebis",
          excerpt: "Participez à notre prochain atelier dégustation consacré aux fromages de brebis le 25 mars à 18h30 à la fromagerie.",
          image: "/images/news/sheep-cheese-tasting.jpg",
          category: "Événements",
          date: "2024-03-01"
        },
        {
          id: 4,
          title: "Le saviez-vous ? L'histoire du Roquefort",
          slug: "histoire-roquefort",
          excerpt: "Plongez dans l'histoire fascinante du Roquefort, premier fromage à avoir obtenu une Appellation d'Origine Contrôlée en 1925.",
          image: "/images/news/roquefort-history.jpg",
          category: "Culture fromagère",
          date: "2024-02-25"
        },
        {
          id: 5,
          title: "Recette : tarte aux poireaux et au Morbier",
          slug: "recette-tarte-poireaux-morbier",
          excerpt: "Découvrez notre recette de tarte aux poireaux et au Morbier, un plat réconfortant et savoureux pour les soirées d'hiver.",
          image: "/images/news/morbier-leek-tart.jpg",
          category: "Recettes",
          date: "2024-02-20"
        },
        {
          id: 6,
          title: "Rencontre avec un producteur : la Ferme des Alpilles",
          slug: "rencontre-producteur-ferme-alpilles",
          excerpt: "Nous avons rencontré Marie et Jean de la Ferme des Alpilles, qui produisent d'excellents fromages de chèvre près de Saint-Rémy-de-Provence.",
          image: "/images/news/alpilles-farm.jpg",
          category: "Producteurs",
          date: "2024-02-15"
        }
      ],
      selectedCategory: null,
      searchQuery: '',
      currentPage: 1,
      perPage: 6,
      newsletter: {
        email: ''
      },
      isSubscribing: false
    }
  },
  computed: {
    categoryOptions() {
      const categories = this.articles.map(article => article.category);
      const uniqueCategories = [...new Set(categories)];
      return [
        { value: null, text: 'Toutes les catégories' },
        ...uniqueCategories.map(category => ({ value: category, text: category }))
      ];
    },
    filteredArticles() {
      let filtered = [...this.articles];
      
      // Filtrer par catégorie
      if (this.selectedCategory) {
        filtered = filtered.filter(article => article.category === this.selectedCategory);
      }
      
      // Filtrer par recherche
      if (this.searchQuery) {
        const query = this.searchQuery.toLowerCase();
        filtered = filtered.filter(article => 
          article.title.toLowerCase().includes(query) || 
          article.excerpt.toLowerCase().includes(query)
        );
      }
      
      // Trier par date (plus récent d'abord)
      filtered.sort((a, b) => new Date(b.date) - new Date(a.date));
      
      return filtered;
    },
    paginatedArticles() {
      const start = (this.currentPage - 1) * this.perPage;
      const end = start + this.perPage;
      return this.filteredArticles.slice(start, end);
    }
  },
  methods: {
    formatDate(dateString) {
      const options = { day: 'numeric', month: 'long', year: 'numeric' };
      return new Date(dateString).toLocaleDateString('fr-FR', options);
    },
    async subscribeNewsletter() {
      if (!this.newsletter.email) return;
      
      try {
        this.isSubscribing = true;
        
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
      } finally {
        this.isSubscribing = false;
      }
    }
  },
  head() {
    return {
      title: 'Actualités - Fromagerie du Baou'
    }
  }
}
</script>

<style scoped>
.news-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.news-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}
</style>
