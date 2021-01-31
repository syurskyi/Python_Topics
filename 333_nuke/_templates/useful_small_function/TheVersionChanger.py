_____ re, __.pa__, ?, n_s_


Selection _ ?.sN..

OldSelect1 _ []

   
___ SplitDir(fileknob):


    FileName _ __.pa__.b__(fileknob)

         
    Dir _ __.pa__.d..(fileknob)
                    
                    
    DirUp _ __.pa__.s..(Dir)
                    
                    
    Joined _ __.pa__.n_p_ (__.pa__.j..(DirUp[1],FileName))
                    
                    
    Joined _ re.sub(r'\\', r'/' ,Joined)
    
    
    r_ Joined
    
    
        
___ SplitDirUp(fileknob):


    FileName _ __.pa__.b__(fileknob)
    
         
    Dir _ __.pa__.d..(fileknob)
    
                    
    DirUp _ __.pa__.s..(Dir)[0]
    
    
    r_ DirUp
    
    

___ FindVersion(fileknob):


    pattern _ "v" + "\d+"


    MyList _ re.findall(pattern,fileknob,re.IGNORECASE)


    __ MyList:
  

        version _ MyList[0][:1]


        versionNumber _ MyList[0][1:]


        r_ versionNumber



___ ListVersions(fileknob):


    FileName _ __.pa__.b__(fileknob)


    FileBase _ FileName.s..(FindVersion(SplitDir(fileknob)))[0]

 
    Dir _ __.pa__.d..(fileknob)


    DirUp _ __.pa__.s..(Dir)[0]


    Names _ [name ___ name __ __.l_d_(DirUp) __ FileBase __ name]


    OnlyFolders _ []


    ___ i __ Names:


        Joined _ __.pa__.n_p_ (__.pa__.j..(DirUp,i))


        check _ __.pa__.i_d_(Joined)


        version _ FindVersion(i)


        __ check:


            __ version no. __ OnlyFolders:


                OnlyFolders.ap..(version)


    r_ sorted(OnlyFolders)

    
    
___ ListVersionsFiles(fileknob):


    FileName _ __.pa__.b__(fileknob)


    FileBase _ FileName.s..(FindVersion(FileName))[0]

 
    Dir _ __.pa__.d..(fileknob)


    Names _ [name ___ name __ __.l_d_(Dir) __ FileBase __ name]


    OnlyFiles _ []


    ___ i __ Names:


        Joined _ __.pa__.n_p_ (__.pa__.j..(Dir,i))


        check _ __.pa__.isfile(Joined)


        version _ FindVersion(i)


        __ check:


            __ version no. __ OnlyFiles:


                OnlyFiles.ap..(version)


    r_ sorted(OnlyFiles)



___ VersionUp(KnobTypes,NodeTypes):

    count _ 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:

                ___

                    fileknob _ node[n].v.. ()
                    

                    FileName _ __.pa__.b__(fileknob)
                    

                    version _ FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile _ FindVersion(FileName)


                    __ version !_ versionFile:


                        print "Error: different versions found in " + node.n..  + " " + n

                     
                    __ version:

                
                        Next _ in_(version)+1

                  
                        string_Next _ "%03d" % Next

                  
                        __ version < max(ListVersions(fileknob)):

                 
                            while string_Next no. __ ListVersions(fileknob):
                   
                   
                                Next+_1
                   
                   
                                string_Next _ "%03d" % Next
          
                
                            old _ node[n].v.. ()
                   
                   
                            NewStr_re.sub("v"+version,"v"+string_Next,SplitDir(fileknob))

                            
                            Joined _ __.pa__.n_p_ (__.pa__.j..(SplitDirUp(fileknob),NewStr))
                    
                    
                            Joined _ re.sub(r'\\', r'/' ,Joined)
                   
                   
                            node[n].sV..(Joined)


                            new _ node[n].v.. ()


                            __ old !_ new:


                                count+_1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n

                except :

                    pass


    r_ count
    
       
       
