# pyright: reportShadowedImports=false
#========================================== Déclaration des imports ==========================================
# Import pour la connexion
import ssl
import wifi
import socketpool
import adafruit_requests

# Import pour la mort de JL
import time
import board
import analogio
from digitalio import DigitalInOut, Direction, Pull

# DHT
import adafruit_dht

# Moteur
import pwmio
from adafruit_motor import servo, motor

# Led et buzzer
import simpleio
import adafruit_rgbled

#========================================== Déclaration des capteurs ==========================================

# Déclaration de la switch
# switch = DigitalInOut(board.D13)
# switch.direction = Direction.INPUT
# switch.pull = Pull.DOWN

# Déclaration du bouton
bouton = DigitalInOut(board.A0)
bouton.direction = Direction.INPUT
bouton.pull = Pull.DOWN

# Initial the dht device, with data pin connected to:
dht = adafruit_dht.DHT11(board.D10)

# Déclaration du capteur d'eau
# capteur_eau = analogio.AnalogIn(board.D5)


#========================================== Déclaration des actuateurs ==========================================

#Déclarer le buzzer
pin_buzzer = board.D11

# Déclarer moteur DC
pwm_moteur1 = pwmio.PWMOut(board.A2)
pwm_moteur2 = pwmio.PWMOut(board.A3)
moteur = motor.DCMotor(pwm_moteur1, pwm_moteur2)
moteur.throttle = 0

# Déclaration de la del
RED_PIN = board.D9
GREEN_PIN = board.D6
BLUE_PIN = board.D5

led = adafruit_rgbled.RGBLED(RED_PIN, GREEN_PIN,BLUE_PIN)

# Déclaration de la pompe
# pompe = DigitalInOut(board.A3)
# pompe.direction = Direction.OUTPUT

# Déclaration du servomoteurs
servo_pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
porte = servo.Servo(servo_pwm, min_pulse=500, max_pulse= 2500)
porte.angle = 0

#========================================== Gestion du wifi ==========================================

timerWifi = time.monotonic()

key = "O1MV7NRO1B07USO7"
URL = "https://api.thingspeak.com/update.json"

socket = socketpool.SocketPool(wifi.radio)
context = ssl.create_default_context()
https = adafruit_requests.Session(socket, context)

