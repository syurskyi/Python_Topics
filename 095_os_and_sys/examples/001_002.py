import os

path = 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/004_Text data formats/'
# /Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced\ Python\ Scripting/004_Text\ data\ formats/
fileName = 'settings.txt'

class settingClass(object):
	def __init__(self):
		self.fullPath = os.path.join(path, fileName)
		if not os.path.exists(self.fullPath):
			open(self.fullPath, 'w').close()

	def __readFile(self):
		f = open(self.fullPath)
		text = f.readlines()
		f.close()
		# data = {}
		for line in text:
			key, value = line.strip().split("=")
			# data[key] = value
			print(key, value)
		# return data

	def __writeFile(self, data):
		f = open(self.fullPath, 'w')
		for k, v in data.items():
			f.write('%s=%s\n' % (k, v))
		f.close()

	def readSetting(self):
		data = self.__readFile()
		return data


	def writeSetting(self, data):
		# check
		self.__writeFile()


	def readValue(self, key):
		pass

	def writeValue(self, key, value):
		pass

s = settingClass()
# d = {'key1':1, 'key2':2}
# s.writeSetting(d)
s.readSetting()