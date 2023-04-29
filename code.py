# pyright: reportShadowedImports=false
# Contien toutes les imports et les déclarations
from init_projet import *
from fonctions import *

    
# Fonction de la boucle principale.
def boucle_principale():
    # Déclare les variables necessaire a la boucle.
    val_bouton_dernere_boucle = 0
    nb_ouverture = 0
    while True:
        # Déclare les variables pour la boucle
        temperature = dht.temperature
        humidite = dhtDevice.humidity
        val_bouton = bouton.value
        
        # Allume ou eteindre la lumière
        Del.value = switch.value()
        
        # Vérifie si le frigot doit etre refroidi
        pourcent_moteur = refroidissement(temperature)
        
        # Quand on lache le bouton,
        if val_bouton == 0 and val_bouton_dernere_boucle == 1:
            #compte le nombre d'ouverture de la porte
            nb_ouverture += 1
            porte_ouverte = not porte_ouverte
            # Ouvre/ferme la porte
            controle_porte(porte_ouverte)
        
        # Vérifie le niveau d'eau dans le reservoire
        pass
        
        # Vérifie si l'humiditée des légumes sont bonnes
        
        
        # Affichage : Entrée = temperature, niveau d'eau ; Sortie = moteur, nb d'ouverture de porte.
        affichage(temperature, pourcent_moteur)
        
        # Envois des information par Wi-Fi.
        envoisWifi(temperature)
        
        # Garde en memoire la valeur du bouton 
        val_bouton_dernere_boucle = val_bouton
        
        # empeche de bruler l'esp
        time.sleep(0.1)

