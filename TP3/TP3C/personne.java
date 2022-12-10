class personne {
    private String naissance;
    private int nbcafe = 1;
    //builder. personne() has to be given AT LEAST a birth date, the number of coffees is optional(1 by default)
    public personne(String naissance) {
        this.naissance = naissance;
        this.nbcafe = 1;
    }
    public personne(String naissance, int nbcafe) {
        this.naissance = naissance;
        this.nbcafe = nbcafe;
    }
    //setter setNbcafe() takes an int as it's argument and changes the number of coffee for that person
    public void setNbcafe(int nbcafe) {
        this.nbcafe = nbcafe;
    }
    public String getNaissance() {
        return naissance;
    }
    public int getNbcafe() {
        return nbcafe;
    }
    //getter afficher() takes a strings as its argument then prints that string with the person's information
    public String afficher(String str) {
        if (nbcafe < 1) {
            nbcafe = 1;
        }
        return str + ":\n naissance:" + naissance + "\n nbcafe:" + nbcafe + "\n";
    }
    //main function (printer and adder)
    public static void main(String[] args) {
        personne pers1 = new personne("19/05/1997", 4);
        personne pers2 = new personne("31/12/1990");
        personne pers3 = new personne("08/05/1994", 2);
        //print
        System.out.println(pers1.afficher("Informations de la premiere personne"));
        System.out.println(pers2.afficher("Informations de la deuxieme personne"));
        System.out.println(pers3.afficher("Informations de la troisieme personne"));
    }
}

//RESULTATS:
// Informations de la premiere personne:
//  naissance:19/05/1997
//  nbcafe:4

// Informations de la deuxieme personne:
//  naissance:31/12/1990
//  nbcafe:1

// Informations de la troisieme personne:
//  naissance:08/05/1994
//  nbcafe:2
