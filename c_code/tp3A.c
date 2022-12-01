#include<stdio.h>//Gabriel Derome 20216134
//create pre-main function to print table
void printTable(char poste[], int Nbcafe[], int age[], int lengthlist)
{
    printf("\n\nle tableau des poste:");//affichage des tableaux lignes 12-26
    for (int i = 0; i < lengthlist; i++) 
        {     
        printf("%c ", poste[i]); 
        }
    printf("\n\nle tableau des cafes:");
    for (int i = 0; i < lengthlist; i++) 
        {     
        printf("%d ", Nbcafe[i]);     
        }
    printf("\n\nle tableau des ages:");
    for (int i = 0; i < lengthlist; i++) 
        {     
        printf("%d ", age[i]);     
        }
}
void countperjob(char poste[], int lengthlist)
{
    int countprog = 0, countsec = 0, countop = 0, counta = 0;
    for (int i = 0; i < lengthlist; i++)//compte et affichage du nombre de programmeurs lignes 27-34
    {
        if (poste[i] == 'p')
        {
            countprog += 1;
        }
    }
    for (int i = 0; i < lengthlist; i++)//compte  et affichage du nombre de secraitaires lignes 35-42
    {
        if (poste[i] == 'o')
        {
           countop += 1; 
        }
    }
    for (int i = 0; i < lengthlist; i++)//compte et affichage du nombre d'analystes lignes 51-58
    {
        if (poste[i] == 'a')
        {
            counta += 1;
        }
    }
    printf("\n\nIl y as %d programmeurs, %d analystes et %d operateur\n\n", countprog, counta, countop);
}
int trente_ans_trois_cafe(char poste[], int Nbcafe[], int age[], int lengthlist)
{
  //count people who are older then 30 and drink at least 3 coffees
    int count = 0;
    for (int i = 0; i < lengthlist; i++)
    if (age[i] > 30 && Nbcafe[i] >= 3)
    {
        count += 1;
    }
    return count;
}
void MaxCoffeeMaxAge(int Nbcafe[], int age[], int lengthlist)
{
    int maxagep = 0, maxcafe = 0;
    for (int i = 0; i < lengthlist; i++)//calcul et affichage de l'age maximal des programmeurs ligmes 54-64
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
    printf("\nLe plus vieux des programmeurs a:\n%d ans\n", maxagep);
    printf("\nLe plus grand nombre de cafe matinal est:\n%d\n", maxcafe);
}
void filtertablesperage(char poste[], int Nbcafe[], int age[], int lengthlist)
{
   //function that will filter all three tables by ascending age and print them
    int temp;
    //loop through lengthlist and filter age, Nbcafe and poste by age
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
    printTable(poste, Nbcafe, age, lengthlist);
}
//create table  char poste[] = {'p', 'p', 'o', 'a', 'p', 'a', 'p', 'p'}, int Nbcafe[] = {3, 1, 5, 0, 3, 4, 0, 3}, int age[] = {25, 19, 27, 30, 65, 24, 56, 29};
//call void functions on main
int main()
{
    char poste[] = {'p', 'p', 'o', 'a', 'p', 'a', 'p', 'p'};
    int Nbcafe[] = {3, 1, 5, 0, 3, 4, 0, 3};
    int age[] = {25, 19, 27, 30, 65, 24, 56, 29};
    int lengthlist = sizeof(poste)/sizeof(poste[0]);
    printTable(poste, Nbcafe, age, lengthlist);
    countperjob(poste, lengthlist);
    trente_ans_trois_cafe(poste, Nbcafe, age, lengthlist);
    MaxCoffeeMaxAge(Nbcafe, age, lengthlist);
    filtertablesperage(poste, Nbcafe, age, lengthlist);
    return 0;
}