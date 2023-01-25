#include <stdio.h>//entete etudiant:Gabriel Derome
int main() {//principale
  char shape, circle = 'c', circlec = 'C', rectangle = 'r', rectangler = 'R', square = 'k', squarek = 'K';//definition de variables
  int choice, reccompte = 0;
  float maxperimetrec = 0.00, maxairer = 0.00, mincote = 0.00, sumperimetre = 0.00;
  while(1)//boucle
  {
      printf("tapez c pour cercle \ntapez r pour rectangle \ntapez k pour carre\n");//choix de la forme
      scanf("\n %c", &shape);
      if ((shape == circle) || (shape == circlec)) {//CERCLE
      float rayon;//definition de variable
      printf("veuillez entrer le rayon du cercle: \n");//entre du rayon
      scanf("\n %f", &rayon);
      float airec = 3.14159 * rayon * rayon, perimetrec = 3.14159 * 2 * rayon;//calculs
      if (perimetrec > maxperimetrec){//max perimetre?
         maxperimetrec = perimetrec;
      }
      printf("l'aire du cercle = %.2f\n", airec);//affichage des donnes
      printf("le perimetre du cercle = %.2f\n", perimetrec);                                                                 
    } else if ((shape == rectangle) || (shape == rectangler)) {//RECTANGLE
      float base, hauteur;//definition de variables
      printf("veuillez entrer la hauteur puis, la base du rectangle\n");//entre de la base et de la hauteur
      scanf("\n %f", &base);
      scanf("\n %f", &hauteur);
      float airer = base * hauteur, perimetrer = 2 * base + 2 * hauteur;//calculs
      printf("l'aire du rectangle= %2.f\n", airer);//affichage des donnes
      printf("le perimetre du rectangle = %2.f\n", perimetrer);                                                      
      reccompte += 1;//compte de rectangles
      sumperimetre += perimetrer;//sum des perimetres
      if (airer > maxairer){//max aire?
         maxairer = airer;
      }
    } else if ((shape == square) || (shape == squarek)){//CARRE
      float cote;//definition de variable
      printf("veuillez entrer le cote du carre\n");//entre du cote
      scanf("\n %f", & cote);
      float airek = cote * cote, perimetrek = cote * 4;//calculs
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
// OUTPUT
// tapez c pour cercle 
// tapez r pour rectangle 
// tapez k pour carre
// C
// veuillez entrer le rayon du cercle: 
// 7.5
// l'aire du cercle = 176.71
// le perimetre du cercle = 47.12

// Avez vous fini? 2 pour oui, 1 pour Non: 1
// tapez c pour cercle 
// tapez r pour rectangle 
// tapez k pour carre
// r
// veuillez entrer la hauteur puis, la base du rectangle
// 9.2
// 4.8
// l'aire du rectangle= 44
// le perimetre du rectangle = 28

// Avez vous fini? 2 pour oui, 1 pour Non: 1
// tapez c pour cercle 
// tapez r pour rectangle 
// tapez k pour carre
// c
// veuillez entrer le rayon du cercle: 
// 8.3
// l'aire du cercle = 216.42
// le perimetre du cercle = 52.15

// Avez vous fini? 2 pour oui, 1 pour Non: 1
// tapez c pour cercle 
// tapez r pour rectangle 
// tapez k pour carre
// R
// veuillez entrer la hauteur puis, la base du rectangle
// 5.3
// 3.7
// l'aire du rectangle= 20
// le perimetre du rectangle = 18

// Avez vous fini? 2 pour oui, 1 pour Non: 1
// tapez c pour cercle 
// tapez r pour rectangle 
// tapez k pour carre
// C
// veuillez entrer le rayon du cercle: 
// 3.9
// l'aire du cercle = 47.78
// le perimetre du cercle = 24.50

// Avez vous fini? 2 pour oui, 1 pour Non: 1
// tapez c pour cercle 
// tapez r pour rectangle 
// tapez k pour carre
// r
// veuillez entrer la hauteur puis, la base du rectangle
// 15.1
// 5.9
// l'aire du rectangle= 89
// le perimetre du rectangle = 42

// Avez vous fini? 2 pour oui, 1 pour Non: 2
// nombre de rectangle construit: 3
// le cercle avec le plus grand perimetre as un perimetre de: 52.150394
// le rectangle avec la plus grande aire as une aire de: 89.090004
// le carre avec le plus petit cote avait un cote de: 0.000000
// le perimetre moyen des rectangles: 29