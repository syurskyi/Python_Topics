# ______ ?.r_p.. __ rp
# ______ ma..
#
# rpNode _ ?.sN__
# cKnob_ ? *cu..
# root _ ?.rL..
#
# ___ shape __ ?
#     print ?.n..
#
# k.tE.. *Rectangle1
# ############################
# shape _ ?.S.. ?
# r__.ap.. ?
# ?.ap.. ?.ACP.. 500 500
# ?.ap.. ?.ACP.. 2500 500
# ?.ap.. ?.ACP.. 500 2500
# #################################
#
#
# ########################################################################################################################
# ______ ?.r_p.. __ rp
# ______ ma..
#
# roto _ ?.no__.RP..
# ck _ ? *cu..
#
# # create shape
#
# shape _ ?.S.. ?
# ?.n.. _ *star
# points _ # list
# count _ 15
# rad1 _ mi. ?.wi.. ?.he.. /2
# rad2 _ rad1*0.5
# center _ ?.w.. /2, ?.h.. /2
# angl _ 360.0 / c..*2
# ___ i __ ra.. c..*2
#     r _ _1 __ ?%2 ____ _2
#     x _ ma__.si. ma__.ra.. a..*? * r +ce.. 0
#     y _ ma__.cos(ma__.ra.. a..*? * r +ce.. 1
#     p__.ap.. x,y
# ___ pt __ p..
#     s__.ap.. ?.ACP.. $?
#
# atr _ s__.gA..
# ?.se. 1, ?.kBA.. , 0
# ? *c.. .cA..
#
# ?.se. 1 ?.kFTA.. 1
# ?.se. 1 ?.kFXA.. 5
# ?.se. 1 ?.kFYA.. 5
# n *fe.. .cA..
#
# # ## create layer
#
# stroke _ ?.S.. ?
# center_2000
# step _ 15
# count _ 400
# rad _ 1500
# ___ i __ ra.. c..
#     r _ r.. * 1.0/c..*?
#     x _  ma__.si. ma__.ra.. s..*? * ? +ce..
#     y _  ma__.co. ma__.ra.. s..*? * ? +ce..
#     s__.ap.. ?.ACP.. x y
#
# Root _ ?.tL..
# newLayer _ ?.L.. ?
# ?.n.. _ *Spiral
# ?.ap..?
# ?.ap.. s..