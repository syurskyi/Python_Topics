'''
Functions to access values from Nuke Nodes
'''

______ __
______ re
______ ?
______ getseq

______ dd.xplatform

____ dd.runtime.api ______ relativeImport, l..
____ dd.runtime ______ info
l..('ddlogger')
______ ddlogger
LOGGER _ ddlogger.getLogger('getfromnode')

l..('nukepipeline')
__ info.getVersionToBeLoaded("nukepipeline") >_ "3.1.0":
    relativeImport('matchnode', 'nukepipeline/common/utils')
____
    relativeImport('matchnode', 'common/utils')
____ matchnode ______ byClass


___ filePath(node_N.., proxy_F.., regex_N.., force_match_T..):
    
    """
    Retrieves the file path of any node that has one associated with it.
    regex can be used to filter only to nodes with file knobs whose
    Class() fits the pattern
    """
    
    result _ N..

    # check node, use selected Node in dag if no arg
    __ no. node:
        node _ ?.sN__
        
    # check for regex, eliminate non-matching node
    __ regex:
        __ no. byClass(node, regex, force_match):
            node _ N..
    
    # check for node elimination
    __ node:
        ___
            my_knob _ node.knob('file')
            ___
                # attempt to get file knob from linked (gizmos < 5.2v1)
                result _ my_knob.getLinkedKnob().gV..
            ______ AttributeError:
                # attempt to get file knob value directly (gizmos >= 5.2v1)
                result _ my_knob.gV..
            # end try
        ______ AttributeError:
            ___
                # grab filename directly from node with nuke.filename
                result _ ?.filename(node)
            ______ NameError:
                # do nothing if nuke.filename errors out (earlier Nuke version)
                p..
            # end try
        ______
            raise
        # end try
        
        # check if proxy enabled, if so return Proxy knob instead of File
        __ proxy:
            __ ?.r.. .proxy
                __ 'proxy' __ node.knobs
                    ___
                        # attempt to get proxy knob from linked (gizmos < 5.2v1)
                        __ node.getLinkedKnob().knob('proxy').v..:
                            result _ node.getLinkedKnob().knob('proxy').v..
                    ______ AttributeError:
                        # attempt to get proxy knob value directly (gizmos >= 5.2v
                        __ node.knob('proxy').v..:
                            result _ node.knob('proxy').v..
        # end if

        # check if a TCL expression might exist in the result (ie: containts [{($)}])

        expression_check _ re.search('[\[\{\(\]\}\)\$]', st.(result))
        # if an expression might exist, attempt to evaluate
        __ expression_check:
            # make a copy of the result to process
            eval_result _ result

            # create a tmp write node to do the evaluation in
            # if you can figure out a better way to evaluate as Nuke does, be my guest
            tmp _ ?.cN..('Write', inpanel_F..)

            ___
                # LOGIC (IF ANY) BEHIND THE FOLLOWING:
                # knob.evaluate() always evaluates fully, so %V is replaced with the
                # full view name, %v is always replaced with the lowercase first
                # letter of the view, and the %d range string (ie %04d, %03d) is
                # always replaced with the then-current frame value.
                # This is not desireable for most uses, but it is still desireable
                # to evaluate any internal TCL expressions before returning the
                # filePath (otherwise you get the lengthy tcl gibberish instead
                # of a meaningful value) ... hence what follows.
                # NOTE: If someone is actually trying to include the View or
                # Range variable characters inside their pre-evaluation expression,
                # we're hosed.

                # we need the %v or %V variable to remain unevaluated
                view_test _ re.search('(%[V|v])', eval_result)
                # if it exists, log old value and replace with !VIEW! placeholder
                __ view_test:
                    old_view _ view_test.groups()[0]
                    eval_result _ re.sub(old_view, '!VIEW!', eval_result)

                # we need the %d frame range variable to remain unevaluated
                range_test _ re.search('(%[0-9]+d)', eval_result)
                # if it exists, log old value and replace with !RANGE! placeholder
                __ range_test:
                    old_range _ range_test.groups()[0]
                    eval_result _ re.sub(old_range, '!RANGE!', eval_result)

                # let nuke do the actual evaluation work
                tmp.knob('file').sV..(eval_result)
                eval_result _ tmp.knob('file').e..

                # put the stored range variable back
                __ range_test:
                    eval_result _ re.sub('!RANGE!', old_range, eval_result)

                # put the stored view variable back
                __ view_test:
                    eval_result _ re.sub('!VIEW!', old_view, eval_result)

                # evaluation succeeded
                result _ eval_result
            ______
                # evaluation failed, leave result alone and let the gods sort it out
                p..
            finally:
                # one way or another, clean up the tmp node
                ?.delete(tmp)

    __ result !_ N..:
        result _ dd.xplatform.xpath(__.pa__.n_p_(result))
        LOGGER.debug('Discovered path @ for node @' % (
            result, node.knob('name').v.. ()))
        r_ result
    ____
        LOGGER.debug('Discovered no path for node @' % node.knob('name').v.. ())
        r_ N..
