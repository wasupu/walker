#!/usr/bin/env python3
import ev3dev2
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent


def main():
    sound = Sound()
    sound.speak('Welcome to the E V 3 dev project!')

    tank_drive = MoveTank(OUTPUT_A, OUTPUT_B, motor_class=ev3dev2.motor.MediumMotor)
    tank_drive.on_for_seconds(SpeedPercent(-150), SpeedPercent(150), 5)


main()
