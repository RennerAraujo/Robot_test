#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()

left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
medium_motor = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter=41, axle_track = 170)

# while robot.distance() < 300:
#     robot.drive(100,0)
# robot.stop()
# left_motor.brake()
# right_motor.brake()
# wait(2000)
# robot.turn(75) #Fazer o robô andar enquanto a distancia for menor que 300 e girar depois de 2 segundos

# while True:
#     if Button.CENTER in ev3.buttons.pressed():
#         robot.straight(200)
#         wait(500)
#     else:
#         robot.drive(0, 50)
