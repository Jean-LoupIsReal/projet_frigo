# pyright: reportShadowedImports=false
import ssl
import wifi
import socketpool
import adafruit_requests
import time
import board
import analogio
from digitalio import DigitalInOut, Direction, Pull
import pwmio
import adafruit_dht
from adafruit_motor import servo, motor

#========================================== Déclaration des capteurs ==========================================

# Déclaration de la switch
switch = DigitalInOut(board.D13)
switch.Direction = Direction.INPUT
switch.Pull = Pull.DOWN

# Déclaration du bouton
bouton = DigitalInOut(board.D12)
bouton.Direction = Direction.INPUT
bouton.Pull = Pull.DOWN

# Initial the dht device, with data pin connected to:
dht = adafruit_dht.DHT11(board.D6)

# Déclaration du capteur d'eau
capteur_eau = analogio.AnalogIn(board.D5)

#========================================== Déclaration des actuateurs ==========================================

#Déclarer le buzzer
pin_buzzer = board.D13

# Déclarer moteur DC
pwm_moteur1 = pwmio.PWMOut(board.A0)
pwm_moteur2 = pwmio.PWMOut(board.A1)
moteur = motor.DCMotor(pwm_moteur1, pwm_moteur2)
moteur.throttle = 0

# Déclaration de la del
Del = DigitalInOut(board.A2)
Del.Direction = Direction.OUTPUT
Del.value = False

# Déclaration de la pompe
pompe = DigitalInOut(board.A3)
pompe.Direction = Direction.OUTPUT
pompe.value = False

# Déclaration du servomoteurs
servo_pwm = pwmio.PWMOut(board.A4, duty_cycle=2 ** 15, frequency=50)
porte = servo.Servo(servo_pwm, min_pulse=500, max_pulse= 2500)
porte.angle = 0

#========================================== Gestion du wifi ==========================================

timerWifi = time.monotonic()

key = "O1MV7NRO1B07USO7"
URL = "https://api.thingspeak.com/update.json"

socket = socketpool.SocketPool(wifi.radio)
context = ssl.create_default_context()
https = adafruit_requests.Session(socket, context)

