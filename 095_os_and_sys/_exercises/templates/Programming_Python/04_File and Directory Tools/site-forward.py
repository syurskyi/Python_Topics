"""
################################################################################
Create forward-link pages for relocating a web site.
Generates one page for every existing site html file; upload the generated
files to your old web site.  See ftplib later in the book for ways to run
uploads in scripts either after or during page file creation.
################################################################################
"""

______ __
servername   = 'learning-python.com'     # where site is relocating to
homedir      = 'books'                   # where site will be rooted
sitefilesdir = r'C:\temp\public_html'    # where site files live locally
uploaddir    = r'C:\temp\isp-forward'    # where to store forward files
templatename = 'template.html'           # template for generated pages

try:
    __.mkdir(uploaddir)                  # make upload dir if needed
except OSError: pass

template  = o..(templatename).read()    # load or ______ template text
sitefiles = __.listdir(sitefilesdir)     # filenames, no directory prefix

count = 0
___ filename __ sitefiles:
    if filename.endswith('.html') or filename.endswith('.htm'):
        fwdname = __.p...j..(uploaddir, filename)
        print('creating', filename, 'as', fwdname)

        filetext = template.replace('$server$', servername)   # insert text
        filetext = filetext.replace('$home$',   homedir)      # and write
        filetext = filetext.replace('$file$',   filename)     # file varies
        o..(fwdname, 'w').w..(filetext)
        count += 1

print('Last file =>\n', filetext, sep='')
print('Done:', count, 'forward files created.')
