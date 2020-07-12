______ nuke
______ nukescripts

___ newUserKnob(knob, value):
    knob.setValue(value)
    r_ knob

___ allReads():
    readNodes = []
    ___ i __ nuke.allNodes():
        __ i.Class() __ 'Read':
            readNodes.append(i)
    r_ readNodes

___ selectRead():
    ___ i __ allReads():
        i.knob('selected').setValue('True')

___ setLocalize():
    pass

___ setFrameRange():
    f = nukescripts.PythonPanel('Set read nodes frame range')
    f.nodesSelection = nuke.Enumeration_Knob('nodesSel', 'Nodes selections', ['All read nodes', 'Selected nodes only', 'Exclude selected nodes'])
    f.divText = nuke.Text_Knob('divText', '')
    f.firstFrame = newUserKnob(nuke.Int_Knob('first_frame', 'frame range', 1), int(nuke.root().firstFrame()))
    f.before = nuke.Enumeration_Knob('before', '', ['hold', 'loop', 'bounce', 'black'])
    f.lastFrame = newUserKnob(nuke.Int_Knob('last_frame', '', 100), int(nuke.root().lastFrame()))
    f.after = nuke.Enumeration_Knob('after', '', ['hold', 'loop', 'bounce', 'black'])

    #Set nodes selection and after as end line
    ___ s __ (f.nodesSelection, f.after):
        s.setFlag(0x2000)
    ___ k __ (f.nodesSelection, f.divText, f.firstFrame, f.before, f.lastFrame, f.after):
        f.addKnob(k)

    #show dialog
    __ f.sMD..:
        __ f.nodesSelection.v.. __ 'All read nodes':
            Sel = allReads()
        ____ f.nodesSelection.v.. __ 'Selected nodes only':
            Sel = nuke.sN..
        else:
            Sel = allReads()
            ___ i __ nuke.sN..:
                ___
                    Sel.remove(i)
                except ValueError:
                    pass

        ___ r __ Sel:
            ___
                r['first'].setValue(f.firstFrame.value())
                r['before'].setValue(f.before.value())
                r['last'].setValue(f.lastFrame.value())
                r['after'].setValue(f.after.value())
            except ValueError:
                nuke.m..('No nodes selected!')
            except NameError:
                pass

___ setError():
    e = nukescripts.PythonPanel('Missing frames setting')
    e.nodesSelection = nuke.Enumeration_Knob('nodesSel', 'Nodes selections', ['All read nodes', 'Selected nodes only', 'Exclude selected nodes'])
    e.divText = nuke.Text_Knob('divText', '')
    e.onError = nuke.Enumeration_Knob('onError', 'missing frames', ['error', 'black', 'checkerboard', 'nearest frame'])
    e.reload = newUserKnob(nuke.Boolean_Knob('reload', 'Reload changed nodes', '0'), 0)
    ___ k __ (e.nodesSelection, e.divText, e.onError, e.reload):
        k.setFlag(0x1000)
        e.addKnob(k)

    #show dialog
    __ e.sMD..:
        __ e.nodesSelection.v.. __ 'All read nodes':
            Sel = allReads()
        ____ e.nodesSelection.v.. __ 'Selected nodes only':
            Sel = nuke.sN..
        else:
            Sel = allReads()
            ___ i __ nuke.sN..:
                ___
                    Sel.remove(i)
                except ValueError:
                    nuke.m..('No nodes selected!')
                except NameError:
                    pass

        ___ r __ Sel:
            ___
                r['on_error'].setValue(int(e.onError.getValue()))
                __ e.reload.v..:
                    r.knob('reload').execute()
            except ValueError:
                nuke.m..('No nodes selected!')
            except NameError:
                pass


