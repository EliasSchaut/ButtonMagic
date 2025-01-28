
from src.IButton import IButton

class Test(IButton):

    def on_press(self):
        print("Pressed")

    def on_release(self):
        print("Released")
