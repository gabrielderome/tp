#include<stdio.h>//Gabriel Derome 20216134
void printTable(char poste[], int Nbcafe[], int age[], int lengthlist)
{
    printf("\n\nle tableau des poste:");
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
    for (int i = 0; i < lengthlist; i++)
    {
        if (poste[i] == 'p')
        {
            countprog += 1;
        }
    }
    for (int i = 0; i < lengthlist; i++)
    {
        if (poste[i] == 'o')
        {
           countop += 1; 
        }
    }
    for (int i = 0; i < lengthlist; i++)
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
    printf("\nLe plus vieux des programmeurs a:\n%d ans\n", maxagep);
    printf("\nLe plus grand nombre de cafe matinal est:\n%d\n", maxcafe);
}
void filtertablesperage(char poste[], int Nbcafe[], int age[], int lengthlist)
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
    printTable(poste, Nbcafe, age, lengthlist);
}
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