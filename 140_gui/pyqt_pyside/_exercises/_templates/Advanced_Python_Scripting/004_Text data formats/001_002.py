_____ __

path _ 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/004_Text data formats/'
# /Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced\ Python\ Scripting/004_Text\ data\ formats/
fileName _ 'settings.txt'

c_ settingClass(object
	___  -  
		fullPath _ __.path.j..(path, fileName)
		__ no. __.path.exists(fullPath
			o..(fullPath, 'w').c..

	___ __readFile 
		f _ o..(fullPath)
		t.. _ f.readlines
		f.c..
		# data = {}
		___ line __ t..:
			key, value _ line.strip.split("=")
			# data[key] = value
			print(key, value)
		# return data

	___ __writeFile , data
		f _ o..(fullPath, 'w')
		___ k, v __ data.items(
			f.w..('%s=%s\n' % (k, v))
		f.c..

	___ readSetting 
		data _ __readFile
		r_ data


	___ writeSetting , data
		# check
		__writeFile


	___ readValue , key
		p..

	___ writeValue , key, value
		p..

s _ settingClass
# d = {'key1':1, 'key2':2}
# s.writeSetting(d)
s.readSetting