___ VersionUpFiles(KnobTypes,NodeTypes):

    count _ 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:

                ___

                    fileknob _ node[n].v.. ()
                    
                    FileName _ __.pa__.b__(fileknob)
         
                    Dir _ __.pa__.d..(fileknob)
                   
                    version _ FindVersion(FileName)
                     
                    __ version:
                
                        Next _ in_(version)+1
                  
                        string_Next _ "%03d" % Next
                  
                        __ version < max(ListVersionsFiles(fileknob)):
                 
                            while string_Next no. __ ListVersionsFiles(fileknob):
                   
                   
                                Next+_1
                   
                   
                                string_Next _ "%03d" % Next
          
                
                            old _ node[n].v.. ()
                            
                   
                            FileName_re.sub("v"+version,"v"+string_Next,FileName)
                            

                            Joined _ __.pa__.n_p_ (__.pa__.j..(Dir,FileName))
                            
                            
                            Joined _ re.sub(r'\\', r'/' ,Joined)
                            
                   
                            node[n].sV..(Joined)

                            
                            new _ node[n].v.. ()


                            __ old !_ new:


                                count+_1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n

                ______

                     pass


    r_ count
    
       
___ VersionDown(KnobTypes,NodeTypes):

    count _ 0

    ___ node __ ?.sN.. :

        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:
    
                ___

                    fileknob _ node[n].v.. ()


                    FileName _ __.pa__.b__(fileknob)
                    

                    version _ FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile _ FindVersion(FileName)


                    __ version !_ versionFile:


                        print "Error: different versions found in " + node.n..  + " " + n


                    __ version:


                        Previous _ in_(version)-1

          
                        string_Previous _ "%03d" % Previous


                        __ version > min(ListVersions(fileknob)):


                            while string_Previous no. __ ListVersions(fileknob):


                                Previous-_1


                                string_Previous _ "%03d" % Previous


                            old _ node[n].v.. ()
                   
                   
                            NewStr_re.sub("v"+version,"v"+string_Previous,SplitDir(fileknob))

                            
                            Joined _ __.pa__.n_p_ (__.pa__.j..(SplitDirUp(fileknob),NewStr))
                    
                    
                            Joined _ re.sub(r'\\', r'/' ,Joined)
                   
                   
                            node[n].sV..(Joined)


                            new _ node[n].v.. ()


                            __ old !_ new:


                                count+_1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n


                ______

                    pass


    r_ count
    

___ VersionDownFiles(KnobTypes,NodeTypes):

    count _ 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:
        
                ___


                    fileknob _ node[n].v.. ()

                    
                    FileName _ __.pa__.b__(fileknob)

         
                    Dir _ __.pa__.d..(fileknob)

                   
                    version _ FindVersion(FileName)


                    __ version:


                        Previous _ in_(version)-1

          
                        string_Previous _ "%03d" % Previous


                        __ version > min(ListVersionsFiles(fileknob)):


                            while string_Previous no. __ ListVersionsFiles(fileknob):


                                Previous-_1


                                string_Previous _ "%03d" % Previous


                            old _ node[n].v.. ()

          
                            FileName_re.sub("v"+version,"v"+string_Previous,FileName)
                            

                            Joined _ __.pa__.n_p_ (__.pa__.j..(Dir,FileName))
                            
                            
                            Joined _ re.sub(r'\\', r'/' ,Joined)
                            
                   
                            node[n].sV..(Joined)


                            new _ node[n].v.. ()


                            __ old !_ new:


                                count+_1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n


                ______

                    pass


    r_ count
    

___ VersionLast(KnobTypes,NodeTypes):

    count _ 0

    ___ node __ ?.sN.. :
    
        ___ n __ KnobTypes:

            __ node.C..  __ NodeTypes:
            
                ___

                    fileknob _ node[n].v.. ()


                    FileName _ __.pa__.b__(fileknob)
                    

                    version _ FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile _ FindVersion(FileName)


                    __ version !_ versionFile:


                        print "Error: different versions found in " + node.n..  + " " + n


                    __ version:

           
                        Last _ max(ListVersions(fileknob))


                        old _ node[n].v.. ()
                   
                   
                        NewStr_re.sub("v"+version,"v"+Last,SplitDir(fileknob))

                            
                        Joined _ __.pa__.n_p_ (__.pa__.j..(SplitDirUp(fileknob),NewStr))
                    
                    
                        Joined _ re.sub(r'\\', r'/' ,Joined)
                   
                   
                        node[n].sV..(Joined)


                        new _ node[n].v.. ()


                        __ old !_ new:


                            count+_1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n


                ______

                    pass


    r_ count
    
   
