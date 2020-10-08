class Ray:
	"""Ray is a half life with an origin and normalized direction"""
	def __init__(self, origin, direction):
		self.origin = origin
		self.direction = direction.normalize()
