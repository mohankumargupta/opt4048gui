#!/usr/bin/env python

# For raspberry pi. LIBGL_ALWAYS_SOFTWARE=1 python main.py

import pyglet
from dataclasses import dataclass
from colormath.color_objects import XYZColor, sRGBColor
from colormath.color_conversions import convert_color
from opt4048gui import qwiic_opt4048
import sys
import time


@dataclass
class RGBColor:
    r: int = 0
    g: int = 0
    b: int = 0


class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(800, 600)
        self.opt4048 = qwiic_opt4048.QwOpt4048()
        if not self.opt4048.is_connected():
            print("cant find opt4048")
            sys.exit(1)
        if not self.opt4048.begin():
            print("cant talk to opt4048")
            sys.exit(2)
        self.opt4048.set_basic_setup()
        self.color = RGBColor()
        self.square = pyglet.shapes.Rectangle(
            x=300, y=100, width=200, height=200, color=(255, 255, 255, 255)
        )
        self.labelX = pyglet.text.Label(
            "X:",
            font_name="Times New Roman",
            font_size=36,
            x=50,
            y=520,
        )
        self.labelY = pyglet.text.Label(
            "Y:",
            font_name="Times New Roman",
            font_size=36,
            x=50,
            y=450,
        )
        self.labelZ = pyglet.text.Label(
            "Z:",
            font_name="Times New Roman",
            font_size=36,
            x=50,
            y=380,
        )
        self.labelXValue = pyglet.text.Label(
            "0.00",
            font_name="Arial",
            font_size=36,
            color=(255, 0, 0, 255),
            x=115,
            y=520,
        )
        self.labelYValue = pyglet.text.Label(
            "0.00",
            font_name="Arial",
            color=(0, 255, 0, 255),
            font_size=36,
            x=115,
            y=450,
        )
        self.labelZValue = pyglet.text.Label(
            "0.00",
            font_name="Arial",
            font_size=36,
            x=115,
            y=380,
            color=(0, 0, 255, 255),
        )

    def on_draw(self):
        self.clear()
        self.labelX.draw()
        self.labelY.draw()
        self.labelZ.draw()
        self.labelXValue.draw()
        self.labelYValue.draw()
        self.labelZValue.draw()
        self.square.draw()

    def update(self, dt):
        x, y, z = self.opt4048.get_CIE_color()
        total = x + y + z
        normalized_x = x / total
        normalized_y = y / total
        normalized_z = z / total
        xyz = XYZColor(normalized_x, normalized_y, normalized_z)
        #xyz = XYZColor(41.246 / 100, 21.267 / 100, 1.933 / 100)
        rgb = convert_color(xyz, sRGBColor)
        r = int(rgb.rgb_r * 255)
        g = int(rgb.rgb_g * 255)
        b = int(rgb.rgb_b * 255)
        print(r, g, b)
        self.labelXValue.text = str(round(xyz.xyz_x, 5))
        self.labelYValue.text = str(round(xyz.xyz_y, 5))
        self.labelZValue.text = str(round(xyz.xyz_z, 5))
        self.square.color = (r, g, b, 255)


def main():
    window = HelloWorldWindow()
    pyglet.clock.schedule_interval(window.update, 1.0)
    pyglet.app.run()


if __name__ == "__main__":
    main()
    
