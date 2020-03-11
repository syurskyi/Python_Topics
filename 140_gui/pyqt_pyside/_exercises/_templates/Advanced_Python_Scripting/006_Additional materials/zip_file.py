import os, sys, time, getopt
import zipfile
from datetime import datetime


def usage():
	print "usage:\n \tarchiveit2.py -f/somedir/folder -t/backup\nwill create '/backup/folder-<YYYYMMDD-hhmmss>.zip'\nwhere the filename is composed from zipped folder name, current date and time"

def get_zipfilepath(frm, to):
	dt = datetime.now()
	if not os.path.isdir(frm):
		print "'" + frm + "' this is not valid source dir"
		sys.exit(2)
	if not os.path.isdir(to):
		print "'" + to + "' this is not valid target dir"
		sys.exit(2)

	name = os.path.split(frm)[1] + '-' + dt.strftime("%Y%m%d-%H%M%S") + '.zip'
	archive_full_path = os.path.join(to, name)

	return archive_full_path

def make_archive(zip_archive_file, directory, *args):
	def recursive_zip(zipf, directory, *args):
		nodes = os.listdir(directory)
		for item in nodes:
			path = os.path.join(directory, item)
			if os.path.isfile(path):
				zipf.write(path, unicode(path,'utf-8').encode('cp852'))
			elif os.path.isdir(path):
				if not item in args:
					recursive_zip(zipf, path, *args)

	zipf = zipfile.ZipFile(zip_archive_file, 'w', compression=zipfile.ZIP_DEFLATED)
	recursive_zip(zipf, directory, *args)
	zipf.close()

def process(srcdir, outdir, *excludes):
	archive_full_path = get_zipfilepath(srcdir, outdir)	
	'''
	important: because we pass list as last argument it needs to be expanded
	that's why we use *
	'''
	os.chdir(srcdir)
	make_archive(archive_full_path, './', *excludes)

	return archive_full_path
	

def main():
	frm = ''
	to = ''
	try:
		opts, rest = getopt.getopt(sys.argv[1:],"f:t:h")
	except getopt.GetoptError, err:
		print(err)
		usage()
		sys.exit(2)
		
	if not opts:
		opts.append(('-h',''))

	for o, a in opts:
		if o == '-h':
			usage()
			sys.exit(0)
		# frm dir
		elif o == '-f':
			frm = a
		elif o == '-t':
			to = a			

	if not (frm and to):
		print "not sufficent parameters provided to: '" + to + "' from: '" + frm + "'"
		sys.exit(2)
		
	zip_full_path = process(frm, to)
	print 'success ' + zip_full_path + ' was created'
		

if __name__ == "__main__":
	main()
