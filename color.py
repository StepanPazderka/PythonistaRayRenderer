import ImageColor
from vector import Vector

class Color(Vector):
	
	@classmethod
	def from_hex(cls, hexcolor="#000000"):
		x = int(hexcolor[1:3], 16) / 255.0
		y = int(hexcolor[3:5], 16) / 255.0
		z = int(hexcolor[5:7], 16) / 255.0
		return cls(x, y, z)
		
	def getColor(self):
		return [self.x, self.y, self.z]
		
	def __str__(self):
		return str(self.x) + " " + str(self.y) + " " + str(self.z)
		
	def __repr__(self):
		return str(str(self.x) + str(self.y) + str(self.x))
