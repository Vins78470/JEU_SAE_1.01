>CARRET Vincent et MAROUAN Hazim-Rayan
# Compte rendu - Projet ESN Wars


# Sommaire

1. [Introduction](#introduction)
2. [Répartition du Travail](#Répartition-du-Travail)
3. [Difficultés Rencontrées](#difficultés-rencontrées)
4. [Les idées Novatrices](#Les-idées-Novatrices )
5. [Architecture du Code](#architecture-du-code)
    - [Classes Principales](#classes-principales)
    - [Fonctionnalités principales](#fonctionnalités-principales)
    - [Interaction et fonctionnement](#interaction-et-fonctionnement)
6. [Améliorations Futures](#améliorations-futures)
7. [Conclusion](#conclusion)

## Introduction
Dans un premier temps, nous avons décomposé le lancement du jeu en deux parties distinctes. Afin d'initier le jeu, nous devons ajuster les paramètres de la fonction Play(), lesquels comprennent les attributs game et mode. L'utilisation du mode 0 permet de lancer le jeu dans le terminal, tandis que le mode 1 est réservé au lancement du jeu dans l'interface graphique. L'appel de la fonction se trouve à la fin du fichier principal. Enfin, pour débuter le jeu, il est nécessaire d'être situé dans le fichier principal.

## Répartition du Travail 

Tout d'abord, Vincent et moi-même ne disposons pas du même niveau en Python. C'est pourquoi il a décidé de m'accompagner dans le projet et de prendre le temps de m'expliquer de nouvelles notions, notamment la programmation orientée objet. J'ai créé quelques classes avec leurs objets et réalisé la mise en place de certaines fonctions. Néanmoins, Vincent a réalisé la majeure partie du travail. J'ai beaucoup appris à travers les enseignements de Vincent, tels que la création du tableau de jeu (Board), les déplacements, et bien d'autres aspects.

Je tiens à être le plus honnête possible en ce qui concerne mon travail et ma contribution.

## Difficultés Rencontrées

**Adaptation du code en objets** : Lors du développement initial, une partie du jeu a été construite sans utiliser la programmation orientée objet (POO). Cependant, lorsqu'on a envisagé d'ajouter une interface graphique, on a réalisé qu'il était nécessaire de restructurer tout le code en utilisant des objets pour permettre une meilleure intégration de cette nouvelle fonctionnalité.

**Transition de la console à l'interface graphique** : La transition de la version console à une version avec une interface graphique a été particulièrement difficile. La logique de jeu conçue pour la console devait être revue entièrement pour s'adapter à l'interface graphique. Cela a impliqué des changements significatifs dans la gestion des interactions et de l'affichage.

**Complexité de la conversion** : La complexité de cette conversion était notable. Passer du mode console au mode graphique a requis une refonte totale de la structure et de l'organisation du code. Séparer les éléments visuels de la logique du jeu, ainsi que mettre en place une communication efficace entre ces deux parties, a représenté un défi technique de taille.

## Les idées Novatrices 

Nous nous sommes inspirés du jeu d'échecs pour créer un tableau (Board) avec des lettres en abscisse et des numéros en ordonnée, facilitant ainsi la repérage du joueur dans le tableau. De plus, dans la partie graphique, nous avons ajouté des boutons "Améliorer l'énergie maximale" et "Améliorer le niveau de coding" pour permettre au joueur de jouer sans avoir à utiliser le terminal.

![Alt text](image.png)

## Architecture du Code


#### Classes Principales

- **Coder** : Cette classe représente les joueurs du jeu. Elle contient des attributs tels que le symbole du joueur, sa position sur la carte, son niveau de codage, son énergie, et son argent. Des méthodes sont définies pour les actions possibles par le joueur : se déplacer, améliorer son niveau, ou encore gérer son énergie et son argent.

- **Mission** : Représente les missions disponibles dans le jeu. Chaque mission a un symbole, un niveau de difficulté, un travail initial à réaliser, et un travail restant à effectuer. Des méthodes permettent de gérer l'état de la mission (disponible ou non), de la redessiner, de la réinitialiser, et d'effectuer des modifications sur son travail restant.
  
- **Configuration** : Gère la lecture et l'écriture des données à partir de fichiers, permettant une configuration flexible du jeu.
  
- **Game** : Ce module gère la logique du jeu en utilisant les classes Coder et Mission. Il initialise le jeu, gère le déroulement des tours, les interactions entre les joueurs et les missions, et détecte les conditions de fin de jeu.
  
- **Partie Graphique** : Responsable de l'interface graphique du jeu. Cette partie inclut les éléments nécessaires à la création de la fenêtre de jeu, au dessin du plateau, et à la gestion des événements graphiques (clics, mouvements de souris, etc.).
  
- **Rules** : Ce module définit les règles du jeu et les validations des actions des joueurs. Il contient des fonctions de vérification, telles que la validation du nombre de joueurs choisis, du niveau de difficulté, ou encore la validation des déplacements et des actions des joueurs.
  
- **TestUnitaire** : Ce dossier contient les tests unitaires pour valider le bon fonctionnement de chaque classe et de leurs méthodes respectives.

Chaque classe correspond à un aspect spécifique du jeu, ce qui permet une organisation claire et une gestion modulaire du code. Les fichiers associés à ces classes facilitent la maintenance, les tests et l'extension du jeu, assurant ainsi une base solide pour son développement.


## Fonctionnalités principales

**Règles logiques du jeu** : La classe `Rules` contient l'ensemble des règles logiques du jeu, dictant les actions permises, les conditions de victoire ou de fin de partie, ainsi que la validation des actions des joueurs.

**Initialisation du plateau** : Lors du lancement du jeu, une carte ou un plateau est généré(e) et affiché(e), montrant les positions des joueurs et des missions.

**Actions des joueurs** : Les joueurs peuvent se déplacer, améliorer leurs compétences, prendre des missions, les accomplir et gagner des récompenses. Les actions disponibles dépendent des ressources et de la position du joueur.

**Gestion des missions** : Les missions apparaissent à des emplacements spécifiques, elles ont des objectifs et des difficultés. Les joueurs peuvent les prendre, les réaliser, et gagner des récompenses en fonction de leur niveau de difficulté.

**Détection de fin de jeu** : Le jeu se termine lorsqu'un joueur atteint 5000 bitcoins

**Fonctionnement de la console ou de l'interface graphique** : Chaque mode offre une expérience de jeu différente mais suit la même logique de fonctionnement et les mêmes règles.

**Organisation du code** :

- **Classe par classe** : Chaque classe possède ses propres attributs et méthodes spécifiques définissant ses actions et ses interactions avec les autres classes.
  
- **Fonctions principales** : Les fonctions centrales gèrent les principaux mécanismes du jeu, telles que l'initialisation, le déroulement des tours, la validation des actions, etc.
  
- **Interactions entre classes** : Les classes communiquent entre elles pour permettre le fonctionnement du jeu. Par exemple, les actions des joueurs peuvent affecter l'état des missions, ou les actions des missions peuvent modifier l'état des joueurs.


## Interaction et fonctionnement

**Console vs. Interface graphique** : L'application peut être exécutée en mode console, où les actions et le suivi du jeu se font via des commandes textuelles, ou bien via une interface graphique où le jeu est représenté visuellement.

**Initialisation du jeu** : Lorsque le jeu démarre, les paramètres tels que le nombre de joueurs, le niveau de difficulté, et le nombre de missions sont définis. La carte de jeu est initialisée en fonction de ces paramètres.

**Déroulement du jeu** : Le jeu avance tour par tour, chaque joueur effectue ses actions (se déplacer, améliorer son niveau, réaliser des missions, etc.) selon les règles établies. Les missions peuvent apparaître ou disparaître, et les joueurs gagnent ou perdent en fonction de leurs actions.

**Logique des actions** : Chaque action (déplacement, amélioration, réalisation de mission) a des conséquences sur l'état du jeu et sur les ressources des joueurs. Ces actions sont validées selon les règles prédéfinies.

**Gestion des missions** : Les missions sont créées aléatoirement au début du jeu. Leurs positions et leurs niveaux de difficulté sont définis. À mesure que les joueurs interagissent avec elles, leurs états changent et les missions peuvent être accomplies ou indisponible.

**Tests unitaires** : Ces tests garantissent que chaque classe et chaque méthode fonctionnent correctement et produisent les résultats attendus.


### Gestion des Missions et de la Carte :
 Cela inclut la distribution des missions sur la carte, le suivi de leur progression, ainsi que la gestion de la carte du jeu (sa structure, ses limites, etc.).

#### Mécaniques du Jeu : 
Comprend les règles spécifiques régissant les actions possibles des joueurs, telles que les mouvements des coders, la réalisation des missions, la gestion de l'énergie, et la fin de la partie.

#### Partie Interface Graphique
Affichage de la Carte : Gère l'affichage visuel de la grille, des coders, des missions et de tout élément interactif sur la fenêtre de jeu.

#### Interactions Utilisateur : 
Réagit aux actions de l'utilisateur, telles que les déplacements de coder, les améliorations, et les sélections d'actions à effectuer pendant le tour.

#### Rafraîchissement et Actualisation :
 S'occupe de mettre à jour l'interface graphique pour refléter les changements dans la partie logique, assurant ainsi la cohérence entre la représentation visuelle et l'état actuel du jeu.

Cette architecture séparée entre la partie logique et l'interface graphique permet une meilleure gestion du jeu, facilite les tests et les modifications ultérieures, et rend l'ensemble du code plus modulaire et compréhensible.

## Difficultés Rencontrées

**Adaptation du code en objets** : Lors du développement initial, une partie du jeu a été construite sans utiliser la programmation orientée objet (POO). Cependant, lorsqu'on a envisagé d'ajouter une interface graphique, on a réalisé qu'il était nécessaire de restructurer tout le code en utilisant des objets pour permettre une meilleure intégration de cette nouvelle fonctionnalité.

**Transition de la console à l'interface graphique** : La transition de la version console à une version avec une interface graphique a été particulièrement difficile. La logique de jeu conçue pour la console devait être revue entièrement pour s'adapter à l'interface graphique. Cela a impliqué des changements significatifs dans la gestion des interactions et de l'affichage.

**Complexité de la conversion** : La complexité de cette conversion était notable. Passer du mode console au mode graphique a requis une refonte totale de la structure et de l'organisation du code. Séparer les éléments visuels de la logique du jeu, ainsi que mettre en place une communication efficace entre ces deux parties, a représenté un défi technique de taille.


## Conclusion
"ESN Wars" a été une aventure riche en enseignements, nous plongeant au cœur de la programmation orientée objet. La transition de la logique console à une interface graphique a été un véritable défi, mais surtout une opportunité d'apprentissage majeure.

Cette expérience nous a permis de saisir l'importance de la modularité, de l'encapsulation et de l'abstraction dans la conception de logiciels complexes. La refonte totale du code pour intégrer l'interface graphique nous a poussés à repenser notre approche du développement logiciel. Ce processus a été bien plus qu'une simple transformation technique : il a été une leçon, nous montrant l'importance de la planification minutieuse et de la flexibilité constante.

"ESN Wars" a été un véritable terrain d'expérimentation, nous offrant un aperçu passionnant des défis et des opportunités du développement logiciel moderne. Cette aventure nous a inculqué les bases essentielles de la programmation orientée objet et nous a offert des perspectives enrichissantes sur les rouages de la création de logiciels robustes et évolutifs.

Cette exploration approfondie de la POO a été un pilier majeur de notre expérience, nous donnant un aperçu tangible de ses applications concrètes dans le développement de jeux et d'applications interactives.
