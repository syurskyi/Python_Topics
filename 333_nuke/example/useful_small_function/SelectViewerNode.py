#Selects Node in Viewer

# To Install 

# 1.copy the script to your nuke scripts / plugin folder

# 2.and add these lines to your menu.py

"""

import SelectViewerNode

menubar=nuke.menu("Nuke")

m=menubar.addMenu("CUSTOM")

m.addCommand("Select Node in Viewer","SelectViewerNode.Launcher()")


"""


import re, nuke, nukescripts


ViewersList = []

def GetViewerList(ViewersList):
    ViewersList = []
    ActiveViewer=""
    try:
        ActiveViewer = nuke.ViewerWindow.node(nuke.activeViewer()).name()
        ActiveViewer = "      "+ActiveViewer.split("Viewer")[1]+"    "
    except:
        pass
    for v in nuke.allNodes():
        Name = v.name()
        Class = v.Class()
        if Class == "Viewer":
            Number = "      "+ Name.split(Class)[1]+"    "
            if Number not in ViewersList:
                ViewersList.append(Number)
    ViewersList = sorted(ViewersList)
    if ActiveViewer!="":
        ViewersList.remove(ActiveViewer)
        ViewersList.insert(0,ActiveViewer)
    return ViewersList
   
def SelectNode(Viewer,warning):
    SelectedNodes = []
    Nodes=[]
    ActiveViewer=""
    Viewer = re.sub(" ","",Viewer.value())
    Viewer = "Viewer"+Viewer
    try:
        ActiveViewer = nuke.ViewerWindow.node(nuke.activeViewer()).name()
    except:
        pass
    Inputs = nuke.toNode(Viewer).inputs()
    if Inputs==0:
        print Viewer + " Has no Inputs"
        warning.setValue("        "+Viewer + " Has no Inputs")
        warning.setVisible(True)
        raise ValueError      
    elif Inputs>1:
        for n in nuke.allNodes():
            n.setSelected(False)
        if Viewer == ActiveViewer:     
            index1 = nuke.ViewerWindow.activeInput(nuke.activeViewer(),False)+1
            Nodes=[index1]
            try:
                index2 = nuke.ViewerWindow.activeInput(nuke.activeViewer(),True)+1
                Nodes.append(index2)
            except:
                pass
            for index in Nodes:
                Node = nuke.toNode(nuke.toNode(Viewer).input(index-1).name())
                Node.setSelected(True)
                nuke.show(Node)
        else:
            for i in range(0,Inputs):
                try:
                    Node = nuke.toNode(nuke.toNode(Viewer).input(i).name())
                    Node.setSelected(True)
                    nuke.show(Node)
                except:
                    pass               
    else:
        for n in nuke.allNodes():
            n.setSelected(False)
        if Viewer == ActiveViewer:     
            try:
                index1 = nuke.ViewerWindow.activeInput(nuke.activeViewer(),False)
                Node = nuke.toNode(nuke.toNode(Viewer).input(index1).name())
                Node.setSelected(True)
                nuke.show(Node)
            except:
                pass
        else:
            for i in range(0,Inputs):
                try:
                    Node = nuke.toNode(nuke.toNode(Viewer).input(i).name())
                    Node.setSelected(True)
                    nuke.show(Node)
                except:
                    pass
    return nuke.selectedNodes()

def Zoom(zoom,node):
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
    
     
   
class SelectViewerNode(nukescripts.PythonPanel):
   
   
    def __init__(self): 

        nukescripts.PythonPanel.__init__(self,"Select Node in Viewer","Select Node in Viewer")

        self.setMinimumSize(200, 115)

        # Create Knobs
       
        self.Viewers = nuke.Enumeration_Knob("Viewer","Viewer",GetViewerList(ViewersList))
    
        self.Zoom = nuke.Boolean_Knob("Zoom")

        self.Zoom.setValue(False)

        self.dividerA = nuke.Text_Knob("")

        self.warning = nuke.Text_Knob('warning',"")

        self.warning.setVisible(False)

         
        #Tooltips

        self.Viewers.setTooltip("""
If the selected viewer is active, only active viewer nodes will be selected.

If the selected viewer is not active, all viewer nodes will be selected
        """)
   
        # Add Knobs

        self.addKnob(self.Viewers)

        self.addKnob(self.Zoom)

        self.addKnob(self.dividerA)

        self.addKnob(self.warning)


    def knobChanged(self,knob):

        if knob.name()== "OK":

            if not self.warning.visible():

                self.dividerA.setVisible(False)
     
                Zoom(self.Zoom,SelectNode(self.Viewers,self.warning))

            else:

                return

        if knob is self.Viewers:
        
            self.warning.setVisible(False)

            self.dividerA.setVisible(True)


def Launcher(): 

    panel = SelectViewerNode()

    panel.showModalDialog()
   


        