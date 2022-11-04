#include<stdio.h>
int main()
{
    char poste[] = {'p', 'p', 'o', 'a', 'p', 'a', 'p', 'a'};
    int Nbcafe[] = {2, 1, 7, 0, 5, 2, 1, 3};
    int age[] = {25, 19, 27, 26, 49, 24, 56, 29};
    int lengthp = sizeof(poste)/sizeof(poste[0]);
    int lengthN = sizeof(Nbcafe)/sizeof(Nbcafe[0]);
    int lengtha = sizeof(age)/sizeof(age[0]);
    int countprog = 0;
    int countsec = 0;
    int mincafea = 100;
    printf("\nle tableau des poste:\n");
    for (int i = 0; i < lengthp; i++) 
        {     
        printf("%d ", poste[i]); 
        }
    printf("\n\nle tableau des cafes:\n");
    for (int i = 0; i < lengthN; i++) 
        {     
        printf("%d ", Nbcafe[i]);     
        }
    printf("\n\nle tableau des ages:\n");
    for (int i = 0; i < lengtha; i++) 
        {     
        printf("%d ", age[i]);     
        }
    for (int i = 0; i < lengthp; i++)
    {
        if (poste[i] == 'p')
        {
            countprog += 1;
        }
    }
    printf("\nil y a %d programmeurs", countprog);
    for (int i = 0; i < lengthp; i++)
    {
        if (poste[i] == 's')
        {
           countsec += 1; 
        }
    }
    printf("\nil y a %d secraitaires", countsec);
    for (int i = 0; i < lengthp; i++)
    {
        if (poste[i] == 'a')
        {
            if (Nbcafe[i] < mincafea)
            {
                mincafea = Nbcafe[i];
            }
        }
    }
    printf("\nLe plus petits nombre de cafes matinal pour les analyste est:\n%d\n", mincafea);
return 0;
}