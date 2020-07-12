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


ViewersList _ []

___ GetViewerList(ViewersList):
    ViewersList _ []
    ActiveViewer_""
    ___
        ActiveViewer _ nuke.ViewerWindow.node(nuke.activeViewer()).name()
        ActiveViewer _ "      "+ActiveViewer.split("Viewer")[1]+"    "
    ______
        pass
    ___ v __ nuke.allNodes():
        Name _ v.name()
        Class _ v.Class()
        __ Class __ "Viewer":
            Number _ "      "+ Name.split(Class)[1]+"    "
            __ Number no. __ ViewersList:
                ViewersList.append(Number)
    ViewersList _ sorted(ViewersList)
    __ ActiveViewer!_"":
        ViewersList.remove(ActiveViewer)
        ViewersList.insert(0,ActiveViewer)
    r_ ViewersList
   
___ SelectNode(Viewer,warning):
    SelectedNodes _ []
    Nodes_[]
    ActiveViewer_""
    Viewer _ re.sub(" ","",Viewer.value())
    Viewer _ "Viewer"+Viewer
    ___
        ActiveViewer _ nuke.ViewerWindow.node(nuke.activeViewer()).name()
    ______
        pass
    Inputs _ nuke.toNode(Viewer).inputs()
    __ Inputs__0:
        print Viewer + " Has no Inputs"
        warning.setValue("        "+Viewer + " Has no Inputs")
        warning.setVisible(T..)
        raise ValueError      
    ____ Inputs>1:
        ___ n __ nuke.allNodes():
            n.setSelected(F..)
        __ Viewer __ ActiveViewer:
            index1 _ nuke.ViewerWindow.activeInput(nuke.activeViewer(),F..)+1
            Nodes_[index1]
            ___
                index2 _ nuke.ViewerWindow.activeInput(nuke.activeViewer(),T..)+1
                Nodes.append(index2)
            ______
                pass
            ___ index __ Nodes:
                Node _ nuke.toNode(nuke.toNode(Viewer).input(index-1).name())
                Node.setSelected(T..)
                nuke.show(Node)
        else:
            ___ i __ range(0,Inputs):
                ___
                    Node _ nuke.toNode(nuke.toNode(Viewer).input(i).name())
                    Node.setSelected(T..)
                    nuke.show(Node)
                ______
                    pass               
    else:
        ___ n __ nuke.allNodes():
            n.setSelected(F..)
        __ Viewer __ ActiveViewer:
            ___
                index1 _ nuke.ViewerWindow.activeInput(nuke.activeViewer(),F..)
                Node _ nuke.toNode(nuke.toNode(Viewer).input(index1).name())
                Node.setSelected(T..)
                nuke.show(Node)
            ______
                pass
        else:
            ___ i __ range(0,Inputs):
                ___
                    Node _ nuke.toNode(nuke.toNode(Viewer).input(i).name())
                    Node.setSelected(T..)
                    nuke.show(Node)
                ______
                    pass
    r_ nuke.sN..

___ Zoom(zoom,node):
    __ zoom.getValue():
        x1 _ node[0].xpos()
        y1 _ node[0].ypos()
        w1 _ node[0].screenWidth()
        h1 _ node[0].screenHeight()
        __ le.(node)__1:
            nuke.zoom(2,(x1+w1/2,y1+h1/2))
        ____ le.(node)>1:
            x2 _ node[1].xpos()
            y2 _ node[1].ypos()
            w2 _ node[1].screenWidth()
            h2 _ node[1].screenHeight()
            nuke.zoom(0,((x1+x2)/2+w1/2,(y1+y2)/2+h1/2))
    
     
   
c_ SelectViewerNode(nukescripts.PythonPanel):
   
   
    ___ -

        nukescripts.PythonPanel.- (self,"Select Node in Viewer","Select Node in Viewer")

        setMinimumSize(200, 115)

        # Create Knobs
       
        Viewers _ nuke.Enumeration_Knob("Viewer","Viewer",GetViewerList(ViewersList))
    
        Zoom _ nuke.B_K..("Zoom")

        Zoom.setValue(F..)

        dividerA _ nuke.Text_Knob("")

        warning _ nuke.Text_Knob('warning',"")

        warning.setVisible(F..)

         
        #Tooltips

        Viewers.setTooltip("""
If the selected viewer is active, only active viewer nodes will be selected.

If the selected viewer is not active, all viewer nodes will be selected
        """)
   
        # Add Knobs

        aK..(Viewers)

        aK..(Zoom)

        aK..(dividerA)

        aK..(warning)


    ___ knobChanged(self,knob):

        __ knob.name()__ "OK":

            __ no. warning.visible():

                dividerA.setVisible(F..)
     
                Zoom(Zoom,SelectNode(Viewers,warning))

            else:

                r_

        __ knob __ Viewers:
        
            warning.setVisible(F..)

            dividerA.setVisible(T..)


___ Launcher():

    panel _ SelectViewerNode()

    panel.sMD..
   


        