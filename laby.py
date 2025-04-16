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


'''def look():
    print ([line_sensor(LineSensor.L1),line_sensor(LineSensor.M),line_sensor(LineSensor.R1)])
    return [line_sensor(LineSensor.L1),line_sensor(LineSensor.M),line_sensor(LineSensor.R1)]'''


'''def mur_attention():
    global visto
    if look() != [WHITE,WHITE,WHITE]:
        print("Achtung")
        #motor_stop(Motor.ALL)
        sleep(10)
        motor_run(Motor.RIGHT,0,BACKWARD)
        motor_run(Motor.LEFT,30, FORWARD)'''

'''def En_avant_vers_le_bout_du_monde():  
    mur_attention()
    sleep(600)
    motor_run(Motor.LEFT,speed,FORWARD)
    motor_run(Motor.RIGHT,speed,FORWARD)'''
    
def mira_las_paredes():
    print ([line_sensor(LineSensor.L2),line_sensor(LineSensor.L1),line_sensor(LineSensor.M),line_sensor(LineSensor.R1),line_sensor(LineSensor.R2)])
    return [line_sensor(LineSensor.L2),line_sensor(LineSensor.M)]

def direction_en_espagnol():
    mira = mira_las_paredes()
    print(mira)
    if mira == [WHITE,WHITE]:
        motor_run(Motor.LEFT,speed_slow,BACKWARD)
        motor_run(Motor.RIGHT,speed,FORWARD)
    elif mira == [BLACK,WHITE]:
        motor_run(Motor.LEFT,speed,FORWARD)
        motor_run(Motor.RIGHT,speed,FORWARD)
    elif mira == [WHITE,BLACK]:
        print("mama guevo")
    elif mira == [BLACK,BLACK]:
        motor_run(Motor.RIGHT,speed,BACKWARD)
        motor_run(Motor.LEFT,speed, FORWARD)
        sleep(300)
    sleep(100)

#MAMA GUEVO on est là biloute
    
led_rgb(rgb(255,255,255))

'''while True:
    if Init:
        # Vitesse maximale des moteurs
        speed:int = 25   
        speed_slow:int = 12 
        Init = False
    
    En_avant_vers_le_bout_du_monde()
    sleep(10)'''


while True:
    if Init:
        # Vitesse maximale des moteurs
        speed:int = 40   
        speed_slow:int = 10
        Init = False
    direction_en_espagnol()
    sleep(10)
    
