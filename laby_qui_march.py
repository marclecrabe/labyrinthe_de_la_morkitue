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
        motor_run(Motor.LEFT,speed_s,BACKWARD)
        motor_run(Motor.RIGHT,speed_f,FORWARD)
    elif mira == [BLACK,WHITE]:
        motor_run(Motor.LEFT,speed_m,FORWARD)
        motor_run(Motor.RIGHT,speed_m,FORWARD)
    elif mira == [WHITE,BLACK]:
        motor_run(Motor.RIGHT,speed_m,BACKWARD)
        motor_run(Motor.LEFT,speed_f, FORWARD)
        print("mama guevo")
    elif mira == [BLACK,BLACK]:
        motor_run(Motor.RIGHT,speed_ff,BACKWARD)
        motor_run(Motor.LEFT,speed_ff, FORWARD)
#         sleep(face)
    sleep(lapse)

def das_ende():
  #  sleep(dodo)
    u = ultrasonic()
    if u < 5 :
        u = ultrasonic()
  #      sleep(5)
        if u < 3 :
            print(u)
            motor_stop()
            payload = [69] 
            send_msg(73,payload,userId, destId)
            '''m = receive_msg(userId)
            if m and m.msgId==73 and len(m.payload) == 1:
                if m.payload[0]:
            the reciever of memories'''
            while True :
                print("bite")
                sleep(100)
#MAMA GUEVO = DANGER
led_rgb(rgb(255,255,255))

face = 1
lapse = 1
dodo = 1

while True:
    if Init:
        # Vitesse maximale des moteurs
        speed_ff:int = 150
        speed_f:int = 120
        speed:int = 100
        speed_m:int = 60
        speed_s:int = 40
        speed_ss:int = 20
        Init = False
    direction_en_espagnol()
#     sleep(dodo)
 #   das_ende()

    
    ''' rest a faire
- portocole (lllamar amigos)
- la bandera de Spain'''