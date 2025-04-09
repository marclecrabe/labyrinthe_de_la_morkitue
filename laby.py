from maqueen import *
from microbit import *
import utime

'''
   /''''^''''\
  /  L1 M R1  \
 |             |
 |L2         R2|
o|.............|o

'''
# Constantes
WHITE = 0
BLACK = 1
BACKWARD = 1
FORWARD = 0
# Variable globale
Init = True
final = False
visto = False
#def motor_run(motor: int, speed: int, dir: int = Direction.FORWARD):


def look():
    print ([line_sensor(LineSensor.L1),line_sensor(LineSensor.M),line_sensor(LineSensor.R1)])
    return [line_sensor(LineSensor.L1),line_sensor(LineSensor.M),line_sensor(LineSensor.R1)]


def mur_attention():
    global visto
    if look() != [WHITE,WHITE,WHITE]:
        print("Achtung")
        motor_stop(Motor.ALL)
        sleep(100)
        motor_run(Motor.RIGHT,0,FORWARD)
        motor_run(Motor.LEFT,speed, FORWARD)

def En_avant_vers_le_bout_du_monde():
    mur_attention()
    sleep(500)
    motor_run(Motor.LEFT,speed,FORWARD)
    motor_run(Motor.RIGHT,speed,FORWARD)
     
#MAMA GUEVO on est là biloute$
    
led_rgb(rgb(255,255,255))

while True:
    if Init:
        # Vitesse maximale des moteurs
        speed:int = 20   
        speed_slow:int = 12 
        Init = False
    
    En_avant_vers_le_bout_du_monde()
    sleep(10)