import re, __.path, nuke, nukescripts


Selection = nuke.selectedNodes()

OldSelect1 = []

   
def SplitDir(fileknob):


    FileName = __.path.basename(fileknob)

         
    Dir = __.path.dirname(fileknob)
                    
                    
    DirUp = __.path.s..(Dir)
                    
                    
    Joined = __.path.n_p_ (__.path.join(DirUp[1],FileName))
                    
                    
    Joined = re.sub(r'\\', r'/' ,Joined)
    
    
    return Joined
    
    
        
def SplitDirUp(fileknob):


    FileName = __.path.basename(fileknob)
    
         
    Dir = __.path.dirname(fileknob)
    
                    
    DirUp = __.path.s..(Dir)[0]
    
    
    return DirUp
    
    

def FindVersion(fileknob):


    pattern = "v" + "\d+"


    MyList = re.findall(pattern,fileknob,re.IGNORECASE)


    if MyList:
  

        version = MyList[0][:1]


        versionNumber = MyList[0][1:]


        return versionNumber



def ListVersions(fileknob):


    FileName = __.path.basename(fileknob)


    FileBase = FileName.s..(FindVersion(SplitDir(fileknob)))[0]

 
    Dir = __.path.dirname(fileknob)


    DirUp = __.path.s..(Dir)[0]


    Names = [name for name in __.listdir(DirUp) if FileBase in name]


    OnlyFolders = []


    for i in Names:


        Joined = __.path.n_p_ (__.path.join(DirUp,i))


        check = __.path.isdir(Joined)


        version = FindVersion(i)


        if check:


            if version not in OnlyFolders:


                OnlyFolders.append(version)


    return sorted(OnlyFolders)

    
    
def ListVersionsFiles(fileknob):


    FileName = __.path.basename(fileknob)


    FileBase = FileName.s..(FindVersion(FileName))[0]

 
    Dir = __.path.dirname(fileknob)


    Names = [name for name in __.listdir(Dir) if FileBase in name]


    OnlyFiles = []


    for i in Names:


        Joined = __.path.n_p_ (__.path.join(Dir,i))


        check = __.path.isfile(Joined)


        version = FindVersion(i)


        if check:


            if version not in OnlyFiles:


                OnlyFiles.append(version)


    return sorted(OnlyFiles)



def VersionUp(KnobTypes,NodeTypes):

    count = 0

    for node in nuke.selectedNodes():
    
        if node.Class() in NodeTypes:
        
            for n in KnobTypes:

                try:

                    fileknob = node[n].value()
                    

                    FileName = __.path.basename(fileknob)
                    

                    version = FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile = FindVersion(FileName)


                    if version != versionFile:


                        print "Error: different versions found in " + node.n..  + " " + n

                     
                    if version:

                
                        Next = int(version)+1

                  
                        string_Next = "%03d" % Next

                  
                        if version < max(ListVersions(fileknob)):

                 
                            while string_Next not in ListVersions(fileknob):
                   
                   
                                Next+=1
                   
                   
                                string_Next = "%03d" % Next
          
                
                            old = node[n].value()
                   
                   
                            NewStr=re.sub("v"+version,"v"+string_Next,SplitDir(fileknob))

                            
                            Joined = __.path.n_p_ (__.path.join(SplitDirUp(fileknob),NewStr))
                    
                    
                            Joined = re.sub(r'\\', r'/' ,Joined)
                   
                   
                            node[n].setValue(Joined)


                            new = node[n].value()


                            if old != new:


                                count+=1

                    else:

                        print "Error: No versions found in " + node.n..  + " " + n

                except :

                    pass


    return count
    
       
       
def VersionUpFiles(KnobTypes,NodeTypes):

    count = 0

    for node in nuke.selectedNodes():
    
        if node.Class() in NodeTypes:
        
            for n in KnobTypes:

                try:

                    fileknob = node[n].value()
                    
                    FileName = __.path.basename(fileknob)
         
                    Dir = __.path.dirname(fileknob)
                   
                    version = FindVersion(FileName)
                     
                    if version:
                
                        Next = int(version)+1
                  
                        string_Next = "%03d" % Next
                  
                        if version < max(ListVersionsFiles(fileknob)):
                 
                            while string_Next not in ListVersionsFiles(fileknob):
                   
                   
                                Next+=1
                   
                   
                                string_Next = "%03d" % Next
          
                
                            old = node[n].value()      
                            
                   
                            FileName=re.sub("v"+version,"v"+string_Next,FileName) 
                            

                            Joined = __.path.n_p_ (__.path.join(Dir,FileName))
                            
                            
                            Joined = re.sub(r'\\', r'/' ,Joined)
                            
                   
                            node[n].setValue(Joined)

                            
                            new = node[n].value()


                            if old != new:


                                count+=1

                    else:

                        print "Error: No versions found in " + node.n..  + " " + n

                except:

                     pass


    return count
    
       
