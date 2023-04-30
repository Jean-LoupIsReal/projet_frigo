# pyright: reportShadowedImports=false
# Contien toutes les imports et les déclarations
from init_projet import *
from fonctions import *

# Fonction de la boucle principale.
def boucle_principale():
    # Déclare les variables necessaire a la boucle.
    val_bouton_dernere_boucle = 0
    nb_ouverture = 0
    porte_ouverte = False
    led.color = (255,255,255)
    timer_spray = time.monotonic()
    pompe.value = False
    

    while True:
        # Déclare les variables pour la boucle
        try:
            temperature = dht.temperature
            humidite = dht.humidity
        except(RuntimeError):
            pass
        
        val_bouton = bouton.value

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
        reservoir = pourcent_capt(capteur_eau.value)
        
        #Vérifie si le reservoir est vide
        if reservoir == 0:
            # Active le remplissage
            remplissage = True
        
        if remplissage:
            #Rempli le reservoir
            remplissage = remplir_reservoir(reservoir, remplissage)
        
    
        # Vérifie si l'humiditée des légumes est bonne
        if timer_spray + 10 <= time.monotonic():
            verification_humidite(humidite)
            timer_spray = time.monotonic()

        
        # Affichage : Entrée = temperature, niveau d'eau ; Sortie = moteur, nb d'ouverture de porte.
        affichage(temperature, pourcent_moteur)
        
        # Envois des information par Wi-Fi.
        envoisWifi(temperature)
        
        # Garde en memoire la valeur du bouton 
        val_bouton_dernere_boucle = val_bouton
        
        # empeche de bruler l'esp
        time.sleep(0.1)

while True:

    boucle_principale()