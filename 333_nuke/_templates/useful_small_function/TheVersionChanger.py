_____ re, __.pa__, ?, n_s_


Selection = ?.sN..

OldSelect1 = []

   
___ SplitDir(fileknob):


    FileName = __.pa__.b__(fileknob)

         
    Dir = __.pa__.d..(fileknob)
                    
                    
    DirUp = __.pa__.s..(Dir)
                    
                    
    Joined = __.pa__.n_p_ (__.pa__.join(DirUp[1],FileName))
                    
                    
    Joined = re.sub(r'\\', r'/' ,Joined)
    
    
    r_ Joined
    
    
        
___ SplitDirUp(fileknob):


    FileName = __.pa__.b__(fileknob)
    
         
    Dir = __.pa__.d..(fileknob)
    
                    
    DirUp = __.pa__.s..(Dir)[0]
    
    
    r_ DirUp
    
    

___ FindVersion(fileknob):


    pattern = "v" + "\d+"


    MyList = re.findall(pattern,fileknob,re.IGNORECASE)


    __ MyList:
  

        version = MyList[0][:1]


        versionNumber = MyList[0][1:]


        r_ versionNumber



___ ListVersions(fileknob):


    FileName = __.pa__.b__(fileknob)


    FileBase = FileName.s..(FindVersion(SplitDir(fileknob)))[0]

 
    Dir = __.pa__.d..(fileknob)


    DirUp = __.pa__.s..(Dir)[0]


    Names = [name ___ name __ __.l_d_(DirUp) __ FileBase __ name]


    OnlyFolders = []


    ___ i __ Names:


        Joined = __.pa__.n_p_ (__.pa__.join(DirUp,i))


        check = __.pa__.i_d_(Joined)


        version = FindVersion(i)


        __ check:


            __ version no. __ OnlyFolders:


                OnlyFolders.ap..(version)


    r_ sorted(OnlyFolders)

    
    
___ ListVersionsFiles(fileknob):


    FileName = __.pa__.b__(fileknob)


    FileBase = FileName.s..(FindVersion(FileName))[0]

 
    Dir = __.pa__.d..(fileknob)


    Names = [name ___ name __ __.l_d_(Dir) __ FileBase __ name]


    OnlyFiles = []


    ___ i __ Names:


        Joined = __.pa__.n_p_ (__.pa__.join(Dir,i))


        check = __.pa__.isfile(Joined)


        version = FindVersion(i)


        __ check:


            __ version no. __ OnlyFiles:


                OnlyFiles.ap..(version)


    r_ sorted(OnlyFiles)



___ VersionUp(KnobTypes,NodeTypes):

    count = 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:

                ___

                    fileknob = node[n].v.. ()
                    

                    FileName = __.pa__.b__(fileknob)
                    

                    version = FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile = FindVersion(FileName)


                    __ version != versionFile:


                        print "Error: different versions found in " + node.n..  + " " + n

                     
                    __ version:

                
                        Next = in_(version)+1

                  
                        string_Next = "%03d" % Next

                  
                        __ version < max(ListVersions(fileknob)):

                 
                            while string_Next no. __ ListVersions(fileknob):
                   
                   
                                Next+=1
                   
                   
                                string_Next = "%03d" % Next
          
                
                            old = node[n].v.. ()
                   
                   
                            NewStr=re.sub("v"+version,"v"+string_Next,SplitDir(fileknob))

                            
                            Joined = __.pa__.n_p_ (__.pa__.join(SplitDirUp(fileknob),NewStr))
                    
                    
                            Joined = re.sub(r'\\', r'/' ,Joined)
                   
                   
                            node[n].sV..(Joined)


                            new = node[n].v.. ()


                            __ old != new:


                                count+=1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n

                except :

                    pass


    r_ count
    
       
       
___ VersionUpFiles(KnobTypes,NodeTypes):

    count = 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:

                ___

                    fileknob = node[n].v.. ()
                    
                    FileName = __.pa__.b__(fileknob)
         
                    Dir = __.pa__.d..(fileknob)
                   
                    version = FindVersion(FileName)
                     
                    __ version:
                
                        Next = in_(version)+1
                  
                        string_Next = "%03d" % Next
                  
                        __ version < max(ListVersionsFiles(fileknob)):
                 
                            while string_Next no. __ ListVersionsFiles(fileknob):
                   
                   
                                Next+=1
                   
                   
                                string_Next = "%03d" % Next
          
                
                            old = node[n].v.. ()
                            
                   
                            FileName=re.sub("v"+version,"v"+string_Next,FileName) 
                            

                            Joined = __.pa__.n_p_ (__.pa__.join(Dir,FileName))
                            
                            
                            Joined = re.sub(r'\\', r'/' ,Joined)
                            
                   
                            node[n].sV..(Joined)

                            
                            new = node[n].v.. ()


                            __ old != new:


                                count+=1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n

                ______

                     pass


    r_ count
    
       
