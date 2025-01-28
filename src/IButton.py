from abc import ABC

class IButton(ABC):

    def on_press(self) -> None:
        pass

    def on_release(self) -> None:
        pass