def VersionDown(KnobTypes,NodeTypes):

    count = 0

    for node in nuke.selectedNodes():

        if node.Class() in NodeTypes:
        
            for n in KnobTypes:
    
                try:

                    fileknob = node[n].value()    


                    FileName = __.path.basename(fileknob)
                    

                    version = FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile = FindVersion(FileName)


                    if version != versionFile:


                        print "Error: different versions found in " + node.n..  + " " + n


                    if version:


                        Previous = int(version)-1

          
                        string_Previous = "%03d" % Previous


                        if version > min(ListVersions(fileknob)):


                            while string_Previous not in ListVersions(fileknob):


                                Previous-=1


                                string_Previous = "%03d" % Previous


                            old = node[n].value()
                   
                   
                            NewStr=re.sub("v"+version,"v"+string_Previous,SplitDir(fileknob))

                            
                            Joined = __.path.n_p_ (__.path.join(SplitDirUp(fileknob),NewStr))
                    
                    
                            Joined = re.sub(r'\\', r'/' ,Joined)
                   
                   
                            node[n].setValue(Joined)


                            new = node[n].value()


                            if old != new:


                                count+=1

                    else:

                        print "Error: No versions found in " + node.n..  + " " + n


                except:

                    pass


    return count
    

def VersionDownFiles(KnobTypes,NodeTypes):

    count = 0

    for node in nuke.selectedNodes():
    
        if node.Class() in NodeTypes:
        
            for n in KnobTypes:
        
                try:


                    fileknob = node[n].value()

                    
                    FileName = __.path.basename(fileknob)

         
                    Dir = __.path.dirname(fileknob)

                   
                    version = FindVersion(FileName)


                    if version:


                        Previous = int(version)-1

          
                        string_Previous = "%03d" % Previous


                        if version > min(ListVersionsFiles(fileknob)):


                            while string_Previous not in ListVersionsFiles(fileknob):


                                Previous-=1


                                string_Previous = "%03d" % Previous


                            old = node[n].value()

          
                            FileName=re.sub("v"+version,"v"+string_Previous,FileName) 
                            

                            Joined = __.path.n_p_ (__.path.join(Dir,FileName))
                            
                            
                            Joined = re.sub(r'\\', r'/' ,Joined)
                            
                   
                            node[n].setValue(Joined)


                            new = node[n].value()


                            if old != new:


                                count+=1

                    else:

                        print "Error: No versions found in " + node.n..  + " " + n


                except:

                    pass


    return count
    

def VersionLast(KnobTypes,NodeTypes):

    count = 0

    for node in nuke.selectedNodes():
    
        for n in KnobTypes:

            if node.Class() in NodeTypes:
            
                try:

                    fileknob = node[n].value()  


                    FileName = __.path.basename(fileknob)
                    

                    version = FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile = FindVersion(FileName)


                    if version != versionFile:


                        print "Error: different versions found in " + node.n..  + " " + n


                    if version:

           
                        Last = max(ListVersions(fileknob))


                        old = node[n].value()
                   
                   
                        NewStr=re.sub("v"+version,"v"+Last,SplitDir(fileknob))

                            
                        Joined = __.path.n_p_ (__.path.join(SplitDirUp(fileknob),NewStr))
                    
                    
                        Joined = re.sub(r'\\', r'/' ,Joined)
                   
                   
                        node[n].setValue(Joined)


                        new = node[n].value()


                        if old != new:


                            count+=1

                    else:

                        print "Error: No versions found in " + node.n..  + " " + n


                except:

                    pass


    return count
    
   
