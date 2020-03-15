

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Rectangle

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        color = (random(), random(), random())
        self.canvas.clear()
        with self.canvas: # area where things can be drawn
            # usually rgb ([0, 255], [0, 255], [0, 255])
            #Color(*color, mode='hsv') # sets random color
            size = (80.0, 80.0)
            Rectangle(
                    source="leo.png",
                    pos=(touch.x - size[0]/2, touch.y - size[1]/2), 
                    size=size)
            # dictionary for touch that allows users to store attributes
            # for touch
            touch.ud["line"] = Line(points=(touch.x, touch.y))
    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text="Clear")
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent
    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == "__main__":
    MyPaintApp().run()
