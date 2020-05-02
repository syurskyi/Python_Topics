_____ os, ___, time, getopt
_____ zipfile
____ datetime _____ datetime


___ usage(
	print "usage:\n \tarchiveit2.py -f/somedir/folder -t/backup\nwill create '/backup/folder-<YYYYMMDD-hhmmss>.zip'\nwhere the filename is composed from zipped folder name, current date and time"

___ get_zipfilepath(frm, to
	dt = datetime.now()
	__ not os.path.isdir(frm
		print "'" + frm + "' this is not valid source dir"
		___.e..(2)
	__ not os.path.isdir(to
		print "'" + to + "' this is not valid target dir"
		___.e..(2)

	name = os.path.split(frm)[1] + '-' + dt.strftime("%Y%m%d-%H%M%S") + '.zip'
	archive_full_path = os.path.join(to, name)

	return archive_full_path

___ make_archive(zip_archive_file, directory, *args
	___ recursive_zip(zipf, directory, *args
		nodes = os.listdir(directory)
		for item in nodes:
			path = os.path.join(directory, item)
			__ os.path.isfile(path
				zipf.write(path, unicode(path,'utf-8').encode('cp852'))
			elif os.path.isdir(path
				__ not item in args:
					recursive_zip(zipf, path, *args)

	zipf = zipfile.ZipFile(zip_archive_file, 'w', compression=zipfile.ZIP_DEFLATED)
	recursive_zip(zipf, directory, *args)
	zipf.close()

___ process(srcdir, outdir, *excludes
	archive_full_path = get_zipfilepath(srcdir, outdir)	
	'''
	important: because we pass list as last argument it needs to be expanded
	that's why we use *
	'''
	os.chdir(srcdir)
	make_archive(archive_full_path, './', *excludes)

	return archive_full_path
	

___ main(
	frm = ''
	to = ''
	try:
		opts, rest = getopt.getopt(___.argv[1:],"f:t:h")
	except getopt.GetoptError, err:
		print(err)
		usage()
		___.e..(2)
		
	__ not opts:
		opts.append(('-h',''))

	for o, a in opts:
		__ o __ '-h':
			usage()
			___.e..(0)
		# frm dir
		elif o __ '-f':
			frm = a
		elif o __ '-t':
			to = a			

	__ not (frm and to
		print "not sufficent parameters provided to: '" + to + "' from: '" + frm + "'"
		___.e..(2)
		
	zip_full_path = process(frm, to)
	print 'success ' + zip_full_path + ' was created'
		

__ __name__ __ "__main__":
	main()
