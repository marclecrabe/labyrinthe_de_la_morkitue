from maqueen import *
from microbit import *
import utime

# Constantes
blanco = 0
negro = 1

# Variable globale
Init = True
final = False
visto = False

def mirar():
    return [line_sensor(LineSensor.L1),line_sensor(LineSensor.M),line_sensor(LineSensor.R1)]

def pared():
    if mirar() != [blanco,blanco,blanco]:
        visto = True

def jirar():
    if visto = True:
         motor_stop()
         motor_run(Motor.LEFT,speed						#MAMA GUEVO on est là biloute, cara de verga

def 
while True:
    if Init:
        # Vitesse maximale des moteurs
        speed:int = 40   
        speed_slow:int = 12 
        Init = False
        music.pitch(880,10)
        
    utime.sleep(10)
    
    pared()