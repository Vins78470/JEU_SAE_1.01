>CARRET Vincent et MAROUAN Hazim-Rayan
# Compte rendu - Projet ESN Wars


# Sommaire

1. [Introduction](#introduction)
2. [Répartition du Travail](#Répartition-du-Travail)
3. [Difficultés Rencontrées](#difficultés-rencontrées)
4. [Les idées Novatrices](#Les-idées-Novatrices)
5. [Architecture du Code](#architecture-du-code)
    - [Classes Principales](#classes-principales)
6. [Conclusion](#conclusion)

## Introduction
Dans un premier temps, nous avons décomposé le lancement du jeu en deux parties distinctes. Afin d'initier le jeu, nous devons ajuster les paramètres de la fonction Play(), lesquels comprennent les attributs game et mode. L'utilisation du mode 0 permet de lancer le jeu dans le terminal, tandis que le mode 1 est réservé au lancement du jeu dans l'interface graphique. L'appel de la fonction se trouve à la fin du fichier principal. Enfin, pour débuter le jeu, il est nécessaire d'être situé dans le fichier principal ( Main.py).

## Répartition du Travail

Tout d'abord, Vincent et moi-même ne disposons pas du même niveau en Python. C'est pourquoi il a décidé de m'accompagner dans le projet et de prendre le temps de m'expliquer de nouvelles notions, notamment la programmation orientée objet. J'ai créé quelques classes avec leurs objets et réalisé la mise en place de certaines fonctions. Néanmoins, Vincent a réalisé la majeure partie du travail. J'ai beaucoup appris à travers les enseignements de Vincent, tels que la création du tableau de jeu (Board), les déplacements, et bien d'autres aspects.

Nous tenons à être les plus honnêtes possible en ce qui concerne la répartition du travail.


## Difficultés Rencontrées

**Adaptation du code en objets** : Lors du développement initial, une partie du jeu a été construite sans utiliser la programmation orientée objet (POO). Cependant, lorsqu'on a envisagé d'ajouter une interface graphique, on a réalisé qu'il était nécessaire de restructurer tout le code en utilisant des objets pour permettre une meilleure intégration de cette nouvelle fonctionnalité.

**Transition de la console à l'interface graphique** : La transition de la version console à une version avec une interface graphique a été particulièrement difficile. La logique de jeu conçue pour la console devait être revue entièrement pour s'adapter à l'interface graphique. Cela a impliqué des changements significatifs dans la gestion des interactions et de l'affichage.

**Complexité de la conversion** : La complexité de cette conversion était notable. Passer du mode console au mode graphique a requis une refonte totale de la structure et de l'organisation du code. Séparer les éléments visuels de la logique du jeu, ainsi que mettre en place une communication efficace entre ces deux parties, a représenté un défi technique de taille.

## Les idées Novatrices 

Nous nous sommes inspirés du jeu d'échecs pour créer un tableau (Board) avec des lettres en abscisse et des numéros en ordonnée, facilitant ainsi la repérage du joueur dans le tableau. De plus, dans la partie graphique, nous avons ajouté des boutons "Améliorer l'énergie maximale" et "Améliorer le niveau de coding" pour permettre au joueur de jouer sans avoir à utiliser le terminal. Lorsque le mode graphique est activé, la fenêtre graphique et la console s'ouvrent simultanément. Les messages d'interaction destinés au joueur apparaissent dans la console. Par conséquent, il est essentiel de maintenir ouvertes les deux fenêtres pendant le jeu.  

## Architecture du Code


#### Classes Principales

- **Coder** : Cette classe représente les joueurs du jeu. Elle contient des attributs tels que le symbole du joueur, sa position sur la carte, son niveau de codage, son énergie, et son argent. Des méthodes sont définies pour les actions possibles par le joueur : se déplacer, améliorer son niveau, ou encore gérer son énergie et son argent.

- **Mission** : Représente les missions disponibles dans le jeu. Chaque mission à un symbole, un niveau de difficulté, un travail initial à réaliser, et un travail restant à effectuer. Des méthodes permettent de gérer l'état de la mission (disponible ou non), de la redessiner, de la réinitialiser, et d'effectuer des modifications sur son travail restant.
  
- **Configuration** : Gère la lecture et l'écriture des données à partir de fichiers, permettant une configuration flexible du jeu.
  
- **Game** : Ce module gère la logique du jeu en utilisant les classes Coder et Mission. Il initialise le jeu, gère le déroulement des tours, les interactions entre les joueurs et les missions, et détecte les conditions de fin de jeu.
  
- **Partie Graphique** : Responsable de l'interface graphique du jeu. Cette partie inclut les éléments nécessaires à la création de la fenêtre de jeu, au dessin du plateau, et à la gestion des événements graphiques.
  
- **Rules** : Ce module définit les règles du jeu et les validations des actions des joueurs. Il contient des fonctions de vérification, telles que la validation du nombre de joueurs choisis, du niveau de difficulté, ou encore la validation des déplacements et des actions des joueurs.
  
- **TestUnitaire** : Ce dossier contient les tests unitaires pour valider le bon fonctionnement de chaque classe et de leurs méthodes respectives.

Chaque classe correspond à un aspect spécifique du jeu, ce qui permet une organisation claire et une gestion modulaire du code. Les fichiers associés à ces classes facilitent la maintenance, les tests et l'extension du jeu, assurant ainsi une base solide pour son développement.


## Conclusion
"ESN Wars" a été une aventure riche en enseignements, nous plongeant au cœur de la programmation orientée objet. La transition de la logique console à une interface graphique a été un véritable défi, mais surtout une opportunité d'apprentissage majeure.

Cette expérience nous a permis de saisir l'importance de la modularité, de l'encapsulation et de l'abstraction dans la conception de logiciels complexes. La refonte totale du code pour intégrer l'interface graphique nous a poussés à repenser notre approche du développement logiciel. Ce processus a été bien plus qu'une simple transformation technique : il a été une leçon, nous montrant l'importance de la planification minutieuse et de la flexibilité constante.

"ESN Wars" a été un véritable terrain d'expérimentation, nous offrant un aperçu passionnant des défis et des opportunités du développement logiciel moderne. Cette aventure nous a inculqué les bases essentielles de la programmation orientée objet et nous a offert des perspectives enrichissantes sur les rouages de la création de logiciels robustes et évolutifs.

