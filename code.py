class Student:
	def __init__(self, id, first, last):
		self.id=id
		self.first=first
		self.last=last
		self.grade=[]
	def add_grade(self,n):
		self.grade.append(n)
	def calculate_grade(self):
		self.sum=0
		for i in self.grade:
			self.sum+=i
		self.sum=self.sum/(len(self.grade))
		import math
		return math.floor(self.sum)
	def print_transcript(self):
		import math 
		print(self.last,", ",self.first," : ",self.id,"; ",math.floor(self.sum),"%",sep="")
		