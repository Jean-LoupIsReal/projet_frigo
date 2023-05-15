from init_projet import *

#========================================== Fonction recevoir/envoie de donnée ==========================================

# Fonction qui envoie les données sur Adafruit IO
def envoi_donnee(temps, hum, moteur, porte, led, reservoir):

    try:
        io.send_data(io.create_and_get_feed("temperature")["key"], temps)
        io.send_data(io.create_and_get_feed("humidite")["key"], hum)
        io.send_data(io.create_and_get_feed("moteur")["key"], moteur)
        io.send_data(io.create_and_get_feed("porte")["key"], porte)
        io.send_data(io.create_and_get_feed("led-frigidaire")["key"], led)
        io.send_data(io.create_and_get_feed("reservoir")["key"], reservoir)
    except RuntimeError:
        print("Erreur d'envoie de donnée")

# Fonction qui recoie les données d'Adafruit IO

def reception_donnee():
    
    # Reception des données d'Adafruit IO
    # Récupere la valeur de la porte
    porte = io.receive_data("controle.porte")
    porte_distance = int(porte['value'])

    # Récupere la valeur du spray
    spray = io.receive_data("controle.spray")
    spray_distance = int(spray['value'])
    if spray_distance == 1:
        spray_legumes()

    # Récupere la valeur pour remplir
    remplissage = io.receive_data("controle.remplir")
    remplissage_distance = int(remplissage['value'])
         
    return porte_distance, spray_distance, remplissage_distance

#========================================== Fonctions du buzzer (spray) ==========================================
# Déclanche la musique de zelda.
def music_zelda():
    melodie = [392,
            370,
            311,
            220,
            208,
            330,
            415,
            523]
    
    for i in range(len(melodie)):
        simpleio.tone(pin_buzzer, melodie[i], duration=0.15)
        
# Vérifie si l'on doit arroser les fruits et les légumes.
def verification_humidite(humidite, spray_distance):
    if humidite < 55:
                spray_legumes()
                
# Arrose les fruits et les légumes. (buzzer pour simulation)
def spray_legumes():
        simpleio.tone(pin_buzzer, 349, duration=0.15)
        
        
#========================================== Fonctions de la porte ==========================================

# Ouvre la porte du frigo.
def ouverture_porte():
    porte.angle = 0

# Ferme la porte du frigo.
def fermeture_porte():
    porte.angle = 100
    
# Controle de la porte
def controle_porte(porte_ouverte):
    #Transforme l'ouverture de la porte en bool
    if porte_ouverte:
        ouverture_porte()
        # Allume la lumière
        led.color = (0,0,0)
        music_zelda()
        # Retoune une valeur pour compter le nombre d'ouverture.
        return 1
    else:
        fermeture_porte()
        # Ferme la lumière.
        led.color = (255,255,255)
        # Retoune une valeur pour compter le nombre d'ouverture.
        return 0

#========================================== Fonctions du moteur (refroidissement) ==========================================

# Vérifie si le frigo est assez froid.
def refroidissement(temp):
    # Donne une valeur de 0 a 1 selon la temperature 
    val_moteur = (temp - 5) /5
    # S'assure que la valeur soit entre 0 et 1
    if val_moteur < 0:
        val_moteur = 0
    elif val_moteur > 1:
        val_moteur = 1
    moteur.throttle = val_moteur
    return val_moteur * 100

#========================================== Fonctions du reservoir ==========================================
def pourcent_capt(val_capt):
    # Normaliser en % la valeur du capteur
    pourcent_eau = (val_capt - 15000)/12500 * 100
    if pourcent_eau < 0:
        pourcent_eau = 0
    elif pourcent_eau > 100:
        pourcent_eau = 100
    return pourcent_eau  

# Utilise la pompe pour remplir le reservoir d'eau jusqu'à 100%.
def remplir_reservoir(pourcent_capt):
    # Tant qu'elle n'arrive pas 100%, continuer de remplir le reservoir 
    if pourcent_capt < 100:
        pompe.value = True
        return True
    else:
        pompe.value = False
        return False

#========================================== Fonctions de l'affichage ==========================================

# Fonction qui affiche les information a l'écran
def affichage(temp, hum, moteur, nb_ouverture, reservoir):
    text = "Temperature = {0} \nHumidité = {1} \nMoteur = {2} \nNb ouverture = {3} \nReservoir = {4}".format(temp, hum, moteur, nb_ouverture, reservoir)
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=2)
    text_area.x = 10
    text_area.y = 7
    board.DISPLAY.show(text_area)