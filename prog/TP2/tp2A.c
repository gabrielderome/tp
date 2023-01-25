#include<stdio.h>
int main()//Gabriel Derome 20216134
{
    int xi = 20, somme1 = 0, num = 720, div = 720, count = 0;//definitions de variables lignes 4-5
    float n = 5, yi = 1 / n, somme2 = 0;
    while (xi <= 100)//calcul et affichage de la somme1 lignes 6-11
    {
        somme1 += xi;
        xi += 5;
    }
    printf("\nLa somme #1:\n%d\n", somme1);
    while (n <= 9999)//calcul et affichage de la somme2 lignes 12-17
    {
        somme2 += yi;
        n += 2;
    }
    printf("\nLa somme #2:\n%.9f\n", somme2);
    while (div > 0)//compte et affichage du nombre de diviseurs de 720 lignes 18-30
    {
        if (num % div == 0)
        {
            count += 1;
            div -= 1;
        }
        else
        {
            div -= 1;
        }
    }
    printf("\ncompte de diviseur de 720:\n%d\n\n", count);
return 0;
}

//RESULTATS
//---------------
// La somme #1:
// 1020

// La somme #2:
// 999.642578125

// compte de diviseur de 720:
// 30