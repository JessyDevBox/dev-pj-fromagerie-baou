<template>
  <div>
    <div v-if="article" class="article-page">
      <!-- En-tête de l'article -->
      <div class="article-header position-relative">
        <b-img :src="article.image" fluid alt="Article header" class="w-100 article-banner"></b-img>
        <div class="article-overlay"></div>
        <b-container class="position-relative">
          <div class="article-header-content text-white">
            <b-badge variant="primary" class="mb-2">{{ article.category }}</b-badge>
            <h1 class="display-4">{{ article.title }}</h1>
            <div class="d-flex align-items-center mt-3">
              <b-avatar :src="article.author.avatar" class="me-2"></b-avatar>
              <div>
                <div>{{ article.author.name }}</div>
                <small>{{ formatDate(article.date) }}</small>
              </div>
            </div>
          </div>
        </b-container>
      </div>
      
      <!-- Contenu de l'article -->
      <b-container class="py-5">
        <b-row>
          <b-col lg="8" class="mx-auto">
            <!-- Introduction -->
            <div class="article-intro mb-4">
              <p class="lead">{{ article.intro }}</p>
            </div>
            
            <!-- Corps de l'article -->
            <div class="article-content">
              <div v-for="(section, index) in article.content" :key="index" class="mb-4">
                <h2 v-if="section.title" class="mb-3">{{ section.title }}</h2>
                <b-img v-if="section.image" :src="section.image" fluid class="rounded mb-3" :alt="section.imageAlt || 'Article image'"></b-img>
                <div v-html="section.text"></div>
              </div>
            </div>
            
            <!-- Tags -->
            <div class="article-tags mt-5">
              <h5>Tags</h5>
              <div>
                <b-badge 
                  v-for="tag in article.tags" 
                  :key="tag" 
                  variant="light" 
                  class="me-2 mb-2 p-2"
                >
                  {{ tag }}
                </b-badge>
              </div>
            </div>
            
            <!-- Partage -->
            <div class="article-share mt-4 p-3 bg-light rounded">
              <h5>Partager cet article</h5>
              <div class="d-flex">
                <b-button variant="outline-primary" size="sm" class="me-2">
                  <b-icon icon="facebook"></b-icon> Facebook
                </b-button>
                <b-button variant="outline-info" size="sm" class="me-2">
                  <b-icon icon="twitter"></b-icon> Twitter
                </b-button>
                <b-button variant="outline-success" size="sm">
                  <b-icon icon="envelope"></b-icon> Email
                </b-button>
              </div>
            </div>
            
            <!-- Articles liés -->
            <div class="related-articles mt-5">
              <h3 class="mb-4">Articles similaires</h3>
              <b-row>
                <b-col v-for="article in relatedArticles" :key="article.id" md="6" class="mb-4">
                  <b-card
                    :title="article.title"
                    :img-src="article.image"
                    :img-alt="article.title"
                    img-top
                    class="h-100"
                  >
                    <b-card-text>
                      <small class="text-muted">{{ formatDate(article.date) }}</small>
                    </b-card-text>
                    <b-button variant="outline-primary" :to="`/actualites/${article.slug}`" size="sm">
                      Lire l'article
                    </b-button>
                  </b-card>
                </b-col>
              </b-row>
            </div>
            
            <!-- Commentaires -->
            <div class="article-comments mt-5">
              <h3 class="mb-4">Commentaires ({{ article.comments.length }})</h3>
              
              <b-form @submit.prevent="submitComment" class="mb-5">
                <b-form-group label="Votre commentaire">
                  <b-form-textarea
                    v-model="newComment.text"
                    rows="4"
                    placeholder="Partagez votre avis sur cet article..."
                    required
                  ></b-form-textarea>
                </b-form-group>
                <div class="d-flex justify-content-end">
                  <b-button type="submit" variant="primary" :disabled="isSubmitting">
                    <b-spinner small v-if="isSubmitting" class="me-2"></b-spinner>
                    Publier le commentaire
                  </b-button>
                </div>
              </b-form>
              
              <div v-if="article.comments.length > 0">
                <div v-for="comment in article.comments" :key="comment.id" class="comment mb-4 p-3 border rounded">
                  <div class="d-flex align-items-center mb-2">
                    <b-avatar :src="comment.author.avatar" size="sm" class="me-2"></b-avatar>
                    <div>
                      <strong>{{ comment.author.name }}</strong>
                      <small class="text-muted ms-2">{{ formatDate(comment.date) }}</small>
                    </div>
                  </div>
                  <p class="mb-0">{{ comment.text }}</p>
                </div>
              </div>
              <div v-else class="text-center py-4 text-muted">
                <b-icon icon="chat" font-scale="2" class="mb-3"></b-icon>
                <p>Soyez le premier à commenter cet article !</p>
              </div>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </div>
    
    <!-- Chargement -->
    <div v-else class="text-center py-5">
      <b-spinner variant="primary" label="Chargement..."></b-spinner>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      article: null,
      relatedArticles: [],
      newComment: {
        text: ''
      },
      isSubmitting: false
    }
  },
  async created() {
    // Simuler le chargement des données depuis une API
    await this.fetchArticle();
    this.fetchRelatedArticles();
  },
  methods: {
    formatDate(dateString) {
      const options = { day: 'numeric', month: 'long', year: 'numeric' };
      return new Date(dateString).toLocaleDateString('fr-FR', options);
    },
    async fetchArticle() {
      // Simuler une requête API
      await new Promise(resolve => setTimeout(resolve, 500));
      
      // Dans un vrai projet, on récupérerait l'article depuis l'API
      // Ici, on utilise des données statiques pour la démonstration
      if (this.$route.params.slug === 'comte-ete-vs-hiver') {
        this.article = {
          id: 1,
          title: "Le Comté d'été vs d'hiver : quelles différences ?",
          slug: "comte-ete-vs-hiver",
          category: "Fromages",
          date: "2024-03-10",
          image: "/images/news/comte-seasons.jpg",
          author: {
            name: "Sophie Martin",
            avatar: "/images/team/sophie.jpg"
          },
          intro: "Le Comté, ce fromage emblématique du Jura, présente des caractéristiques différentes selon la saison de production du lait. Découvrez les subtilités qui distinguent un Comté d'été d'un Comté d'hiver, et comment ces variations saisonnières influencent ses arômes et sa texture.",
          content: [
            {
              title: "L'influence de l'alimentation des vaches",
              text: "<p>La principale différence entre un Comté d'été et un Comté d'hiver réside dans l'alimentation des vaches Montbéliardes qui produisent le lait.</p><p>En été, de mai à octobre, les vaches paissent dans les pâturages d'altitude et se nourrissent d'herbe fraîche et de fleurs diverses. Cette alimentation riche et variée confère au lait, et donc au fromage, des arômes plus complexes et fruités.</p><p>En hiver, de novembre à avril, les vaches sont nourries principalement de foin récolté pendant l'été. Le lait produit est alors moins riche en arômes, donnant des fromages aux saveurs plus douces et beurrées.</p>"
            },
            {
              title: "Caractéristiques organoleptiques",
              image: "/images/news/comte-tasting.jpg",
              imageAlt: "Dégustation de Comté",
              text: "<p>Un Comté d'été présente généralement :</p><ul><li>Une couleur plus jaune due à la présence de carotène dans l'herbe fraîche</li><li>Des arômes plus intenses et complexes, avec des notes florales, fruitées et parfois épicées</li><li>Une texture plus souple et fondante</li></ul><p>Un Comté d'hiver se caractérise par :</p><ul><li>Une couleur plus pâle</li><li>Des arômes plus doux, avec des notes beurrées et de noisette</li><li>Une texture parfois plus ferme</li></ul>"
            },
            {
              title: "Comment les reconnaître ?",
              text: "<p>Pour identifier la saison de fabrication d'un Comté, il suffit de regarder la plaque de caséine verte présente sur la croûte. Le premier chiffre du numéro indique le trimestre de fabrication :</p><ul><li>1 : janvier-mars (hiver)</li><li>2 : avril-juin (printemps/début d'été)</li><li>3 : juillet-septembre (été)</li><li>4 : octobre-décembre (automne/début d'hiver)</li></ul><p>Cette information peut vous aider à choisir un Comté selon vos préférences gustatives, ou à varier les plaisirs au fil des saisons.</p>"
            },
            {
              title: "Notre sélection",
              text: "<p>À la Fromagerie du Baou, nous vous proposons des Comtés de différentes saisons et d'affinages variés pour vous permettre de découvrir toute la richesse de ce fromage d'exception.</p><p>N'hésitez pas à demander conseil à nos fromagers qui sauront vous guider dans votre choix en fonction de vos goûts et de l'utilisation que vous souhaitez en faire (dégustation, cuisine, plateau...).</p>"
            }
          ],
          tags: ["Comté", "AOP", "Saisonnalité", "Jura", "Pâte pressée cuite"],
          comments: [
            {
              id: 101,
              author: {
                name: "Jean Dupont",
                avatar: "/images/avatars/user1.jpg"
              },
              date: "2024-03-11",
              text: "Article très instructif ! Je ne savais pas que la saison avait autant d'impact sur le goût du Comté. Je vais faire plus attention lors de mes prochains achats."
            },
            {
              id: 102,
              author: {
                name: "Marie Leroy",
                avatar: "/images/avatars/user2.jpg"
              },
              date: "2024-03-12",
              text: "J'ai toujours préféré le Comté d'été sans savoir pourquoi. Maintenant je comprends mieux ces notes plus fruitées que j'apprécie tant. Merci pour ces explications !"
            }
          ]
        };
      } else {
        // Article par défaut ou redirection vers 404
        this.$router.push('/404');
      }
    },
    fetchRelatedArticles() {
      // Simuler une requête API
      // Dans un vrai projet, on récupérerait les articles liés depuis l'API
      this.relatedArticles = [
        {
          id: 4,
          title: "Le saviez-vous ? L'histoire du Roquefort",
          slug: "histoire-roquefort",
          image: "/images/news/roquefort-history.jpg",
          date: "2024-02-25"
        },
        {
          id: 6,
          title: "Rencontre avec un producteur : la Ferme des Alpilles",
          slug: "rencontre-producteur-ferme-alpilles",
          image: "/images/news/alpilles-farm.jpg",
          date: "2024-02-15"
        }
      ];
    },
    async submitComment() {
      if (!this.newComment.text) return;
      
      try {
        this.isSubmitting = true;
        
        // Simuler une requête API
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // Ajouter le commentaire à la liste (dans un vrai projet, ce serait fait via l'API)
        const newCommentObj = {
          id: Date.now(),
          author: {
            name: "Vous",
            avatar: "/images/avatars/default.jpg"
          },
          date: new Date().toISOString().split('T')[0],
          text: this.newComment.text
        };
        
        this.article.comments.push(newCommentObj);
        this.newComment.text = '';
        
        this.$bvToast.toast('Votre commentaire a été publié avec succès.', {
          title: 'Commentaire ajouté',
          variant: 'success',
          solid: true
        });
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
      title: this.article ? `${this.article.title} - Fromagerie du Baou` : 'Article - Fromagerie du Baou'
    }
  }
}
</script>

<style scoped>
.article-banner {
  height: 400px;
  object-fit: cover;
  object-position: center;
}

.article-header {
  margin-bottom: 2rem;
}

.article-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.7));
}

.article-header-content {
  position: absolute;
  bottom: 2rem;
  max-width: 800px;
}

.article-intro {
  font-size: 1.2rem;
  border-left: 4px solid #007bff;
  padding-left: 1rem;
}

.article-content {
  line-height: 1.8;
}

.comment {
  background-color: #f8f9fa;
  transition: background-color 0.3s ease;
}

.comment:hover {
  background-color: #f0f0f0;
}
</style>