___ VersionDown(KnobTypes,NodeTypes):

    count = 0

    ___ node __ ?.sN.. :

        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:
    
                ___

                    fileknob = node[n].v.. ()


                    FileName = __.pa__.b__(fileknob)
                    

                    version = FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile = FindVersion(FileName)


                    __ version != versionFile:


                        print "Error: different versions found in " + node.n..  + " " + n


                    __ version:


                        Previous = in_(version)-1

          
                        string_Previous = "%03d" % Previous


                        __ version > min(ListVersions(fileknob)):


                            while string_Previous no. __ ListVersions(fileknob):


                                Previous-=1


                                string_Previous = "%03d" % Previous


                            old = node[n].v.. ()
                   
                   
                            NewStr=re.sub("v"+version,"v"+string_Previous,SplitDir(fileknob))

                            
                            Joined = __.pa__.n_p_ (__.pa__.join(SplitDirUp(fileknob),NewStr))
                    
                    
                            Joined = re.sub(r'\\', r'/' ,Joined)
                   
                   
                            node[n].sV..(Joined)


                            new = node[n].v.. ()


                            __ old != new:


                                count+=1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n


                ______

                    pass


    r_ count
    

___ VersionDownFiles(KnobTypes,NodeTypes):

    count = 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:
        
                ___


                    fileknob = node[n].v.. ()

                    
                    FileName = __.pa__.b__(fileknob)

         
                    Dir = __.pa__.d..(fileknob)

                   
                    version = FindVersion(FileName)


                    __ version:


                        Previous = in_(version)-1

          
                        string_Previous = "%03d" % Previous


                        __ version > min(ListVersionsFiles(fileknob)):


                            while string_Previous no. __ ListVersionsFiles(fileknob):


                                Previous-=1


                                string_Previous = "%03d" % Previous


                            old = node[n].v.. ()

          
                            FileName=re.sub("v"+version,"v"+string_Previous,FileName) 
                            

                            Joined = __.pa__.n_p_ (__.pa__.join(Dir,FileName))
                            
                            
                            Joined = re.sub(r'\\', r'/' ,Joined)
                            
                   
                            node[n].sV..(Joined)


                            new = node[n].v.. ()


                            __ old != new:


                                count+=1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n


                ______

                    pass


    r_ count
    

___ VersionLast(KnobTypes,NodeTypes):

    count = 0

    ___ node __ ?.sN.. :
    
        ___ n __ KnobTypes:

            __ node.C..  __ NodeTypes:
            
                ___

                    fileknob = node[n].v.. ()


                    FileName = __.pa__.b__(fileknob)
                    

                    version = FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile = FindVersion(FileName)


                    __ version != versionFile:


                        print "Error: different versions found in " + node.n..  + " " + n


                    __ version:

           
                        Last = max(ListVersions(fileknob))


                        old = node[n].v.. ()
                   
                   
                        NewStr=re.sub("v"+version,"v"+Last,SplitDir(fileknob))

                            
                        Joined = __.pa__.n_p_ (__.pa__.join(SplitDirUp(fileknob),NewStr))
                    
                    
                        Joined = re.sub(r'\\', r'/' ,Joined)
                   
                   
                        node[n].sV..(Joined)


                        new = node[n].v.. ()


                        __ old != new:


                            count+=1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n


                ______

                    pass


    r_ count
    
   
___ VersionLastFiles(KnobTypes,NodeTypes):

    count = 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:

                ___


                    fileknob = node[n].v.. ()

                    
                    FileName = __.pa__.b__(fileknob)

         
                    Dir = __.pa__.d..(fileknob)

                   
                    version = FindVersion(FileName)


                    __ version:

           
                        Last = max(ListVersionsFiles(fileknob))


                        old = node[n].v.. ()


                        FileName=re.sub("v"+version,"v"+Last,FileName) 
                            

                        Joined = __.pa__.n_p_ (__.pa__.join(Dir,FileName))
                        
                        
                        Joined = re.sub(r'\\', r'/' ,Joined)
                            
                   
                        node[n].sV..(Joined)


                        new = node[n].v.. ()


                        __ old != new:


                            count+=1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n


                ______

                    pass


    r_ count


