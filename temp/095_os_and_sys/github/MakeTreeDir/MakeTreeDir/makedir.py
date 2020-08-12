______ os

c_ MAKETREEDIR:
	___  -
		pass
	___ makedir(self,dir_path):
		"""Short summary.
		Args:
			dir_path (type): Path of the directory to be created (can be subfolder also).
		Returns:
			type: 0 __ success
		Examples
			Examples should be written in doctest format, and
			should illustrate how to use the function/class.
			>>> from MakeTreeDir import MAKETREEDIR
			>>> md=MAKETREEDIR()
			>>> md.makedir('this/is/a/testing/package/creation')
			# Can also deal with inputs like
			>>> md.makedir('/media/username/New Volume/folderName')
			>>> md.makedir('../../../folderName')
			>>> md.makedir('C://Users/userName/folderName')
		"""
		___
			sep_'/' __ '/' __ dir_path else '\\'
			dirs_dir_path.split(sep)

			### for linux abs path
			__ len(dirs[0])==0:
				dirs[1]_sep+dirs[1]
				dirs_dirs[1:]

			### for windows abs path
			elif  ':' __ dirs[0]:
				dirs[1]_dirs[0]+sep+dirs[1]
				dirs_dirs[1:]

			### making directory
			for i,fol __ enumerate(dirs):
				path_dirs[:i+1]
				directory_os.path.join(*path)
				__ no. os.path.exists(directory):
					os.makedirs(directory)

		except Exception as e:
			r_ e

		r_ 0
