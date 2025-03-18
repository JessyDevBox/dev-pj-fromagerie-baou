<template>
  <div>
    <b-container class="py-5">
      <h1>{{ $t('account.title') }}</h1>
      
      <b-row class="mt-4">
        <b-col md="3">
          <b-list-group>
            <b-list-group-item 
              :active="activeTab === 'profile'"
              button
              @click="activeTab = 'profile'"
            >
              <b-icon icon="person" class="me-2"></b-icon>
              {{ $t('account.profile') }}
            </b-list-group-item>
            <b-list-group-item 
              :active="activeTab === 'orders'"
              button
              @click="activeTab = 'orders'"
            >
              <b-icon icon="bag" class="me-2"></b-icon>
              {{ $t('account.orders') }}
            </b-list-group-item>
            <b-list-group-item 
              :active="activeTab === 'requests'"
              button
              @click="activeTab = 'requests'"
            >
              <b-icon icon="card-checklist" class="me-2"></b-icon>
              {{ $t('account.requests') }}
            </b-list-group-item>
            <b-list-group-item 
              :active="activeTab === 'messages'"
              button
              @click="activeTab = 'messages'"
            >
              <b-icon icon="chat" class="me-2"></b-icon>
              {{ $t('account.messages') }}
            </b-list-group-item>
            <b-list-group-item 
              button
              @click="logout"
              variant="danger"
            >
              <b-icon icon="box-arrow-right" class="me-2"></b-icon>
              {{ $t('account.logout') }}
            </b-list-group-item>
          </b-list-group>
        </b-col>
        
        <b-col md="9">
          <!-- Profil -->
          <b-card v-if="activeTab === 'profile'">
            <template #header>
              <h4 class="mb-0">{{ $t('account.profile') }}</h4>
            </template>
            
            <b-form @submit.prevent="updateProfile">
              <b-row>
                <b-col md="6">
                  <b-form-group label="Prénom">
                    <b-form-input v-model="profile.firstName"></b-form-input>
                  </b-form-group>
                </b-col>
                <b-col md="6">
                  <b-form-group label="Nom">
                    <b-form-input v-model="profile.lastName"></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
              
              <b-form-group label="Email">
                <b-form-input v-model="profile.email" disabled></b-form-input>
              </b-form-group>
              
              <b-form-group label="Téléphone">
                <b-form-input v-model="profile.phone"></b-form-input>
              </b-form-group>
              
              <b-form-group label="Adresse">
                <b-form-input v-model="profile.address"></b-form-input>
              </b-form-group>
              
              <b-row>
                <b-col md="4">
                  <b-form-group label="Code postal">
                    <b-form-input v-model="profile.postalCode"></b-form-input>
                  </b-form-group>
                </b-col>
                <b-col md="8">
                  <b-form-group label="Ville">
                    <b-form-input v-model="profile.city"></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
              
              <div class="d-flex justify-content-end">
                <b-button type="submit" variant="primary" :disabled="isUpdating">
                  <b-spinner small v-if="isUpdating" class="me-2"></b-spinner>
                  Enregistrer les modifications
                </b-button>
              </div>
            </b-form>
          </b-card>
          
          <!-- Commandes -->
          <b-card v-if="activeTab === 'orders'">
            <template #header>
              <h4 class="mb-0">{{ $t('account.orders') }}</h4>
            </template>
            
            <div v-if="orders.length > 0">
              <b-table
                :items="orders"
                :fields="orderFields"
                striped
                hover
                responsive
              >
                <template #cell(status)="data">
                  <b-badge :variant="getOrderStatusVariant(data.value)">
                    {{ data.value }}
                  </b-badge>
                </template>
                <template #cell(actions)="data">
                  <b-button size="sm" variant="outline-primary" @click="viewOrder(data.item)">
                    Détails
                  </b-button>
                </template>
              </b-table>
            </div>
            <div v-else class="text-center py-4">
              <b-icon icon="basket" font-scale="3" class="mb-3"></b-icon>
              <p>Vous n'avez pas encore passé de commande.</p>
              <b-button variant="primary" to="/fromages">
                Découvrir nos fromages
              </b-button>
            </div>
          </b-card>
          
          <!-- Demandes de plateaux -->
          <b-card v-if="activeTab === 'requests'">
            <template #header>
              <h4 class="mb-0">{{ $t('account.requests') }}</h4>
            </template>
            
            <div v-if="platterRequests.length > 0">
              <b-table
                :items="platterRequests"
                :fields="requestFields"
                striped
                hover
                responsive
              >
                <template #cell(status)="data">
                  <b-badge :variant="getRequestStatusVariant(data.value)">
                    {{ data.value }}
                  </b-badge>
                </template>
                <template #cell(actions)="data">
                  <b-button size="sm" variant="outline-primary" @click="viewRequest(data.item)">
                    Détails
                  </b-button>
                </template>
              </b-table>
            </div>
            <div v-else class="text-center py-4">
              <b-icon icon="card-checklist" font-scale="3" class="mb-3"></b-icon>
              <p>Vous n'avez pas encore fait de demande de plateau personnalisé.</p>
              <b-button variant="primary" to="/plateaux">
                Créer un plateau sur mesure
              </b-button>
            </div>
          </b-card>
          
          <!-- Messages -->
          <b-card v-if="activeTab === 'messages'">
            <template #header>
              <h4 class="mb-0">{{ $t('account.messages') }}</h4>
            </template>
            
            <div v-if="messages.length > 0">
              <b-table
                :items="messages"
                :fields="messageFields"
                striped
                hover
                responsive
              >
                <template #cell(is_read)="data">
                  <b-badge v-if="data.value" variant="success">Lu</b-badge>
                  <b-badge v-else variant="warning">Non lu</b-badge>
                </template>
                <template #cell(actions)="data">
                  <b-button size="sm" variant="outline-primary" @click="viewMessage(data.item)">
                    Lire
                  </b-button>
                </template>
              </b-table>
            </div>
            <div v-else class="text-center py-4">
              <b-icon icon="chat" font-scale="3" class="mb-3"></b-icon>
              <p>Vous n'avez pas encore de messages.</p>
              <b-button variant="primary" to="/contact">
                Nous contacter
              </b-button>
            </div>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    
    <!-- Modals pour afficher les détails -->
    <b-modal id="order-details-modal" title="Détails de la commande" size="lg" hide-footer>
      <div v-if="selectedOrder">
        <p><strong>Numéro de commande:</strong> #{{ selectedOrder.id }}</p>
        <p><strong>Date:</strong> {{ formatDate(selectedOrder.created_at) }}</p>
        <p><strong>Statut:</strong> 
          <b-badge :variant="getOrderStatusVariant(selectedOrder.status)">
            {{ selectedOrder.status }}
          </b-badge>
        </p>
        <p><strong>Montant total:</strong> {{ selectedOrder.total_amount.toFixed(2) }} €</p>
        
        <h5 class="mt-4">Articles</h5>
        <b-table
          :items="selectedOrder.items"
          :fields="orderItemFields"
          striped
          responsive
        ></b-table>
      </div>
    </b-modal>
    
    <b-modal id="request-details-modal" title="Détails de la demande" size="lg" hide-footer>
      <div v-if="selectedRequest">
        <p><strong>Numéro de demande:</strong> #{{ selectedRequest.id }}</p>
        <p><strong>Date:</strong> {{ formatDate(selectedRequest.created_at) }}</p>
        <p><strong>Statut:</strong> 
          <b-badge :variant="getRequestStatusVariant(selectedRequest.status)">
            {{ selectedRequest.status }}
          </b-badge>
        </p>
        <p><strong>Nombre de personnes:</strong> {{ selectedRequest.guests_count }}</p>
        <p v-if="selectedRequest.budget"><strong>Budget:</strong> {{ selectedRequest.budget.toFixed(2) }} € par personne</p>
        
        <h5 class="mt-4">Description</h5>
        <p>{{ selectedRequest.description }}</p>
        
        <h5 class="mt-4" v-if="selectedRequest.special_requests">Demandes particulières</h5>
        <p v-if="selectedRequest.special_requests">{{ selectedRequest.special_requests }}</p>
      </div>
    </b-modal>
    
    <b-modal id="message-details-modal" title="Message" hide-footer>
      <div v-if="selectedMessage">
        <p><strong>Date:</strong> {{ formatDate(selectedMessage.created_at) }}</p>
        <p><strong>Sujet:</strong> {{ selectedMessage.subject }}</p>
        
        <h5 class="mt-4">Message</h5>
        <p>{{ selectedMessage.content }}</p>
      </div>
    </b-modal>
  </div>
