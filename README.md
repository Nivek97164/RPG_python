# RPG_python
Projet RPG python
2022/2023
Sujet :
Vous devez créer un jeu de type RPG retro-style au tour par tour sur console.
Voici le synopsis : « Votre nom est Bob. Vous vous réveillez au milieu d’une forêt avec un sac ne contenant qu’un seul objet : un
couteau. Vous devrez gagner de l’XP et récupérer de nouvelles armes pour devenir plus fort et battre le boss pour sortir de la forêt. »
Voici comment marche le jeu :
Le jeu commence avec un menu comme ci-dessous (l’option « Load Saved Game » Ne peut pas fonctionner sur Colab) :
En commençant le jeu, on doit écrire son nom.
On contrôle le jeu en tapant les commandes : « Go East », « Go North », « Go West » ou « Go South » (ou des textes plus simples).
Quand on arrive sur un nouvel endroit, on a une description du lieu. Aléatoirement, on peut soit se faire attaquer par un monstre et
passer en mode combat, soit trouver un objet.
La map ne doit pas être générée aléatoirement et le placement du boss est défini dans le code. Evidemment, pas de notion d’aléatoire
(combats ou objets) sur le lieu de départ ou celui du boss.
Une fois le boss vaincu le jeu, ou que le personnage n’a plu de vie, le jeu s’arrête en affichant le message correspondant et en revenant
au menu principal. Le joueur peut aussi quitter le jeu à tout moment et revenir au menu principal.
Le personnage a de la vie, des compétences d’attaque et de défense. A chaque combat gagné, il gagne de l’XP pour gagner un niveau
(plus le niveau est suivant est élevé, plus il y a besoin d’XP pour l’atteindre). Quand il gagne un niveau ses autres caractéristiques
augmentent (HP, Attaque et Défense).
Les monstres ont aussi un niveau, du HP, des compétences d’attaque et de défense. Plus le niveau est élevé, plus ses caractéristiques le
sont aussi. Le plus fort étant le boss.
Mode combat :
On commence par indiquer le nom et le niveau du monstre à affronter.
Puis on peut attaquer, utiliser un objet de l’inventaire ou courir pour échapper au combat (mais ne rien gagner).
L’attaque du personnage cause un nombre de dommage dépendant des compétences d’attaque du personnage et des compétences de
défense du monstre (et inversement quand le monstre attaque). Il y a aussi une chance aléatoire (à définir) que l’attaque manque ou
que l’attaque cause un coup critique (Optionnel).
Les objets dans l’inventaire sont ceux que l’on peut ramasser (Potions, Attack Boost ou Defense Boost). Une fois utilisé, il est supprimé
de l’inventaire. La potion permet de regagner de la vie, et l’Attack Boost et le Defense Boost augmentent les caractéristiques pendant la
durée du combat. On peut revenir en arrière s’il ne veut finalement pas utiliser d’objets mais attaquer.
On ne peut utiliser qu’une action à chaque tour (attaque ou objet). Puis le monstre attaque et ainsi de suite jusqu’à que l’un des deux
n’ai plus de vie.

## Installation :

`make install`
## Lancement du programme :

`make run`
