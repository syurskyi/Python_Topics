______ __
node = ?.sN__

node['icon'].sV..('C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/004_Pipeline/icons/cgninjas.png')
k = ?.Text_Knob('tutor', 'Tutorial')
node.addKnob(k)
node["tutor"].setLabel('<h4><a style="color:lightgray;" href="http://cgninjas.ru">CGNINJAS<a></h4>')

#######################
h = ?.Double_Knob('sue', '')
h.setLabel('<h2>H </h2><img src="%s/icons/hue.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(h)

s = ?.Double_Knob('sat', '')
s.setLabel('<h2>S </h2><img src="%s/icons/saturation.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(s)

v = ?.Double_Knob('val', '')
v.setLabel('<h2>V </h2><img src="%s/icons/lightness.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(v)


#######################
node.addKnob(?.Text_Knob('',''))
#######################

###### node icon
node['icon'].sV..('C:/pipeline/icons/cgninjas_node.png')

###### Label HTML
# link

k = ?.Text_Knob('tutor', 'Tutorial')
node.addKnob(k)
k.setLabel('<h4><a style="color:lightgray;" href="http://cgninjas.ru">CGNINJAS<a></h4>')

###########################
# image label

h = ?.Double_Knob('sue', '')
h.setLabel('<h2>H </h2><img src="%s/icons/h.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(h)

s = ?.Double_Knob('sat', '')
s.setLabel('<h2>S </h2><img src="%s/icons/s.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(s)

v = ?.Double_Knob('val', '')
v.setLabel('<h2>V </h2><img src="%s/icons/v.png">' % __.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(v)

########################
node.addKnob(?.Text_Knob('',''))
##########################

# interactive label

power = ?.Double_Knob('power', 'Power')
node.addKnob(power)

___ powerKnob(a):
    k = ?.thisKnob()
    __ k.name() == 'power' and a=='Blur':
        v = k.getValue()
        img = int((v*5)+1)
        k.setLabel('<img src="%s/icons/power%s.png">' % (__.environ['NUKE_PATH'].replace('\\','/'), img))

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
 addUserKnob {26 "" +STARTLINE}
 addUserKnob {7 power l "<h3>POWER</h3><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/power/power6.png\">"}
 power 1
}
