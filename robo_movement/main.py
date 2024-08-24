
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Definição de motores (Inicialização do Programa)
ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
medium_motor = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter=41, axle_track = 170)

 medium_motor.run_target(900, 3000) (Fechar garra)
# left_motor.run_target(3000,610)(curva de 90 graus para esqueda)
# robot.turn(75) # (90 graus perfeito, sendo diferença de 15 graus)
# robot.straight(250) #(Andar reto)
# robot.stop left_motor.brake() right_motor.brake() # Parada com mais precisão

# robot.straight(250)
# robot.turn(-75)
# robot.straight(250)
# robot.turn(-75)
# robot.straight(250)
# robot.turn(-75)
# robot.straight(250)
# robot.turn(-75) # Teste do quadrado