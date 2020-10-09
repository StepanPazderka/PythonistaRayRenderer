from image import Image
from ray import Ray
from point import Point
from color import Color
from material import Material
import random
import canvas

class RenderEngine:
	"""Renders 3D objects into 2D objects"""
	def render(self, scene, samples):
		width = scene.width
		height = scene.height
		canvas.set_size(width, height)
		aspect_ratio = float(width) / height
		x0 = -1.0
		x1 = +1.0
		xstep = (x1 - x0) / (width - 1)
		y0 = -1.0 / aspect_ratio
		y1 = +1.0 / aspect_ratio
		ystep = (y1 - y0) / (height - 1)
		
		camera = scene.camera
		pixels = Image(width, height)
		
		heightRange = list(range(height))
		widthRange = list(range(width))
		
		#random.shuffle(heightRange)
		#random.shuffle(widthRange)
		
		for j in heightRange:
			y = y0 + j * ystep
			for i in widthRange:
				x = x0 + i * xstep
				renderedSamples = []
				for _ in range(samples):
					if samples > 1:
						ray = Ray(camera, Point(x+random.uniform(xstep*-1,xstep),y+random.uniform(xstep*-1,ystep)) - camera)
					else:
						ray = Ray(camera, Point(x,y) - camera)
					raytracedColorSample = self.ray_trace(ray, scene)
					renderedSamples.append(raytracedColorSample)
				finalPixel = sum(renderedSamples, Color(0,0,0)) / len(renderedSamples)
				pixels.set_pixel(i, j, finalPixel)
				canvas.set_fill_color(finalPixel.x, finalPixel.y, finalPixel.z)
				canvas.fill_rect(i, j, 1, 1)
		return pixels
		
	def ray_trace(self, ray, scene):
		color = Color(0, 0, 0)
		# Find the nearest object
		dist_hit, obj_hit = self.find_nearest(ray, scene)
		if obj_hit is None:
			return color
		hit_pos = ray.origin + ray.direction * dist_hit
		color += self.color_at(obj_hit, hit_pos, scene)
		return color
		
	def find_nearest(self, ray, scene):
		dist_min = None
		obj_hit = None
		for obj in scene.objects:
			dist = obj.intersects(ray)
			if dist is not None and (obj_hit is None or dist < dist_min):
				dist_min = dist
				obj_hit = obj
		return (dist_min, obj_hit)
		
	def color_at(self, obj_hit, hit_pos, scene):
		return obj_hit.material
