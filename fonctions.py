from init_projet import *
import terminalio
from adafruit_display_text import bitmap_label

#========================================== Fonction du wifi ==========================================

# Fonction qui gère l'envois de l'information à internet
def envoisWifi(temp):
    global timerWifi
    if timerWifi + 5 <= time.monotonic():
        json_data = {
            "api_key" : key,
            "field1": temp
        }
        try:
            response = https.post(URL, json = json_data)
        except:
            print("probleme wifi")
        timerWifi = time.monotonic()


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
        
# Vérifie si l'on doit aroser les légumes.
def verification_humidite(humidite):
    if humidite < 55:
                # Arose les légumes. (buzzer pour simulation)
                spray_legumes()
                
# Arose les légumes. (simuler par buzzer)
def spray_legumes():
        simpleio.tone(pin_buzzer, 349, duration=0.15)
        
        
#========================================== Fonctions de la porte ==========================================

# Ouvre la porte du frigo.
def ouverture_porte():
    porte.angle = 120

# Ferme la porte du frigot.
def fermeture_porte():
    porte.angle = 0
    
# Controle de la porte
def controle_porte(porte_ouverte):
    #Transforme l'ouverture de la porte en bool
    if porte_ouverte:
        ouverture_porte()
        led.color = (0,0,0)
        music_zelda()
    else:
        fermeture_porte()
        led.color = (255,255,255)

#========================================== Fonctions du moteur (refroidissement) ==========================================

# Vérifie si le frigo est assé froid.
def refroidissement(temp):
    # donne une valeur de 0 a 1 selon la temperature 
    val_moteur = (temp - 5) /5
    #s'assure que la valeur soit entre 0 et 1
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
def affichage(temp, moteur, nb_ouverture, reservoir):
    text = "Temperature = {0} \nMoteur = {1} \nNb ouverture = {2} \nReservoir = {3}".format(temp, moteur, nb_ouverture, reservoir)
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=2)
    text_area.x = 10
    text_area.y = 10
    board.DISPLAY.show(text_area)

