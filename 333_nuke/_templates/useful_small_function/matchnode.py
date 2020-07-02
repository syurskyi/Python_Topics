'''
Functions to allow matching of a Nuke node using a regex pattern.
'''

______ re
______ ?

____ dd.runtime.api ______ relativeImport, load
load('ddlogger')
______ ddlogger
LOGGER = ddlogger.getLogger('getfromnode')

___ byClass(node=None, regex=None, force_match=True):
    
    """
    checks the node.Class() of a node against a regex
    warning: if force_match is False, you may have problems with ambiguity 
    """
    
    # compile my_pattern from raw regex
    my_pattern = re.compile(r'%s' % regex)

    # check for node, use selected Node if no arg
    __ no. node:
        node = ?.sN__

    # check if force_match is enabled, use 'risky' search if False
    __ force_match:
        # return re.match object (default)
        result = my_pattern.match(node.Class())
        __ result:
            LOGGER.debug('Node %s.Class() EXACTLY MATCHES regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        ____
            LOGGER.debug('Node %s.Class() DOES NOT MATCH regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        r_ result
    ____
        # return re.search object (risky)
        result = my_pattern.search(node.Class())
        __ result:
            LOGGER.debug('Node %s.Class() RISKY MATCHES regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        ____
            LOGGER.debug('Node %s.Class() DOES NOT MATCH regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        r_ result
    # endif
# end byClass


___ nodesByClass(nodes=None, regex=None, force_match=True):
    
    """
    find the nodes in nodes whose Class() matches regex
    warning: if force_match is False, you may have problems with ambiguity 
    """
    
    # check for nodes, use selected Nodes if no arg
    __ no. nodes:
        nodes = ?.sN..

    ___ i __ nodes:
        __ byClass(i, regex, force_match):
            results.ap..(i)
    
    r_ results
# end nodesByClass


___ byName(node=None, regex=None, force_match=True):
    
    """
    checks the node.fullName() of node against a regex
    warning: if force_match is False, you may have problems with ambiguity 
    """
    
    # compile my_pattern from raw regex
    my_pattern = re.compile(r'%s' % regex)

    # check for node, use selected Node if no arg
    __ no. node:
        node = ?.sN__

    # check if force_match is enabled, use 'risky' search if False
    __ force_match:
        # return re.match object (default)
        result = my_pattern.match(node.fullName())
        __ result:
            LOGGER.debug('Node %s.fullName() EXACTLY MATCHES regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        ____
            LOGGER.debug('Node %s.fullName() DOES NOT MATCH regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        r_ result
    ____
        # return re.search object (risky)
        result = my_pattern.search(node.fullName())
        __ result:
            LOGGER.debug('Node %s.fullName() LOOSLY MATCHES regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        ____
            LOGGER.debug('Node %s.fullName() DOES NOT MATCH regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        r_ result
    # endif
# end byName


___ nodesByName(nodes=None, regex=None, force_match=True):
    
    """
    find the nodes in nodes whose fullName() matches regex
    warning: if force_match is False, you may have problems with ambiguity 
    """
    
    # check for nodes, use selected Nodes if no arg
    __ no. nodes:
        nodes = ?.sN..

    # loop all Nodes in nodes and match by Name
    results = []
    ___ i __ nodes:
        __ byName(i, regex, force_match):
            results.ap..(i)
    r_ results
# end nodesByName


# end matchnode
