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
gyro = GyroSensor(Port.S3)
color = ColorSensor(Port.S1)
# gyro.reset_angle(0)
# print(gyro.angle())

# while gyro.angle() < 90:
#     print(gyro.angle())
#     robot.drive(250,100)

# robot.stop()
# left_motor.brake()
# right_motor.brake() #Utilizando o sensor giroscopio para fazer uma curva de 90 graus.
 
while color.reflection() > 15:
    robot.drive(100,0)
robot.stop()
left_motor.brake()
right_motor.brake()