# end filePath
   

___ filePathWithRange(node_N.., proxy_F.., regex_N.., force_match_T..):
    
    """
    Retrieves the file path of any node that has one associated with it.
    regex can be used to filter only to nodes with file knobs whose
    Class() fits the pattern.
    """
    
    result _ N..

    # check node, use selected Node in DAG if no arg
    __ no. node:
        node _ ?.sN__

    # check node again (in case user has no selection made)
    # get file path from node
    __ node:
        pa__ _ filePath(node, proxy, regex, force_match)
        # if file path found, append frame range data
        # use getseq instad of root range
        # makes more sense eh? #61881 / #64178
        __ pa__:
            first_frame, last_frame _ getseq.getRange(pa__)
            LOGGER.debug('Discovered range of @-@' % (first_frame, last_frame))
            result _ '@ @-@' % (pa__, first_frame, last_frame)

    # return the path and range discovered
    r_ result
#  end filePathWithRange


___ filePaths(no___N.., proxy_F.., regex_N.., force_match_T..):
    
    """
    Returns a list of the file paths (if any) associated with the nodes in the
    nodes.  Filter using regex to restrict the results to 
    nodes whose Class() matches the pattern.
    """
    
    result _ # list

    # check nodes, use selected Nodes in DAG if no arg
    __ no. n__:
        n__ _ ?.sN..

    # loop through nodes and get path for each Node
    ___ i __ n__:
        ___
            result.ap..(filePath(i, proxy, regex, force_match))
        ______ AttributeError:
            p..
    
    r_ result
# end filePaths


___ filePathsWithRanges(nodes_N.., proxy_F.., regex_N.., force_match_T..):
    
    """
    Returns a list of the file paths (if any) associated with the nodes in the
    nodes.  Filter using regex to restrict the results to 
    nodes whose Class() matches the pattern.
    """
    
    result _ # list

    # check nodes, use selected Nodes in DAG if no arg
    __ no. n__:
        n__ _ ?.sN..

    # loop through nodes and get path and range for each Node
    ___ i __ n__:
        ___
            ra.. _ filePathWithRange(i, proxy, regex, force_match)
            __ ra..:
                result.ap..(ra..)
        ______ AttributeError:
            p..
    
    r_ result
# end filePaths

___ fileType(node):
    """
    Returns the file extension of the node given
    """
    result _ __.pa__.s_t_(filePath(node))[1].lstrip('.')
    LOGGER.debug('Filetype for node @ is @' % (node.knob('name').v.., result))
    r_ result
# end fileType

___ f..(node):
    
    """
    Returns the format of the specified Node, if in the nuke.formats() list
    """
    
    my_format _ N..
    
    # check for node; default to selected Node in DAG if no arg
    __ no. node:
        node _ ?.sN__
    # endif

    # check for Node again (see if user has failed to make selection)
    __ node:
        # grab height from node
        my_height _ node.height()
        
        # grab width from node
        my_width _ node.width()
        
        # grab pixel aspect ratio from node as float
        my_pixel_aspect _ fl..(?.v.. ('@.pixel_aspect' % node.fullName()))
        
        # this is the format to search for
        my_format _ (my_height, my_width, my_pixel_aspect)
        
        # scan nuke.formats for matching format
        ___ i __ ?.formats
            thisFormat _ (i.height(), i.width(), i.pixelAspect())
            # if matching format found, assign my_format to the match
            __ thisFormat __ my_format:
                my_format _ i
                break
                
    # return whatever is the current value of my_format
    LOGGER.debug('Format for node @ is @' % (node.knob('name').v.., my_format))
    r_ my_format
# end format


# end getfromnode
