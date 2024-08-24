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
ultrasonic = UltrasonicSensor(Port.S2)
robot = DriveBase(left_motor, right_motor, wheel_diameter=41, axle_track=170)
gyro = GyroSensor(Port.S3)
color = ColorSensor(Port.S1)

matriz = [[0 for _ in range(6)] for _ in range(8)]

gyro.reset_angle(0)
#medium_motor.run_target(900, 3000)
cont = 0
ignore_blue = False
comeco = False
while not comeco and color.color() == Color.BLUE:
    correction = (0 - gyro.angle()) * 2.5
    robot.drive(150, correction)
    if color.color() == Color.WHITE:
        comeco = True

while True:
    correction = (0 - gyro.angle()) * 2.5
    robot.drive(150, correction)
    
    if color.reflection() < 30 or color.color() == Color.BLACK and color.color() != Color.BLUE and color.color() != Color.YELLOW and color.color() != Color.WHITE:
        robot.stop()
        while gyro.angle() > -88:
            robot.drive(0, -100)
        robot.stop()
        gyro.reset_angle(0)
    wait(10)
    
    if color.color() == Color.YELLOW:
        robot.stop()
        while gyro.angle() < 88:
            robot.drive(0, 100)
        robot.stop()
        gyro.reset_angle(0)
    wait(10)
    
    if color.color() == Color.BLUE and not ignore_blue:
        robot.stop()
        while gyro.angle() < 85:
            robot.drive(0, 100)
        robot.stop()
        gyro.reset_angle(0)
        
        while True:
            robot.drive(100, correction)
            if color.reflection() < 10 and color.color() != Color.BLUE:
                robot.stop()
                robot.straight(-105)
                gyro.reset_angle(0)
                
                while gyro.angle() > -80:
                    robot.drive(0, -100)
                robot.stop()
                gyro.reset_angle(0)
                break
        
        cont = 0 
        
        while cont < 3:
            robot.drive(90, correction)
            if ultrasonic.distance() <= 30: 
                cont += 1  
                wait(1000)  
        
        robot.stop()
        left_motor.brake()
        right_motor.brake()
        medium_motor.run_until_stalled(-5000, duty_limit=50)
        wait(1000)  

        while gyro.angle() > -88:
            robot.drive(0, -100)
        robot.stop()
        gyro.reset_angle(0)
        
        ignore_blue = True
    
    wait(10)
# while True:
#     print(color.reflection())