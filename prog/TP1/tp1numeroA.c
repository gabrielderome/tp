#include<stdio.h>//entete  etudiant:Gabriel Derome
int main()//principal
{
    int compte_de_patient = 0, choice;//compte de client a l'origine et definition de la variable "choice"
    while (1)//boucle
    {
        float weight, hight;//definition de variables
        compte_de_patient = compte_de_patient + 1;//compte d'iteration
        printf("\nveuillez entrer le poids du patient(kg), suivis de ca grandeur(m): \n");//prompt
        scanf("%f%f", & weight, & hight);//reponses
        float imc = weight/(hight*hight);//calcul de l'imc
        printf("\nClient#:%d",compte_de_patient);//affichage du compte de client
        printf("\nl'indice de masse corporelle du patient est de:%f", imc);//affichage de l'imc
        printf("\nle poids du patient en kg est de: %.2f", weight);//affichage du poids
        printf("\nla taille du patient en m: %.2f", hight);//affichage de la taille
        if (imc < 18.5)//if statement
        {
            printf("\nMAIGREUR, RISQUE ELEVE A ACCRU");//avertissement
        }
        else if (imc < 25)//else if statement
        {
        printf("\nPOIDS NORMAL, RISQUE FAIBLE");//avertissement
        }
        else if (imc < 30)//else if statement
        {
        printf("\nEMBONPOINT, RISQUE ELEVE");//avertissement
        }
        else//else statement
        {
        printf("\nOBESITE, RISQUE TRES ELEVE");//avertissement
        }
        printf("\n\nAvez vous fini? 2 pour oui, 1 pour Non: ");//l'utilisateur veut-il continuer?
        scanf("%d", &choice);//reponse
        if (choice == 2)//if statement
         {
           printf("\ncompte total de client:%d\n",compte_de_patient);//affichage du nombre de patients
           break;//la boucle est boucle
         }
        }
return 0;
}
// OUTPUT
// veuillez entrer le poids du patient(kg), suivis de ca grandeur(m): 
// 51
// 1.98

// Client#:1
// l'indice de masse corporelle du patient est de:13.008876
// le poids du patient en kg est de: 51.00
// la taille du patient en m: 1.98
// MAIGREUR, RISQUE ELEVE A ACCRU

// Avez vous fini? 2 pour oui, 1 pour Non: 1

// veuillez entrer le poids du patient(kg), suivis de ca grandeur(m): 
// 69.4
// 1.63

// Client#:2
// l'indice de masse corporelle du patient est de:26.120668
// le poids du patient en kg est de: 69.40
// la taille du patient en m: 1.63
// EMBONPOINT, RISQUE ELEVE

// Avez vous fini? 2 pour oui, 1 pour Non: 1

// veuillez entrer le poids du patient(kg), suivis de ca grandeur(m): 
// 60
// 1.65

// Client#:3
// l'indice de masse corporelle du patient est de:22.038568
// le poids du patient en kg est de: 60.00
// la taille du patient en m: 1.65
// POIDS NORMAL, RISQUE FAIBLE

// Avez vous fini? 2 pour oui, 1 pour Non: 1

// veuillez entrer le poids du patient(kg), suivis de ca grandeur(m): 
// 100
// 1.72

// Client#:4
// l'indice de masse corporelle du patient est de:33.802055
// le poids du patient en kg est de: 100.00
// la taille du patient en m: 1.72
// OBESITE, RISQUE TRES ELEVE

// Avez vous fini? 2 pour oui, 1 pour Non: 2

// compte total de client:4