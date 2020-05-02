_____ os

path _ 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/004_Text data formats/'
# /Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced\ Python\ Scripting/004_Text\ data\ formats/
fileName _ 'settings.txt'

c_ settingClass(object
	___  -  
		fullPath _ os.path.join(path, fileName)
		__ not os.path.exists(fullPath
			open(fullPath, 'w').close()

	___ __readFile 
		f _ open(fullPath)
		t.. _ f.readlines()
		f.close()
		# data = {}
		___ line __ t..:
			key, value _ line.strip().split("=")
			# data[key] = value
			print(key, value)
		# return data

	___ __writeFile , data
		f _ open(fullPath, 'w')
		___ k, v __ data.items(
			f.write('%s=%s\n' % (k, v))
		f.close()

	___ readSetting 
		data _ __readFile()
		r_ data


	___ writeSetting , data
		# check
		__writeFile()


	___ readValue , key
		pass

	___ writeValue , key, value
		pass

s _ settingClass()
# d = {'key1':1, 'key2':2}
# s.writeSetting(d)
s.readSetting()