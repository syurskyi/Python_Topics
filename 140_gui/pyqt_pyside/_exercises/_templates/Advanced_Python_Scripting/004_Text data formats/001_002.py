_____ os

path = 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/004_Text data formats/'
# /Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced\ Python\ Scripting/004_Text\ data\ formats/
fileName = 'settings.txt'

c_ settingClass(object
	___  -  
		fullPath = os.path.join(path, fileName)
		__ not os.path.exists(fullPath
			open(fullPath, 'w').close()

	___ __readFile 
		f = open(fullPath)
		text = f.readlines()
		f.close()
		# data = {}
		for line in text:
			key, value = line.strip().split("=")
			# data[key] = value
			print(key, value)
		# return data

	___ __writeFile , data
		f = open(fullPath, 'w')
		for k, v in data.items(
			f.write('%s=%s\n' % (k, v))
		f.close()

	___ readSetting 
		data = __readFile()
		return data


	___ writeSetting , data
		# check
		__writeFile()


	___ readValue , key
		pass

	___ writeValue , key, value
		pass

s = settingClass()
# d = {'key1':1, 'key2':2}
# s.writeSetting(d)
s.readSetting()