</template>

<script>
export default {
  middleware: 'auth',
  data() {
    return {
      activeTab: 'profile',
      isUpdating: false,
      profile: {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        address: '',
        postalCode: '',
        city: ''
      },
      orders: [],
      platterRequests: [],
      messages: [],
      selectedOrder: null,
      selectedRequest: null,
      selectedMessage: null,
      orderFields: [
        { key: 'id', label: 'N°' },
        { key: 'created_at', label: 'Date', formatter: this.formatDate },
        { key: 'total_amount', label: 'Montant', formatter: value => `${value.toFixed(2)} €` },
        { key: 'status', label: 'Statut' },
        { key: 'actions', label: 'Actions' }
      ],
      orderItemFields: [
        { key: 'name', label: 'Produit' },
        { key: 'quantity', label: 'Quantité' },
        { key: 'price', label: 'Prix unitaire', formatter: value => `${value.toFixed(2)} €` },
        { key: 'total', label: 'Total', formatter: value => `${value.toFixed(2)} €` }
      ],
      requestFields: [
        { key: 'id', label: 'N°' },
        { key: 'created_at', label: 'Date', formatter: this.formatDate },
        { key: 'guests_count', label: 'Personnes' },
        { key: 'status', label: 'Statut' },
        { key: 'actions', label: 'Actions' }
      ],
      messageFields: [
        { key: 'subject', label: 'Sujet' },
        { key: 'created_at', label: 'Date', formatter: this.formatDate },
        { key: 'is_read', label: 'Statut' },
        { key: 'actions', label: 'Actions' }
      ]
    }
  },
  created() {
    this.loadUserData();
    this.loadOrders();
    this.loadPlatterRequests();
    this.loadMessages();
  },
  methods: {
    formatDate(value) {
      if (!value) return '';
      const date = new Date(value);
      return date.toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit', year: 'numeric' });
    },
    getOrderStatusVariant(status) {
      const variants = {
        'pending': 'warning',
        'confirmed': 'info',
        'shipped': 'primary',
        'delivered': 'success',
        'cancelled': 'danger'
      };
      return variants[status] || 'secondary';
    },
    getRequestStatusVariant(status) {
      const variants = {
        'pending': 'warning',
        'approved': 'info',
        'completed': 'success',
        'cancelled': 'danger'
      };
      return variants[status] || 'secondary';
    },
    async loadUserData() {
      try {
        // Dans un vrai projet, ces données viendraient de l'API
        // Ici, on simule avec les données de l'utilisateur connecté
        const user = this.$auth.user;
        this.profile = {
          firstName: user.first_name,
          lastName: user.last_name,
          email: user.email,
          phone: user.phone || '',
          address: user.address || '',
          postalCode: user.postal_code || '',
          city: user.city || ''
        };
      } catch (error) {
        console.error('Erreur lors du chargement des données utilisateur:', error);
      }
    },
    async updateProfile() {
      try {
        this.isUpdating = true;
        
        // Simuler une requête API
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        this.$bvToast.toast('Vos informations ont été mises à jour avec succès.', {
          title: 'Profil mis à jour',
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
        this.isUpdating = false;
      }
    },
    async loadOrders() {
      // Simuler le chargement des commandes
      this.orders = [
        {
          id: 1001,
          created_at: '2024-03-15',
          total_amount: 45.80,
          status: 'delivered',
          items: [
            { name: 'Comté AOP 18 mois', quantity: 0.5, price: 29.90, total: 14.95 },
            { name: 'Roquefort AOP', quantity: 0.4, price: 32.50, total: 13.00 },
            { name: 'Tomme de Savoie', quantity: 0.7, price: 24.80, total: 17.36 }
          ]
        },
        {
          id: 1002,
          created_at: '2024-03-10',
          total_amount: 39.90,
          status: 'delivered',
          items: [
            { name: 'Plateau Tradition', quantity: 1, price: 39.90, total: 39.90 }
          ]
        }
      ];
    },
    async loadPlatterRequests() {
      // Simuler le chargement des demandes de plateaux
      this.platterRequests = [
        {
          id: 501,
          created_at: '2024-03-12',
          guests_count: 8,
          budget: 10,
          status: 'completed',
          description: 'Plateau pour un anniversaire avec des fromages variés.',
          special_requests: 'Si possible, inclure un fromage de chèvre doux.'
        }
      ];
    },
    async loadMessages() {
      // Simuler le chargement des messages
      this.messages = [
        {
          id: 201,
          subject: 'Demande d\'information sur le Comté',
          content: 'Bonjour, j\'aimerais savoir si vous proposez différents âges d\'affinage pour le Comté. Merci d\'avance pour votre réponse.',
          created_at: '2024-03-14',
          is_read: true
        },
        {
          id: 202,
          subject: 'Confirmation de commande',
          content: 'Votre commande #1002 a été confirmée et sera préparée pour le retrait en boutique demain.',
          created_at: '2024-03-10',
          is_read: true
        }
      ];
    },
    viewOrder(order) {
      this.selectedOrder = order;
      this.$bvModal.show('order-details-modal');
    },
    viewRequest(request) {
      this.selectedRequest = request;
      this.$bvModal.show('request-details-modal');
    },
    viewMessage(message) {
      this.selectedMessage = message;
      this.$bvModal.show('message-details-modal');
    },
    async logout() {
      await this.$auth.logout();
      this.$router.push('/');
    }
  },
  head() {
    return {
      title: 'Mon Compte - Fromagerie du Baou'
    }
  }
}
</script>
