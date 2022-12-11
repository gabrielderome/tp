//Gabriel Derome 20216134
class personne {
    private String naissance;
    private int nbcafe = 1;
    //constructeur pour classe personne
    public personne(String naissance) {
        this.naissance = naissance;
        this.nbcafe = 1;
    }
    public personne(String naissance, int nbcafe) {
        this.naissance = naissance;
        this.nbcafe = nbcafe;
    }
    //methode pour editer le nombre de cafe
    public void setNbcafe(int nbcafe) {
        this.nbcafe = nbcafe;
    }
    //methode pour obtenir la date de naissance et le nombre de cafe
    public String getNaissance() {
        return naissance;
    }
    public int getNbcafe() {
        return nbcafe;
    }
    //la methode afficher() prend une chaine de caracteres en argument et affiche cette chaine avec les informations de la personne
    public String afficher(String str) {
        if (nbcafe < 1) {
            nbcafe = 1;
        }
        return str + ":\n naissance:" + naissance + "\n nbcafe:" + nbcafe + "\n";
    }
    public static void main(String[] args) {
        //ajouter pers1, pers2 et pers3
        personne pers1 = new personne("19/05/1997", 4);
        personne pers2 = new personne("31/12/1990");
        personne pers3 = new personne("08/05/1994", 2);
        //afficher leurs informations
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
