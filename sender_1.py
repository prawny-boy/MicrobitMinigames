# Revised sender_mb_1.py (Upload this to Micro:bit 1)

from microbit import *
import radio

MICROBIT_ID = "MB1"

radio.on()
radio.config(group=23) # <<< ENSURE THIS MATCHES YOUR GATEWAY

while True:
    # Read all sensor data and button states
    accel_x = accelerometer.get_x()
    accel_y = accelerometer.get_y()
    accel_z = accelerometer.get_z()
    button_a_pressed = button_a.is_pressed()
    button_b_pressed = button_b.is_pressed()

    # Send each piece of data as a separate, smaller radio message
    # Adding small sleeps between sends to avoid overwhelming the radio or receiver
    radio.send("{}_AX:{}".format(MICROBIT_ID, accel_x))
    sleep(10)
    radio.send("{}_AY:{}".format(MICROBIT_ID, accel_y))
    sleep(10)
    radio.send("{}_AZ:{}".format(MICROBIT_ID, accel_z))
    sleep(10)
    radio.send("{}_BA:{}".format(MICROBIT_ID, int(button_a_pressed)))
    sleep(10)
    radio.send("{}_BB:{}".format(MICROBIT_ID, int(button_b_pressed)))
    sleep(50) # Longer delay after sending all items, before starting next full cycle
