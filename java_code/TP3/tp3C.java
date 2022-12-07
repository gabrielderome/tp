class Personne
{ 
	private String naissance ; // format "jj/mm/aaaa", ex : "25/12/1990"
    private int nbCafe ; // nb de tasses de café consommé par jour
    private int id ; // identifiant unique de la personne
    //constructeur
    public Personne(String naissance, int nbCafe) {
        this.naissance = naissance;
        this.nbCafe = nbCafe;
        this.id = 1;
        //increase id by 1 for each new Personne object
        id++;
    }
    //getters
    public String getNaissance() {
        return naissance;
    }
    public int getNbCafe() {
        return nbCafe;
    }
    public int getId() {
        return id;
    }
    //printer method
    //for exemple '''les informations de la personne 1 sont : \n naissance : 25/12/1990 \n nbCafe : 2'''
    public void afficher() {
        System.out.println("les informations de la personne " + id + " sont : \n naissance : " + naissance + "\n nbCafe : " + nbCafe);
    }
    public static void main(String[] args) {
        Personne pers1 = new Personne("19/05/1997", 4);
        Personne pers2 = new Personne("31/12/1990", 0);
        Personne pers3 = new Personne("08/05/1994", 2);
        //print all the Personne objects
        pers1.afficher();
        pers2.afficher();
        pers3.afficher();
    }
}