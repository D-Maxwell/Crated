
from src.Ship.Crate import Crate


class Rect(Crate):
	def __init__(self):
		super().__init__()
		self.bg = None
		self.size = None
		self.pos = None

	def pack(self, line):
		super().pack(line)

		self.pos = self.attributes.get("pos",[0,0])
		self.position()

		self.size = self.attributes.get("size",[0,0])
		self.resize()

		self.bg = self.attributes.get("bg","00000000")


	def position(self):
		mode = None
		for idx in range(len(self.pos)):
			#self.pos[idx] = self.attributes.get("pos")[1]
			#print(self.pos[idx])
			if type(self.pos[idx]) is str:
				#print(self.pos[idx].__contains__("R"))
				if self.pos[idx].__contains__("R"):
					mode = "R"

				# exclude "", temp
				self.pos[idx] = int(self.pos[idx][0:-1])

				if self.parent is not None:
					if mode == "R":
						#self.pos[idx] += self.hook("#main")[0]
						self.pos[idx] += self.parent.pos[idx]
						#pass

	def resize(self):

		for s,size in enumerate(self.size):
			if type(size) is float:
				if self.parent is None:
					# last hack before going to bed
					print(self.cargo.dock.surface.get_size())
					self.size[s] = int(self.size[s] * self.cargo.dock.surface.get_size()[s])
					print(self.size[s])
				else:
					self.size[s] = int(self.size[s] * self.parent.size[s])
