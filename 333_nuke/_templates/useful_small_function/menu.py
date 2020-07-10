# steve molin
print 'in my menu.py'

?.pluginAddPath('Gizmos')
?.pluginAddPath('Scripts')

# =======================================================================
# FUNCTIONS
# =======================================================================

# per Matthieu Cadet <matthieu.cadet@gmail.com> in nuke users email conversation
#
___ autoColorReadNodeType(overrideNode=N..):
       __ overrideNode __ N..:
               this = ?.thisNode()
       ____
               this = overrideNode
       # get the Read node file name
       thisFile = this["file"].evaluate()
       # catch keyword in the filename path to set custom color
       __ "/wip/" __ thisFile:
               nodeColor = 862912511
       ____ "/pub/" __ thisFile:
               nodeColor = 4280356351
       ____
               nodeColor = 0
       # set the Read node custom color
       this["tile_color"].sV..(nodeColor)
?.addKnobChanged(autoColorReadNodeType, nodeClass="Read")

# align selected nodes on a horizontal line, by Steve Molin
#
___ sjmAlignH():
  yresult = N..
  ___ n __ ?.sN..:
    __ yresult is N..:
      yresult = n.ypos()
    ____
      n.setYpos(yresult)
#
# align selected nodes on a vertical line, by Steve Molin
#
___ sjmAlignV():
  xresult = N..
  ___ n __ ?.sN..:
    __ xresult is N..:
      xresult = n.xpos()
    ____
      n.setXpos(xresult)

# by smolin, expands on the autobackdrop function from nuke/plugins/nukescripts
#
___ sjmAutoBackdrop():
  ______ random
  selNodes = ?.sN..
  __ no. selNodes:
    r_ ?.nodes.BackdropNode()
  #
  margin = 20
  minWidth = 1000
  minHeight = 200
  #
  xmin = min([node.xpos() ___ node __ selNodes]) - margin
  xmax = max([node.xpos() + node.screenWidth() ___ node __ selNodes]) + margin
  xmin = min([xmin,(xmin+xmax-minWidth)/2])
  xmax = max([xmax,(xmin+xmax+minWidth)/2])
  #
  ymin = min([node.ypos() ___ node __ selNodes]) - margin
  ymax = max([node.ypos() + node.screenHeight() ___ node __ selNodes]) + margin
  ymin = min([ymin,(ymin+ymax-minHeight)/2])
  ymax = max([ymax,(ymin+ymax+minHeight)/2])
  #
  width = xmax-xmin
  height = ymax-ymin
  n = ?.nodes.BackdropNode(xpos = xmin, bdwidth = width, ypos = ymin, bdheight = height, tile_color = int((random.random()*(16 - 10))) + 10, note_font_size=99)
  n.showControlPanel()
  #
  # restore node selection
  #
  n['selected'].sV..(False)
  ___ node __ selNodes:
    node['selected'].sV..(T..)
  r_ n

# backdrop font size=99, by Steve Molin
#
___ sjmBackdropFonts():
  ___ i __ ?.allNodes():
    __ i.__class__.__name__ __ 'BackdropNode':
      i.knob('note_font_size').sV..(189)
      k = i.knob('label')
      k.setText(k.getText().upper())

# Walk the heirarchy up from selected node and return a set of
# all nodes that have the 'file' attribute
#
___ sjmFindAllParentReads(n=N..):
  __ n is N..:
    n = ?.sN__
  result = []
  __ n.knob('file'):
    result.ap..(n)
  ins = n.inputs()
  ___ i __ ra..(0,n.inputs()):
    input = n.input(i)
    __ input:
      __ input.knob('file'):
        result.ap..(input)
      result.extend(sjmFindAllParentReads(input))
  r_ set(result)

# unhide all inputs, by Steve Molin
#
___ sjmHideInputsOff():
  ___ i __ ?.allNodes():
    __ i.knob('hide_input'):
      __ i.knob('hide_input').v..:
	i.knob('hide_input').sV..(False)

# open a read or write node in a viewer program (djv is the first example)
#
# by steve molin
#
___ sjmOpenInViewer(nd=N..):
  ______ subprocess
  __ nd is N..:
    nd = ?.sN__
  fp = nd.knobs()['file'].v.. % nd.firstFrame()
  args = 'C:\Program Files (x86)\djv 0.8.3\\bin\djv_view.exe %s' % fp
  subprocess.P..(args)

