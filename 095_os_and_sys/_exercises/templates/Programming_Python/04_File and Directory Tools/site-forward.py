"""
################################################################################
Create forward-link pages for relocating a web site.
Generates one page for every existing site html file; upload the generated
files to your old web site.  See ftplib later in the book for ways to run
uploads in scripts either after or during page file creation.
################################################################################
"""

______ __
servername   _ 'learning-python.com'     # where site is relocating to
homedir      _ 'books'                   # where site will be rooted
sitefilesdir _ r'C:\temp\public_html'    # where site files live locally
uploaddir    _ r'C:\temp\isp-forward'    # where to store forward files
templatename _ 'template.html'           # template for generated pages

___
    __.mkdir(uploaddir)                  # make upload dir if needed
______ O..: pass

template  _ o..(templatename).read()    # load or ______ template text
sitefiles _ __.l_d_(sitefilesdir)     # filenames, no directory prefix

count _ 0
___ filename __ sitefiles:
    __ filename.endswith('.html') or filename.endswith('.htm'):
        fwdname _ __.p...j..(uploaddir, filename)
        print('creating', filename, 'as', fwdname)

        filetext _ template.replace('$server$', servername)   # insert text
        filetext _ filetext.replace('$home$',   homedir)      # and write
        filetext _ filetext.replace('$file$',   filename)     # file varies
        o..(fwdname, 'w').w..(filetext)
        count +_ 1

print('Last file =>\n', filetext, sep_'')
print('Done:', count, 'forward files created.')
