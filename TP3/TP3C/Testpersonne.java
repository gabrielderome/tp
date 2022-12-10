class Testpersonne {
    public static void main(String[] args) {
        //create 5 persons and and add them to a table with an incrementing id
        personne[] pers = new personne[5];
        pers[0] = new personne("16/05/2001", 2);
        pers[1] = new personne("02/05/1990");
        pers[2] = new personne("23/11/1996", 5);
        pers[3] = new personne("19/02/2000", 0);
        pers[4] = new personne("30/05/1991", 2);
        System.out.println("\n\nindex | naissance |nbcafe");
        for (int i = 0; i < 5; i++) {
            System.out.println((i + 1)+ "     |" + pers[i].getNaissance() + " |" + pers[i].getNbcafe());
        }
        System.out.println("\n\n");
        //print the table
        for (int i = 0; i < 5; i++) {
            if (i == 0){
                System.out.println(pers[i].afficher("Information de la premiere personne:"));
            } else if (i == 1) {
                System.out.println(pers[i].afficher("Information de la deuxieme personne:"));
            } else if (i == 2) {
                System.out.println(pers[i].afficher("Information de la troisieme personne:"));
            } else if (i > 2) {
                System.out.println(pers[i].afficher("Information de la " + (i + 1) + "eme personne:"));
            }
        }
        System.out.println("\n\n");
        //determine who drinks the most coffee and print "la personne qui boit le plus de cafe est la personne #{id}"
        int max = 0;
        int id = 0;
        for (int i = 0; i < 5; i++) {
            if (pers[i].getNbcafe() > max) {
                max = pers[i].getNbcafe();
                id = i;
            }
        }
        System.out.println("la personne qui boit le plus de cafe est la personne #" + (id + 1) + "\n\n");
        //substract 1 from everyone who has at least 1 coffee
       for (int x = 0; x < 5; x++) {
           if (pers[x].getNbcafe() > 0) {
                pers[x].setNbcafe(pers[x].getNbcafe() - 1);
           }
       }
       System.out.println("\n\nindex | naissance |nbcafe");
        for (int i = 0; i < 5; i++) {
            System.out.println((i + 1)+ "     |" + pers[i].getNaissance() + " |" + pers[i].getNbcafe());
        }
        System.out.println("\n\n");
        //count the number of people with naissence matching month 05
        int count = 0;
        for (int i = 0; i < 5; i++) {
            if (pers[i].getNaissance().substring(3, 5).equals("05")) {
                count++;
            }
        }
        System.out.println("il y a " + count + " personnes qui sont nee en mai\n\n");
    }
}

//RESULTATS:

// index | naissance |nbcafe
// 1     |16/05/2001 |2
// 2     |02/05/1990 |1
// 3     |23/11/1996 |5
// 4     |19/02/2000 |0
// 5     |30/05/1991 |2



// Information de la premiere personne::
//  naissance:16/05/2001
//  nbcafe:2

// Information de la deuxieme personne::
//  naissance:02/05/1990
//  nbcafe:1

// Information de la troisieme personne::
//  naissance:23/11/1996
//  nbcafe:5

// Information de la 4eme personne::
//  naissance:19/02/2000
//  nbcafe:1

// Information de la 5eme personne::
//  naissance:30/05/1991
//  nbcafe:2




// la personne qui boit le plus de cafe est la personne #3




// index | naissance |nbcafe
// 1     |16/05/2001 |1
// 2     |02/05/1990 |0
// 3     |23/11/1996 |4
// 4     |19/02/2000 |0
// 5     |30/05/1991 |1



// il y a 3 personnes qui sont nee en mai