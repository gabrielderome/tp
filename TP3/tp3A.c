#include<stdio.h>//Gabriel Derome 20216134
void printTable(char poste[], int Nbcafe[], int age[], int lengthlist)//fonction d'affichage des tableaux
{
    printf("\n\nle tableau des poste:"); //tableau des poste
    for (int i = 0; i < lengthlist; i++) 
        {     
        printf("%c ", poste[i]); 
        }
    printf("\n\nle tableau des cafes:"); //tableau des cafes
    for (int i = 0; i < lengthlist; i++) 
        {     
        printf("%d ", Nbcafe[i]);     
        }
    printf("\n\nle tableau des ages:"); //tableau des ages
    for (int i = 0; i < lengthlist; i++) 
        {     
        printf("%d ", age[i]);     
        }
}
void countperjob(char poste[], int lengthlist) //compter le nombre de gens par poste
{
    int countprog = 0, countsec = 0, countop = 0, counta = 0;
    for (int i = 0; i < lengthlist; i++) //compte des programmeurs
    {
        if (poste[i] == 'p')
        {
            countprog += 1;
        }
    }
    for (int i = 0; i < lengthlist; i++) //compte des operateurs
    {
        if (poste[i] == 'o')
        {
           countop += 1; 
        }
    }
    for (int i = 0; i < lengthlist; i++) //compte des analystes
    {
        if (poste[i] == 'a')
        {
            counta += 1;
        }
    }
    printf("\n\nIl y as %d programmeurs, %d analystes et %d operateur\n\n", countprog, counta, countop); //affichage des compte par poste
}
int trente_ans_trois_cafe(char poste[], int Nbcafe[], int age[], int lengthlist) //compte des programmeurs de plus de 30 ans et qui ont bu 3 cafe ou plus
{
    int count = 0;
    for (int i = 0; i < lengthlist; i++)
    if (age[i] > 30 && Nbcafe[i] >= 3)
    {
        count += 1;
    }
    return count;
}
void MaxCoffeeMaxAge(int Nbcafe[], int age[], int lengthlist) //determiner le plus vieux des programmeurs et le plus grand nombre de cafe matinal
{
    int maxagep = 0, maxcafe = 0;
    for (int i = 0; i < lengthlist; i++)
    {
        if (age[i] > maxagep)
        {
            maxagep = age[i];
        }
        if (Nbcafe[i] > maxcafe)
        {
            maxcafe = Nbcafe[i];
        }
    }
    printf("\nLe plus vieux des programmeurs a:\n%d ans\n", maxagep); //affichage du plus vieux des programmeurs
    printf("\nLe plus grand nombre de cafe matinal est:\n%d\n", maxcafe); //affichage du plus grand nombre de cafe matinal
}
void filtertablesperage(char poste[], int Nbcafe[], int age[], int lengthlist)//definition de la methode de tri
{
    int temp;
    for (int i = 0; i < lengthlist; i++)
    {
        for (int j = i + 1; j < lengthlist; j++)
        {
            if (age[i] > age[j])
            {
                temp = age[i];
                age[i] = age[j];
                age[j] = temp;
                temp = Nbcafe[i];
                Nbcafe[i] = Nbcafe[j];
                Nbcafe[j] = temp;
                temp = poste[i];
                poste[i] = poste[j];
                poste[j] = temp;
            }
        }
    }
    printTable(poste, Nbcafe, age, lengthlist); // affichage des tableaux triés
}
int main()
{
    char poste[] = {'p', 'p', 'o', 'a', 'p', 'a', 'p', 'p'}; //definition des tableaux de bases
    int Nbcafe[] = {3, 1, 5, 0, 3, 4, 0, 3};
    int age[] = {25, 19, 27, 30, 65, 24, 56, 29};
    int lengthlist = sizeof(poste)/sizeof(poste[0]);
    printTable(poste, Nbcafe, age, lengthlist); //utilisation des methodes definies plus haut
    countperjob(poste, lengthlist);
    trente_ans_trois_cafe(poste, Nbcafe, age, lengthlist);
    MaxCoffeeMaxAge(Nbcafe, age, lengthlist);
    filtertablesperage(poste, Nbcafe, age, lengthlist);
    return 0;
}

// RESULTATS:
// le tableau des poste:p p o a p a p p 

// le tableau des cafes:3 1 5 0 3 4 0 3 

// le tableau des ages:25 19 27 30 65 24 56 29 

// Il y as 5 programmeurs, 2 analystes et 1 operateur


// Le plus vieux des programmeurs a:
// 65 ans

// Le plus grand nombre de cafe matinal est:
// 5


// le tableau des poste:p a p o p a p p 

// le tableau des cafes:1 4 3 5 3 0 0 3 

// le tableau des ages:19 24 25 27 29 30 56 65