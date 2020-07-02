#Selects Node in Viewer

# To Install 

# 1.copy the script to your nuke scripts / plugin folder

# 2.and add these lines to your menu.py

"""

______ SelectViewerNode

menubar=nuke.menu("Nuke")

m=menubar.addMenu("CUSTOM")

m.addCommand("Select Node in Viewer","SelectViewerNode.Launcher()")


"""


______ re, nuke, nukescripts


ViewersList = []

___ GetViewerList(ViewersList):
    ViewersList = []
    ActiveViewer=""
    ___
        ActiveViewer = nuke.ViewerWindow.node(nuke.activeViewer()).name()
        ActiveViewer = "      "+ActiveViewer.split("Viewer")[1]+"    "
    ______
        pass
    ___ v __ nuke.allNodes():
        Name = v.name()
        Class = v.Class()
        if Class == "Viewer":
            Number = "      "+ Name.split(Class)[1]+"    "
            if Number not __ ViewersList:
                ViewersList.append(Number)
    ViewersList = sorted(ViewersList)
    if ActiveViewer!="":
        ViewersList.remove(ActiveViewer)
        ViewersList.insert(0,ActiveViewer)
    return ViewersList
   
___ SelectNode(Viewer,warning):
    SelectedNodes = []
    Nodes=[]
    ActiveViewer=""
    Viewer = re.sub(" ","",Viewer.value())
    Viewer = "Viewer"+Viewer
    ___
        ActiveViewer = nuke.ViewerWindow.node(nuke.activeViewer()).name()
    ______
        pass
    Inputs = nuke.toNode(Viewer).inputs()
    if Inputs==0:
        print Viewer + " Has no Inputs"
        warning.setValue("        "+Viewer + " Has no Inputs")
        warning.setVisible(True)
        raise ValueError      
    elif Inputs>1:
        ___ n __ nuke.allNodes():
            n.setSelected(False)
        if Viewer == ActiveViewer:     
            index1 = nuke.ViewerWindow.activeInput(nuke.activeViewer(),False)+1
            Nodes=[index1]
            ___
                index2 = nuke.ViewerWindow.activeInput(nuke.activeViewer(),True)+1
                Nodes.append(index2)
            ______
                pass
            ___ index __ Nodes:
                Node = nuke.toNode(nuke.toNode(Viewer).input(index-1).name())
                Node.setSelected(True)
                nuke.show(Node)
        else:
            ___ i __ range(0,Inputs):
                ___
                    Node = nuke.toNode(nuke.toNode(Viewer).input(i).name())
                    Node.setSelected(True)
                    nuke.show(Node)
                ______
                    pass               
    else:
        ___ n __ nuke.allNodes():
            n.setSelected(False)
        if Viewer == ActiveViewer:     
            ___
                index1 = nuke.ViewerWindow.activeInput(nuke.activeViewer(),False)
                Node = nuke.toNode(nuke.toNode(Viewer).input(index1).name())
                Node.setSelected(True)
                nuke.show(Node)
            ______
                pass
        else:
            ___ i __ range(0,Inputs):
                ___
                    Node = nuke.toNode(nuke.toNode(Viewer).input(i).name())
                    Node.setSelected(True)
                    nuke.show(Node)
                ______
                    pass
    return nuke.selectedNodes()

___ Zoom(zoom,node):
    if zoom.getValue():
        x1 = node[0].xpos()
        y1 = node[0].ypos()
        w1 = node[0].screenWidth()
        h1 = node[0].screenHeight()
        if len(node)==1:       
            nuke.zoom(2,(x1+w1/2,y1+h1/2))
        elif len(node)>1:           
            x2 = node[1].xpos()
            y2 = node[1].ypos()
            w2 = node[1].screenWidth()
            h2 = node[1].screenHeight()
            nuke.zoom(0,((x1+x2)/2+w1/2,(y1+y2)/2+h1/2))
    
     
   
c_ SelectViewerNode(nukescripts.PythonPanel):
   
   
    ___ -

        nukescripts.PythonPanel.- (self,"Select Node in Viewer","Select Node in Viewer")

        setMinimumSize(200, 115)

        # Create Knobs
       
        Viewers = nuke.Enumeration_Knob("Viewer","Viewer",GetViewerList(ViewersList))
    
        Zoom = nuke.Boolean_Knob("Zoom")

        Zoom.setValue(False)

        dividerA = nuke.Text_Knob("")

        warning = nuke.Text_Knob('warning',"")

        warning.setVisible(False)

         
        #Tooltips

        Viewers.setTooltip("""
If the selected viewer is active, only active viewer nodes will be selected.

If the selected viewer is not active, all viewer nodes will be selected
        """)
   
        # Add Knobs

        addKnob(Viewers)

        addKnob(Zoom)

        addKnob(dividerA)

        addKnob(warning)


    ___ knobChanged(self,knob):

        if knob.name()== "OK":

            if not warning.visible():

                dividerA.setVisible(False)
     
                Zoom(Zoom,SelectNode(Viewers,warning))

            else:

                return

        if knob is Viewers:
        
            warning.setVisible(False)

            dividerA.setVisible(True)


___ Launcher():

    panel = SelectViewerNode()

    panel.showModalDialog()
   


        