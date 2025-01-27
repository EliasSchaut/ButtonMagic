from gpiozero import Button
import os
from signal import pause

button = Button(5, bounce_time=0.05)
toggled = False


def turn_display_on():
    os.system("echo 0 | sudo tee /sys/class/backlight/*/bl_power")

def turn_display_off():
    os.system("echo 1 | sudo tee /sys/class/backlight/*/bl_power")

def on_button_released():
    global toggled
    if toggled:
        turn_display_on()
    else:
        turn_display_off()
    toggled = not toggled

button.when_pressed = on_button_released

if __name__ == '__main__':
    print("Monitoring button on GPIO5...")
    pause()
