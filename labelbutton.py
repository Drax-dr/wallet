from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from kivy.uix.label import Label


class LabelButton(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(LabelButton, self).__init__(**kwargs)

    def animation_label(self) -> None:
        def set_default_state_label(*args):
            Animation(opacity=1, d=0.1, t="in_cubic").start(self)

        anim = Animation(opacity=0.5, d=0.2, t="in_elastic")
        anim.bind(on_complete=set_default_state_label)
        anim.start(self)

    def on_press(self, **args):
        self.animation_label()

class ReactButton(ButtonBehavior):
    def __init__(self):
        super(ReactButton).__init__()

    def animate(self) -> None:
        pass