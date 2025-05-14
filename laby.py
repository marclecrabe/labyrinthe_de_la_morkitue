'''🇪 🇱  🇬 🇦 🇹 🇴  🇨 🇴 🇳  🇧 🇴 🇹 🇦 🇸
code de marque_le_crabe et alex_lamourtardededijon
labyrinthe maqueen'''

from maprincess import *
from microbit import *
import utime
#from el_proto_del_minigato import *


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

#test premiere stra
# deuxieme strat suivre le mur sur la gauche, MÉLENCHON!    
def mira_las_paredes():
    print ([line_sensor(LineSensor.L2),line_sensor(LineSensor.L1),line_sensor(LineSensor.M),line_sensor(LineSensor.R1),line_sensor(LineSensor.R2)])
    return [line_sensor(LineSensor.L2),line_sensor(LineSensor.L1)]

def direction_en_espagnol():
    mira = mira_las_paredes()
    print(mira)
    if mira == [WHITE,WHITE]:
        motor_run(Motor.LEFT,speed_slow,BACKWARD)
        motor_run(Motor.RIGHT,speed,FORWARD)
    elif mira == [BLACK,WHITE]:
        motor_run(Motor.LEFT,speed,FORWARD)
        motor_run(Motor.RIGHT,speed-moins,FORWARD)
    elif mira == [WHITE,BLACK]:
        print("mama guevo")
    elif mira == [BLACK,BLACK]:
        motor_run(Motor.RIGHT,speed,BACKWARD)
        motor_run(Motor.LEFT,speed, FORWARD)
        sleep(face)
    sleep(lapse)
#MAMA GUEVO = DANGER
led_rgb(rgb(255,255,255))

face = 1
lapse = 1
dodo = 1

while True:
    if Init:
        # Vitesse maximale des moteurs
        speed:int = 80
        speed_slow:int = 14
        moins=sp
        Init = False
    direction_en_espagnol()
    sleep(dodo)