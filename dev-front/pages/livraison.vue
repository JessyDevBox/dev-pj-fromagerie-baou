<template>
  <div>
    <div class="page-header bg-light py-5">
      <b-container>
        <h1>Livraison</h1>
        <p class="lead">Informations sur nos options de livraison et de retrait</p>
      </b-container>
    </div>

    <b-container class="py-5">
      <b-row>
        <b-col lg="8" class="mx-auto">
          <!-- Options de livraison -->
          <b-card class="mb-5">
            <h3 class="mb-4">Nos options de livraison</h3>
            
            <div class="delivery-option mb-4 p-3 border rounded">
              <div class="d-flex align-items-center mb-2">
                <b-icon icon="shop" variant="primary" font-scale="1.5" class="me-3"></b-icon>
                <h4 class="mb-0">Retrait en boutique</h4>
              </div>
              <p>
                Commandez en ligne et venez chercher vos produits directement à la fromagerie.
                Nous préparons votre commande avec soin pour qu'elle soit prête à l'heure convenue.
              </p>
              <div class="d-flex justify-content-between align-items-center">
                <span class="text-success fw-bold">Gratuit</span>
                <span class="text-muted">Délai : 2h minimum</span>
              </div>
            </div>
            
            <div class="delivery-option mb-4 p-3 border rounded">
              <div class="d-flex align-items-center mb-2">
                <b-icon icon="truck" variant="primary" font-scale="1.5" class="me-3"></b-icon>
                <h4 class="mb-0">Livraison locale</h4>
              </div>
              <p>
                Nous livrons dans un rayon de 15 km autour de Peypin. Votre commande est livrée
                dans un emballage isotherme pour garantir la fraîcheur de vos fromages.
              </p>
              <div class="d-flex justify-content-between align-items-center">
                <span class="fw-bold">5€ (gratuit à partir de 50€ d'achat)</span>
                <span class="text-muted">Délai : Sous 24h</span>
              </div>
            </div>
            
            <div class="delivery-option mb-4 p-3 border rounded">
              <div class="d-flex align-items-center mb-2">
                <b-icon icon="box-seam" variant="primary" font-scale="1.5" class="me-3"></b-icon>
                <h4 class="mb-0">Expédition nationale</h4>
              </div>
              <p>
                Nous expédions nos fromages dans toute la France métropolitaine en Chronofresh,
                garantissant une livraison à température contrôlée pour préserver la qualité de nos produits.
              </p>
              <div class="d-flex justify-content-between align-items-center">
                <span class="fw-bold">12€ (gratuit à partir de 80€ d'achat)</span>
                <span class="text-muted">Délai : 24h-48h</span>
              </div>
            </div>
          </b-card>
          
          <!-- Zones de livraison -->
          <b-card class="mb-5">
            <h3 class="mb-4">Zones de livraison locale</h3>
            
            <p>
              Notre service de livraison locale couvre les communes suivantes :
            </p>
            
            <b-row>
              <b-col md="6">
                <ul>
                  <li>Peypin</li>
                  <li>Aubagne</li>
                  <li>La Destrousse</li>
                  <li>Roquevaire</li>
                  <li>Auriol</li>
                  <li>La Bouilladisse</li>
                </ul>
              </b-col>
              <b-col md="6">
                <ul>
                  <li>Cadolive</li>
                  <li>Saint-Savournin</li>
                  <li>Gréasque</li>
                  <li>Belcodène</li>
                  <li>Gardanne</li>
                  <li>Allauch</li>
                </ul>
              </b-col>
            </b-row>
            
            <div class="mt-3">
              <p>
                Pour les communes en dehors de cette zone, veuillez opter pour l'expédition nationale
                ou nous contacter pour étudier les possibilités.
              </p>
            </div>
          </b-card>
          
          <!-- Emballage -->
          <b-card class="mb-5">
            <h3 class="mb-4">Notre engagement qualité</h3>
            
            <div class="mb-4">
              <h4>Emballage éco-responsable</h4>
              <p>
                Nous utilisons des emballages recyclables et biodégradables pour nos fromages.
                Nos sacs et boîtes sont fabriqués à partir de matériaux recyclés et peuvent être
                compostés ou recyclés après utilisation.
              </p>
            </div>
            
            <div class="mb-4">
              <h4>Conservation optimale</h4>
              <p>
                Pour les livraisons et expéditions, nous utilisons des emballages isothermes et des
                packs réfrigérants pour maintenir la chaîne du froid et garantir la fraîcheur de vos fromages.
              </p>
            </div>
            
            <div>
              <h4>Traçabilité</h4>
              <p>
                Chaque commande est suivie de la préparation à la livraison. Pour les expéditions nationales,
                un numéro de suivi vous est communiqué par email dès l'envoi de votre colis.
              </p>
            </div>
          </b-card>
          
          <!-- FAQ -->
          <b-card>
            <h3 class="mb-4">Questions fréquentes sur la livraison</h3>
            
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block variant="light" v-b-toggle.accordion-1>
                  Quels sont les délais de livraison ?
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-1" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <p>
                    Pour le retrait en boutique, votre commande est disponible dans un délai minimum de 2 heures
                    après validation (pendant nos heures d'ouverture).
                  </p>
                  <p>
                    Pour la livraison locale, nous livrons sous 24h, du mardi au samedi entre 14h et 18h.
                  </p>
                  <p>
                    Pour l'expédition nationale, le délai est de 24h à 48h ouvrées après validation de la commande.
                    Les commandes passées le week-end sont traitées le lundi.
                  </p>
                </b-card-body>
              </b-collapse>
            </b-card>
            
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block variant="light" v-b-toggle.accordion-2>
                  Comment sont emballés les fromages pour l'expédition ?
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <p>
                    Nos fromages sont d'abord emballés individuellement dans du papier spécial fromage qui
                    leur permet de "respirer" tout en conservant leur fraîcheur. Ils sont ensuite placés dans
                    une boîte isotherme avec des packs réfrigérants pour maintenir une température optimale
                    pendant le transport.
                  </p>
                  <p>
                    Pour les fromages plus fragiles, nous utilisons des protections supplémentaires pour
                    éviter qu'ils ne s'écrasent pendant le transport.
                  </p>
                </b-card-body>
              </b-collapse>
            </b-card>
            
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block variant="light" v-b-toggle.accordion-3>
                  Que faire si je ne suis pas présent lors de la livraison ?
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <p>
                    Pour la livraison locale, vous pouvez indiquer un lieu sûr où déposer votre commande
                    dans les instructions de livraison (voisin, concierge, etc.).
                  </p>
                  <p>
                    Pour l'expédition nationale avec Chronofresh, en cas d'absence, le livreur laissera un avis
                    de passage et vous pourrez reprogrammer la livraison ou retirer votre colis au point relais
                    indiqué. Attention, les colis contenant des produits frais ne peuvent pas être conservés
                    plus de 48h au point relais.
                  </p>
                </b-card-body>
              </b-collapse>
            </b-card>
            
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block variant="light" v-b-toggle.accordion-4>
                  Est-il possible de programmer une livraison à une date précise ?
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <p>
                    Oui, lors de la validation de votre commande, vous pouvez sélectionner une date de livraison
                    souhaitée (sous réserve de disponibilité). Cette option est particulièrement utile si vous
                    commandez pour une occasion spéciale.
                  </p>
                  <p>
                    Pour les commandes importantes ou les événements, nous vous recommandons de nous contacter
                    directement par téléphone pour organiser la livraison.
                  </p>
                </b-card-body>
              </b-collapse>
            </b-card>
            
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block variant="light" v-b-toggle.accordion-5>
                  Livrez-vous à l'international ?
                </b-button>
              </b-card-header>
              <b-collapse id="accordion-5" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <p>
                    Actuellement, nous ne proposons pas de livraison internationale en raison des contraintes
                    réglementaires liées à l'exportation de produits laitiers et de la difficulté à garantir
                    la chaîne du froid sur de longues distances.
                  </p>
                  <p>
                    Nous livrons uniquement en France métropolitaine (Corse incluse).
                  </p>
                </b-card-body>
              </b-collapse>
            </b-card>
          </b-card>
          
          <!-- Calendrier de livraison -->
          <b-card class="mt-5">
            <h3 class="mb-4">Calendrier de livraison</h3>
            
            <b-table
              :items="deliverySchedule"
              :fields="scheduleFields"
              striped
              responsive
              class="text-center"
            >
              <template #cell(morning)="data">
                <span v-if="data.value" class="text-success">
                  <b-icon icon="check" font-scale="1.2"></b-icon>
                </span>
                <span v-else class="text-danger">
                  <b-icon icon="x" font-scale="1.2"></b-icon>
                </span>
              </template>
              <template #cell(afternoon)="data">
                <span v-if="data.value" class="text-success">
                  <b-icon icon="check" font-scale="1.2"></b-icon>
                </span>
                <span v-else class="text-danger">
                  <b-icon icon="x" font-scale="1.2"></b-icon>
                </span>
              </template>
            </b-table>
            
            <p class="mt-3 text-muted">
              * Les commandes passées après 12h sont traitées le jour ouvré suivant.<br>
              * Les livraisons locales du matin sont effectuées entre 9h et 12h, celles de l'après-midi entre 14h et 18h.
            </p>
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
      scheduleFields: [
        { key: 'day', label: 'Jour' },
        { key: 'morning', label: 'Matin (9h-12h)' },
        { key: 'afternoon', label: 'Après-midi (14h-18h)' }
      ],
      deliverySchedule: [
        { day: 'Lundi', morning: false, afternoon: false },
        { day: 'Mardi', morning: false, afternoon: true },
        { day: 'Mercredi', morning: true, afternoon: true },
        { day: 'Jeudi', morning: false, afternoon: true },
        { day: 'Vendredi', morning: true, afternoon: true },
        { day: 'Samedi', morning: true, afternoon: false },
        { day: 'Dimanche', morning: false, afternoon: false }
      ]
    }
  },
  head() {
    return {
      title: 'Livraison - Fromagerie du Baou'
    }
  }
}
</script>

<style scoped>
.delivery-option {
  transition: all 0.3s ease;
}

.delivery-option:hover {
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  transform: translateY(-5px);
}
</style>
