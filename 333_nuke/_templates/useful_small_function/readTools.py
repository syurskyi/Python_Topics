______ nuke
______ nukescripts

___ newUserKnob(knob, value):
    knob.setValue(value)
    r_ knob

___ allReads():
    readNodes _ []
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
    f _ nukescripts.PythonPanel('Set read nodes frame range')
    f.nodesSelection _ nuke.E_K..('nodesSel', 'Nodes selections', ['All read nodes', 'Selected nodes only', 'Exclude selected nodes'])
    f.divText _ nuke.T_K..('divText', '')
    f.firstFrame _ newUserKnob(nuke.I_K..('first_frame', 'frame range', 1), in.(nuke.root().firstFrame()))
    f.before _ nuke.E_K..('before', '', ['hold', 'loop', 'bounce', 'black'])
    f.lastFrame _ newUserKnob(nuke.I_K..('last_frame', '', 100), in.(nuke.root().lastFrame()))
    f.after _ nuke.E_K..('after', '', ['hold', 'loop', 'bounce', 'black'])

    #Set nodes selection and after as end line
    ___ s __ (f.nodesSelection, f.after):
        s.sF..(0x2000)
    ___ k __ (f.nodesSelection, f.divText, f.firstFrame, f.before, f.lastFrame, f.after):
        f.aK..(k)

    #show dialog
    __ f.sMD..:
        __ f.nodesSelection.v.. __ 'All read nodes':
            Sel _ allReads()
        ____ f.nodesSelection.v.. __ 'Selected nodes only':
            Sel _ nuke.sN..
        else:
            Sel _ allReads()
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
    e _ nukescripts.PythonPanel('Missing frames setting')
    e.nodesSelection _ nuke.E_K..('nodesSel', 'Nodes selections', ['All read nodes', 'Selected nodes only', 'Exclude selected nodes'])
    e.divText _ nuke.T_K..('divText', '')
    e.onError _ nuke.E_K..('onError', 'missing frames', ['error', 'black', 'checkerboard', 'nearest frame'])
    e.reload _ newUserKnob(nuke.B_K..('reload', 'Reload changed nodes', '0'), 0)
    ___ k __ (e.nodesSelection, e.divText, e.onError, e.reload):
        k.sF..(0x1000)
        e.aK..(k)

    #show dialog
    __ e.sMD..:
        __ e.nodesSelection.v.. __ 'All read nodes':
            Sel _ allReads()
        ____ e.nodesSelection.v.. __ 'Selected nodes only':
            Sel _ nuke.sN..
        else:
            Sel _ allReads()
            ___ i __ nuke.sN..:
                ___
                    Sel.remove(i)
                except ValueError:
                    nuke.m..('No nodes selected!')
                except NameError:
                    pass

        ___ r __ Sel:
            ___
                r['on_error'].setValue(in.(e.onError.getValue()))
                __ e.reload.v..:
                    r.knob('reload').execute()
            except ValueError:
                nuke.m..('No nodes selected!')
            except NameError:
                pass


