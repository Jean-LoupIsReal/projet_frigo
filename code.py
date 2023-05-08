# pyright: reportShadowedImports=false
# Contient tous les imports et les déclarations
from init_projet import *
from fonctions import *
    
# Fonction de la boucle principale.
def boucle_principale():
    # Déclare les variables necessaire a la boucle.
    val_bouton = 1
    nb_ouverture = 0
    porte_ouverte = False
    led.color = (255,255,255)
    led_porte = 0
    remplissage = False
    timer_spray = time.monotonic()
    timer_affichage = time.monotonic()
    timer_envoie = time.monotonic()
    
    while True:
        # Déclare les variables pour la boucle
        interrupteur = switch.value
        try:
            if interrupteur:
                temperature = test_temperature()
            else:  
                temperature = dht.temperature
            humidite = dht.humidity
        except(RuntimeError):
            pass
        
        bouton_relache = bouton.value == 1 and val_bouton == 0
        val_bouton = bouton.value
        # Vérifie si le frigo doit etre refroidi
        pourcent_moteur = refroidissement(temperature)
        
        # Quand on lache le bouton,
        if bouton_relache:
            porte_ouverte = not porte_ouverte
            # Ouvre/ferme la porte et compte le nombre d'ouverture de la porte
            nb_ouverture += controle_porte(porte_ouverte)
        
            if porte_ouverte == True:
                led_porte = 1
            else:
                led_porte = 0

        # Vérifie le niveau d'eau dans le reservoire
        reservoir = pourcent_capt(capteur_eau.value)
       
        #Vérifie si le reservoir est vide
        if reservoir == 0:
            # Active le remplissage
            remplissage = True
        
        if remplissage:
            # Rempli le reservoir
            remplissage = remplir_reservoir(reservoir)
        
        # Vérifie si l'humidité est bonne
        if timer_spray + 10 <= time.monotonic():
            verification_humidite(humidite)
            timer_spray = time.monotonic()

        
        # Affichage : Entrée = temperature, niveau d'eau ; Sortie = moteur, nb d'ouverture de porte.
        if timer_affichage + 0.1 <= time.monotonic():
            print(switch.value)
            timer_affichage = time.monotonic()
            affichage(temperature, humidite, pourcent_moteur, nb_ouverture, reservoir)
        
        # Envoie des données vers Adafruit IO
        if timer_envoie + 15 <= time.monotonic():
           envoi_donnee(temperature, humidite, pourcent_moteur, nb_ouverture, led_porte, reservoir)
           timer_envoie = time.monotonic() 

        # Recoit les données d'Adafruit IO
            # reception_donnee()

        # empeche de bruler l'esp
        time.sleep(0.01)
        
while True:
    boucle_principale()