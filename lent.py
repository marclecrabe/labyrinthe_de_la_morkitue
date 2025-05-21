'''🇪 🇱  🇬 🇦 🇹 🇴  🇨 🇴 🇳  🇧 🇴 🇹 🇦 🇸
code de marque_le_crabe et alex_lamourtardededijon
labyrinthe maqueen'''

from maprincess import *
from microbit import *
import utime
from el_proto_del_minigato import *

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
userId = 12
destId = 20
# Variable globale
Init = True
final = False
visto = False

# deuxieme strat suivre le mur sur la gauche, MÉLENCHON!    
def mira_las_paredes():
    return [line_sensor(LineSensor.L2),line_sensor(LineSensor.L1)]

def direction_en_espagnol():
    if mira_las_paredes() == [BLACK,BLACK]:
        motor_run(Motor.RIGHT,speed_ff,BACKWARD)
        motor_run(Motor.LEFT,speed_ff, FORWARD)
    
    elif mira_las_paredes() == [BLACK,WHITE]:
        motor_run(Motor.RIGHT,speed_ss,FORWARD)
        motor_run(Motor.LEFT,speed_ff,FORWARD)
    
    elif mira_las_paredes() == [WHITE,WHITE]:
        motor_run(Motor.LEFT,speed_s,BACKWARD)
        motor_run(Motor.RIGHT,speed_m,FORWARD)
    
    elif mira_las_paredes() == [WHITE,BLACK]:
        motor_run(Motor.RIGHT,speed_m,BACKWARD)
        motor_run(Motor.LEFT,speed_f, FORWARD)
        print("mama guevo")

a = 1.7

while True:
    if Init:
        # Vitesse maximale des moteurs
        speed_ff:int = int(a*150)
        speed_f:int = int(a*120)
        speed:int = int(a*100)
        speed_m:int = int(a*60)
        speed_s:int = int(a*40)
        speed_ss:int = int(a*20)
        Init = False
        led_rgb(rgb(255,255,255))

    direction_en_espagnol()

