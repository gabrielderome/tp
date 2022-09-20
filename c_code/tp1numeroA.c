#include<stdio.h>//entete  etudiant:Gabriel Derome
int main()//principal
{
    while (1)//boucle
    {
        float weight;//definition de variable
        float hight;//definition de variable
        printf("\nveuillez entrer le poids du patient(kg), suivis de ca grandeur(m): \n");//prompt
        scanf("%f%f", & weight, & hight);//reponses
        float imc = weight/(hight*hight);//calcul de l'imc
        printf("\nvotre indice de masse corporelle est de:%f\n", imc);//affichage de l'imc
        printf("le poids du patient en kg est de: %.2f", weight);//affichage du poids
        printf("la taille du patient en m: %.2f", hight);//affichage de la taille
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
        int compte_de_patient = 0;//compte de client a l'origine
        compte_de_patient = compte_de_patient + 1;//compte d'iteration
        printf("\nClient#:%d",compte_de_patient);//affichage du compte de client
        int choice;//definition de variable
        printf("\nAvez vous fini? 2 pour oui, 1 pour Non: ");//l'utilisateur veut-il continuer?
        scanf("%d", &choice);//reponse
        if (choice == 2)//if statement
         {
           printf("\ncompte total de client:%d\n",compte_de_patient);//affichage du nombre de patients
           break;//la boucle est boucle
         }
        }
    return 0;
}