___ VersionLastFiles(KnobTypes,NodeTypes):

    count _ 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:

                ___


                    fileknob _ node[n].v.. ()

                    
                    FileName _ __.pa__.b__(fileknob)

         
                    Dir _ __.pa__.d..(fileknob)

                   
                    version _ FindVersion(FileName)


                    __ version:

           
                        Last _ max(ListVersionsFiles(fileknob))


                        old _ node[n].v.. ()


                        FileName_re.sub("v"+version,"v"+Last,FileName)
                            

                        Joined _ __.pa__.n_p_ (__.pa__.j..(Dir,FileName))
                        
                        
                        Joined _ re.sub(r'\\', r'/' ,Joined)
                            
                   
                        node[n].sV..(Joined)


                        new _ node[n].v.. ()


                        __ old !_ new:


                            count+_1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n


                ______

                    pass


    r_ count


___ VersionMatchFolder(KnobTypes,NodeTypes):

    count _ 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:

                ___

                    fileknob _ node[n].v.. ()


                    FileName _ __.pa__.b__(fileknob)


                    Dir _ __.pa__.d..(fileknob)
                    
                    
                    DirLast _ __.pa__.s..(Dir)[1]
                    

                    version _ FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile _ FindVersion(FileName)


                    __ version:


                        __ version !_ versionFile:


                            old _ node[n].v.. ()


                            FileName _ re.sub("v"+versionFile,"v"+version,FileName)

                            
                            Joined _ __.pa__.n_p_ (__.pa__.j..(SplitDirUp(fileknob),DirLast,FileName))
                    
                    
                            Joined _ re.sub(r'\\', r'/' ,Joined)

                        
                            node[n].sV..(Joined)


                            new _ node[n].v.. ()


                            __ old !_ new:


                                count+_1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n


                ______

                    pass


    r_ count


___ VersionMatchFiles(KnobTypes,NodeTypes):

    count _ 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:

                ___
         
                    fileknob _ node[n].v.. ()
                    

                    Dir _ __.pa__.d..(fileknob)
                    
                    
                    DirLast _ __.pa__.s..(Dir)[1]


                    FileName _ __.pa__.b__(fileknob)
                    

                    version _ FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile _ FindVersion(FileName)


                    __ version !_ versionFile:


                        old _ node[n].v.. ()


                        DirLast _ re.sub("v"+version,"v"+versionFile, DirLast)
                        
                        
                        Joined _ __.pa__.n_p_ (__.pa__.j..(SplitDirUp(fileknob),DirLast,FileName))
                    
                    
                        Joined _ re.sub(r'\\', r'/' ,Joined)

                        
                        node[n].sV..(Joined)


                        new _ node[n].v.. ()


                        __ old !_ new:


                            count+_1


                ______

                    pass


    r_ count

    
___ OldSelect(SavedSelection):

    global OldSelect1

    OldSelect1 _ []

    ___ n __ SavedSelection:

        OldSelect1.ap..(n)
    
    r_ OldSelect1


___ Warning(warning):

    Selection _ ?.sN..
    
    warning.sV..(st_(le.(Selection))+ ' Nodes Selected')
    
    warning.setVisible T..


___ Warning_changed(warning,count):

    warning.sV..(st_(count)+ ' Nodes Changed')
    
    warning.setVisible T..
    

___ Warning_SaveLoad(warning,warningList,index):

    warning.sV..(warningList[index])
    
    warning.setVisible T..
    

___ Warning_Save(warning,Selection):

    count _ le.(Selection)

    warning.sV..(st_(count)+ ' Nodes Saved')
    
    warning.setVisible T..
    

___ Warning_Load(warning,warningList,index):

    Selection _ ?.sN..

    warning.sV..(warningList[index]+"  "+ st_(le.(Selection))+ ' Nodes Selected')
    
    warning.setVisible T..