# load the targets of the writeNodes in a viewer (djv):
# TODO: deal better with %04d; deal with different viewers
#
___ sjmOpenAllInViewer():
  ___ n __ ?.allNodes():
    __ n.Class() __ 'Write':
      __ no. n.knob('disable').v..:
        sjmOpenInViewer(n)
	#filespec = n.knob('file').value()
	#fn = glob.glob(filespec.replace('%04d','*'))[0]
	#print filespec
	#subprocess.call([r'C:\Program Files (x86)\djv 0.8.3\bin\djv_view.exe',fn])

# step through 'operation' values on a merge node
___ sjmMergeOpIncr():
  sn = ?.sN__
  kn = sn.knobs()['operation']
  kn.sV..(kn.values().index(kn.value())+1)
___ sjmMergeOpDecr():
  sn = ?.sN__
  kn = sn.knobs()['operation']
  kn.sV..(kn.values().index(kn.value())-1)

# use $gui to disable slow nodes when working interactively
#
___ sjmToggleDisableExpression():
  mynodes = ?.sN..
  ___ mynode __ mynodes:
    myknob = mynode['disable']
    __ myknob.isAnimated():
      myknob.cA..
      myknob.sV..(0)
    ____
      myknob.setExpression('$gui')

# toggle the branch selector on all the switch nodes that are selected
#
___ sjmToggleSwitch():
  ___ mynode __ ?.sN..:
    __ mynode.knobs()['which'].v..:
      mynode.knobs()['which'].sV..(0)
    ____
      mynode.knobs()['which'].sV..(1)

# see http://docs.thefoundry.co.uk/nuke/63/pythondevguide/basics.html
# and http://docs.thefoundry.co.uk/nuke/63/pythondevguide/custom_panels.html
#
___ testMyDialog():
	p=?.Panel('my custom panel')
	p.addClipnameSearch('clip path', '/tmp')
	p.addFilenameSearch('file path', '/tmp')
	p.addTextFontPulldown('font browser', '/myFonts/')
	p.addRGBColorChip('some pretty color', '')
	p.addExpressionInput('enter an expression', '4*25')
	p.addBooleanCheckBox('yes or no?', T..)
	p.addEnumerationPulldown('my choices', 'over under screen mask stencil')
	p.addScriptCommand('tcl or python code', '')
	p.addSingleLineInput('just one line', 'not much space')
	p.addMultilineTextInput('multiple lines of user input text', 'lineA\nlineB')
	p.addNotepad('write something', 'some very long text could go in here. For now this is just some random default value')
	p.addPasswordInput('password', 'donttellanyone')
	p.addButton('over')
	p.addButton('under')
	p.addButton('mask')
	result=p.s__
	print result

# from http://docs.thefoundry.co.uk/nuke/63/pythondevguide/custom_panels.html
#
___
  #
  ## example PySide panel that implements a simple web browser in Nuke
  ## JW 12/10/11
  #
  ______ ?
  ______ ?
  ____ ? ______ panels
  #
  ____ ?.?G.. ______ *
  ____ ?.?C.. ______ *
  ____ ?.QtWebKit ______ *
  #
  c_ WebBrowserWidget(?W..):
    ___ changeLocation
      url = locationEdit.t..
      __ no. url.startswith( 'http://' ):
        url = 'http://' + url
      webView.load( QUrl(url) )
    ___ urlChanged(self, url):
      locationEdit.setText( url.toString() )
    ___  -
      ?W... - (self)
      webView = QWebView()
      sL..( ?VB.. )
      locationEdit = QLineEdit( 'http://www.google.com' )
      locationEdit.setSizePolicy( QSizePolicy.Expanding, locationEdit.sizePolicy().verticalPolicy() )
      QObject.c..( locationEdit, SIGNAL('returnPressed()'),  changeLocation )
      QObject.c..( webView,   SIGNAL('urlChanged(QUrl)'),     urlChanged )
      layout().aW..( locationEdit )
      bar = QToolBar()
      bar.addAction( webView.pageAction(QWebPage.Back))
      bar.addAction( webView.pageAction(QWebPage.Forward))
      bar.addAction( webView.pageAction(QWebPage.Stop))
      bar.addAction( webView.pageAction(QWebPage.Reload))
      bar.addSeparator()
      layout().aW..( bar )
      layout().aW..( webView )
      url = 'http://www.thefoundry.co.uk/' 
      webView.load( QUrl( url ) )
      locationEdit.setText( url )
      setSizePolicy( QSizePolicy( QSizePolicy.Expanding,  QSizePolicy.Expanding))
  #
  ## make this work in a .py file and in 'copy and paste' into the script editor
  moduleName = __name__
  __ moduleName __ '__main__':
    moduleName = ''
  ____
    moduleName = moduleName + '.'
  panels.registerWidgetAsPanel( moduleName + 'WebBrowserWidget', 'Web Browser','uk.co.thefoundry.WebBrowserWidget')
