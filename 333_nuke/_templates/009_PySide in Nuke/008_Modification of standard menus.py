# # linearAnim
#
# ______ ?
#
# n _ ?.sN__
# k _ ? translate
# ?.sA..
# ___ i __ ra.. 100
#     ?.sVA. ? ?
#
# # change to function doit
#
# ___ doit
#     k _ ?.tK..
#     __ ?.aS.. > 1
#         index _ gKI..
#     ____
#         index _ 0
#     ?.sA..
#     ___ i __ ra.. 100
#         ?.sVA.  ? ? ?
#
# # shtobu polychit' index knoba, kotoruj nahoditsja v kontexte, dostatochno vuzvat' ety fynkcijy
# # no vuzuvat' ejo sledyet tol'ko dlja knobov gde kanalov bol'she odnogo
#
# ___ getKnobIndex
#
#     tclGetAnimIndex _ """
#
#  set thisanimation [animations]
#  if {[llength $thisanimation] > 1} {
#   return "-1"
#   } else {
#    return [lsearch [in [join [lrange [split [in $thisanimation {animations}] .] 0 end-1] .] {animations}] $thisanimation]
#   }
#  """
#
#     r_ in. ?.t.. ?