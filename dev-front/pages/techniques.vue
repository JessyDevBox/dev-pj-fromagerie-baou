<template>
  <div>
    <div class="page-header bg-light py-5">
      <b-container>
        <h1>Les Techniques</h1>
        <p class="lead">Découvrez les secrets de fabrication et d'affinage des fromages</p>
      </b-container>
    </div>

    <b-container class="py-5">
      <b-row class="mb-5">
        <b-col lg="8" class="mx-auto">
          <b-card no-body>
            <b-tabs card>
              <b-tab title="Fabrication" active>
                <b-card-text>
                  <h3 class="mb-4">Les étapes de fabrication du fromage</h3>
                  
                  <div class="mb-4">
                    <h4>1. Le caillage</h4>
                    <p>
                      Le caillage est la première étape de la transformation du lait en fromage. 
                      Il consiste à faire coaguler le lait pour obtenir un caillé solide. 
                      Cette coagulation peut être obtenue de deux façons :
                    </p>
                    <ul>
                      <li><strong>Coagulation lactique</strong> : sous l'action des ferments lactiques qui transforment le lactose en acide lactique.</li>
                      <li><strong>Coagulation présure</strong> : sous l'action d'enzymes (présure) qui provoquent la coagulation rapide des protéines du lait.</li>
                    </ul>
                  </div>
                  
                  <div class="mb-4">
                    <h4>2. L'égouttage</h4>
                    <p>
                      L'égouttage permet de séparer le caillé (partie solide) du lactosérum (partie liquide).
                      Cette étape détermine la texture finale du fromage. Un égouttage rapide donnera un fromage
                      plus sec, tandis qu'un égouttage lent conservera plus d'humidité.
                    </p>
                  </div>
                  
                  <div class="mb-4">
                    <h4>3. Le moulage</h4>
                    <p>
                      Le caillé égoutté est placé dans des moules qui donneront au fromage sa forme définitive.
                      Selon les fromages, le caillé peut être découpé, brassé ou pressé avant d'être moulé.
                    </p>
                  </div>
                  
                  <div class="mb-4">
                    <h4>4. Le salage</h4>
                    <p>
                      Le salage a plusieurs fonctions : il complète l'égouttage, participe à la formation de la croûte,
                      et apporte du goût. Il peut se faire par frottage de la surface, par immersion dans un bain de saumure,
                      ou par incorporation directe du sel dans le caillé.
                    </p>
                  </div>
                  
                  <div>
                    <h4>5. L'affinage</h4>
                    <p>
                      L'affinage est l'étape finale qui permet au fromage de développer ses arômes et sa texture caractéristiques.
                      Sa durée varie de quelques jours à plusieurs années selon les types de fromages.
                    </p>
                  </div>
                </b-card-text>
              </b-tab>
              
              <b-tab title="Affinage">
                <b-card-text>
                  <h3 class="mb-4">L'art de l'affinage</h3>
                  
                  <p>
                    L'affinage est une étape cruciale dans la fabrication du fromage. C'est durant cette période que le fromage
                    développe ses arômes, ses saveurs et sa texture caractéristiques. L'affineur est un véritable artisan qui
                    surveille et accompagne cette maturation.
                  </p>
                  
                  <div class="mb-4">
                    <h4>Les conditions d'affinage</h4>
                    <p>
                      L'affinage se déroule dans des caves ou des hâloirs où plusieurs paramètres sont contrôlés :
                    </p>
                    <ul>
                      <li><strong>La température</strong> : généralement entre 8°C et 15°C selon les fromages.</li>
                      <li><strong>L'humidité</strong> : entre 85% et 95% pour favoriser le développement des flores de surface.</li>
                      <li><strong>La ventilation</strong> : pour maintenir une atmosphère saine et homogène.</li>
                    </ul>
                  </div>
                  
                  <div class="mb-4">
                    <h4>Les soins pendant l'affinage</h4>
                    <p>
                      Pendant l'affinage, les fromages reçoivent des soins réguliers :
                    </p>
                    <ul>
                      <li><strong>Le retournement</strong> : pour assurer un affinage homogène.</li>
                      <li><strong>Le brossage</strong> : pour éliminer les moisissures indésirables.</li>
                      <li><strong>Le lavage</strong> : pour certains fromages, un lavage à l'eau salée ou à la bière favorise le développement d'une croûte orangée caractéristique (Munster, Epoisses...).</li>
                      <li><strong>Le piquage</strong> : pour les fromages à pâte persillée, afin de permettre à l'air d'entrer et au Penicillium de se développer.</li>
                    </ul>
                  </div>
                  
                  <div class="mb-4">
                    <h4>La durée d'affinage</h4>
                    <p>
                      La durée d'affinage varie considérablement selon les types de fromages :
                    </p>
                    <ul>
                      <li><strong>Fromages frais</strong> : pas d'affinage ou quelques jours seulement (fromage blanc, faisselle).</li>
                      <li><strong>Fromages à pâte molle</strong> : de 2 à 6 semaines (Camembert, Brie).</li>
                      <li><strong>Fromages à pâte pressée non cuite</strong> : de 2 à 3 mois (Tomme, Saint-Nectaire).</li>
                      <li><strong>Fromages à pâte pressée cuite</strong> : de 6 mois à plusieurs années (Comté, Beaufort).</li>
                      <li><strong>Fromages à pâte persillée</strong> : de 3 à 6 mois (Roquefort, Bleu d'Auvergne).</li>
                    </ul>
                  </div>
                </b-card-text>
              </b-tab>
              
              <b-tab title="Types de fromages">
                <b-card-text>
                  <h3 class="mb-4">Les grandes familles de fromages</h3>
                  
                  <div class="mb-4">
                    <h4>Fromages frais</h4>
                    <p>
                      Les fromages frais sont des fromages non affinés, consommés rapidement après leur fabrication.
                      Ils sont caractérisés par une texture molle, une saveur douce et légèrement acidulée.
                    </p>
                    <p><strong>Exemples</strong> : Fromage blanc, Faisselle, Petit-suisse, Brousse</p>
                  </div>
                  
                  <div class="mb-4">
                    <h4>Fromages à pâte molle à croûte fleurie</h4>
                    <p>
                      Ces fromages sont caractérisés par une croûte blanche duveteuse formée par le développement
                      du Penicillium candidum. Leur pâte est souple et crémeuse.
                    </p>
                    <p><strong>Exemples</strong> : Camembert, Brie, Chaource, Coulommiers</p>
                  </div>
                  
                  <div class="mb-4">
                    <h4>Fromages à pâte molle à croûte lavée</h4>
                    <p>
                      Ces fromages sont régulièrement lavés pendant l'affinage avec de l'eau salée, parfois
                      additionnée d'alcool. Leur croûte est orangée et leur odeur souvent prononcée.
                    </p>
                    <p><strong>Exemples</strong> : Munster, Epoisses, Maroilles, Livarot</p>
                  </div>
                  
                  <div class="mb-4">
                    <h4>Fromages à pâte pressée non cuite</h4>
                    <p>
                      Pour ces fromages, le caillé est pressé pour éliminer le lactosérum, mais n'est pas chauffé.
                      Leur texture est souple à ferme et leur goût varie de doux à corsé selon la durée d'affinage.
                    </p>
                    <p><strong>Exemples</strong> : Tomme de Savoie, Saint-Nectaire, Cantal, Morbier</p>
                  </div>
                  
                  <div class="mb-4">
                    <h4>Fromages à pâte pressée cuite</h4>
                    <p>
                      Le caillé de ces fromages est chauffé (entre 50°C et 55°C) avant d'être pressé.
                      Ce sont des fromages à longue durée d'affinage, à pâte ferme et aux arômes complexes.
                    </p>
                    <p><strong>Exemples</strong> : Comté, Beaufort, Emmental, Gruyère</p>
                  </div>
                  
                  <div class="mb-4">
                    <h4>Fromages à pâte persillée</h4>
                    <p>
                      Ces fromages sont caractérisés par le développement de moisissures bleues (Penicillium roqueforti)
                      à l'intérieur de la pâte, créant des veines bleues-vertes. Leur goût est généralement prononcé.
                    </p>
                    <p><strong>Exemples</strong> : Roquefort, Bleu d'Auvergne, Fourme d'Ambert, Bleu des Causses</p>
                  </div>
                  
                  <div>
                    <h4>Fromages de chèvre</h4>
                    <p>
                      Fabriqués à partir de lait de chèvre, ces fromages peuvent appartenir à différentes familles
                      (frais, pâte molle, pâte pressée). Ils sont reconnaissables à leur goût caractéristique.
                    </p>
                    <p><strong>Exemples</strong> : Crottin de Chavignol, Sainte-Maure de Touraine, Picodon, Rocamadour</p>
                  </div>
                </b-card-text>
              </b-tab>
              
              <b-tab title="Conservation">
                <b-card-text>
                  <h3 class="mb-4">Comment bien conserver vos fromages</h3>
                  
                  <div class="mb-4">
                    <h4>Principes généraux</h4>
                    <p>
                      Pour préserver au mieux les qualités organoleptiques de vos fromages,
                      voici quelques principes essentiels à respecter :
                    </p>
                    <ul>
                      <li>Conserver les fromages entre 4°C et 8°C, dans le bac à légumes du réfrigérateur (zone la moins froide et la plus humide).</li>
                      <li>Éviter les variations de température qui accélèrent le développement bactérien.</li>
                      <li>Protéger les fromages du dessèchement tout en leur permettant de "respirer".</li>
                      <li>Séparer les fromages à forte odeur des autres aliments et des autres fromages.</li>
                      <li>Sortir les fromages du réfrigérateur 30 minutes à 1 heure avant dégustation pour qu'ils développent tous leurs arômes.</li>
                    </ul>
                  </div>
                  
                  <div class="mb-4">
                    <h4>Conservation par type de fromage</h4>
                    <ul>
                      <li><strong>Fromages frais</strong> : à conserver dans leur emballage d'origine, à consommer rapidement (3-4 jours).</li>
                      <li><strong>Fromages à pâte molle</strong> : à conserver dans du papier sulfurisé ou du papier d'emballage spécial fromage, à changer régulièrement (durée de conservation : 1-2 semaines).</li>
                      <li><strong>Fromages à pâte pressée</strong> : à conserver dans du papier sulfurisé ou une boîte hermétique (durée de conservation : 2-3 semaines).</li>
                      <li><strong>Fromages à pâte persillée</strong> : à envelopper dans du papier aluminium pour maintenir l'humidité (durée de conservation : 1-2 semaines).</li>
                    </ul>
                  </div>
                  
                  <div class="mb-4">
                    <h4>Conseils pratiques</h4>
                    <ul>
                      <li>Utilisez une cloche à fromage pour conserver vos fromages à température ambiante pendant une courte durée.</li>
                      <li>Ne jetez pas la croûte des fromages à pâte dure, elle peut être utilisée pour parfumer soupes et sauces.</li>
                      <li>Si un fromage présente des moisissures non désirées, grattez simplement la partie affectée (sauf pour les fromages frais qu'il faut jeter).</li>
                      <li>Pour les fromages à pâte molle qui commencent à couler, placez-les dans une petite boîte pour éviter qu'ils ne contaminent les autres aliments.</li>
                      <li>Les fromages à pâte pressée peuvent être congelés, mais cela peut altérer légèrement leur texture.</li>
                    </ul>
                  </div>
                </b-card-text>
              </b-tab>
            </b-tabs>
          </b-card>
        </b-col>
      </b-row>

      <!-- Vidéo explicative -->
      <b-row class="my-5">
        <b-col lg="8" class="mx-auto">
          <h3 class="text-center mb-4">Vidéo : La fabrication du fromage</h3>
          <div class="embed-responsive embed-responsive-16by9">
            <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/example" allowfullscreen></iframe>
          </div>
        </b-col>
      </b-row>

      <!-- Infographie -->
      <b-row class="my-5">
        <b-col lg="10" class="mx-auto">
          <h3 class="text-center mb-4">Les étapes de fabrication du fromage</h3>
          <b-img src="/images/cheese-making-process.jpg" fluid alt="Processus de fabrication du fromage"></b-img>
        </b-col>
      </b-row>

      <!-- FAQ -->
      <b-row class="my-5">
        <b-col lg="8" class="mx-auto">
          <h3 class="text-center mb-4">Questions fréquentes</h3>
          
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-button block variant="light" v-b-toggle.accordion-1>
                Quelle est la différence entre un fromage au lait cru et un fromage au lait pasteurisé ?
              </b-button>
            </b-card-header>
            <b-collapse id="accordion-1" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <p>
                  Un fromage au lait cru est fabriqué avec du lait qui n'a pas subi de traitement thermique,
                  conservant ainsi toute sa flore microbienne naturelle. Cela permet de développer des arômes
                  plus complexes et une typicité liée au terroir.
                </p>
                <p>
                  Un fromage au lait pasteurisé est fabriqué avec du lait chauffé à haute température pour
                  éliminer les bactéries potentiellement pathogènes. Ce traitement détruit également une partie
                  de la flore naturelle, ce qui peut réduire la complexité aromatique du fromage, mais garantit
                  une meilleure sécurité sanitaire et une production plus standardisée.
                </p>
              </b-card-body>
            </b-collapse>
          </b-card>
          
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-button block variant="light" v-b-toggle.accordion-2>
                Peut-on manger la croûte des fromages ?
              </b-button>
            </b-card-header>
            <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <p>
                  La comestibilité de la croûte dépend du type de fromage :
                </p>
                <ul>
                  <li><strong>Croûtes fleuries</strong> (Camembert, Brie) : comestibles et participent à l'expérience gustative.</li>
                  <li><strong>Croûtes lavées</strong> (Munster, Epoisses) : comestibles mais au goût prononcé qui ne plaît pas à tous.</li>
                  <li><strong>Croûtes naturelles</strong> (Tomme, Saint-Nectaire) : comestibles mais peuvent avoir un goût terreux.</li>
                  <li><strong>Croûtes artificielles</strong> (cire, paraffine) : non comestibles, à retirer avant consommation.</li>
                  <li><strong>Croûtes traitées</strong> (avec des conservateurs) : mieux vaut les éviter.</li>
                </ul>
                <p>
                  En cas de doute, n'hésitez pas à nous demander conseil en boutique !
                </p>
              </b-card-body>
            </b-collapse>
          </b-card>
          
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-button block variant="light" v-b-toggle.accordion-3>
                Comment composer un bon plateau de fromages ?
              </b-button>
            </b-card-header>
            <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <p>
                  Pour un plateau équilibré, voici quelques conseils :
                </p>
                <ul>
                  <li>Prévoir environ 100g de fromage par personne pour un repas, 50g pour un apéritif.</li>
                  <li>Varier les familles de fromages : un fromage frais, un à pâte molle, un à pâte pressée, un bleu, un chèvre.</li>
                  <li>Varier les laits : vache, chèvre, brebis.</li>
                  <li>Varier les intensités gustatives, en commençant la dégustation par les plus doux pour finir par les plus forts.</li>
                  <li>Prévoir 3 à 5 fromages pour un plateau classique, jusqu'à 7 pour une occasion spéciale.</li>
                  <li>Accompagner de pain de campagne, fruits frais ou secs, miel, confiture ou chutney.</li>
                </ul>
                <p>
                  N'hésitez pas à consulter notre page <b-link to="/plateaux">Plateaux</b-link> pour découvrir nos suggestions !
                </p>
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
  head() {
    return {
      title: 'Techniques de fabrication - Fromagerie du Baou'
    }
  }
}
</script>
