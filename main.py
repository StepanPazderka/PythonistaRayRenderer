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
from material import Material
import canvas

def main():
	console.clear()
	canvas.clear()
	multiplier = 0.6
	WIDTH = 1920
	HEIGHT = 1080
	camera = Vector(0,0,-1)
	objects = [Sphere(Point(0,0,1.0), 0.3, Color.from_hex("#F24F00")), Sphere(Point(0.2,0,0.4), 0.1, Color.from_hex("#224F00")), Sphere(Point(-0.25,0.0,0.4), 0.1, Color.from_hex("#1f8fd8")), Sphere(Point(0.4,-0.9,1.7), 0.6, Color.from_hex("#d80cac")), Sphere(Point(-0.4,-0.9,1.7), 0.6, Color.from_hex("#d8b63e"))]
	scene = Scene(camera, objects, WIDTH, HEIGHT)
	engine = RenderEngine()
	image = engine.render(scene, 10)
	#print(image)
	#show_render(image)
			
def show_render(image):
	canvas.set_aa_enabled(False)
	canvas.set_size(image.width, image.height)
	
	for y, pixel in enumerate(image.pixels):
		for x, pixel in enumerate(image.pixels[y]):
			try:
				canvas.set_fill_color(pixel.x, pixel.y, pixel.z)
				canvas.fill_rect(x, y, 1, 1)
			except:
				pass
		
if __name__ == "__main__":
	main()
