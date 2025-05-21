'''🇪 🇱  🇬 🇦 🇹 🇴  🇨 🇴 🇳  🇧 🇴 🇹 🇦 🇸
code de marque le crabe et alex_lamourtardededijon
labyrinthe maqueen'''
from maqueen import*
from microbit import*
import utime
'''
   /^  /  L1 M R1   |             |
 |L2         R2|
o|.............|o
'''=0
BLACK=1
BACKWARD=1
FORWARD=0
Init=True
final=False
visto=False
def mira_las_paredes():
 print([line_sensor(LineSensor.L2),line_sensor(LineSensor.L1),line_sensor(LineSensor.M),line_sensor(LineSensor.R1),line_sensor(LineSensor.R2)])
 return[line_sensor(LineSensor.L2),line_sensor(LineSensor.L1)]
def direction_en_espagnol():
 mira=mira_las_paredes()
 print(mira)
 if mira==[WHITE,WHITE]:
  motor_run(Motor.LEFT,speed_slow,BACKWARD)
  motor_run(Motor.RIGHT,speed,FORWARD)
 elif mira==[BLACK,WHITE]:
  motor_run(Motor.LEFT,speed,FORWARD)
  motor_run(Motor.RIGHT,speed,FORWARD)
 elif mira==[WHITE,BLACK]:
  print("mama guevo")
 elif mira==[BLACK,BLACK]:
  motor_run(Motor.RIGHT,speed,BACKWARD)
  motor_run(Motor.LEFT,speed,FORWARD)
  sleep(300)
 sleep(100)
led_rgb(rgb(255,255,255))
while True:
 if Init:
  speed:int=30
  speed_slow:int=8
  Init=False
 direction_en_espagnol()
 sleep(10)
# Created by pyminifier (https://github.com/dzhuang/pyminifier3)
