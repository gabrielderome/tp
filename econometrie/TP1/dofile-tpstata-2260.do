clear
log using log1.log
*Il vous faudra changer le dossier de travail pour un dossier sur votre ordinateur
cd "C:\Users\Public\TP1-2260" 
import excel "Real estate valuation data set.xlsx", firstrow
*On sauvegarde les données en dta
save A1.dta, replace 
* Ceci est un exemple de commentaire
/* Pour les commentaires de plus d'une ligne,
 vous pouvez utiliser cette forme */
 gen variable1 = X5latitude + X6longitude
 label variable variable1 "variable de pratique"
 drop variable1
 replace Yhousepriceofunitarea = 1.2*Yhousepriceofunitarea if X2houseage > 15
 rename Yhousepriceofunitarea prix
 
 tabulate X2houseage
 *Les données sont trop précises, peu utile.
 gen agearrondi = round(X2houseage)
 tabulate agearrondi 
 *C'est mieux
 
 *Ordonner les variables
 order X2houseage, last
 order prix, before(X2houseage)
 
 *Classer à partir d'une variable
 sort X2houseage
 gsort -X2houseage
 
 *Régressions
 reg prix X2houseage X4numberofconveniencestores
 reg prix X2houseage X4numberofconveniencestores X3distancetothenearestMRTst
 *On aurait pu les renommer si on les utilisait souvent.
 
 *Exporter des résultats
 outreg2 using reg1.rtf, replace
 reg prix X2houseage X4numberofconveniencestores X3distancetothenearestMRTst X5latitude
 *Ajoutons ces résultats au fichier reg1
 outreg2 using reg1.rtf, append 
 
 save A1.dta, replace
 
 
 