def VersionLastFiles(KnobTypes,NodeTypes):

    count = 0

    for node in nuke.selectedNodes():
    
        if node.Class() in NodeTypes:
        
            for n in KnobTypes:

                try:


                    fileknob = node[n].value()

                    
                    FileName = __.path.basename(fileknob)

         
                    Dir = __.path.dirname(fileknob)

                   
                    version = FindVersion(FileName)


                    if version:

           
                        Last = max(ListVersionsFiles(fileknob))


                        old = node[n].value()


                        FileName=re.sub("v"+version,"v"+Last,FileName) 
                            

                        Joined = __.path.n_p_ (__.path.join(Dir,FileName))
                        
                        
                        Joined = re.sub(r'\\', r'/' ,Joined)
                            
                   
                        node[n].setValue(Joined)


                        new = node[n].value()


                        if old != new:


                            count+=1

                    else:

                        print "Error: No versions found in " + node.n..  + " " + n


                except:

                    pass


    return count


def VersionMatchFolder(KnobTypes,NodeTypes):

    count = 0

    for node in nuke.selectedNodes():
    
        if node.Class() in NodeTypes:
        
            for n in KnobTypes:

                try:

                    fileknob = node[n].value()    


                    FileName = __.path.basename(fileknob)


                    Dir = __.path.dirname(fileknob)
                    
                    
                    DirLast = __.path.s..(Dir)[1]
                    

                    version = FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile = FindVersion(FileName)


                    if version:


                        if version != versionFile:


                            old = node[n].value()


                            FileName = re.sub("v"+versionFile,"v"+version,FileName)

                            
                            Joined = __.path.n_p_ (__.path.join(SplitDirUp(fileknob),DirLast,FileName))
                    
                    
                            Joined = re.sub(r'\\', r'/' ,Joined)

                        
                            node[n].setValue(Joined)


                            new = node[n].value()


                            if old != new:


                                count+=1

                    else:

                        print "Error: No versions found in " + node.n..  + " " + n


                except:

                    pass


    return count


def VersionMatchFiles(KnobTypes,NodeTypes):

    count = 0

    for node in nuke.selectedNodes():
    
        if node.Class() in NodeTypes:
        
            for n in KnobTypes:

                try:
         
                    fileknob = node[n].value() 
                    

                    Dir = __.path.dirname(fileknob)
                    
                    
                    DirLast = __.path.s..(Dir)[1]


                    FileName = __.path.basename(fileknob)
                    

                    version = FindVersion(SplitDir(fileknob))
                    
                    
                    versionFile = FindVersion(FileName)


                    if version != versionFile:


                        old = node[n].value()


                        DirLast = re.sub("v"+version,"v"+versionFile, DirLast)
                        
                        
                        Joined = __.path.n_p_ (__.path.join(SplitDirUp(fileknob),DirLast,FileName))
                    
                    
                        Joined = re.sub(r'\\', r'/' ,Joined)

                        
                        node[n].setValue(Joined)


                        new = node[n].value()


                        if old != new:


                            count+=1


                except:

                    pass


    return count

    
def OldSelect(SavedSelection):

    global OldSelect1

    OldSelect1 = []

    for n in SavedSelection:

        OldSelect1.append(n)
    
    return OldSelect1


def Warning(warning):

    Selection = nuke.selectedNodes()
    
    warning.setValue(str(len(Selection))+ ' Nodes Selected')
    
    warning.setVisible(True)


def Warning_changed(warning,count): 

    warning.setValue(str(count)+ ' Nodes Changed')
    
    warning.setVisible(True)
    

def Warning_SaveLoad(warning,warningList,index):

    warning.setValue(warningList[index])
    
    warning.setVisible(True)
    

def Warning_Save(warning,Selection):

    count = len(Selection)

    warning.setValue(str(count)+ ' Nodes Saved')
    
    warning.setVisible(True)
    

def Warning_Load(warning,warningList,index):

    Selection = nuke.selectedNodes()

    warning.setValue(warningList[index]+"  "+ str(len(Selection))+ ' Nodes Selected')
    
    warning.setVisible(True)