c_ ChangeVersion(n_s_.PythonPanel):


    ___  -
    

        n_s_.PythonPanel. - (,"The Version Changer","The Version Changer")


        # Create Knobs


        Read _ ?.Boolean_Knob("Read")


        Read.sV.. T..


        Write _ ?.Boolean_Knob("Write")


        DeepRead _ ?.Boolean_Knob("DeepRead")


        DeepWrite _ ?.Boolean_Knob("DeepWrite")


        dividerA _ ?.Text_Knob("")

      
        file _ ?.Boolean_Knob("file","file   ")


        file.sV.. T..


        file.setFlag(?.STARTLINE)


        proxy _ ?.Boolean_Knob("proxy","proxy               ")


        Info _ ?.Boolean_Knob("Info    ")


        Info.sV.. T..
        
        
        VersionFolder _ ?.Boolean_Knob("Version by Folder")


        VersionFolder.sV.. T..
        
        
        dividerB _ ?.Text_Knob("")
        

        Type _ ?.Enumeration_Knob("Type","Type",["All","Selected    ","Custom"])


        Check _ ?.PS_K..('Check', 'Check')


        warning _ ?.Text_Knob('warning',"")

      
        warning.clearFlag(?.STARTLINE)


        warning.setVisible F..


        SelectString _ ?.String_Knob("SelectString", "Select By Value")


        SelectString.setEnabled F..


        Select _ ?.PS_K..('Select', 'Select')


        Select.setEnabled T..


        Select.setFlag(?.STARTLINE)


        Add _ ?.PS_K..('Add', 'Add')


        Add.setEnabled F..


        r__ _ ?.PS_K..('Remove', 'Remove')


        r__.setEnabled F..


        ClearString _ ?.PS_K..('ClearString', 'Clear')


        ClearString.setEnabled F..


        dividerB2 _ ?.Text_Knob("")
        

        ClearSelect _ ?.PS_K..('ClearSelect', 'Clear\n Selection')
        
        
        ClearSelect.setFlag(?.STARTLINE)
        
        
        SaveSelect _ ?.PS_K..('SaveSelect', 'Save\n Selection')

        
        LoadSelect _ ?.PS_K..('LoadSelect', 'Load\n Selection')


        warningD _ ?.Text_Knob('warningD',"")

      
        warningD.clearFlag(?.STARTLINE)


        warningD.setVisible F..


        dividerC _ ?.Text_Knob("")


        SelectManually _ ?.Boolean_Knob("Manual Input")


        SelectVal _ ?.String_Knob("SelectVal", "Select Value")


        SelectVal.setEnabled F..


        ReplaceVal _ ?.String_Knob("ReplaceVal", "Replace With")


        ReplaceVal.setEnabled F..


        Replace _ ?.PS_K..('Replace', 'Replace')


        Replace.setFlag(?.STARTLINE)
        
        
        Replace.setEnabled F..


        Switch _ ?.PS_K..('Switch', 'Switch')


        Switch.setEnabled F..


        Clear _ ?.PS_K..('Clear', 'Clear')


        Clear.setEnabled T..


        Clear.setEnabled F..


        warningB _ ?.Text_Knob('warning',"")

      
        warningB.clearFlag(?.STARTLINE)


        warningB.setVisible F..


        dividerD _ ?.Text_Knob("")


        VersionMatch _ ?.PS_K..("MatchVersions","Version\n Match ")


        VersionMatch.setFlag(?.STARTLINE)


        VersionDown _ ?.PS_K..('VersionDown','Version\n Down')


        VersionUp _ ?.PS_K..('VersionUp','Version\n Up')


        VersionLast _ ?.PS_K..('VersionLast','Version\n Last')


        warningC _ ?.Text_Knob('warning',"")

      
        warningC.clearFlag(?.STARTLINE)


        warningC.setVisible F..


        dividerE _ ?.Text_Knob("")

   
        Reset _ ?.PS_K..('Reset', 'Reset')


        ClearMessage _ ?.PS_K..('ClearMessage', 'Clear')


        dividerF _ ?.Text_Knob("")
        


        # tooltips
        

        Read.setTooltip("""
if checked, panel operations will apply to Read Nodes.
        """)


        Write.setTooltip("""
if checked, panel operations will apply to Write Nodes.
        """)


        DeepRead.setTooltip("""
if checked, panel opertaions will apply to DeepRead Nodes.
        """)

        
        DeepWrite.setTooltip("""
if checked, panel operations will apply to DeepWrite Nodes.
        """)


        file.setTooltip("""
if checked, panel operations will apply to file knobs.
        """)


        proxy.setTooltip("""
if checked, panel operations will apply to proxy knobs.
        """)


        Info.setTooltip("""
if checked, information messages about selected and changed nodes will appear.
        """)
        
        
        VersionFolder.setTooltip("""
versions are set by values containing a "v" prefix followed by a number. (v001, v002 etc...)
        
if checked, existing versions are determined by the folders in one folder up with the same filename.

example: for fileName_v001/fileName_v006.exr version is 001.

if not checked, existing versions are determined by files in the same folder with the same filename.

example: for fileName_v001/fileName_v006.exr version is 006.
        """)


        Type.setTooltip("""
Selection Type:

All - selection will apply to all Nodes, depending on the checked node types ( Read,write, etc... ). 
nodes will be selected only when "Select" Button is pressed.

Selected - operations will apply to selected Nodes. preferably used when node selection is changed via the node graph.

Custom - "Select By Value" option will become available.
nodes will be selected only when "Select" Button is pressed. 
        """)

        ClearSelect.setTooltip("""
deselects all nodes
        """)


        Check.setTooltip("""
checks the amount of selected nodes and outputs a message.
 
preferably used when node selection is changed via the node graph.
        """)


        SelectString.setTooltip("""
selection will apply to nodes containing the value input, depending on checked node types (Read, write etc..) and checked knob types (file and / or proxy ).

nodes will be selected only when "Select" Button is pressed.
        """)


        Select.setTooltip("""
selects nodes by defined node selection type. 

If selection type is "custom", only nodes containing value in "Select By Value" will be selected.
        """)


        Add.setTooltip("""
adds nodes containing value in "Select By Value" to selection.
        """)


        r__.setTooltip("""
removes nodes containing value in "Select By Value" from selection.
        """)


        ClearString.setTooltip("""
clears "Select By Value" field.
        """)


        SaveSelect.setTooltip("""
saves the current selection
        """)

        LoadSelect.setTooltip("""
loads a previosly saved selection.

saved selection is available after panel is closed.

saved selection is not available after script is closed.

        """)


        SelectManually.setTooltip("""
if checked, "Select Value" and "Replace With" fields will become available.
        """)


        SelectVal.setTooltip("""
value to be replaced with the value in "Replace with" inside a knob, 
depending on checked knob type ( file and / or proxy ).
        """)


        ReplaceVal.setTooltip("""
value to replace the selected value in "Select Value" inside a knob,
depending on checked knob type ( file and / or proxy ).
        """)


        Replace.setTooltip("""
replaces value in "Select Value" with "Replace With" value inside a knob,
depending on checked knob type ( file and / or proxy ).
        """)


        Switch.setTooltip("""
switches between values in "Select Value" field and "Replace With" field.
        """)


        Clear.setTooltip("""
clears "Select Value" and "Replace With" fields.
        """)


        VersionMatch.setTooltip("""
if 2 different versions set by "v" prefix are found, they will be matched.

If "Versions By Folder" is checked, the file version will be matched to the folder version.

example: fileName_v001/fileName_v006.exr will become fileName_v001/fileName_v001.exr

If "Versions By Folder" is not checked, the folder version will be matched to the file version.

example: fileName_v001/fileName_v006.exr will become fileName_v006/fileName_v006.exr
        """)


        VersionDown.setTooltip("""
will go to previous available version, set by "v" prefix.

If "Version by Folder" is checked, existing versions are determined by folders names in one folder up with the same filename.
  
example: for "project_name/shot/3d/renders/filename/filename_element_v001/filename_element_v001.%04d.exr", 

exising versions will be determined by folders names existing in "project_name/shot/3d/renders/filename".

If "Versions By Folder" is not checked, existing versions are determined by files in the same folder up with the same filename.

        """)


        VersionUp.setTooltip("""
will go to Next available version, set by "v" prefix.

If "Version by Folder" is checked, existing versions are determined by folders names in one folder up with the same filename.
  
example: for "project_name/shot/3d/renders/filename/filename_element_v001/filename_element_v001.%04d.exr", 

exising versions will be determined by folders names existing in "project_name/shot/3d/renders/filename".

If "Versions By Folder" is not checked, existing versions are determined by files in the same folder up with the same filename.

        """)


        VersionLast.setTooltip("""
will go to Last available version, set by "v" prefix.

If "Version by Folder" is checked, existing versions are determined by folders names in one folder up with the same filename.
  
example: for "project_name/shot/3d/renders/filename/filename_element_v001/filename_element_v001.%04d.exr", 

exising versions will be determined by folders names existing in "project_name/shot/3d/renders/filename".

If "Versions By Folder" is not checked, existing versions are determined by files in the same folder up with the same filename.

        """)


        Reset.setTooltip("""
resets panel
        """)


        ClearMessage.setTooltip("""
clears all messages
        """)



        # add Knobs


        aK..(Read)

    
        aK..(Write)


        aK..(DeepRead)

 
        aK..(DeepWrite)


        aK..(dividerA)


        aK..(file)


        aK..(proxy)


        aK..(Info)
        
        
        aK..(VersionFolder)


        aK..(dividerB)
    

        aK..(Type)


        aK..(Check)


        aK..(warning)


        aK..(SelectString)


        aK..(Select)


        aK..(Add)


        aK..(r__)


        aK..(ClearString)
        
        
        aK..(dividerB2)
        
        
        aK..(ClearSelect)
        
        
        aK..(SaveSelect)
        
        
        aK..(LoadSelect)


        aK..(warningD)


        aK..(dividerC)


        aK..(SelectManually)


        aK..(SelectVal)


        aK..(ReplaceVal)


        aK..(Replace)


        aK..(Switch)


        aK..(Clear)


        aK..(warningB)


        aK..(dividerD)


        aK..(VersionMatch)


        aK..(VersionDown)


        aK..(VersionUp)


        aK..(VersionLast)


        aK..(warningC)


        aK..(dividerE)


        aK..(Reset)


        aK..(ClearMessage)



        # Define node Lists variables


        NodeTypes _ [Read, Write, DeepRead, DeepWrite]


        SelectedNodeTypes _ ["Read"]


        KnobTypes _ [file, proxy]

    
        SelectedKnobTypes _ ["file"]
        
        
        OldSelect _ []


        WarningList _ ["No Nodes Selected","No Selection Saved","Script changed"]



    ___ knobChanged(,knob):
    

        #Selects knob type


        __ knob __ KnobTypes:


            SelectedKnobTypes _ []


            SelectedKnobTypes _ [ k.n..  ___ k __ KnobTypes __ k.gV.. ]



        #Selects node types


        __ knob __ NodeTypes:


            SelectedNodeTypes _ []


            SelectedNodeTypes _ [ node.n..  ___ node __ NodeTypes __ node.gV.. ]
            
            
            
        #Show Info    
        
            
        __ knob __ Info:


            __ Info.gV.. :
            
            
                Check.setEnabled T..


                ClearMessage.setEnabled T..


            ____
            
            
                Check.setEnabled F..
                

                ClearMessage.setEnabled F..


                warning.setVisible F..


                warningB.setVisible F..


                warningC.setVisible F..


                warningD.setVisible F..
                

        #Check Selection    
        

        __ knob __ Check:


            __ Info.gV.. :


                Warning (warning)
                                

       
        #Selects all nodes


        __ Type.v.. ()__"All":
        
        
            SelectString.setEnabled F..
        
        
            Select.setEnabled T..


            Add.setEnabled F..


            r__.setEnabled F..


            ClearString.setEnabled F..


            __ knob __ Select:


                ___ n __ ?.aN..


                    n.sS.. F..


                    __ n.C..  __ SelectedNodeTypes:


                        n.sS.. T..


                __ Info.gV.. :


                    Warning (warning)



        #Selected Nodes


        __ Type.v.. ()__"Selected    ":
        
        
           SelectString.setEnabled F..


           Select.setEnabled F..


           Add.setEnabled F..


           r__.setEnabled F..


           ClearString.setEnabled F..



        #Selects by custom value


        __ Type.v.. ()__"Custom":
        
        
            Select.setEnabled T..


            SelectString.setEnabled T..


            Add.setEnabled T..


            r__.setEnabled T..


            ClearString.setEnabled T..


            __ knob __ Select:


                Custom_SelectString.v.. ()


                ___ n __ ?.aN..


                    n.sS.. F..
                    
                    
                    __ n.C..  __ SelectedNodeTypes:

                
                        ___ knob __ SelectedKnobTypes:


                            __ Custom __ n[knob].v.. () and Custom !_"":


                                n.sS.. T..


                __ Info.gV.. :


                    Warning (warning)


            __ knob __ ClearString:


                SelectString.sV..("")


                __ Info.gV.. :


                    Warning (warning)
                    
                    

        # Adds to Selection


            __ knob __ Add:


                Custom_SelectString.v.. ()


                ___ n __ ?.aN..

    
                    __ n.C..  __ SelectedNodeTypes:

                
                        ___ knob __ SelectedKnobTypes:


                            __ Custom __ n[knob].v.. () and Custom !_"":


                                n.sS.. T..


                __ Info.gV.. :


                    Warning (warning)
 


        #Removes from Selection


            __ knob __ r__:


                Custom _ SelectString.v.. ()


                ___ n __ ?.sN.. :


                    __ n.C..  __ SelectedNodeTypes:

                
                        ___ knob __ SelectedKnobTypes:


                            __ Custom __ n[knob].v.. () and Custom !_"":


                                n.sS.. F..


                __ Info.gV.. :


                    Warning (warning)

      

        #Clears selection


        __ knob __ ClearSelect:


            ___ n __ ?.aN..


                    n.sS.. F..


            __ Info.gV.. :


                Warning (warning)
                
                
        # Save Selection
        
        __ knob __ SaveSelect:
        
            OldSelect _ ?.sN..

            __ no. OldSelect:

                Warning_SaveLoad(warningD,WarningList,0)

            ____

                OldSelect(OldSelect)

                Warning_Save(warningD,OldSelect)

                        
        # Load Selection
           
        __ knob __ LoadSelect:

            __ no. OldSelect1:

                Warning_SaveLoad(warningD,WarningList,1)

            ____

                checkMissing _ F..

                check _ F..
                
                ___ i __ OldSelect1:

                    __ i no. __ ?.aN..

                        checkMissing _ T..
                        
                    __ i __ ?.aN..

                        check _ T..
        
                __ check and no. checkMissing:

                    ___ n __ ?.aN..
    
                        n.sS.. F..

                    ___ i __ OldSelect1:
    
                        i.sS.. T..

                    Warning(warningD)

                ____
                    
                    ___ n __ ?.aN..
    
                        n.sS.. F..

                    ___

                        ___ i __ OldSelect1:
    
                            i.sS.. T..

                    ______

                        pass

                    Warning_Load(warningD,WarningList,2)
               
            

        #Enables/Disables Manual Input


        __ SelectManually.v.. ()__True:
        
        
            SelectVal.setEnabled T..


            ReplaceVal.setEnabled T..


            Replace.setEnabled T..


            Switch.setEnabled T..


            Clear.setEnabled T..
            
            
            VersionMatch.setEnabled F..


            VersionUp.setEnabled F..


            VersionDown.setEnabled F..


            VersionLast.setEnabled F..
            


        ____
        
        
            SelectVal.setEnabled F..


            ReplaceVal.setEnabled F..


            Replace.setEnabled F..

       
            Switch.setEnabled F..


            Clear.setEnabled F..
            
            
            VersionMatch.setEnabled T..


            VersionUp.setEnabled T..


            VersionDown.setEnabled T..


            VersionLast.setEnabled T..
            


        #Replaces String


        __ knob __ Replace:
        

            count _ 0
         

            ___ n __ ?.sN.. :
            
            
                __ n.C..  __ SelectedNodeTypes:


                    ___ knob __ SelectedKnobTypes:

                      
                        old _ n[knob].v.. ()


                        NewStr_re.sub(SelectVal.v.. (),ReplaceVal.v.. (),n[knob].v.. ())


                        n[knob].sV..(NewStr)


                        new _ n[knob].v.. ()


                        __ old !_ new:


                           count+_1


            __ Info.gV.. :


                Warning_changed(warningB,count)



        #Switches between inputs


        __ knob __ Switch:

            temp _ SelectVal.v.. ()
   
            SelectVal.sV..(ReplaceVal.v.. ())

            ReplaceVal.sV..(temp)



        #Clears String Field


        __ knob __ Clear:


            SelectVal.sV..("")


            ReplaceVal.sV..("")



        #Changes Versions    
        
        #Version Match


        __ knob __ VersionMatch:

            ___

                __ Info.gV.. :

                    __ VersionFolder.gV.. :

                        Warning_changed(warningC,VersionMatchFolder(SelectedKnobTypes,SelectedNodeTypes))
                            
                    ____
                        
                        Warning_changed(warningC,VersionMatchFiles(SelectedKnobTypes,SelectedNodeTypes))

                elif VersionFolder.gV.. :

                    VersionMatchFolder(SelectedKnobTypes,SelectedNodeTypes)
                        
                ____
                    
                    VersionMatchFiles(SelectedKnobTypes,SelectedNodeTypes)

            ______

                pass
                   
                   
        #Version Up
        

        __ knob __ VersionUp:

            ___
                    
                __ Info.gV.. :

                    __ VersionFolder.gV.. :

                        Warning_changed(warningC,VersionUp(SelectedKnobTypes,SelectedNodeTypes))
                            
                    ____
                        
                        Warning_changed(warningC,VersionUpFiles(SelectedKnobTypes,SelectedNodeTypes))

                elif VersionFolder.gV.. :

                    VersionUp(SelectedKnobTypes,SelectedNodeTypes)
                        
                ____
                    
                    VersionUpFiles(SelectedKnobTypes,SelectedNodeTypes)

            ______

                pass
                   

        #Version Down    
        

        __ knob __ VersionDown:

            ___

                __ Info.gV.. :

                    __ VersionFolder.gV.. :

                        Warning_changed(warningC,VersionDown(SelectedKnobTypes,SelectedNodeTypes))
                        
                    ____
                        
                        Warning_changed(warningC,VersionDownFiles(SelectedKnobTypes,SelectedNodeTypes))

                elif VersionFolder.gV.. :

                    VersionDown(SelectedKnobTypes,SelectedNodeTypes)
                        
                ____
                    
                    VersionDownFiles(SelectedKnobTypes,SelectedNodeTypes)

            ______

                pass
                    
                    
        #Version Last
        

        __ knob __ VersionLast:

            ___

                __ Info.gV.. :

                    __ VersionFolder.gV.. :

                        Warning_changed(warningC,VersionLast(SelectedKnobTypes,SelectedNodeTypes))
                            
                    ____
                        
                        Warning_changed(warningC,VersionLastFiles(SelectedKnobTypes,SelectedNodeTypes))

                elif VersionFolder.gV.. :

                    VersionLast(SelectedKnobTypes,SelectedNodeTypes)
                        
                ____
                    
                    VersionLastFiles(SelectedKnobTypes,SelectedNodeTypes)

            ______

                pass


        # Resets


        __ knob __ Reset:


            SelectedNodeTypes _ ["Read"]


            SelectedKnobTypes _ ["file"]


            Read.sV.. T..


            Write.sV.. F..


            DeepRead.sV.. F..


            DeepWrite.sV.. F..


            file.sV.. T..


            proxy.sV.. F..
            
            
            Info.sV.. T..


            VersionFolder.sV.. T..


            Type.sV..("All")


            SelectString.sV..("")


            SelectString.setEnabled F..


            Add.setEnabled F..


            r__.setEnabled F..


            ClearString.setEnabled F..


            SelectManually.sV.. F..


            SelectVal.setEnabled F..


            SelectVal.sV..("")


            ReplaceVal.sV..("")


            ReplaceVal.setEnabled F..
            
            
            Replace.setEnabled F..


            Switch.setEnabled F..


            Clear.setEnabled F..
            
            
            VersionMatch.setEnabled T..


            VersionUp.setEnabled T..


            VersionDown.setEnabled T..


            VersionLast.setEnabled T..


            warning.setVisible F..


            warningB.setVisible F..


            warningC.setVisible F..
            

            warningD.setVisible F..


            ClearMessage.setEnabled T..
            


        #Clears Messages            

        
        __ knob __ ClearMessage:


            warning.setVisible F..


            warningB.setVisible F..


            warningC.setVisible F..
            

            warningD.setVisible F..
            


___ addPanel

    pane _ ?.getPaneFor('Viewer.1')

    r_ ChangeVersion().addToPane(pane)


m__ _ ?.m__("Pane")

m__.aC..("The Version Changer",addPanel,"Alt+v")

n_s_.registerPanel("The Version Changer",addPanel)

#ChangeVersion().showModalDialog()0
