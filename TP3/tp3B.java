//Gabriel Derome 20216134
class tp3B
{
    public static void main(String[] args) {
        String telUDM = "5143436111", telJean = "4501897654";
        //extraire et afficher les sous-chaines de telUDM et telJean
        System.out.println("Téléphone d’UDM : (" + telUDM.substring(0, 3) + ") " + telUDM.substring(3, 6) + "-" + telUDM.substring(6, 10) + "\n" + "Téléphone de Jean : (" + telJean.substring(0, 3) + ") " + telJean.substring(3, 6) + "-" + telJean.substring(6, 10));
        //compte et affichage du nombre d’occurrences du chiffre 3 dans telUDM
        int count3 = 0;
        for (int i = 0; i < telUDM.length(); i++) {
            if (telUDM.charAt(i) == '3') {
                count3++;
            }
        }
        System.out.println("Le nombre de 3 dans le numéro de téléphone d’UdM est : " + count3);
        //compte et affichage du nombre d’occurrences du chiffre 1 dans telJean
        int count1 = 0;
        for (int i = 0; i < telUDM.length(); i++) {
            if (telUDM.charAt(i) == '1') {
                count1++;
            }
        }
        System.out.println("Le nombre de 1 dans le numéro de téléphone d’UdM est : " + count1);
        //compte et affichage du nombre d’occurrences du chiffre 2 dans telJean
        int count2 = 0;
        for (int i = 0; i < telJean.length(); i++) {
            if (telJean.charAt(i) == '2') {
                count2++;
            }
        }
        System.out.println("Le nombre de 2 dans le numéro de téléphone de Jean est : " + count2);
        //compte et affichage du nombre d’occurrences du chiffre impaires dans telJean
        int countOdd = 0;
        for (int i = 0; i < telUDM.length(); i++) {
            if (telUDM.charAt(i) == '1' || telUDM.charAt(i) == '3' || telUDM.charAt(i) == '5' || telUDM.charAt(i) == '7' || telUDM.charAt(i) == '9') {
                countOdd++;
            }
        }
        System.out.println("Le nombre de chiffres impairs dans le numéro de téléphone d’UdM est : " + countOdd);
        //compte et affichage du nombre d’occurrences du chiffre pairs dans telJean
        int countEven = 0;
        for (int i = 0; i < telJean.length(); i++) {
            if (telJean.charAt(i) == '0' || telJean.charAt(i) == '2' || telJean.charAt(i) == '4' || telJean.charAt(i) == '6' || telJean.charAt(i) == '8') {
                countEven++;
            }
        }
        System.out.println("Le nombre de chiffres pairs dans le numéro de téléphone de Jean est : " + countEven);
        //trouver et afficher les chiffres impairs communs aux deux numéros de téléphone
        String sharedOdd = "";
        for (int i = 0; i < telUDM.length(); i++) {
            for (int j = 0; j < telJean.length(); j++) {
                if (telUDM.charAt(i) == telJean.charAt(j) && (telUDM.charAt(i) == '1' || telUDM.charAt(i) == '3' || telUDM.charAt(i) == '5' || telUDM.charAt(i) == '7' || telUDM.charAt(i) == '9') && sharedOdd.indexOf(telUDM.charAt(i)) == -1) {
                    sharedOdd += telUDM.charAt(i);
                    sharedOdd += " | ";
                }
            }
        }
        System.out.println("Les chiffres impairs communs aux deux numéros de téléphone sont : " + sharedOdd);
    }
}

// RESULTATS:
// Téléphone d’UDM : (514) 343-6111
// Téléphone de Jean : (450) 189-7654
// Le nombre de 3 dans le numéro de téléphone d’UdM est : 2
// Le nombre de 1 dans le numéro de téléphone d’UdM est : 4
// Le nombre de 2 dans le numéro de téléphone de Jean est : 0
// Le nombre de chiffres impairs dans le numéro de téléphone d’UdM est : 7
// Le nombre de chiffres pairs dans le numéro de téléphone de Jean est : 5
// Les chiffres impairs communs aux deux numéros de téléphone sont : 5 | 1 | 