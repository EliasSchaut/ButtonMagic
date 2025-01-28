import os

from src.IButton import IButton

class DisplayToggle(IButton):

    toggled: bool = False

    def on_press(self):
        if self.toggled:
            self.turn_display_on()
        else:
            self.turn_display_off()
        self.toggled = not self.toggled

    def turn_display_on(self):
        os.system("echo 0 | sudo tee /sys/class/backlight/*/bl_power")

    def turn_display_off(self):
        os.system("echo 1 | sudo tee /sys/class/backlight/*/bl_power")
