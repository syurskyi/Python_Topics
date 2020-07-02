# linearAnim

______ ?

n = ?.sN__
k = n['translate']
k.setAnimated()
___ i __ ra..(100):
    k.setValueAt( i, i )

# change to function doit

___ doit():
    k = ?.thisKnob()
    __ k.arraySize() > 1:
        index = getKnobIndex()
    ____
        index = 0
    k.setAnimated()
    ___ i __ ra..(100):
        k.setValueAt( i, i, index)

# shtobu polychit' index knoba, kotoruj nahoditsja v kontexte, dostatochno vuzvat' ety fynkcijy
# no vuzuvat' ejo sledyet tol'ko dlja knobov gde kanalov bol'she odnogo

___ getKnobIndex():

    tclGetAnimIndex = """

 set thisanimation [animations]
 if {[llength $thisanimation] > 1} {
  return "-1"
  } else {
   return [lsearch [in [join [lrange [split [in $thisanimation {animations}] .] 0 end-1] .] {animations}] $thisanimation]
  }
 """

    r_ int(?.tcl(tclGetAnimIndex))