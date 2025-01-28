from importlib import import_module
from gpiozero import Button
from signal import pause
import actions

button = Button(5, bounce_time=0.01)

def load_button_classes():
    action_classes = []
    for action in actions.__all__:
        module = import_module(f'actions.{action}')
        action_classes.append(getattr(module, action)())
    return action_classes

action_classes = load_button_classes()

def on_button_pressed():
    for button_class in action_classes:
        button_class.on_press()

def on_button_released():
    for button_class in action_classes:
        button_class.on_release()

button.when_pressed = on_button_pressed
button.when_released = on_button_released

if __name__ == '__main__':
    print("Monitoring button on GPIO5...")
    pause()
