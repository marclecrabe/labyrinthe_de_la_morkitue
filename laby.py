from maqueen import *
from microbit import *
import utime

# Constantes
blanco = 0
negro = 1
BACKWARD = 1
FORWARD = 0
# Variable globale
Init = True
final = False
visto = False

#def motor_run(motor: int, speed: int, dir: int = Direction.FORWARD):

def look():
    return [line_sensor(LineSensor.L1),line_sensor(LineSensor.M),line_sensor(LineSensor.R1)]

def mur_attention():
    if look() != [blanco,blanco,blanco]:
        visto = True

def tourner():
    if visto == True:
         motor_stop()
         #motor_run(Motor.LEFT,speed, FORWARD)
         
def En_avant_vers_le_bout_du_monde():
    look()
    mur_attention()
    motor_run(Motor.LEFT,speed,FORWARD)
    motor_run(Motor.RIGHT,speed,FORWARD)
         
#MAMA GUEVO on est là biloute, cara de verga

while True:
    if Init:
        # Vitesse maximale des moteurs
        speed:int = 40   
        speed_slow:int = 12 
        Init = False
    
    En_avant_vers_le_bout_du_monde()
    utime.sleep(10)