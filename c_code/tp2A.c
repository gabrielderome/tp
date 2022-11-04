#include<stdio.h>
int main()
{
    int xi = 20;
    int somme1 = 0;
    while (xi <= 100)
    {
        somme1 += xi;
        xi += 5;
    }
    printf("\nLa somme #1:\n%d\n", somme1);
    float n = 5;
    float yi = 1 / n;
    float somme2 = 0;
    while (n <= 9999)
    {
        somme2 += yi;
        n += 2;
    }
    printf("\nLa somme #2:\n%.9f\n", somme2);
    int num = 720;
    int div = 720;
    int count = 0;
    while (div > 0)
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
    printf("\ncompte de diviseur de 720:\n%d\n", count);
return 0;
}