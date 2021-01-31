# _____ ?
#
# # create  and connect nodes
# r _ ?.cN.. 'Read', in.._F..
# g _ ?.cN.. 'Grade', in.._F..
# c _ ?.n__.CoC.. name_'mainCC',xpos_400,yp__ _ 10, gain_2
# ?.sI.. 0, g
# ?.a..
# b _ ?.n__.B..
# c.cI.. 1 ?
# ?.sI.. 0 g
#
# no1, n02 _ ?.n__.NO. ?.n__.NO..
# m _ ?.n__.M.. i.._ ? ?
#
# ?.cV.. 0 c
#
# # get node
# sel _ ?.sN..
# sel _ ?.sN..
# __ ?
#     v _ ? 0
# v _ ?.tN.. 'Viewer1'
#
# ?.cSI.. 0 c
# ?.sI.. 0 c)
#
# ?.aN.. 'ColorCorrect'
# ?.sN.. 'ColorCorrect'
#
# n__ _ ?.aN..
#  x ___ x __ n__ __ x.C..  __ 'ColorCorrect'
#
# ?.aV__ .n..
#
#
# ?.r__
# ?.tN.. 'preferences'
#
# # knobs #########################################
# # get value
# ?.tN.. 'Write2' 'file' .gV..
# ?.tN.. 'Write2' 'file' .e..
# #set value
# _____ ?
# node _ ?.tN.. 'ColorCorrect2'
# ? 'shadows.gain' .sV.. 2
# ? 'channels' .sV..('rgba')
#
# # link knobs
# ? 'gain' .sE..'@.@' @ 'ColorCorrect1' 'gain'
# ? 'gain' .sE..'shadows.gain * 2')
#
# ? 'scale' .sE.. "[python nuke.frame()]"
#
# n _ ?.tN.. 'Transform1' 'scale' .sE.. '''[python -execlocal x = 2
# for i in range(100):
#     x += i
# ret = x]''')
#
#
# # Move nodes
# node _ ?.n__.T..
# ?.a..
# ?.a.. ?
#
# ? 'xpos' .sV.. 0
# ?.sXY..
# ?.zTFS..
# ?.eS..
