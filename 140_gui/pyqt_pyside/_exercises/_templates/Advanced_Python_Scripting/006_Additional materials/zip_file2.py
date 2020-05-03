_____ os
_____ ___
_____ time
_____ getopt
_____ zipfile

____ datetime _____ datetime


___ usage(
    print("usage:\n \tzip_file2.py -f/somedir/folder -t/backup\nwill create '/backup/folder-<YYYYMMDD-hhmmss>.zip'\n"
          "where the filename is composed from zipped folder name, current date and time")


___ get_zipfilepath(frm, to
    dt _ datetime.now
    __ not os.path.isdir(frm
        print "'" + frm + "' this is not valid source dir"
        ___.e..(2)
    __ not os.path.isdir(to
        print "'" + to + "' this is not valid target dir"
        ___.e..(2)

    name _ os.path.split(frm)[1] + '-' + dt.strftime("%Y%m%d-%H%M%S") + '.zip'
    archive_full_path _ os.path.join(to, name)

    r_ archive_full_path


___ make_archive(zip_archive_file, directory, *args
    ___ recursive_zip(zipf, directory, *args
        nodes _ os.listdir(directory)
        ___ item __ nodes:
            path _ os.path.join(directory, item)
            __ os.path.isfile(path
                zipf.w..(path, unicode(path, 'utf-8').e..('cp852'))
            elif os.path.isdir(path
                __ not item __ args:
                    recursive_zip(zipf, path, *args)

    zipf _ zipfile.ZipFile(zip_archive_file, 'w', compression_zipfile.ZIP_DEFLATED)
    recursive_zip(zipf, directory, *args)
    zipf.c..


___ process(srcdir, outdir, *excludes
    archive_full_path _ get_zipfilepath(srcdir, outdir)
    os.chdir(srcdir)
    make_archive(archive_full_path, './', *excludes)
    r_ archive_full_path


___ main(
    frm _ ''
    to _ ''
    ___
        opts, rest _ getopt.getopt(___.argv[1:], "f:t:h")
    _____ getopt.GetoptError, err:
        print(err)
        usage
        ___.e..(2)

    __ not opts:
        opts.ap..(('-h', ''))

    ___ o, a __ opts:
        __ o __ '-h':
            usage
            ___.e..(0)
        elif o __ '-f':
            frm _ a
        elif o __ '-t':
            to _ a

    __ not(frm an. to
        print "not sufficent parameters provided to: '" + to + "' from: '" + frm + "'"
        ___.e..(2)

    zip_full_path _ process(frm, to)
    print 'success ' + zip_full_path + ' was created'

__ __name__ __ "__main__":
    main

