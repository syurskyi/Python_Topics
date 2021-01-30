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


______ re, ?, n_s_


ViewersList _ # list

___ GetViewerList(ViewersList):
    ViewersList _ # list
    ActiveViewer_""
    ___
        ActiveViewer _ ?.ViewerWindow.node(?.activeViewer()).n..
        ActiveViewer _ "      "+ActiveViewer.s..("Viewer")[1]+"    "
    ______
        p..
    ___ v __ ?.allNodes
        Name _ v.n..
        Class _ v.Class()
        __ Class __ "Viewer":
            Number _ "      "+ Name.s..(Class)[1]+"    "
            __ Number no. __ ViewersList:
                ViewersList.ap..(Number)
    ViewersList _ sorted(ViewersList)
    __ ActiveViewer!_"":
        ViewersList.r__(ActiveViewer)
        ViewersList.insert(0,ActiveViewer)
    r_ ViewersList
   
___ SelectNode(Viewer,warning):
    SelectedNodes _ # list
    Nodes_# list
    ActiveViewer_""
    Viewer _ re.sub(" ","",Viewer.v.. ())
    Viewer _ "Viewer"+Viewer
    ___
        ActiveViewer _ ?.ViewerWindow.node(?.activeViewer()).n..
    ______
        p..
    Inputs _ ?.tN..(Viewer).inputs()
    __ Inputs__0:
        print Viewer + " Has no Inputs"
        warning.sV..("        "+Viewer + " Has no Inputs")
        warning.setVisible(T..)
        raise ValueError      
    ____ Inputs>1:
        ___ n __ ?.allNodes
            n.setSelected(F..)
        __ Viewer __ ActiveViewer:
            index1 _ ?.ViewerWindow.activeInput(?.activeViewer(),F..)+1
            Nodes_[index1]
            ___
                index2 _ ?.ViewerWindow.activeInput(?.activeViewer(),T..)+1
                Nodes.ap..(index2)
            ______
                p..
            ___ index __ Nodes:
                Node _ ?.tN..(?.tN..(Viewer).input(index-1).n..
                Node.setSelected(T..)
                ?.show(Node)
        ____
            ___ i __ ra__(0,Inputs):
                ___
                    Node _ ?.tN..(?.tN..(Viewer).input(i).n..
                    Node.setSelected(T..)
                    ?.show(Node)
                ______
                    p..
    ____
        ___ n __ ?.allNodes
            n.setSelected(F..)
        __ Viewer __ ActiveViewer:
            ___
                index1 _ ?.ViewerWindow.activeInput(?.activeViewer(),F..)
                Node _ ?.tN..(?.tN..(Viewer).input(index1).n..
                Node.setSelected(T..)
                ?.show(Node)
            ______
                p..
        ____
            ___ i __ ra__(0,Inputs):
                ___
                    Node _ ?.tN..(?.tN..(Viewer).input(i).n..
                    Node.setSelected(T..)
                    ?.show(Node)
                ______
                    p..
    r_ ?.sN..

___ Zoom(zoom,node):
    __ zoom.gV..:
        x1 _ node[0].xpos()
        y1 _ node[0].ypos()
        w1 _ node[0].screenWidth()
        h1 _ node[0].screenHeight()
        __ le.(node)__1:
            ?.zoom(2,(x1+w1/2,y1+h1/2))
        ____ le.(node)>1:
            x2 _ node[1].xpos()
            y2 _ node[1].ypos()
            w2 _ node[1].screenWidth()
            h2 _ node[1].screenHeight()
            ?.zoom(0,((x1+x2)/2+w1/2,(y1+y2)/2+h1/2))
    
     
   
c_ SelectViewerNode(n_s_.PP..):
   
   
    ___ -

        n_s_.PP...- (self,"Select Node in Viewer","Select Node in Viewer")

        sMS..(200, 115)

        # Create Knobs
       
        Viewers _ ?.E_K..("Viewer","Viewer",GetViewerList(ViewersList))
    
        Zoom _ ?.B_K..("Zoom")

        Zoom.sV..(F..)

        dividerA _ ?.T_K..("")

        warning _ ?.T_K..('warning',"")

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

        __ knob.n.. __ "OK":

            __ no. warning.visible

                dividerA.setVisible(F..)
     
                Zoom(Zoom,SelectNode(Viewers,warning))

            ____

                r_

        __ knob __ Viewers:
        
            warning.setVisible(F..)

            dividerA.setVisible(T..)


___ Launcher

    panel _ SelectViewerNode()

    panel.sMD..
   


        