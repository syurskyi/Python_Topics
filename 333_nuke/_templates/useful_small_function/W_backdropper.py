#----------------------------------------------------------------------------------------------------------
# Wouter Gilsing
# woutergilsing@hotmail.com
version _ '1.2'
releaseDate _ 'February 06 2018'

#----------------------------------------------------------------------------------------------------------
#
#LICENSE
#
#----------------------------------------------------------------------------------------------------------

'''
Copyright (c) 2018, Wouter Gilsing
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Redistribution of this software in source or binary forms shall be free
      of all charges or fees to the recipient of this software.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

#----------------------------------------------------------------------------------------------------------
#_____ modules
#----------------------------------------------------------------------------------------------------------

_____ ?, n_s_

#Choose between PySide and PySide2 based on Nuke version
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ PySide _____ _C.., _G.., _G.. as _W..
____
    ____ ______ _____ _G.., _C.., _W..

_____ __
_____ re

____ datetime _____ datetime as dt
____ getpass _____ getuser


#----------------------------------------------------------------------------------------------------------

___ backdropper(nodeClass _ 'Backdrop'):
    '''
    Create node, ask user for text to put in the label. Coloirze node based on label.
    '''

    # create panel instance
    panel _ ?.Panel(nodeClass)
    panel.addSingleLineInput('label','')
    __ panel.show
        
        label _ panel.v.. ('label')

        __ nodeClass __ 'StickyNote':
            label _ '   %s   '%label.upper()
            node _ ?.cN..(nodeClass, inpanel _ F..)

        ____
            node _ n_s_.autoBackdrop()

        fontSize _ preferencesNode.knob('backdropper%sFontSize'%nodeClass).v.. ()
        node.knob('note_font_size').sV..(fontSize)

        __ label:

            #set label
            node.knob('label').sV..(label)

            #colorize
            colorizeNode(node)
        
        ____
            #open properties
            ?.show(node)

#----------------------------------------------------------------------------------------------------------
#Node colors
#----------------------------------------------------------------------------------------------------------

___ indexKeywordColors
    '''
    Build color dictionary.
    '''
    colorList _ []
    colorsDict _ {}

    ___ number __ ra..(presetSlots):
        number +_ 1

        stringKnob _ 'backdropperColor%s'%st_(number).zf..(2)
        colorKnob _ 'backdropperColor%sColor'%st_(number).zf..(2)

        keys _ [key ___ key __ preferencesNode.knob(stringKnob).v.. ().s..(' ') __ key]

        #case sensitive
        __ no. preferencesNode.knob('backdropperCaseSensitive').v..
            keys _ [key.lower() ___ key __ keys]

        color _ preferencesNode.knob(colorKnob).v.. ()

        ___ key __ keys:
            colorList.ap..(key)
            colorsDict[key] _ color

    r_ colorList, colorsDict

___ colorizeNode(node):
    '''
    Set color for selected shuffle nodes
    '''

    keywordList, keywordDict _ indexKeywordColors()
    colorNamesList _ reversed(sorted(colorNamesDict.k.. , key _ le.))

    nodeLabel _ node.knob('label').v.. ()

    #order
    #0 = keywords first, 1 = color names first
    order _ in_(preferencesNode.knob('backdropperOrder').gV..  * 2 - 1 )

    colorLists _ [colorNamesList, keywordList][::order]
    colorDicts _ [colorNamesDict, keywordDict][::order]


    ___ index, keys __ enumerate(colorLists):

        label _ nodeLabel

        __ no. preferencesNode.knob('backdropperCaseSensitive').v.. () or keys __ colorList:
            label _ label.lower()

        ___ key __ keys:
            __ key __ label:
                node.knob('tile_color').sV..(colorDicts[index][key])
                r_

#----------------------------------------------------------------------------------------------------------
# Default colors
#----------------------------------------------------------------------------------------------------------

___ indexDefaultColors

    # matplotlibColors is turning out to be problematic 
    # only seems to works for certain  versions of Nuke, etc. 
    # So I decided to just past the color dict in here directly...
    # Very neat, I know...
    colors _ {'indigo': '#4B0082', 'gold': '#FFD700', 'hotpink': '#FF69B4', 'firebrick': '#B22222', 'indianred': '#CD5C5C', 'yellow': '#FFFF00', 'mistyrose': '#FFE4E1', 'darkolivegreen': '#556B2F', 'olive': '#808000', 'darkseagreen': '#8FBC8F', 'pink': '#FFC0CB', 'tomato': '#FF6347', 'lightcoral': '#F08080', 'orangered': '#FF4500', 'navajowhite': '#FFDEAD', 'lime': '#00FF00', 'palegreen': '#98FB98', 'darkslategrey': '#2F4F4F', 'greenyellow': '#ADFF2F', 'burlywood': '#DEB887', 'seashell': '#FFF5EE', 'mediumspringgreen': '#00FA9A', 'fuchsia': '#FF00FF', 'papayawhip': '#FFEFD5', 'blanchedalmond': '#FFEBCD', 'chartreuse': '#7FFF00', 'dimgray': '#696969', 'black': '#000000', 'peachpuff': '#FFDAB9', 'springgreen': '#00FF7F', 'aquamarine': '#7FFFD4', 'white': '#FFFFFF', 'orange': '#FFA500', 'lightsalmon': '#FFA07A', 'darkslategray': '#2F4F4F', 'brown': '#A52A2A', 'ivory': '#FFFFF0', 'dodgerblue': '#1E90FF', 'peru': '#CD853F', 'darkgrey': '#A9A9A9', 'lawngreen': '#7CFC00', 'chocolate': '#D2691E', 'crimson': '#DC143C', 'forestgreen': '#228B22', 'slateblue': '#6A5ACD', 'lightseagreen': '#20B2AA', 'cyan': '#00FFFF', 'mintcream': '#F5FFFA', 'silver': '#C0C0C0', 'antiquewhite': '#FAEBD7', 'mediumorchid': '#BA55D3', 'skyblue': '#87CEEB', 'gray': '#808080', 'darkturquoise': '#00CED1', 'goldenrod': '#DAA520', 'darkgreen': '#006400', 'floralwhite': '#FFFAF0', 'darkviolet': '#9400D3', 'darkgray': '#A9A9A9', 'moccasin': '#FFE4B5', 'saddlebrown': '#8B4513', 'grey': '#808080', 'darkslateblue': '#483D8B', 'lightskyblue': '#87CEFA', 'lightpink': '#FFB6C1', 'mediumvioletred': '#C71585', 'slategrey': '#708090', 'red': '#FF0000', 'deeppink': '#FF1493', 'limegreen': '#32CD32', 'darkmagenta': '#8B008B', 'palegoldenrod': '#EEE8AA', 'plum': '#DDA0DD', 'turquoise': '#40E0D0', 'lightgrey': '#D3D3D3', 'lightgoldenrodyellow': '#FAFAD2', 'darkgoldenrod': '#B8860B', 'lavender': '#E6E6FA', 'maroon': '#800000', 'yellowgreen': '#9ACD32', 'sandybrown': '#FAA460', 'thistle': '#D8BFD8', 'violet': '#EE82EE', 'navy': '#000080', 'magenta': '#FF00FF', 'dimgrey': '#696969', 'tan': '#D2B48C', 'rosybrown': '#BC8F8F', 'olivedrab': '#6B8E23', 'blue': '#0000FF', 'lightblue': '#ADD8E6', 'ghostwhite': '#F8F8FF', 'honeydew': '#F0FFF0', 'cornflowerblue': '#6495ED', 'linen': '#FAF0E6', 'darkblue': '#00008B', 'powderblue': '#B0E0E6', 'seagreen': '#2E8B57', 'darkkhaki': '#BDB76B', 'snow': '#FFFAFA', 'sienna': '#A0522D', 'mediumblue': '#0000CD', 'royalblue': '#4169E1', 'lightcyan': '#E0FFFF', 'green': '#008000', 'mediumpurple': '#9370DB', 'midnightblue': '#191970', 'cornsilk': '#FFF8DC', 'paleturquoise': '#AFEEEE', 'bisque': '#FFE4C4', 'slategray': '#708090', 'darkcyan': '#008B8B', 'khaki': '#F0E68C', 'wheat': '#F5DEB3', 'teal': '#008080', 'darkorchid': '#9932CC', 'deepskyblue': '#00BFFF', 'salmon': '#FA8072', 'darkred': '#8B0000', 'steelblue': '#4682B4', 'palevioletred': '#DB7093', 'lightslategray': '#778899', 'aliceblue': '#F0F8FF', 'lightslategrey': '#778899', 'lightgreen': '#90EE90', 'orchid': '#DA70D6', 'gainsboro': '#DCDCDC', 'mediumseagreen': '#3CB371', 'lightgray': '#D3D3D3', 'mediumturquoise': '#48D1CC', 'lemonchiffon': '#FFFACD', 'cadetblue': '#5F9EA0', 'lightyellow': '#FFFFE0', 'lavenderblush': '#FFF0F5', 'coral': '#FF7F50', 'purple': '#800080', 'aqua': '#00FFFF', 'whitesmoke': '#F5F5F5', 'mediumslateblue': '#7B68EE', 'darkorange': '#FF8C00', 'mediumaquamarine': '#66CDAA', 'darksalmon': '#E9967A', 'beige': '#F5F5DC', 'blueviolet': '#8A2BE2', 'azure': '#F0FFFF', 'lightsteelblue': '#B0C4DE', 'oldlace': '#FDF5E6'}

    defaultColors _ {}

    ___ colorName __ colors.keys

        hexColor _ colors[colorName]
        colorValue _ hex2interface(hexColor)

        ___ prefix __ ['deep', 'dark', 'medium', 'light']:
            colorName _ colorName.replace(prefix, prefix + ' ')

        defaultColors[colorName] _ colorValue
    
    r_ defaultColors

___ hex2interface(hexColor):
    '''
    Convert a color stored as hex values to a 32 bit value as used by nuke for interface colors.
    '''
    hexColor _ hexColor.lstrip('#')
    rgb _ tuple(in_(hexColor[i:i+2], 16) ___ i __ (0, 2 ,4))
    rgb +_ (255,)

    r_ in_('%02x%02x%02x%02x'%rgb,16)


#----------------------------------------------------------------------------------------------------------
# Menu item
#----------------------------------------------------------------------------------------------------------

___ setMenuItem(itemName):
    '''
    Change the shortcut of the menu item of the defined nodeclass.
    '''

    otherMenu _ ?.m__('Nodes').findItem('Other')

    index _ nodeClasses.index(itemName)

    replace _ in_(preferencesNode.knob('backdropper%sReplaceMenuItem'%itemName).v.. ())

    customItemName _ itemName + ' (W_backdropper)'

    #don't replace
    __ no. replace:

        #restore original
        function _ originalMenuItemScripts[index]
        menuItem _ otherMenu.aC..(itemName, function, icon _ itemName + '.png')

    #replace
    ____
        #remove if applicable
        __ otherMenu.findItem(customItemName):
            otherMenu.removeItem(customItemName)

    #new item
    shortcut _ preferencesNode.knob('backdropper%sShortcut'%itemName).v.. ()
    function _ 'W_backdropper.backdropper("%s")'%itemName
    menuItem _ otherMenu.aC..([customItemName, itemName][replace], function, shortcut, icon _ itemName + '.png')

#----------------------------------------------------------------------------------------------------------
# Preferences
#----------------------------------------------------------------------------------------------------------

___ addKnobToPreferences(knobObject, tooltip _ N..):
    '''
    Add a knob to the preference panel.
    Save current preferences to the prefencesfile in the .nuke folder.
    '''

    __ knobObject.n..  no. __ preferencesNode.knobs().keys

        __ tooltip !_ N..:
            knobObject.setTooltip(tooltip)

        preferencesNode.aK..(knobObject)
        savePreferencesToFile()

        r_ preferencesNode.knob(knobObject.n..

___ savePreferencesToFile
    '''
    Save current preferences to the prefencesfile in the .nuke folder.
    Pythonic alternative to the 'ok' button of the preferences panel.
    '''

    nukeFolder _ __.pa__.e__('~') + '/.nuke/'
    preferencesFile _ nukeFolder + 'preferences{0}.{1}.nk'.f..(?.NUKE_VERSION_MAJOR,?.NUKE_VERSION_MINOR)

    preferencesNode _ ?.tN..('preferences')

    customPrefences _ preferencesNode.writeKnobs( ?.WRITE_USER_KNOB_DEFS | ?.WRITE_NON_DEFAULT_ONLY | ?.TO_SCRIPT | ?.TO_VALUE )
    customPrefences _ customPrefences.replace('\n','\n  ')

    preferencesCode _ 'Preferences {\n inputs 0\n name Preferences%s\n}' %customPrefences

    # write to file
    openPreferencesFile _ open( preferencesFile , 'w')
    openPreferencesFile.write( preferencesCode )
    openPreferencesFile.close()

___ deletePreferences(clicked _ F..):
    '''
    Delete all the W_backdropper related items from the properties panel.
    '''

    firstLaunch _ T..

    ___ knobName __ preferencesNode.knobs().keys
        __ knobName.startswith('backdropper'):
            preferencesNode.removeKnob(preferencesNode.knob(knobName))
            firstLaunch _ F..

    # remove TabKnob
    ___
        preferencesNode.removeKnob(preferencesNode.knob('backdropperLabel'))
    ______
        pass

    __ no. firstLaunch:
        savePreferencesToFile()

    __ clicked:

        #click the cancel button
        closePreferencesPanel()

        #re open panel
        openPreferencesPanel()

___ resetPreferences
    '''
    Reset all the W_backdropper related knobs to their default values.
    '''

    # colorknobs
    ___ number __ ra..(presetSlots):
        number _ st_(number + 1).zf..(2)

        knob _ 'backdropperColor%s'%number
        preferencesNode.knob(knob).sV..('')

        knob +_ 'Color'
        preferencesNode.knob(knob).sV..(defaultColor)

    ___ index, knob __ enumerate(['Backdrop', 'StickyNote']):
        preferencesNode.knob('backdropper%sFontSize'%knob).sV..(defaultFontSizes[index])

___ updatePreferences(forceUpdate _ F..):
    '''
    Check whether the script was updated since the last launch. If so refresh the preferences.
    '''

    aK.. _ preferencesNode.knobs().k..

    # always update if beta version
    __ 'b' __ version:
        forceUpdate _ T..

    #check if current version differs from the previously loaded version.
    __ 'backdropperVersion' __ aK.. and no. forceUpdate:
        __ version __ st_(preferencesNode.knob('backdropperVersion').v.. ()):
            r_

    currentSettings _ {knob:preferencesNode.knob(knob).v.. () ___ knob __ aK.. __ knob.startswith('backdropper') and knob !_ 'backdropperVersion'}

    # amount of slots
    __ 'backdropperSlotCount' __ preferencesNode.knobs().keys
        global presetSlots
        presetSlots _ min(50, max(0, in_(preferencesNode.knob('backdropperSlotCount').v.. ())))

    # delete all the preferences
    deletePreferences()

    # re-add all the knobs
    addPreferences()

    # restore settings
    ___ knob __ currentSettings.keys
        ___
            preferencesNode.knob(knob).sV..(currentSettings[knob])
        ______
            pass

    # save to file
    savePreferencesToFile()

___ closePreferencesPanel(save _ F..):
    '''
    Find and invoke a button found at the bottom of the preferences panel.
    '''

    buttonText _ ['Cancel','OK'][in_(save)]
    preferencesButton _ N..

    # find preferences
    ___ widget __ _W...QApplication.instance().allWidgets
        __ widget.objectName() __ 'foundry.hiero.preferencesdialog':

            # loop over children
            ___ child __ widget.children
                __ isinstance(child, _W..._DBB_):

                    # buttons
                    ___ button __ child.buttons
                        __ button.text() __ buttonText:
                            preferencesButton _ button
                            break
                    break
            break

    __ preferencesButton:
        preferencesButton.click()

___ updateSlotCount
    '''
    Update the slot count.
    '''

    # close panel and save
    closePreferencesPanel T..
    # update knobs
    updatePreferences T..
    # close panel 
    openPreferencesPanel()

___ openPreferencesPanel
    '''
    Open the preferences panel
    '''

    event _ _G...QKeyEvent(_C...QEvent.KeyPress, _C...__.Key_S, _C...__.ShiftModifier)
    nukeInstance _ _W...QApplication.instance()
    nukeInstance.postEvent(nukeInstance, event)

___ addPreferences
    '''
    Add knobs to the preferences needed for this module to work properly.
    '''

    # tab
    addKnobToPreferences(?.T_K_('backdropperLabel','W_backdropper'))

    # version knob to check whether the backdropper was updated
    knob _ ?.String_Knob('backdropperVersion','version')
    knob.sV..(version)
    knob.setVisible F..
    addKnobToPreferences(knob)

    # case sensitive
    knob _ ?.Boolean_Knob('backdropperCaseSensitive','Case sensitive')
    knob.sV.. F..
    tooltip _ 'Only colorize nodes when the casing is matching.'
    addKnobToPreferences(knob, tooltip)

    # case sensitive
    knob _ ?.Boolean_Knob('backdropperRecognizeColors','Recognize color names')
    knob.sV.. T..
    # knob.clearFlag(nuke.STARTLINE)  
    tooltip _ 'Change the color of the node whenever it\'s label contains a color name (eg. color the node red when the label contains the word "red").'
    addKnobToPreferences(knob, tooltip)

    # Rule/Class order
    knob _ ?.Enumeration_Knob('backdropperOrder', '', ['Keywords - Color names', 'Color names - Keywords'])
    knob.clearFlag(?.STARTLINE)
    tooltip _ 'Order of importance regarding matching a label of a node to a color.'
    addKnobToPreferences(knob, tooltip)

    addKnobToPreferences(?.Text_Knob('backdropperKeywordLabel','<b>Keywords</b>'))

    # colorknobs
    ___ number __ ra..(in_(presetSlots)):
        number _ st_(number + 1).zf..(2)

        name _ 'backdropperColor%s'%number
        knob _ ?.String_Knob(name,'')
        tooltip _ 'The labels that will have the given default color.'

        addKnobToPreferences(knob, tooltip)

        name +_ 'Color'
        knob _ ?.ColorChip_Knob(name,'')
        knob.sV..(defaultColor)
        knob.clearFlag(?.STARTLINE)
        tooltip _ 'The default color for the given labels.'

        addKnobToPreferences(knob, tooltip)

    ___ nodeClass __ nodeClasses:

        index _ nodeClasses.index(nodeClass)

        addKnobToPreferences(?.Text_Knob('backdropper%sLabel'%nodeClass,'<b>%s</b>'%nodeClass))

        # backdrop font size
        knob _ ?.Int_Knob('backdropper%sFontSize'%nodeClass,'Font size')
        knob.sV..(defaultFontSizes[index])
        tooltip _ 'Default font size for the label of %s nodes.'%nodeClass
        addKnobToPreferences(knob, tooltip)
        
        # backdrop shortcut knob
        knob _ ?.String_Knob('backdropper%sShortcut'%nodeClass,'    Shortcut ')
        knob.sV..('Alt+' + ['b','n'][index])
        knob.clearFlag(?.STARTLINE)
        tooltip _ 'Shortcut to create a %s node.'%nodeClass
        addKnobToPreferences(knob, tooltip)

        # change shortcut

        knob _ ?.PS_K..('backdropper%sSetShortcut'%nodeClass,'set','W_backdropper.setMenuItem("%s")'%nodeClass)
        tooltip _ 'Apply shortcut.'
        addKnobToPreferences(knob, tooltip)

        # replace sticky note
        knob _ ?.Boolean_Knob('backdropper%sReplaceMenuItem'%nodeClass,'replace')
        knob.sV.. F..
        tooltip _ 'Replace original menu item.'
        addKnobToPreferences(knob, tooltip)

    addKnobToPreferences(?.Text_Knob('backdropperPreferences','<b>Preferences</b>'))

    # slot count
    knob _ ?.Int_Knob('backdropperSlotCount','Slots')
    knob.sV..(presetSlots)
    tooltip _ 'The amount of slots available to the user.'
    addKnobToPreferences(knob, tooltip)

    # set slot count
    knob _ ?.PS_K..('backdropperUpdateSlotCount','set', 'W_backdropper.updateSlotCount()')
    tooltip _ "Reset all the W_backdropper related knobs to their default values."
    addKnobToPreferences(knob, tooltip)

    # _____ preferences button knob
    knob _ ?.PS_K..('backdropperImportExportPreferences',' _____/export ','W_backdropper.importExportPanel()')
    tooltip _ "Reset all the W_backdropper related knobs to their default values."
    addKnobToPreferences(knob, tooltip)

    # delete preferences button knob
    knob _ ?.PS_K..('backdropperResetPreferences','clear','W_backdropper.resetPreferences()')
    tooltip _ "Reset all the W_backdropper related knobs to their default values."
    addKnobToPreferences(knob, tooltip)

    # delete preferences button knob
    knob _ ?.PS_K..('backdropperDeletePreferences',' uninstall ','W_backdropper.deletePreferences(True)')
    tooltip _ "Delete all the W_backdropper related knobs from the Preferences Panel. After clicking this button the Preferences Panel should be closed by clicking the 'cancel' button."
    addKnobToPreferences(knob, tooltip)

#----------------------------------------------------------------------------------------------------------
# _____/Export
#----------------------------------------------------------------------------------------------------------

c_ ImportExportWidget(_W..._W..):

    ___  -

        s__(ImportExportWidget, ). - ()

        setParent(_W...QApplication.instance().activeWindow())
        sWF..(_C...__.Tool)

        dividerLine _ '-'*106
        header _ ['#%s'%dividerLine,
            '#',
            '# W_BACKDROPPER SETTINGS FILE',
            '#',
            '# CREATED ON {0} BY {1}'.f..(dt.now().s_t_('%A %d %B %Y (%H:%M)').upper(), getuser().upper()),
            '#',
            '#%s\n\n'%dividerLine]
        header _ '\n'.j..(header)

        #--------------------------------------------------------------------------------------------------
        
        clipboardRadioButton _ _W...QRadioButton('Clipboard')
        clipboardRadioButton.setChecked T..

        fileRadioButton _ _W...QRadioButton('File')
        fileRadioButton.toggled.connect(toggleFileWidgets)

        modeLayout _ _W...QHBoxLayout()
        modeLayout.addStretch()
        ___ widget __ [clipboardRadioButton, fileRadioButton]:
            modeLayout.aW..(widget)
        modeLayout.addStretch()

        #--------------------------------------------------------------------------------------------------

        pathLabel _ _W...QLabel('Path')
        pathLineEdit _ _W...QLineEdit('')
        pathButton _ _W...QPushButton('Browse')
        pathButton.clicked.connect(browseFile)

        toggleFileWidgets()

        pathLayout _ _W...QHBoxLayout()
        ___ widget __ [pathLabel, pathLineEdit, pathButton]:
            pathLayout.aW..(widget)

        #--------------------------------------------------------------------------------------------------

        importButton _ _W...QPushButton('_____')
        importButton.clicked.connect(importSettings)

        exportButton _ _W...QPushButton('Export')
        exportButton.clicked.connect(exportSettings)

        cancelButton _ _W...QPushButton('Cancel')
        cancelButton.clicked.connect(close)

        buttonLayout _ _W...QHBoxLayout()
        ___ widget __ [importButton, exportButton, cancelButton]:
            buttonLayout.aW..(widget)

        #--------------------------------------------------------------------------------------------------

        mainLayout _ _W...QVBoxLayout()

        ___ layout __ [modeLayout, pathLayout, LineWidget(), buttonLayout]:
            __ isinstance(layout, _W...QHBoxLayout):
                mainLayout.addLayout(layout)
            ____
                mainLayout.aW..(layout)

        mainLayout.setSizeConstraint( _W...QLayout.SetFixedSize )
        sL..(mainLayout)

        #--------------------------------------------------------------------------------------------------

        adjustSize()
        move(_G..._C..().p.. - _C..._P..((width()/2),(height()/2)))


    ___ toggleFileWidgets
        '''
        Disable parts of the interface when the switch checkbox changes state
        '''
        
        state _ fileRadioButton.isChecked()

        ___ widget __ [pathLineEdit, pathButton]:
            widget.setEnabled(state)

    ___ browseFile
        '''
        Launch browser to navigate to the desired file
        '''
        extension _ '.backdropper'
        filePath _ ?.getFilename('W_backdropper', '*' + extension)
        __ filePath:
            __ no. filePath.endswith(extension):
                filePath +_ extension

            pathLineEdit.setText(filePath)

    ___ exportSettings
        '''
        Export the current settings to either a file or the clipboard.
        '''

        settings _ preferencesNode.writeKnobs(?.TO_VALUE | ?.WRITE_USER_KNOB_DEFS)

        #replace numbers with placeholder
        indexPlaceHolder _ '_*BACKDROPINDEX*_'
        settings _ re.sub(r'(?<=backdropperColor)([0-9]{2})(?<![\s C])', indexPlaceHolder, settings)

        settings _ settings.s..('\n')
        settings _ [line ___ line __ settings __ 'backdropperColor' __ line]

        #split in chunks of four (textinput and colorswatch, adduserknob command and the stored value)
        settings _ [settings[index:index + 4] ___ index __ ra..(0, le.(settings), 4)]

        settings _ [line ___ line __ settings __ no. (line[1].s..()[-1] __ '""' and line[3].s..()[-1] __ '0xccccccff')]

        settings _ ['\n'.j..(line) ___ line __ settings]
        settings _ [line.replace(indexPlaceHolder, st_(index + 1).zf..(2)) ___ index, line __ enumerate(settings)]

        settings _ '\n'.j..(settings)

        settings _ header + settings

        __ fileRadioButton.isChecked
            location _ pathLineEdit.text()
            with open(location, 'w') as file:
                file.write(settings)

        ____
            _W...QApplication.clipboard().setText(settings)
            location _ 'clipboard'

        ?.m__('W_backdropper settings succesfully writen to {0}.'.f..(location))
        close()

    ___ importSettings
        '''
        _____ settings from either a file or the clipboard.
        '''

        preferencesKnobs _ preferencesNode.knobs().k..
        slotPrefix _ 'backdropperColor'

        __ fileRadioButton.isChecked
            location _ pathLineEdit.text()
            __ no. location.endswith('.backdropper'):
                ?.m__('Invalid file')
                r_

            with open(location) as file:
                settings _ file.read()

        ____
            settings _ _W...QApplication.clipboard().text()

        #remove header and split in lines
        settings _ [line ___ line __ settings.s..('\n') __ line and no. line.startswith('#')]

        # filter addUserKnob line for knobs that are already present
        ___ line __ settings[::1]:

            __ line.startswith('addUserKnob'):

                ___ word __ line.s..(' '):
                    __ word.startswith(slotPrefix):
                        __ word __ preferencesKnobs:
                            settings.r__(line)
                        break

        settings _ '\n'.j..(settings)

        # apply 
        preferencesNode.readKnobs(settings)

        # count slots
        slotCount _ le.([knob ___ knob __ preferencesNode.knobs().k..  __ knob.startswith('backdropperColor') and knob[-1].isdigit()])

        slotCountKnob _ preferencesNode.knob('backdropperSlotCount')
        __ slotCount !_ slotCountKnob.v..
            slotCountKnob.sV..(slotCount)
            
            # save to disk and close preferences
            closePreferencesPanel T..
            updatePreferences T..
            openPreferencesPanel()

        close()

c_ LineWidget(_W...QFrame):

    ___  -

        s__(LineWidget, ). - ()

        setFrameShape(_W...QFrame.HLine)
        setFrameShadow(_W...QFrame.Sunken)

___ importExportPanel
    '''
    Open panel to allow the user to export or _____ settings.
    '''
    global importExportPanelInstance
    ___
        importExportPanelInstance.close()
    ______
        pass
        
    importExportPanelInstance _ ImportExportWidget()
    importExportPanelInstance.show()

#----------------------------------------------------------------------------------------------------------

___ colorizeNodes(all _ F..):
    '''
    Colorize all nodes of a specific class. Pick colors according to their labels.
    '''

    nodeClasses _ ['BackdropNode', 'StickyNote']

    #selection
    __ all:
        selection _ ?.aN..()

        # create panel instance
        panel _ ?.Panel('W_backdropper - Colorize %s nodes'%['selected', 'all'][in_(all)])

        ___ nodeClass __ nodeClasses:
            panel.addBooleanCheckBox(nodeClass, T..)

        __ panel.show

            ___ nodeClass __ nodeClasses:
                __ no. panel.v.. (nodeClass):
                    nodeClasses.r__(nodeClass)

    ____
        selection _ ?.sN..

    #selection
    selection _ [node ___ node __ selection __ node.C..  __ nodeClasses]

    ___ node __ selection:
        colorizeNode(node)

#----------------------------------------------------------------------------------------------------------

colorNamesDict _ indexDefaultColors()
preferencesNode _ ?.tN..('preferences')
importExportPanelInstance _ N..

defaultColor _ 3435973887
defaultFontSizes _ [42, 11]

presetSlots _ 15

nodeClasses _ ['Backdrop', 'StickyNote']

originalMenuItemScripts _ [?.m__('Nodes').findItem('Other/' + nodeClass).script() ___ nodeClass __ nodeClasses]

___ init

    #preferences
    updatePreferences()

    #node menu items
    ___ nodeClass __ nodeClasses:
        setMenuItem(nodeClass)

    #edit menu items
    m__ _ ?.m__('Nuke').findItem('&Edit/Node')
    m__ _ m__.addMenu('W_backdropper')

    ___ nodeClass __ nodeClasses:
        m__.aC..('Colorize selected nodes', colorizeNodes)
        m__.aC..('Colorize all nodes', l____ : colorizeNodes(T..))

#----------------------------------------------------------------------------------------------------------

init()

