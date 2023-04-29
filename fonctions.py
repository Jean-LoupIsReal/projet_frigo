from init_projet import *
import simpleio
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


#========================================== Fonctions du buzzer ==========================================

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
        

def spray_legumes():
        simpleio.tone(pin_buzzer, 349, duration=0.15)
        
        
#========================================== Fonctions de la porte ==========================================

# Fonction qui permet d'ouvrir la porte du frigot
def ouverture_porte():
    porte.angle = 120
    
    
# Fonction qui permet de fermer la porte du frigot
def fermeture_porte():
    porte.angle = 0
    
    
# Fonction qui controle la porte
def controle_porte(porte_ouverte):
    #Transforme l'ouverture de la porte en bool
    if porte_ouverte:
        ouverture_porte()
    else:
        fermeture_porte()


#========================================== Fonctions du moteur (refroidissement) ==========================================

# Fonction qui permet de verifier quand verifier.
def verification_refroidissement(temp):
    # Si la temperature est sous 10 degré, 
    if temp > 10:
        # Commence le refroidissement.
        return refroidissement(temp)

# Fonction qui refroidis le frigo jusqu'a 9 degré.
def refroidissement(temp):
    if temp > 9:
        relais_moteur.value = True
    else:
        relais_moteur.value = False


#========================================== Fonctions du reservoir ==========================================
def pourcent_capt(val_capt):
    # Normaliser en % la valeur du capteur
    pass
    

# Utilise la pompe pour remplir le reservoir d'eau jusqu'à 100%.
def remplir_reservoir(pourcent_capt):
    # Tant qu'elle n'arrive pas 100%, continuer de remplir le reservoir 
    if pourcent_capt < 100:
        #
        pass
    else:
        pass


#========================================== Fonctions de l'affichage ==========================================

# Fonction qui affiche les information a l'écran
def affichage(temp, ):
    pass


#========================================== Fonctions bonus ==========================================
