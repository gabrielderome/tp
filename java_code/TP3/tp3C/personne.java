//create class personne
class personne {
    private String naissance;
    private int nbcafe;
    private int id = 0;
    //constructeur with id automatically incremented
    public personne(String naissance, int nbcafe, int id) {
        this.naissance = naissance;
        this.nbcafe = nbcafe;
        this.id = id;
    }
    //getters
    public String getNaissance() {
        return naissance;
    }
    public int getNbcafe() {
        return nbcafe;
    }
    public int getId() {
        return id;
    }
    //main function (printer and adder)
    public static void main(String[] args) {
        personne pers1 = new personne("1990", 2, 1);
        personne pers2 = new personne("1991", 3, 2);
        personne pers3 = new personne("1992", 4, 3);
        //list of all persons
        personne[] pers = {pers1, pers2, pers3};
        //print all as ( information de la personne #{id}:\n naissance:{naissance}\n nbcafe:{nbcafe}\n)
        for (int i = 0; i < pers.length; i++) {
            System.out.println("information de la personne #" + pers[i].getId() + ":\n naissance:" + pers[i].getNaissance() + "\n nbcafe:" + pers[i].getNbcafe() + "\n");
        }
    }
}