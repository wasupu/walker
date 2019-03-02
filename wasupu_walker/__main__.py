#!/usr/bin/env python3
import time, sched
import ev3dev2
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sound import Sound

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B, motor_class=ev3dev2.motor.MediumMotor)
front_ultrasonic_sensor = UltrasonicSensor("in1")
back_ultrasonic_sensor = UltrasonicSensor("in2")


def main():
    sound = Sound()
    sound.speak('Start program')

    front_ultrasonic_sensor_scheduler = sched.scheduler(time.time, time.sleep)
    front_ultrasonic_sensor_scheduler \
        .enter(1, 1,
               check_front_distance,
               (front_ultrasonic_sensor_scheduler,))

    back_ultrasonic_sensor_scheduler = sched.scheduler(time.time, time.sleep)
    back_ultrasonic_sensor_scheduler \
        .enter(1, 1,
               check_back_distance,
               (back_ultrasonic_sensor,))

    go_ahead()

    time.sleep(30)
    tank_drive.stop()


def check_front_distance(front_ultrasonic_sensor_scheduler):
    front_distance = front_ultrasonic_sensor.distance_centimeters()

    if front_distance < 25:
        turn_left()
        go_ahead()

    front_ultrasonic_sensor_scheduler \
        .enter(1, 1,
               check_front_distance,
               (front_ultrasonic_sensor, front_ultrasonic_sensor_scheduler))


def check_back_distance(back_ultrasonic_sensor_scheduler):
    back_distance = back_ultrasonic_sensor.distance_centimeters()

    if back_distance < 25:
        turn_left()
        go_ahead()

    back_ultrasonic_sensor_scheduler \
        .enter(1, 1,
               check_back_distance,
               (back_ultrasonic_sensor, back_ultrasonic_sensor_scheduler))


def go_ahead():
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(100), 5)


def turn_left():
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(100), 2)


main()
