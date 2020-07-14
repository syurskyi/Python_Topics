# ______ ?
# ______ ?
# ____ ? ______ panels
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
#
# c_ simplePanel ?W..
#     ___  -
#         ?W... -
#         sL.. ?VL..
#         locationEdit _ ?CW..
#         la__ .aW.. ?
#
# pa__.rWAP.. simplePanel Simple
#
# w = ?
# ?.s__
#
# # Eto chesnuj sposob vstavki widgeta vnytri Nuke
# # Y etogo sposoba est'  tol'ko odno neydobstvoeto ykazanie widgeta strokoj.
# # To est' ne ssulkoj na objekt a strokoj otkyda ego nyzno importit'
# # Esli etot klass nahoditsja v nekotorom module na diske, to nyzno napisat'  polnostjy ego pyt', to est' ne pyt' k fajly na diske a pyt'k etomy widgety vnytri modulja
# # toest' snachalo imja modulja ptom bnytri nego imja klass
# # ______ mod
# # w = mod.simplePanel()
# # no pri registracii panelja eto nikak ne pomozet, ne ______ , ne sozdanie exampljara
# # shtobu eta fynkcija nashla klass vnytri modulja, nam nyzno napisat' polnuj ego pyt' imja modylja a potom imja klassa, fynkcija sama importiryet vsjo shto nado i sozdat exampljar
#
# # panels.rWAP..('mod.simplePanel', 'Simple', "")
#
# # Vslychae esli registracija modulja nahoditsja v tom ze module , v kotorom nahoditsja klass , to mozno napisat tak
#
# # panels.rWAP..(__name__.'simplePanel', 'Simple', "")
# # V name obuchno pishetsja imja modlja v kotorom proishodit vupolnenie danngo koda