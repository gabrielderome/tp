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
    int countop = 0;
    int counta = 0;
    int mincafea = 100;
    int maxagep = 0;
    int sommecafeo = 0;
    int sommeageo = 0;
    int sommeagep = 0;
    int sommeagea = 0;
    float avgcafeo, avgageo, avgagep, avgagea;
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
    printf("\n\nil y a %d programmeurs\n", countprog);
    for (int i = 0; i < lengthp; i++)
    {
        if (poste[i] == 's')
        {
           countsec += 1; 
        }
    }
    printf("\nil y a %d secraitaires\n", countsec);
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
     for (int i = 0; i < lengthp; i++)
    {
        if (poste[i] == 'p')
        {
            if (age[i] > maxagep)
            {
                maxagep = age[i];
            }
        }
    }
    printf("\nLe plus vieux des programmeurs a %d ans\n", maxagep);
     for (int i = 0; i < lengthp; i++)
    {
        if (poste[i] == 'o')
        {
        countop += 1;
           sommecafeo += Nbcafe[i];
        }
    }
    avgcafeo = sommecafeo / countop;
    printf("\nLa consomation moyenne de cafe chez les operateurs est de:\n %.2f", avgcafeo);
    for (int i = 0; i < lengthp; i++)
    {
        if (poste[i] == 'o')
        {
           sommeageo += age[i];
        }
        else if (poste[i] == 'p')
        {
            sommeagep += age[i];
        }
        else if (poste[i] == 'a')
        {
            counta += 1;
            sommeagea += age[i];
        }
    }
    avgageo = sommeageo / countop;
    avgagep = sommeagep / countprog;
    avgagea = sommeagea / counta;
    printf("\nL'age moyen chez les operateurs est de:\n %.2f\n", avgageo);
    printf("\nL'age moyen chez les programmeurs est de:\n %.2f\n", avgagep);
    printf("\nL'age moyen chez les analystes est de:\n %.2f\n", avgagea);
return 0;
}