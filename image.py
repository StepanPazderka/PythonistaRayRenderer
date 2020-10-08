from color import Color

class Image:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.pixels = [[None for _ in range(width)] for _ in range(height)]
		
	def set_pixel(self, x, y, color):
		self.pixels[y][x] = color
		
	def __str__(self):
		returnString = []
		
		for id, pixel in enumerate(self.pixels):
			returnString.append("\n")
			for id, pixel in enumerate(self.pixels[0]):
				returnString.append(str(pixel.x) + " " + str(pixel.y) + " " + str(pixel.z))
				#returnString.append("Konec")
		
		return str(returnString)