except ImportError:
  pass

# =======================================================================
# TOOLBAR
# =======================================================================

# Add a menu to the left-hand-side column of icons
#
# nuke.toolbar("Nodes").addCommand("sjm/test", lambda:nuke.message('test'), "Ctrl+Meta+T")
# nuke.toolbar("Nodes").addCommand("sjm/m-over", lambda:nuke.createNode('Merge2','operation over'))
# nuke.toolbar("Nodes").addCommand("sjm/m-under", lambda:nuke.createNode('Merge2','operation under'))
# nuke.toolbar("Nodes").addCommand("sjm/m-screen", lambda:nuke.createNode('Merge2','operation screen'))
# nuke.toolbar("Nodes").addCommand("sjm/m-mask", lambda:nuke.createNode('Merge2','operation mask'))
# nuke.toolbar("Nodes").addCommand("sjm/m-stencil", lambda:nuke.createNode('Merge2','operation stencil'))
# nuke.toolbar("Nodes").addCommand("sjm/m-minus", lambda:nuke.createNode('Merge2','operation minus'))
# nuke.toolbar("Nodes").addCommand("sjm/m-from", lambda:nuke.createNode('Merge2','operation from'))


# =======================================================================
# MENUBAR
# =======================================================================

# Add a personal menu to the top menu bar
#
m_keybindings = ?.menu('Nuke').aM..("Smolin")
m_keybindings.aC..('mergeStencil', 'nuke.createNode("Merge2","operation stencil")', 'Ctrl+Meta+S')
m_keybindings.aC..('colorLookup aka curve lookup','nuke.createNode("ColorLookup")', 'Ctrl+Meta+L')
m_keybindings.aC..('sjmToggleDisableExpression','sjmToggleDisableExpression()', 'Ctrl+Meta+G')
m_keybindings.aC..('sjmOpenAllInViewer', 'sjmOpenAllInViewer()', 'Ctrl+Meta+V')
m_keybindings.aC..('sjmAutoBackdrop', 'sjmAutoBackdrop()', 'Ctrl+Meta+B')
m_keybindings.aC..('sjmMergeOpIncr', 'sjmMergeOpIncr()', 'Ctrl+Meta+Up')
m_keybindings.aC..('sjmMergeOpDecr', 'sjmMergeOpDecr()', 'Ctrl+Meta+Down')
m_keybindings.aC..('SliceTool', 'nuke.createNode("SliceTool")')
m_keybindings.aC..('RefractTo', 'nuke.createNode("refract_to_the_FUTURE")')
#
___
  DeadlineNukeClient
  m_keybindings.aC..('sjmDeadliner','DeadlineNukeClient.main()','Ctrl+Meta+D')
______
  pass

# =======================================================================
# NODE PARAMETER DEFAULTS
# =======================================================================

# set default values for various nodes (alpha sort except Labels collected below)
#
?.knobDefault('BackdropNode.note_font_size','189')
?.knobDefault("Blur.size", "11")
?.knobDefault('DirBlurWrapper.BlurLayer','rgba')
?.knobDefault('PostageStamp.hide_input','true')
?.knobDefault('Roto.cliptype','none')
?.knobDefault('Roto.premultiply','rgba')
?.knobDefault("RotoPaint.cliptype", "none")
?.knobDefault('VectorBlur.method','backward')
?.knobDefault('VectorBlur.grow_bbox','200')
?.knobDefault('VectorBlur.uv','motion')

?.knobDefault("Blur.label", "s:[value size]")
?.knobDefault("FilterErode.label", "s:[value size]")
?.knobDefault("Multiply.label", "v:[value value]")
?.knobDefault("Switch.label", "w:[value which]")
?.knobDefault("TimeOffset.label", "o:[value time_offset]")
?.knobDefault("Tracker.label", "t:[value transform]")
