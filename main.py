#!/usr/bin/env python

import console
from vector import Vector
from point import Point
from color import Color
from sphere import Sphere
from ray import Ray
from engine import RenderEngine
from image import Image
from custom_scene import Scene
import canvas

def main():
	console.clear()
	WIDTH = 400
	HEIGHT = 250
	camera = Vector(0,0,-1)
	objects = [Sphere(Point(0,0.5,1.5), 0.5, Color.from_hex("#224F00"))]
	scene = Scene(camera, objects, WIDTH, HEIGHT)
	engine = RenderEngine()
	image = engine.render(scene)
	#print(image)
	show_render(image)
			
def show_render(image):
	canvas.clear()
	canvas.set_aa_enabled(False)
	canvas.set_size(image.width, image.height)
	
	for y, pixel in enumerate(image.pixels):
		for x, pixel in enumerate(image.pixels[y]):
			try:
				canvas.set_fill_color(pixel.x, pixel.y, pixel.z)
				#print(pixel)
				canvas.fill_rect(x, y, 1, 1)
			except:
				pass
				#print(str(x) + " " + str(y))
			
		
if __name__ == "__main__":
	main()
