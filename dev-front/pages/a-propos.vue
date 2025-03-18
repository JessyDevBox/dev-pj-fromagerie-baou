<template>
  <div>
    <div class="page-header bg-light py-5">
      <b-container>
        <h1>{{ $t('about.title') }}</h1>
      </b-container>
    </div>

    <b-container class="py-5">
      <!-- Histoire -->
      <b-row class="mb-5 align-items-center">
        <b-col md="6">
          <h2>{{ $t('about.history.title') }}</h2>
          <p>{{ $t('about.history.description') }}</p>
          <p>
            La Fromagerie du Baou a été créée en 2024 par des passionnés de fromages artisanaux.
            Notre objectif est de faire découvrir les richesses fromagères de notre terroir français,
            en privilégiant les produits de qualité issus de petits producteurs locaux.
          </p>
          <p>
            Nous avons choisi de nous installer à Peypin, dans les Bouches-du-Rhône, pour être au plus près
            de notre clientèle locale tout en proposant une sélection de fromages venus de toute la France.
          </p>
        </b-col>
        <b-col md="6">
          <b-img src="/images/shop-exterior.jpg" fluid rounded alt="Extérieur de la fromagerie"></b-img>
        </b-col>
      </b-row>

      <!-- Nos valeurs -->
      <h2 class="text-center mb-4">{{ $t('about.values.title') }}</h2>
      <b-row class="mb-5">
        <b-col md="4" class="mb-4">
          <b-card class="h-100 text-center p-4">
            <b-icon icon="geo-alt" variant="primary" font-scale="3" class="mb-3"></b-icon>
            <h3>{{ $t('about.values.local') }}</h3>
            <p>
              Nous sélectionnons nos fromages auprès de producteurs locaux et régionaux,
              pour valoriser les savoir-faire de nos terroirs et réduire notre impact environnemental.
            </p>
          </b-card>
        </b-col>
        <b-col md="4" class="mb-4">
          <b-card class="h-100 text-center p-4">
            <b-icon icon="truck" variant="primary" font-scale="3" class="mb-3"></b-icon>
            <h3>{{ $t('about.values.short') }}</h3>
            <p>
              Nous privilégions les circuits courts pour garantir la fraîcheur de nos produits
              et soutenir directement les producteurs, sans intermédiaires.
            </p>
          </b-card>
        </b-col>
        <b-col md="4" class="mb-4">
          <b-card class="h-100 text-center p-4">
            <b-icon icon="hand-thumbs-up" variant="primary" font-scale="3" class="mb-3"></b-icon>
            <h3>{{ $t('about.values.artisanal') }}</h3>
            <p>
              Nous mettons en avant les méthodes de fabrication traditionnelles et artisanales,
              garantes de la qualité et de l'authenticité des fromages que nous proposons.
            </p>
          </b-card>
        </b-col>
      </b-row>

      <!-- Notre équipe -->
      <h2 class="text-center mb-4">Notre équipe</h2>
      <b-row>
        <b-col md="4" class="mb-4">
          <b-card class="text-center border-0">
            <b-avatar size="lg" src="/images/team-1.jpg" class="mb-3"></b-avatar>
            <h4>Sophie Martin</h4>
            <p class="text-muted">Fondatrice & Fromagère</p>
            <p>
              Passionnée de fromages depuis toujours, Sophie a travaillé pendant 10 ans
              dans différentes fromageries avant de créer la Fromagerie du Baou.
            </p>
          </b-card>
        </b-col>
        <b-col md="4" class="mb-4">
          <b-card class="text-center border-0">
            <b-avatar size="lg" src="/images/team-2.jpg" class="mb-3"></b-avatar>
            <h4>Thomas Durand</h4>
            <p class="text-muted">Affineur</p>
            <p>
              Spécialiste de l'affinage, Thomas veille à ce que chaque fromage soit
              proposé à son point optimal de dégustation.
            </p>
          </b-card>
        </b-col>
        <b-col md="4" class="mb-4">
          <b-card class="text-center border-0">
            <b-avatar size="lg" src="/images/team-3.jpg" class="mb-3"></b-avatar>
            <h4>Julie Blanc</h4>
            <p class="text-muted">Conseillère en vente</p>
            <p>
              Avec son expertise en accords fromages et vins, Julie vous guide dans
              vos choix pour trouver les fromages parfaits pour chaque occasion.
            </p>
          </b-card>
        </b-col>
      </b-row>

      <!-- Nos partenaires -->
      <h2 class="text-center my-5">Nos partenaires</h2>
      <b-row class="align-items-center text-center">
        <b-col md="3" class="mb-4">
          <b-img src="/images/partner-1.png" height="80" alt="GAEC Éleveurs des Baous"></b-img>
          <p class="mt-2">GAEC Éleveurs des Baous</p>
        </b-col>
        <b-col md="3" class="mb-4">
          <b-img src="/images/partner-2.png" height="80" alt="Ferme de la Tinée"></b-img>
          <p class="mt-2">Ferme de la Tinée</p>
        </b-col>
        <b-col md="3" class="mb-4">
          <b-img src="/images/partner-3.png" height="80" alt="Coopérative laitière de Beaufort"></b-img>
          <p class="mt-2">Coopérative laitière de Beaufort</p>
        </b-col>
        <b-col md="3" class="mb-4">
          <b-img src="/images/partner-4.png" height="80" alt="Maison Mons Fromager-Affineur"></b-img>
          <p class="mt-2">Maison Mons Fromager-Affineur</p>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: 'À propos - Fromagerie du Baou'
    }
  }
}
</script>
