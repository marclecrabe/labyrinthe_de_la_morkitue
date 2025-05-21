'''🇪 🇱  🇬 🇦 🇹 🇴  🇨 🇴 🇳  🇧 🇴 🇹 🇦 🇸
code de marque_le_crabe et alex_lamourtardededijon
labyrinthe maqueen'''

from maprincess import *
from microbit import *
import utime
# from el_proto_del_minigato import *

'''
   /''''^''''\
  /   1 2 3   \
 |             |
 |0           4|
o|.............|o

'''
# Constantes
WHITE = 0
BLACK = 1
BACKWARD = 1
FORWARD = 0
'''userId = 12
destId = 20'''

# Variable globale
Init = True
final = False
visto = False

# deuxieme strat suivre le mur sur la gauche, MÉLENCHON!    
def mira_las_paredes():
    return [line_sensor(LineSensor.L2),line_sensor(LineSensor.L1),line_sensor(LineSensor.M),line_sensor(LineSensor.R1),line_sensor(LineSensor.R2)]

def direction_en_espagnol():
    if mira_las_paredes()[2] == BLACK:
        motor_run(Motor.RIGHT,speed,BACKWARD)
        motor_run(Motor.LEFT,speed, FORWARD)
    elif mira_las_paredes()[1] == BLACK:
        motor_run(Motor.RIGHT,speed_ss,BACKWARD)
        motor_run(Motor.LEFT,speed,FORWARD)
    elif mira_las_paredes()[0] == WHITE:
        motor_run(Motor.LEFT,speed,BACKWARD)
        motor_run(Motor.RIGHT,speed,FORWARD)
    elif mira_las_paredes()[0] == BLACK:
        motor_run(Motor.LEFT,speed_m,FORWARD)
        motor_run(Motor.RIGHT,speed_s,FORWARD)

a = 1.7

led_rgb(rgb(255,255,255))

speed_ff:int = int(a*150)
speed_f:int = int(a*120)
speed:int = int(a*100)
speed_m:int = int(a*60)
speed_s:int = int(a*40)
speed_ss:int = int(a*20)

while True:
    direction_en_espagnol()
