# _______
# ___  dirname subshere fileshere i_ __.wa.. '.'
#     print('[' + d.. + ']')
#     ___ fname i_ f...
#         print __.pa__.jo.. d.n. f... # handle one file
#
# # [.]
# # .\random.bin
# # .\spam.txt
# # .\temp.bin
# # .\temp.txt
# # [.\parts]
# # .\parts\part0001
# # .\parts\part0002
# # .\parts\part0003
# # .\parts\part0004
# #
# # C:\...\PP4E\System\Filetools> python lister_walk.py C:\temp\test
# # [C:\temp\test]
# # C:\temp\test\random.bin
# # C:\temp\test\spam.txt
# # C:\temp\test\temp.bin
# # C:\temp\test\temp.txt
# # [C:\temp\test\parts]
# # C:\temp\test\parts\part0001
# # C:\temp\test\parts\part0002
# # C:\temp\test\parts\part0003
# # C:\temp\test\parts\part0004
# # ######################################################################################################################
#
# ______ __
# matches _     # list
# ___ (dirname, dirshere, fileshere) in __.wa.. _'C:\temp\PP3E\Examples
#     ___ filename i_ f..
#         i_ ?.e.w. '.py'
#             pathname _ __.pa__.jo.. d... f..
#         i_ 'mimetypes' i_ o.. ?.r..
#             ma__.ap.. ?
#
# ___ name i_ m.. print ?
#
# # C:\temp\PP3E\Examples\PP3E\Internet\Email\mailtools\mailParser.py
# # C:\temp\PP3E\Examples\PP3E\Internet\Email\mailtools\mailSender.py
# # C:\temp\PP3E\Examples\PP3E\Internet\Ftp\mirror\downloadflat.py
# # C:\temp\PP3E\Examples\PP3E\Internet\Ftp\mirror\downloadflat_modular.py
# # C:\temp\PP3E\Examples\PP3E\Internet\Ftp\mirror\ftptools.py
# # C:\temp\PP3E\Examples\PP3E\Internet\Ftp\mirror\uploadflat.py
# # C:\temp\PP3E\Examples\PP3E\System\Media\playfile.py
# # ######################################################################################################################
#
# gen = __.wa.. _'C:\temp\test')
# ?. -n
# # ('C:\\temp\\test', ['parts'], ['random.bin', 'spam.txt', 'temp.bin', 'temp.txt'])
# ?. -n
# # ('C:\\temp\\test\\parts', [], ['part0001', 'part0002', 'part0003', 'part0004'])
# ?. -n
# # Traceback (most recent call last):
# # File "<stdin>", line 1, in <module>
# # StopIteration
# # ######################################################################################################################
#