___ VersionMatchFolder(KnobTypes,NodeTypes):

    count = 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:

                ___

                    fileknob = node[n].v.. ()


                    FileName = __.pa__.b__(fileknob)


                    Dir = __.pa__.d..(fileknob)
                    
                    
                    DirLast = __.pa__.s..(Dir)[1]
                    

                    version = FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile = FindVersion(FileName)


                    __ version:


                        __ version != versionFile:


                            old = node[n].v.. ()


                            FileName = re.sub("v"+versionFile,"v"+version,FileName)

                            
                            Joined = __.pa__.n_p_ (__.pa__.join(SplitDirUp(fileknob),DirLast,FileName))
                    
                    
                            Joined = re.sub(r'\\', r'/' ,Joined)

                        
                            node[n].sV..(Joined)


                            new = node[n].v.. ()


                            __ old != new:


                                count+=1

                    ____

                        print "Error: No versions found in " + node.n..  + " " + n


                ______

                    pass


    r_ count


___ VersionMatchFiles(KnobTypes,NodeTypes):

    count = 0

    ___ node __ ?.sN.. :
    
        __ node.C..  __ NodeTypes:
        
            ___ n __ KnobTypes:

                ___
         
                    fileknob = node[n].v.. ()
                    

                    Dir = __.pa__.d..(fileknob)
                    
                    
                    DirLast = __.pa__.s..(Dir)[1]


                    FileName = __.pa__.b__(fileknob)
                    

                    version = FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile = FindVersion(FileName)


                    __ version != versionFile:


                        old = node[n].v.. ()


                        DirLast = re.sub("v"+version,"v"+versionFile, DirLast)
                        
                        
                        Joined = __.pa__.n_p_ (__.pa__.join(SplitDirUp(fileknob),DirLast,FileName))
                    
                    
                        Joined = re.sub(r'\\', r'/' ,Joined)

                        
                        node[n].sV..(Joined)


                        new = node[n].v.. ()


                        __ old != new:


                            count+=1


                ______

                    pass


    r_ count

    
___ OldSelect(SavedSelection):

    global OldSelect1

    OldSelect1 = []

    ___ n __ SavedSelection:

        OldSelect1.ap..(n)
    
    r_ OldSelect1


___ Warning(warning):

    Selection = ?.sN..
    
    warning.sV..(str(le.(Selection))+ ' Nodes Selected')
    
    warning.setVisible T..


___ Warning_changed(warning,count):

    warning.sV..(str(count)+ ' Nodes Changed')
    
    warning.setVisible T..
    

___ Warning_SaveLoad(warning,warningList,index):

    warning.sV..(warningList[index])
    
    warning.setVisible T..
    

___ Warning_Save(warning,Selection):

    count = le.(Selection)

    warning.sV..(str(count)+ ' Nodes Saved')
    
    warning.setVisible T..
    

___ Warning_Load(warning,warningList,index):

    Selection = ?.sN..

    warning.sV..(warningList[index]+"  "+ str(le.(Selection))+ ' Nodes Selected')
    
    warning.setVisible T..


