class Scene:
	"""Scene has all the information needed for raytracing engine"""
	def __init__(self, camera, objects, width, height):
		self.camera = camera
		self.objects = objects
		self.width = width
		self.height = height
