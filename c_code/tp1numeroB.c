#include <stdarg.h>//entete etudiant:Gabriel Derome
#include <stdio.h>
#include <stdlib.h>
int main() {//principale
  char shape;//definition de variables
  char circle = 'c';
  char rectangle = 'r';
  char square = 'k';
  int choice;
  float maxperimetrec = 0.00;
  float maxairer = 0.00;
  float mincote = 0;
  int reccompte = 0;
  float sumperimetre = 0;
  while(1)//boucle
  {
    printf("tapez c pour cercle \ntapez r pour rectangle \ntapez k pour carre\n");//choix de la forme
    scanf("\n %c", &shape);
    if (shape == circle) {//CERCLE
      float rayon;//definition de variable
      printf("veuillez entrer le rayon du cercle: \n");//entre du rayon
      scanf("\n %f", &rayon);
      float airec = 3.14159 * rayon * rayon;//calculs
      float perimetrec = 3.14159 * 2 * rayon;
      if (perimetrec > maxperimetrec){//max perimetre?
         maxperimetrec = perimetrec;
      }
      printf("l'aire du cercle = %.2f\n", airec);//affichage des donnes
      printf("le perimetre du cercle = %.2f", perimetrec);                                                                 
    } else if (shape == rectangle) {//RECTANGLE
      float base;//definition de variables
      float hauteur;
      printf("veuillez entrer la hauteur puis, la base du rectangle\n");//entre de la base et de la hauteur
      scanf("\n %f", &base);
      scanf("\n %f", &hauteur);
      float airer = base * hauteur;//calculs
      float perimetrer = 2 * base + 2 * hauteur;
      printf("l'aire du rectangle= %2.f\n", airer);//affichage des donnes
      printf("le perimetre du rectangle = %2.f\n", perimetrer);                                                      
      reccompte = reccompte + 1;//compte de rectangles
      sumperimetre = sumperimetre + perimetrer;//sum des perimetres
      if (airer > maxairer){//max aire?
         maxairer = airer;
      }
    } else if (shape == square){//CARRE
      float cote;//definition de variable
      printf("veuillez entrer le cote du carre\n");//entre du cote
      scanf("\n %f", & cote);
      float airek = cote * cote;//calculs
      float perimetrek = cote * 4;
      printf("l'aire du carre= %2.f\n", airek);//affichage des donnes
      printf("le perimetre du carre= %2.f\n", perimetrek);
      if ((cote < mincote) || (mincote == 0)){//min cote?
         mincote = cote;
      }
    } else {//not a valid shape
      printf("entree invalide");
    }
    printf("\nAvez vous fini? 2 pour oui, 1 pour Non: ");//l'utilisateur veut-il continuer?          
    scanf("\n %d", &choice);
    if (choice == 2)                                            
    {
    break;//la boucle est boucle                                               
    }
  }
  float avgperi = sumperimetre / reccompte;//moyenne des perimetres
  printf("nombre de rectangle construit: %d\n", reccompte);//affichage d'info
  printf("le cercle avec le plus grand perimetre as un perimetre de: %.6f\n", maxperimetrec);
  printf("le rectangle avec la plus grande aire as une aire de: %.6f\n", maxairer);
  printf("le carre avec le plus petit cote avait un cote de: %.6f\n", mincote);
  printf("le perimetre moyen des rectangles: %2.f\n", avgperi);
  return 0;
}
// c1 
// 7.5 = rayon
// l'aire du cercle = 176.71
// le perimetre du cercle = 47.12

// r1
// 9.2 = hauteur
// 4.8 = base
// l'aire du rectangle= 44
// le perimetre du rectangle = 28

// c2
// 8.3 = rayon
// l'aire du cercle = 216.42
// le perimetre du cercle = 52.15

// r2
// 5.3 = hauteur
// 3.7 = base
// l'aire du rectangle= 20
// le perimetre du rectangle = 18

// c3
// 3.9 = rayon
// l'aire du cercle = 47.78
// le perimetre du cercle = 24.50

// r3
// 15.1 = hauteur
// 5.9 = base
// l'aire du rectangle= 89
// le perimetre du rectangle = 42

// nombre de rectangle construit: 3
// le cercle avec le plus grand perimetre as un perimetre de: 52.150394
// le rectangle avec la plus grande aire as une aire de: 89.090004
// le carre avec le plus petit cote avait un cote de: 0
// le perimetre moyen des rectangles: 29