class ChangeVersion(n_s_.PythonPanel):


    ___ __init__(self):
    

        n_s_.PythonPanel.__init__(self,"The Version Changer","The Version Changer")


        # Create Knobs


        self.Read = ?.Boolean_Knob("Read")


        self.Read.sV.. T..


        self.Write = ?.Boolean_Knob("Write")


        self.DeepRead = ?.Boolean_Knob("DeepRead")


        self.DeepWrite = ?.Boolean_Knob("DeepWrite")


        self.dividerA = ?.Text_Knob("")

      
        self.file = ?.Boolean_Knob("file","file   ")


        self.file.sV.. T..


        self.file.setFlag(?.STARTLINE)


        self.proxy = ?.Boolean_Knob("proxy","proxy               ")


        self.Info = ?.Boolean_Knob("Info    ")


        self.Info.sV.. T..
        
        
        self.VersionFolder = ?.Boolean_Knob("Version by Folder")


        self.VersionFolder.sV.. T..
        
        
        self.dividerB = ?.Text_Knob("")
        

        self.Type = ?.Enumeration_Knob("Type","Type",["All","Selected    ","Custom"])


        self.Check = ?.PS_K..('Check', 'Check')


        self.warning = ?.Text_Knob('warning',"")

      
        self.warning.clearFlag(?.STARTLINE)


        self.warning.setVisible F..


        self.SelectString = ?.String_Knob("SelectString", "Select By Value")


        self.SelectString.setEnabled F..


        self.Select = ?.PS_K..('Select', 'Select')


        self.Select.setEnabled T..


        self.Select.setFlag(?.STARTLINE)


        self.Add = ?.PS_K..('Add', 'Add')


        self.Add.setEnabled F..


        self.r__ = ?.PS_K..('Remove', 'Remove')


        self.r__.setEnabled F..


        self.ClearString = ?.PS_K..('ClearString', 'Clear')


        self.ClearString.setEnabled F..


        self.dividerB2 = ?.Text_Knob("")
        

        self.ClearSelect = ?.PS_K..('ClearSelect', 'Clear\n Selection')
        
        
        self.ClearSelect.setFlag(?.STARTLINE)
        
        
        self.SaveSelect = ?.PS_K..('SaveSelect', 'Save\n Selection')

        
        self.LoadSelect = ?.PS_K..('LoadSelect', 'Load\n Selection')


        self.warningD = ?.Text_Knob('warningD',"")

      
        self.warningD.clearFlag(?.STARTLINE)


        self.warningD.setVisible F..


        self.dividerC = ?.Text_Knob("")


        self.SelectManually = ?.Boolean_Knob("Manual Input")


        self.SelectVal = ?.String_Knob("SelectVal", "Select Value")


        self.SelectVal.setEnabled F..


        self.ReplaceVal = ?.String_Knob("ReplaceVal", "Replace With")


        self.ReplaceVal.setEnabled F..


        self.Replace = ?.PS_K..('Replace', 'Replace')


        self.Replace.setFlag(?.STARTLINE)
        
        
        self.Replace.setEnabled F..


        self.Switch = ?.PS_K..('Switch', 'Switch')


        self.Switch.setEnabled F..


        self.Clear = ?.PS_K..('Clear', 'Clear')


        self.Clear.setEnabled T..


        self.Clear.setEnabled F..


        self.warningB = ?.Text_Knob('warning',"")

      
        self.warningB.clearFlag(?.STARTLINE)


        self.warningB.setVisible F..


        self.dividerD = ?.Text_Knob("")


        self.VersionMatch = ?.PS_K..("MatchVersions","Version\n Match ")


        self.VersionMatch.setFlag(?.STARTLINE)


        self.VersionDown = ?.PS_K..('VersionDown','Version\n Down')


        self.VersionUp = ?.PS_K..('VersionUp','Version\n Up')


        self.VersionLast = ?.PS_K..('VersionLast','Version\n Last')


        self.warningC = ?.Text_Knob('warning',"")

      
        self.warningC.clearFlag(?.STARTLINE)


        self.warningC.setVisible F..


        self.dividerE = ?.Text_Knob("")

   
        self.Reset = ?.PS_K..('Reset', 'Reset')


        self.ClearMessage = ?.PS_K..('ClearMessage', 'Clear')


        self.dividerF = ?.Text_Knob("")
        


        # tooltips
        

        self.Read.setTooltip("""
if checked, panel operations will apply to Read Nodes.
        """)


        self.Write.setTooltip("""
if checked, panel operations will apply to Write Nodes.
        """)


        self.DeepRead.setTooltip("""
if checked, panel opertaions will apply to DeepRead Nodes.
        """)

        
        self.DeepWrite.setTooltip("""
if checked, panel operations will apply to DeepWrite Nodes.
        """)


        self.file.setTooltip("""
if checked, panel operations will apply to file knobs.
        """)


        self.proxy.setTooltip("""
if checked, panel operations will apply to proxy knobs.
        """)


        self.Info.setTooltip("""
if checked, information messages about selected and changed nodes will appear.
        """)
        
        
        self.VersionFolder.setTooltip("""
versions are set by values containing a "v" prefix followed by a number. (v001, v002 etc...)
        
if checked, existing versions are determined by the folders in one folder up with the same filename.

example: for fileName_v001/fileName_v006.exr version is 001.

if not checked, existing versions are determined by files in the same folder with the same filename.

example: for fileName_v001/fileName_v006.exr version is 006.
        """)


        self.Type.setTooltip("""
Selection Type:

All - selection will apply to all Nodes, depending on the checked node types ( Read,write, etc... ). 
nodes will be selected only when "Select" Button is pressed.

Selected - operations will apply to selected Nodes. preferably used when node selection is changed via the node graph.

Custom - "Select By Value" option will become available.
nodes will be selected only when "Select" Button is pressed. 
        """)

        self.ClearSelect.setTooltip("""
deselects all nodes
        """)


        self.Check.setTooltip("""
checks the amount of selected nodes and outputs a message.
 
preferably used when node selection is changed via the node graph.
        """)


        self.SelectString.setTooltip("""
selection will apply to nodes containing the value input, depending on checked node types (Read, write etc..) and checked knob types (file and / or proxy ).

nodes will be selected only when "Select" Button is pressed.
        """)


        self.Select.setTooltip("""
selects nodes by defined node selection type. 

If selection type is "custom", only nodes containing value in "Select By Value" will be selected.
        """)


        self.Add.setTooltip("""
adds nodes containing value in "Select By Value" to selection.
        """)


        self.r__.setTooltip("""
removes nodes containing value in "Select By Value" from selection.
        """)


        self.ClearString.setTooltip("""
clears "Select By Value" field.
        """)


        self.SaveSelect.setTooltip("""
saves the current selection
        """)

        self.LoadSelect.setTooltip("""
loads a previosly saved selection.

saved selection is available after panel is closed.

saved selection is not available after script is closed.

        """)


        self.SelectManually.setTooltip("""
if checked, "Select Value" and "Replace With" fields will become available.
        """)


        self.SelectVal.setTooltip("""
value to be replaced with the value in "Replace with" inside a knob, 
depending on checked knob type ( file and / or proxy ).
        """)


        self.ReplaceVal.setTooltip("""
value to replace the selected value in "Select Value" inside a knob,
depending on checked knob type ( file and / or proxy ).
        """)


        self.Replace.setTooltip("""
replaces value in "Select Value" with "Replace With" value inside a knob,
depending on checked knob type ( file and / or proxy ).
        """)


        self.Switch.setTooltip("""
switches between values in "Select Value" field and "Replace With" field.
        """)


        self.Clear.setTooltip("""
clears "Select Value" and "Replace With" fields.
        """)


        self.VersionMatch.setTooltip("""
if 2 different versions set by "v" prefix are found, they will be matched.

If "Versions By Folder" is checked, the file version will be matched to the folder version.

example: fileName_v001/fileName_v006.exr will become fileName_v001/fileName_v001.exr

If "Versions By Folder" is not checked, the folder version will be matched to the file version.

example: fileName_v001/fileName_v006.exr will become fileName_v006/fileName_v006.exr
        """)


        self.VersionDown.setTooltip("""
will go to previous available version, set by "v" prefix.

If "Version by Folder" is checked, existing versions are determined by folders names in one folder up with the same filename.
  
example: for "project_name/shot/3d/renders/filename/filename_element_v001/filename_element_v001.%04d.exr", 

exising versions will be determined by folders names existing in "project_name/shot/3d/renders/filename".

If "Versions By Folder" is not checked, existing versions are determined by files in the same folder up with the same filename.

        """)


        self.VersionUp.setTooltip("""
will go to Next available version, set by "v" prefix.

If "Version by Folder" is checked, existing versions are determined by folders names in one folder up with the same filename.
  
example: for "project_name/shot/3d/renders/filename/filename_element_v001/filename_element_v001.%04d.exr", 

exising versions will be determined by folders names existing in "project_name/shot/3d/renders/filename".

If "Versions By Folder" is not checked, existing versions are determined by files in the same folder up with the same filename.

        """)


        self.VersionLast.setTooltip("""
will go to Last available version, set by "v" prefix.

If "Version by Folder" is checked, existing versions are determined by folders names in one folder up with the same filename.
  
example: for "project_name/shot/3d/renders/filename/filename_element_v001/filename_element_v001.%04d.exr", 

exising versions will be determined by folders names existing in "project_name/shot/3d/renders/filename".

If "Versions By Folder" is not checked, existing versions are determined by files in the same folder up with the same filename.

        """)


        self.Reset.setTooltip("""
resets panel
        """)


        self.ClearMessage.setTooltip("""
clears all messages
        """)



        # add Knobs


        self.aK..(self.Read)

    
        self.aK..(self.Write)


        self.aK..(self.DeepRead)

 
        self.aK..(self.DeepWrite)


        self.aK..(self.dividerA)


        self.aK..(self.file)


        self.aK..(self.proxy)


        self.aK..(self.Info)
        
        
        self.aK..(self.VersionFolder)


        self.aK..(self.dividerB)
    

        self.aK..(self.Type)


        self.aK..(self.Check)


        self.aK..(self.warning)


        self.aK..(self.SelectString)


        self.aK..(self.Select)


        self.aK..(self.Add)


        self.aK..(self.r__)


        self.aK..(self.ClearString)
        
        
        self.aK..(self.dividerB2)
        
        
        self.aK..(self.ClearSelect)
        
        
        self.aK..(self.SaveSelect)
        
        
        self.aK..(self.LoadSelect)


        self.aK..(self.warningD)


        self.aK..(self.dividerC)


        self.aK..(self.SelectManually)


        self.aK..(self.SelectVal)


        self.aK..(self.ReplaceVal)


        self.aK..(self.Replace)


        self.aK..(self.Switch)


        self.aK..(self.Clear)


        self.aK..(self.warningB)


        self.aK..(self.dividerD)


        self.aK..(self.VersionMatch)


        self.aK..(self.VersionDown)


        self.aK..(self.VersionUp)


        self.aK..(self.VersionLast)


        self.aK..(self.warningC)


        self.aK..(self.dividerE)


        self.aK..(self.Reset)


        self.aK..(self.ClearMessage)



        # Define node Lists variables


        self.NodeTypes = [self.Read, self.Write, self.DeepRead, self.DeepWrite]


        self.SelectedNodeTypes = ["Read"]


        self.KnobTypes = [self.file, self.proxy]

    
        self.SelectedKnobTypes = ["file"]
        
        
        self.OldSelect = []


        self.WarningList = ["No Nodes Selected","No Selection Saved","Script changed"]



    ___ knobChanged(self,knob):
    

        #Selects knob type


        __ knob __ self.KnobTypes:


            self.SelectedKnobTypes = []


            self.SelectedKnobTypes = [ k.n..  ___ k __ self.KnobTypes __ k.gV.. ]



        #Selects node types


        __ knob __ self.NodeTypes:


            self.SelectedNodeTypes = []


            self.SelectedNodeTypes = [ node.n..  ___ node __ self.NodeTypes __ node.gV.. ]
            
            
            
        #Show Info    
        
            
        __ knob __ self.Info:


            __ self.Info.gV.. :
            
            
                self.Check.setEnabled T..


                self.ClearMessage.setEnabled T..


            ____
            
            
                self.Check.setEnabled F..
                

                self.ClearMessage.setEnabled F..


                self.warning.setVisible F..


                self.warningB.setVisible F..


                self.warningC.setVisible F..


                self.warningD.setVisible F..
                

        #Check Selection    
        

        __ knob __ self.Check:


            __ self.Info.gV.. :


                Warning (self.warning)
                                

       
        #Selects all nodes


        __ self.Type.v.. ()__"All":
        
        
            self.SelectString.setEnabled F..
        
        
            self.Select.setEnabled T..


            self.Add.setEnabled F..


            self.r__.setEnabled F..


            self.ClearString.setEnabled F..


            __ knob __ self.Select:


                ___ n __ ?.aN..


                    n.sS.. F..


                    __ n.C..  __ self.SelectedNodeTypes:


                        n.sS.. T..


                __ self.Info.gV.. :


                    Warning (self.warning)



        #Selected Nodes


        __ self.Type.v.. ()__"Selected    ":
        
        
           self.SelectString.setEnabled F..


           self.Select.setEnabled F..


           self.Add.setEnabled F..


           self.r__.setEnabled F..


           self.ClearString.setEnabled F..



        #Selects by custom value


        __ self.Type.v.. ()__"Custom":
        
        
            self.Select.setEnabled T..


            self.SelectString.setEnabled T..


            self.Add.setEnabled T..


            self.r__.setEnabled T..


            self.ClearString.setEnabled T..


            __ knob __ self.Select:


                self.Custom=self.SelectString.v.. ()


                ___ n __ ?.aN..


                    n.sS.. F..
                    
                    
                    __ n.C..  __ self.SelectedNodeTypes:

                
                        ___ knob __ self.SelectedKnobTypes:


                            __ self.Custom __ n[knob].v.. () and self.Custom !="":


                                n.sS.. T..


                __ self.Info.gV.. :


                    Warning (self.warning)


            __ knob __ self.ClearString:


                self.SelectString.sV..("")


                __ self.Info.gV.. :


                    Warning (self.warning)
                    
                    

        # Adds to Selection


            __ knob __ self.Add:


                self.Custom=self.SelectString.v.. ()


                ___ n __ ?.aN..

    
                    __ n.C..  __ self.SelectedNodeTypes:

                
                        ___ knob __ self.SelectedKnobTypes:


                            __ self.Custom __ n[knob].v.. () and self.Custom !="":


                                n.sS.. T..


                __ self.Info.gV.. :


                    Warning (self.warning)
 


        #Removes from Selection


            __ knob __ self.r__:


                self.Custom = self.SelectString.v.. ()


                ___ n __ ?.sN.. :


                    __ n.C..  __ self.SelectedNodeTypes:

                
                        ___ knob __ self.SelectedKnobTypes:


                            __ self.Custom __ n[knob].v.. () and self.Custom !="":


                                n.sS.. F..


                __ self.Info.gV.. :


                    Warning (self.warning)

      

        #Clears selection


        __ knob __ self.ClearSelect:


            ___ n __ ?.aN..


                    n.sS.. F..


            __ self.Info.gV.. :


                Warning (self.warning)
                
                
        # Save Selection
        
        __ knob __ self.SaveSelect:
        
            self.OldSelect = ?.sN..

            __ no. self.OldSelect:

                Warning_SaveLoad(self.warningD,self.WarningList,0)

            ____

                OldSelect(self.OldSelect)

                Warning_Save(self.warningD,self.OldSelect)

                        
        # Load Selection
           
        __ knob __ self.LoadSelect:

            __ no. OldSelect1:

                Warning_SaveLoad(self.warningD,self.WarningList,1)

            ____

                checkMissing = False

                check = False
                
                ___ i __ OldSelect1:

                    __ i no. __ ?.aN..

                        checkMissing = T..
                        
                    __ i __ ?.aN..

                        check = T..
        
                __ check and no. checkMissing:

                    ___ n __ ?.aN..
    
                        n.sS.. F..

                    ___ i __ OldSelect1:
    
                        i.sS.. T..

                    Warning(self.warningD)

                ____
                    
                    ___ n __ ?.aN..
    
                        n.sS.. F..

                    ___

                        ___ i __ OldSelect1:
    
                            i.sS.. T..

                    ______

                        pass

                    Warning_Load(self.warningD,self.WarningList,2)
               
            

        #Enables/Disables Manual Input


        __ self.SelectManually.v.. ()__True:
        
        
            self.SelectVal.setEnabled T..


            self.ReplaceVal.setEnabled T..


            self.Replace.setEnabled T..


            self.Switch.setEnabled T..


            self.Clear.setEnabled T..
            
            
            self.VersionMatch.setEnabled F..


            self.VersionUp.setEnabled F..


            self.VersionDown.setEnabled F..


            self.VersionLast.setEnabled F..
            


        ____
        
        
            self.SelectVal.setEnabled F..


            self.ReplaceVal.setEnabled F..


            self.Replace.setEnabled F..

       
            self.Switch.setEnabled F..


            self.Clear.setEnabled F..
            
            
            self.VersionMatch.setEnabled T..


            self.VersionUp.setEnabled T..


            self.VersionDown.setEnabled T..


            self.VersionLast.setEnabled T..
            


        #Replaces String


        __ knob __ self.Replace:
        

            count = 0
         

            ___ n __ ?.sN.. :
            
            
                __ n.C..  __ self.SelectedNodeTypes:


                    ___ knob __ self.SelectedKnobTypes:

                      
                        old = n[knob].v.. ()


                        NewStr=re.sub(self.SelectVal.v.. (),self.ReplaceVal.v.. (),n[knob].v.. ())


                        n[knob].sV..(NewStr)


                        new = n[knob].v.. ()


                        __ old != new:


                           count+=1


            __ self.Info.gV.. :


                Warning_changed(self.warningB,count) 



        #Switches between inputs


        __ knob __ self.Switch:

            temp = self.SelectVal.v.. ()
   
            self.SelectVal.sV..(self.ReplaceVal.v.. ())

            self.ReplaceVal.sV..(temp)



        #Clears String Field


        __ knob __ self.Clear:


            self.SelectVal.sV..("")


            self.ReplaceVal.sV..("")



        #Changes Versions    
        
        #Version Match


        __ knob __ self.VersionMatch:

            ___

                __ self.Info.gV.. :

                    __ self.VersionFolder.gV.. :

                        Warning_changed(self.warningC,VersionMatchFolder(self.SelectedKnobTypes,self.SelectedNodeTypes))
                            
                    ____
                        
                        Warning_changed(self.warningC,VersionMatchFiles(self.SelectedKnobTypes,self.SelectedNodeTypes))

                elif self.VersionFolder.gV.. :

                    VersionMatchFolder(self.SelectedKnobTypes,self.SelectedNodeTypes)
                        
                ____
                    
                    VersionMatchFiles(self.SelectedKnobTypes,self.SelectedNodeTypes)

            ______

                pass
                   
                   
        #Version Up
        

        __ knob __ self.VersionUp:

            ___
                    
                __ self.Info.gV.. :

                    __ self.VersionFolder.gV.. :

                        Warning_changed(self.warningC,VersionUp(self.SelectedKnobTypes,self.SelectedNodeTypes))
                            
                    ____
                        
                        Warning_changed(self.warningC,VersionUpFiles(self.SelectedKnobTypes,self.SelectedNodeTypes))

                elif self.VersionFolder.gV.. :

                    VersionUp(self.SelectedKnobTypes,self.SelectedNodeTypes)
                        
                ____
                    
                    VersionUpFiles(self.SelectedKnobTypes,self.SelectedNodeTypes)

            ______

                pass
                   

        #Version Down    
        

        __ knob __ self.VersionDown:

            ___

                __ self.Info.gV.. :

                    __ self.VersionFolder.gV.. :

                        Warning_changed(self.warningC,VersionDown(self.SelectedKnobTypes,self.SelectedNodeTypes))
                        
                    ____
                        
                        Warning_changed(self.warningC,VersionDownFiles(self.SelectedKnobTypes,self.SelectedNodeTypes))

                elif self.VersionFolder.gV.. :

                    VersionDown(self.SelectedKnobTypes,self.SelectedNodeTypes)
                        
                ____
                    
                    VersionDownFiles(self.SelectedKnobTypes,self.SelectedNodeTypes)

            ______

                pass
                    
                    
        #Version Last
        

        __ knob __ self.VersionLast:

            ___

                __ self.Info.gV.. :

                    __ self.VersionFolder.gV.. :

                        Warning_changed(self.warningC,VersionLast(self.SelectedKnobTypes,self.SelectedNodeTypes))
                            
                    ____
                        
                        Warning_changed(self.warningC,VersionLastFiles(self.SelectedKnobTypes,self.SelectedNodeTypes))

                elif self.VersionFolder.gV.. :

                    VersionLast(self.SelectedKnobTypes,self.SelectedNodeTypes)
                        
                ____
                    
                    VersionLastFiles(self.SelectedKnobTypes,self.SelectedNodeTypes)

            ______

                pass


        # Resets


        __ knob __ self.Reset:


            self.SelectedNodeTypes = ["Read"]


            self.SelectedKnobTypes = ["file"]


            self.Read.sV.. T..


            self.Write.sV.. F..


            self.DeepRead.sV.. F..


            self.DeepWrite.sV.. F..


            self.file.sV.. T..


            self.proxy.sV.. F..
            
            
            self.Info.sV.. T..


            self.VersionFolder.sV.. T..


            self.Type.sV..("All")


            self.SelectString.sV..("")


            self.SelectString.setEnabled F..


            self.Add.setEnabled F..


            self.r__.setEnabled F..


            self.ClearString.setEnabled F..


            self.SelectManually.sV.. F..


            self.SelectVal.setEnabled F..


            self.SelectVal.sV..("")


            self.ReplaceVal.sV..("")


            self.ReplaceVal.setEnabled F..
            
            
            self.Replace.setEnabled F..


            self.Switch.setEnabled F..


            self.Clear.setEnabled F..
            
            
            self.VersionMatch.setEnabled T..


            self.VersionUp.setEnabled T..


            self.VersionDown.setEnabled T..


            self.VersionLast.setEnabled T..


            self.warning.setVisible F..


            self.warningB.setVisible F..


            self.warningC.setVisible F..
            

            self.warningD.setVisible F..


            self.ClearMessage.setEnabled T..
            


        #Clears Messages            

        
        __ knob __ self.ClearMessage:


            self.warning.setVisible F..


            self.warningB.setVisible F..


            self.warningC.setVisible F..
            

            self.warningD.setVisible F..
            


___ addPanel

    pane = ?.getPaneFor('Viewer.1')

    r_ ChangeVersion().addToPane(pane)


m__ = ?.m__("Pane")

m__.aC..("The Version Changer",addPanel,"Alt+v")

n_s_.registerPanel("The Version Changer",addPanel)

#ChangeVersion().showModalDialog()0
