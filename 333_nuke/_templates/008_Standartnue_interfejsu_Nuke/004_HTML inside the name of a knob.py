______ __
node _ ?.sN__

node['icon'].sV..('C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/004_Pipeline/icons/cgninjas.png')
k _ ?.Text_Knob('tutor', 'Tutorial')
node.aK..(k)
node["tutor"].sL..('<h4><a style="color:lightgray;" href="http://cgninjas.ru">CGNINJAS<a></h4>')

#######################
h _ ?.D_K..('sue', '')
h.sL..('<h2>H </h2><img src="%s/icons/hue.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.aK..(h)

s _ ?.D_K..('sat', '')
s.sL..('<h2>S </h2><img src="%s/icons/saturation.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.aK..(s)

v _ ?.D_K..('val', '')
v.sL..('<h2>V </h2><img src="%s/icons/lightness.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.aK..(v)


#######################
node.aK..(?.Text_Knob('',''))
#######################

###### node icon
node['icon'].sV..('C:/pipeline/icons/cgninjas_node.png')

###### Label HTML
# link

k _ ?.Text_Knob('tutor', 'Tutorial')
node.aK..(k)
k.sL..('<h4><a style="color:lightgray;" href="http://cgninjas.ru">CGNINJAS<a></h4>')

###########################
# image label

h _ ?.D_K..('sue', '')
h.sL..('<h2>H </h2><img src="%s/icons/h.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.aK..(h)

s _ ?.D_K..('sat', '')
s.sL..('<h2>S </h2><img src="%s/icons/s.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.aK..(s)

v _ ?.D_K..('val', '')
v.sL..('<h2>V </h2><img src="%s/icons/v.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.aK..(v)

########################
node.aK..(?.Text_Knob('',''))
##########################

# interactive label

power _ ?.D_K..('power', 'Power')
node.aK..(power)

___ powerKnob(a):
    k _ ?.thisKnob()
    __ k.name() __ 'power' and a__'Blur':
        v _ k.getValue()
        img _ int((v*5)+1)
        k.sL..('<img src="%s/icons/power%s.png">' % (__.environ['NUKE_PATH'].replace('\\','/'), img))

?.addKnobChanged(powerKnob, 'Blur')
?.removeKnobChanged(powerKnob, 'Blur')

########################################################################################################################

set cut_paste_input [stack 0]
version 10.0 v4
push $cut_paste_input
Blur {
 channels rgba
 name Blur1
 label "---------------\n\[value size]"
 selected true
 xpos 219
 ypos -135
 icon "C:/Users/serge/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/004_Pipeline/icons/cgninjas.png"
 addUserKnob {20 User}
 addUserKnob {26 tutor l "<h4><a style=\"color:lightgray;\" href=\"http://cgninjas.ru\">CGNINJAS<a></h4>"}
 addUserKnob {7 hue l "<h2>H </h2><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/hue.png\">"}
 addUserKnob {7 sat l "<h2>S </h2><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/saturation.png\">"}
 addUserKnob {7 val l "<h2>V </h2><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/lightness.png\">"}
 addUserKnob {26 "" +ST..}
 addUserKnob {7 power l "<h3>POWER</h3><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/power/power6.png\">"}
 power 1
}
