#include<stdio.h>//Gabriel Derome 20216134
int main()
{
    char poste[] = {'p', 'p', 'o', 'a', 'p', 'a', 'p', 'a'};//creations des tableaux lignes 4-6
    int Nbcafe[] = {2, 1, 7, 0, 5, 2, 1, 3};
    int age[] = {25, 19, 27, 26, 49, 24, 56, 29};
    int lengthp = sizeof(poste)/sizeof(poste[0]);//creation de variable pour la longueur des tableaux lignes 7-9
    int lengthN = sizeof(Nbcafe)/sizeof(Nbcafe[0]);
    int lengtha = sizeof(age)/sizeof(age[0]);
    int countprog = 0, countsec = 0, countop = 0, counta = 0, mincafea = 100, maxagep = 0, sommecafeo = 0, sommeageo = 0, sommeagep = 0, sommeagea = 0;//defninition des comptes, des sommes, des maximums et des minimums
    float avgcafeo, avgageo, avgagep, avgagea; //definition des moyennes
    printf("\nle tableau des poste:\n");//affichage des tableaux lignes 12-26
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
    for (int i = 0; i < lengthp; i++)//compte et affichage du nombre de programmeurs lignes 27-34
    {
        if (poste[i] == 'p')
        {
            countprog += 1;
        }
    }
    printf("\n\nil y a %d programmeurs\n", countprog);
    for (int i = 0; i < lengthp; i++)//compte  et affichage du nombre de secraitaires lignes 35-42
    {
        if (poste[i] == 's')
        {
           countsec += 1; 
        }
    }
    printf("\nil y a %d secraitaires\n", countsec);
    for (int i = 0; i < lengthp; i++)//calcul et affichage du minimum de cafes pour un analyste lignes 43-53
    {
        if (poste[i] == 'a')
        {
            if (Nbcafe[i] < mincafea)
            {
                mincafea = Nbcafe[i];
            }
        }
    }
    printf("\nLe plus petits nombre de cafes matinal pour les analyste est:\n %d\n", mincafea);
     for (int i = 0; i < lengthp; i++)//calcul et affichage de l'age maximal des programmeurs ligmes 54-64
    {
        if (poste[i] == 'p')
        {
            if (age[i] > maxagep)
            {
                maxagep = age[i];
            }
        }
    }
    printf("\nLe plus vieux des programmeurs a:\n %d ans\n", maxagep);
     for (int i = 0; i < lengthp; i++)//calcul et affichage de la moyenne de cafe des programmeurs lignes 65-74
    {
        if (poste[i] == 'o')
        {
        countop += 1;
           sommecafeo += Nbcafe[i];
        }
    }
    avgcafeo = sommecafeo / countop;
    printf("\nLa consomation moyenne de cafe chez les operateurs est de:\n %.0f\n", avgcafeo);
    for (int i = 0; i < lengthp; i++)//calcul et affichage de lage moyen pour tout les postes lignes 75-96
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
    printf("\nL'age moyen chez les operateurs est de:\n %.0f\n", avgageo);
    printf("\nL'age moyen chez les programmeurs est de:\n %.0f\n", avgagep);
    printf("\nL'age moyen chez les analystes est de:\n %.0f\n", avgagea);
    int x, j, tempa, tempN, tempp;//rearangage et affichage des tableaux en ordre croissant d'age lignes 97-130
    for (x = 0; x < (lengtha - 1); ++x)
    {
        for (j = 0; j < lengtha - 1 - x; ++j )
        {
            if (age[j] > age[j+1])
            {
                tempa = age[j+1];
                tempN = Nbcafe[j+1];
                tempp = poste[j+1];
                age[j+1] = age[j];
                Nbcafe[j+1] = Nbcafe[j];
                poste[j+1] = poste[j];
                age[j] = tempa;
                Nbcafe[j] = tempN;
                poste[j] = tempp;
            }
        }
    }
    printf("\n\nle tableau des ages rearange:\n");
    for (int i = 0; i < lengtha; i++) 
    {     
        printf("%d ", age[i]);     
    }
    printf("\n\nle tableau des cafes rearanger:\n");
    for (int i = 0; i < lengthN; i++) 
    {     
        printf("%d ", Nbcafe[i]);     
    }
    printf("\n\nle tableau des postes rearanger:\n");
    for (int i = 0; i < lengthN; i++) 
    {     
        printf("%c ", poste[i]);     
    }
    printf("\n\n");
return 0;
}

// RESULTATS
//-------------------------------
// le tableau des poste:
// 112 112 111 97 112 97 112 97 

// le tableau des cafes:
// 2 1 7 0 5 2 1 3 

// le tableau des ages:
// 25 19 27 26 49 24 56 29 

// il y a 4 programmeurs

// il y a 0 secraitaires

// Le plus petits nombre de cafes matinal pour les analyste est:
//  0

// Le plus vieux des programmeurs a:
//  56 ans

// La consomation moyenne de cafe chez les operateurs est de:
//  7

// L'age moyen chez les operateurs est de:
//  27

// L'age moyen chez les programmeurs est de:
//  37

// L'age moyen chez les analystes est de:
//  26


// le tableau des ages rearange:
// 19 24 25 26 27 29 49 56 

// le tableau des cafes rearanger:
// 1 2 2 0 7 3 5 1 

// le tableau des postes rearanger:
// p a p a o a p p