class ChangeVersion(nukescripts.PythonPanel):


    def __init__(self):
    

        nukescripts.PythonPanel.__init__(self,"The Version Changer","The Version Changer")


        # Create Knobs


        self.Read = nuke.Boolean_Knob("Read")


        self.Read.setValue(True)


        self.Write = nuke.Boolean_Knob("Write")


        self.DeepRead = nuke.Boolean_Knob("DeepRead")


        self.DeepWrite = nuke.Boolean_Knob("DeepWrite")


        self.dividerA = nuke.Text_Knob("")

      
        self.file = nuke.Boolean_Knob("file","file   ")


        self.file.setValue(True)


        self.file.setFlag(nuke.STARTLINE)


        self.proxy = nuke.Boolean_Knob("proxy","proxy               ")


        self.Info = nuke.Boolean_Knob("Info    ")


        self.Info.setValue(True)
        
        
        self.VersionFolder = nuke.Boolean_Knob("Version by Folder")


        self.VersionFolder.setValue(True)
        
        
        self.dividerB = nuke.Text_Knob("")
        

        self.Type = nuke.Enumeration_Knob("Type","Type",["All","Selected    ","Custom"])


        self.Check = nuke.PyScript_Knob('Check', 'Check')


        self.warning = nuke.Text_Knob('warning',"")

      
        self.warning.clearFlag(nuke.STARTLINE)


        self.warning.setVisible(False)


        self.SelectString = nuke.String_Knob("SelectString", "Select By Value")


        self.SelectString.setEnabled(False)


        self.Select = nuke.PyScript_Knob('Select', 'Select')


        self.Select.setEnabled(True)


        self.Select.setFlag(nuke.STARTLINE)


        self.Add = nuke.PyScript_Knob('Add', 'Add')


        self.Add.setEnabled(False)


        self.Remove = nuke.PyScript_Knob('Remove', 'Remove')


        self.Remove.setEnabled(False)


        self.ClearString = nuke.PyScript_Knob('ClearString', 'Clear')


        self.ClearString.setEnabled(False)


        self.dividerB2 = nuke.Text_Knob("")
        

        self.ClearSelect = nuke.PyScript_Knob('ClearSelect', 'Clear\n Selection')
        
        
        self.ClearSelect.setFlag(nuke.STARTLINE)
        
        
        self.SaveSelect = nuke.PyScript_Knob('SaveSelect', 'Save\n Selection')

        
        self.LoadSelect = nuke.PyScript_Knob('LoadSelect', 'Load\n Selection')


        self.warningD = nuke.Text_Knob('warningD',"")

      
        self.warningD.clearFlag(nuke.STARTLINE)


        self.warningD.setVisible(False)


        self.dividerC = nuke.Text_Knob("")


        self.SelectManually = nuke.Boolean_Knob("Manual Input")


        self.SelectVal = nuke.String_Knob("SelectVal", "Select Value")


        self.SelectVal.setEnabled(False)


        self.ReplaceVal = nuke.String_Knob("ReplaceVal", "Replace With")


        self.ReplaceVal.setEnabled(False)


        self.Replace = nuke.PyScript_Knob('Replace', 'Replace')


        self.Replace.setFlag(nuke.STARTLINE)
        
        
        self.Replace.setEnabled(False)


        self.Switch = nuke.PyScript_Knob('Switch', 'Switch')


        self.Switch.setEnabled(False)


        self.Clear = nuke.PyScript_Knob('Clear', 'Clear')


        self.Clear.setEnabled(True)


        self.Clear.setEnabled(False)


        self.warningB = nuke.Text_Knob('warning',"")

      
        self.warningB.clearFlag(nuke.STARTLINE)


        self.warningB.setVisible(False)


        self.dividerD = nuke.Text_Knob("")


        self.VersionMatch = nuke.PyScript_Knob("MatchVersions","Version\n Match ")


        self.VersionMatch.setFlag(nuke.STARTLINE)


        self.VersionDown = nuke.PyScript_Knob('VersionDown','Version\n Down')


        self.VersionUp = nuke.PyScript_Knob('VersionUp','Version\n Up')


        self.VersionLast = nuke.PyScript_Knob('VersionLast','Version\n Last')


        self.warningC = nuke.Text_Knob('warning',"")

      
        self.warningC.clearFlag(nuke.STARTLINE)


        self.warningC.setVisible(False)


        self.dividerE = nuke.Text_Knob("")

   
        self.Reset = nuke.PyScript_Knob('Reset', 'Reset')


        self.ClearMessage = nuke.PyScript_Knob('ClearMessage', 'Clear')


        self.dividerF = nuke.Text_Knob("")
        


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


        self.Remove.setTooltip("""
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


        self.addKnob(self.Read)

    
        self.addKnob(self.Write)


        self.addKnob(self.DeepRead)

 
        self.addKnob(self.DeepWrite)


        self.addKnob(self.dividerA)


        self.addKnob(self.file)


        self.addKnob(self.proxy)


        self.addKnob(self.Info)
        
        
        self.addKnob(self.VersionFolder)


        self.addKnob(self.dividerB)
    

        self.addKnob(self.Type)


        self.addKnob(self.Check)


        self.addKnob(self.warning)


        self.addKnob(self.SelectString)


        self.addKnob(self.Select)


        self.addKnob(self.Add)


        self.addKnob(self.Remove)


        self.addKnob(self.ClearString)
        
        
        self.addKnob(self.dividerB2)
        
        
        self.addKnob(self.ClearSelect)
        
        
        self.addKnob(self.SaveSelect)
        
        
        self.addKnob(self.LoadSelect)


        self.addKnob(self.warningD)


        self.addKnob(self.dividerC)


        self.addKnob(self.SelectManually)


        self.addKnob(self.SelectVal)


        self.addKnob(self.ReplaceVal)


        self.addKnob(self.Replace)


        self.addKnob(self.Switch)


        self.addKnob(self.Clear)


        self.addKnob(self.warningB)


        self.addKnob(self.dividerD)


        self.addKnob(self.VersionMatch)


        self.addKnob(self.VersionDown)


        self.addKnob(self.VersionUp)


        self.addKnob(self.VersionLast)


        self.addKnob(self.warningC)


        self.addKnob(self.dividerE)


        self.addKnob(self.Reset)


        self.addKnob(self.ClearMessage)



        # Define node Lists variables


        self.NodeTypes = [self.Read, self.Write, self.DeepRead, self.DeepWrite]


        self.SelectedNodeTypes = ["Read"]


        self.KnobTypes = [self.file, self.proxy]

    
        self.SelectedKnobTypes = ["file"]
        
        
        self.OldSelect = []


        self.WarningList = ["No Nodes Selected","No Selection Saved","Script changed"]



    def knobChanged(self,knob):
    

        #Selects knob type


        if knob in self.KnobTypes:


            self.SelectedKnobTypes = []


            self.SelectedKnobTypes = [ k.n..  for k in self.KnobTypes if k.getValue()]



        #Selects node types


        if knob in self.NodeTypes:


            self.SelectedNodeTypes = []


            self.SelectedNodeTypes = [ node.n..  for node in self.NodeTypes if node.getValue()]
            
            
            
        #Show Info    
        
            
        if knob is self.Info:


            if self.Info.getValue():
            
            
                self.Check.setEnabled(True)


                self.ClearMessage.setEnabled(True)


            else:  
            
            
                self.Check.setEnabled(False)
                

                self.ClearMessage.setEnabled(False)


                self.warning.setVisible(False)


                self.warningB.setVisible(False)


                self.warningC.setVisible(False)


                self.warningD.setVisible(False)
                

        #Check Selection    
        

        if knob is self.Check:


            if self.Info.getValue():


                Warning (self.warning)
                                

       
        #Selects all nodes


        if self.Type.value()=="All":
        
        
            self.SelectString.setEnabled(False)
        
        
            self.Select.setEnabled(True)


            self.Add.setEnabled(False)


            self.Remove.setEnabled(False)


            self.ClearString.setEnabled(False)


            if knob is self.Select:


                for n in nuke.allNodes():


                    n.setSelected(False)


                    if n.Class() in self.SelectedNodeTypes:


                        n.setSelected(True)


                if self.Info.getValue():


                    Warning (self.warning)



        #Selected Nodes


        if self.Type.value()=="Selected    ":
        
        
           self.SelectString.setEnabled(False)


           self.Select.setEnabled(False)


           self.Add.setEnabled(False)


           self.Remove.setEnabled(False)


           self.ClearString.setEnabled(False)



        #Selects by custom value


        if self.Type.value()=="Custom":
        
        
            self.Select.setEnabled(True)


            self.SelectString.setEnabled(True)


            self.Add.setEnabled(True)


            self.Remove.setEnabled(True)


            self.ClearString.setEnabled(True)


            if knob is self.Select:


                self.Custom=self.SelectString.value()


                for n in nuke.allNodes():


                    n.setSelected(False)
                    
                    
                    if n.Class() in self.SelectedNodeTypes:

                
                        for knob in self.SelectedKnobTypes:


                            if self.Custom in n[knob].value() and self.Custom !="":


                                n.setSelected(True)


                if self.Info.getValue():


                    Warning (self.warning)


            if knob is self.ClearString:


                self.SelectString.setValue("")


                if self.Info.getValue():


                    Warning (self.warning)
                    
                    

        # Adds to Selection


            if knob is self.Add:


                self.Custom=self.SelectString.value()


                for n in nuke.allNodes():

    
                    if n.Class() in self.SelectedNodeTypes:

                
                        for knob in self.SelectedKnobTypes:


                            if self.Custom in n[knob].value() and self.Custom !="":


                                n.setSelected(True)


                if self.Info.getValue():


                    Warning (self.warning)
 


        #Removes from Selection


            if knob is self.Remove:


                self.Custom = self.SelectString.value()


                for n in nuke.selectedNodes():


                    if n.Class() in self.SelectedNodeTypes:

                
                        for knob in self.SelectedKnobTypes:


                            if self.Custom in n[knob].value() and self.Custom !="":


                                n.setSelected(False)


                if self.Info.getValue():


                    Warning (self.warning)

      

        #Clears selection


        if knob is self.ClearSelect:


            for n in nuke.allNodes():


                    n.setSelected(False)


            if self.Info.getValue():


                Warning (self.warning)
                
                
        # Save Selection
        
        if knob is self.SaveSelect:
        
            self.OldSelect = nuke.selectedNodes()

            if not self.OldSelect:

                Warning_SaveLoad(self.warningD,self.WarningList,0)

            else:

                OldSelect(self.OldSelect)

                Warning_Save(self.warningD,self.OldSelect)

                        
        # Load Selection
           
        if knob is self.LoadSelect:

            if not OldSelect1:

                Warning_SaveLoad(self.warningD,self.WarningList,1)

            else:

                checkMissing = False

                check = False
                
                for i in OldSelect1:

                    if i not in nuke.allNodes():

                        checkMissing = True
                        
                    if i in nuke.allNodes():

                        check = True
        
                if check and not checkMissing:

                    for n in nuke.allNodes():
    
                        n.setSelected(False)

                    for i in OldSelect1:
    
                        i.setSelected(True)

                    Warning(self.warningD)

                else:
                    
                    for n in nuke.allNodes():
    
                        n.setSelected(False)

                    try:

                        for i in OldSelect1:
    
                            i.setSelected(True)

                    except:

                        pass

                    Warning_Load(self.warningD,self.WarningList,2)
               
            

        #Enables/Disables Manual Input


        if self.SelectManually.value()==True:
        
        
            self.SelectVal.setEnabled(True)


            self.ReplaceVal.setEnabled(True)


            self.Replace.setEnabled(True)


            self.Switch.setEnabled(True)


            self.Clear.setEnabled(True)
            
            
            self.VersionMatch.setEnabled(False)


            self.VersionUp.setEnabled(False)


            self.VersionDown.setEnabled(False)


            self.VersionLast.setEnabled(False)
            


        else:
        
        
            self.SelectVal.setEnabled(False)


            self.ReplaceVal.setEnabled(False)


            self.Replace.setEnabled(False)

       
            self.Switch.setEnabled(False)


            self.Clear.setEnabled(False)
            
            
            self.VersionMatch.setEnabled(True)


            self.VersionUp.setEnabled(True)


            self.VersionDown.setEnabled(True)


            self.VersionLast.setEnabled(True)
            


        #Replaces String


        if knob is self.Replace:
        

            count = 0
         

            for n in nuke.selectedNodes():
            
            
                if n.Class() in self.SelectedNodeTypes:


                    for knob in self.SelectedKnobTypes:

                      
                        old = n[knob].value()


                        NewStr=re.sub(self.SelectVal.value(),self.ReplaceVal.value(),n[knob].value())


                        n[knob].setValue(NewStr)


                        new = n[knob].value()


                        if old != new:


                           count+=1


            if self.Info.getValue():


                Warning_changed(self.warningB,count) 



        #Switches between inputs


        if knob is self.Switch:

            temp = self.SelectVal.value()
   
            self.SelectVal.setValue(self.ReplaceVal.value())

            self.ReplaceVal.setValue(temp)



        #Clears String Field


        if knob is self.Clear:


            self.SelectVal.setValue("")


            self.ReplaceVal.setValue("")



        #Changes Versions    
        
        #Version Match


        if knob is self.VersionMatch:

            try:

                if self.Info.getValue():   

                    if self.VersionFolder.getValue():

                        Warning_changed(self.warningC,VersionMatchFolder(self.SelectedKnobTypes,self.SelectedNodeTypes))
                            
                    else:
                        
                        Warning_changed(self.warningC,VersionMatchFiles(self.SelectedKnobTypes,self.SelectedNodeTypes))

                elif self.VersionFolder.getValue():

                    VersionMatchFolder(self.SelectedKnobTypes,self.SelectedNodeTypes)
                        
                else:
                    
                    VersionMatchFiles(self.SelectedKnobTypes,self.SelectedNodeTypes)

            except:

                pass
                   
                   
        #Version Up
        

        if knob is self.VersionUp:

            try:
                    
                if self.Info.getValue():   

                    if self.VersionFolder.getValue():

                        Warning_changed(self.warningC,VersionUp(self.SelectedKnobTypes,self.SelectedNodeTypes))
                            
                    else:
                        
                        Warning_changed(self.warningC,VersionUpFiles(self.SelectedKnobTypes,self.SelectedNodeTypes))

                elif self.VersionFolder.getValue():

                    VersionUp(self.SelectedKnobTypes,self.SelectedNodeTypes)
                        
                else:
                    
                    VersionUpFiles(self.SelectedKnobTypes,self.SelectedNodeTypes)

            except:

                pass
                   

        #Version Down    
        

        if knob is self.VersionDown:

            try:

                if self.Info.getValue():    

                    if self.VersionFolder.getValue():

                        Warning_changed(self.warningC,VersionDown(self.SelectedKnobTypes,self.SelectedNodeTypes))
                        
                    else:
                        
                        Warning_changed(self.warningC,VersionDownFiles(self.SelectedKnobTypes,self.SelectedNodeTypes))

                elif self.VersionFolder.getValue():

                    VersionDown(self.SelectedKnobTypes,self.SelectedNodeTypes)
                        
                else:
                    
                    VersionDownFiles(self.SelectedKnobTypes,self.SelectedNodeTypes)

            except:

                pass
                    
                    
        #Version Last
        

        if knob is self.VersionLast:

            try:

                if self.Info.getValue():        

                    if self.VersionFolder.getValue():

                        Warning_changed(self.warningC,VersionLast(self.SelectedKnobTypes,self.SelectedNodeTypes))
                            
                    else:
                        
                        Warning_changed(self.warningC,VersionLastFiles(self.SelectedKnobTypes,self.SelectedNodeTypes))

                elif self.VersionFolder.getValue():

                    VersionLast(self.SelectedKnobTypes,self.SelectedNodeTypes)
                        
                else:
                    
                    VersionLastFiles(self.SelectedKnobTypes,self.SelectedNodeTypes)

            except:

                pass


        # Resets


        if knob is self.Reset:


            self.SelectedNodeTypes = ["Read"]


            self.SelectedKnobTypes = ["file"]


            self.Read.setValue(True)


            self.Write.setValue(False)


            self.DeepRead.setValue(False)


            self.DeepWrite.setValue(False)


            self.file.setValue(True)


            self.proxy.setValue(False)
            
            
            self.Info.setValue(True)


            self.VersionFolder.setValue(True)


            self.Type.setValue("All")


            self.SelectString.setValue("")


            self.SelectString.setEnabled(False)


            self.Add.setEnabled(False)


            self.Remove.setEnabled(False)


            self.ClearString.setEnabled(False)


            self.SelectManually.setValue(False)


            self.SelectVal.setEnabled(False)


            self.SelectVal.setValue("")


            self.ReplaceVal.setValue("")


            self.ReplaceVal.setEnabled(False)
            
            
            self.Replace.setEnabled(False)


            self.Switch.setEnabled(False)


            self.Clear.setEnabled(False)
            
            
            self.VersionMatch.setEnabled(True)


            self.VersionUp.setEnabled(True)


            self.VersionDown.setEnabled(True)


            self.VersionLast.setEnabled(True)


            self.warning.setVisible(False)


            self.warningB.setVisible(False)


            self.warningC.setVisible(False)
            

            self.warningD.setVisible(False)


            self.ClearMessage.setEnabled(True)         
            


        #Clears Messages            

        
        if knob is self.ClearMessage:


            self.warning.setVisible(False)


            self.warningB.setVisible(False)


            self.warningC.setVisible(False)
            

            self.warningD.setVisible(False)
            


def addPanel():

    pane = nuke.getPaneFor('Viewer.1')

    return ChangeVersion().addToPane(pane)


menu = nuke.menu("Pane")

menu.addCommand("The Version Changer",addPanel,"Alt+v")

nukescripts.registerPanel("The Version Changer",addPanel)

#ChangeVersion().showModalDialog()0
