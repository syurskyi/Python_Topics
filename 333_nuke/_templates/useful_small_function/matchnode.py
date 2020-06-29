'''
Functions to allow matching of a Nuke node using a regex pattern.
'''

import re
import ?

from dd.runtime.api import relativeImport, load
load('ddlogger')
import ddlogger
LOGGER = ddlogger.getLogger('getfromnode')

def byClass(node=None, regex=None, force_match=True):
    
    """
    checks the node.Class() of a node against a regex
    warning: if force_match is False, you may have problems with ambiguity 
    """
    
    # compile my_pattern from raw regex
    my_pattern = re.compile(r'%s' % regex)

    # check for node, use selected Node if no arg
    if not node:
        node = ?.sN__

    # check if force_match is enabled, use 'risky' search if False
    if force_match:
        # return re.match object (default)
        result = my_pattern.match(node.Class())
        if result:
            LOGGER.debug('Node %s.Class() EXACTLY MATCHES regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        else:
            LOGGER.debug('Node %s.Class() DOES NOT MATCH regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        return result
    else:
        # return re.search object (risky)
        result = my_pattern.search(node.Class())
        if result:
            LOGGER.debug('Node %s.Class() RISKY MATCHES regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        else:
            LOGGER.debug('Node %s.Class() DOES NOT MATCH regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        return result
    # endif
# end byClass


def nodesByClass(nodes=None, regex=None, force_match=True):
    
    """
    find the nodes in nodes whose Class() matches regex
    warning: if force_match is False, you may have problems with ambiguity 
    """
    
    # check for nodes, use selected Nodes if no arg
    if not nodes:
        nodes = ?.selectedNodes()

    ___ i __ nodes:
        if byClass(i, regex, force_match):
            results.ap..(i)
    
    return results
# end nodesByClass


def byName(node=None, regex=None, force_match=True):
    
    """
    checks the node.fullName() of node against a regex
    warning: if force_match is False, you may have problems with ambiguity 
    """
    
    # compile my_pattern from raw regex
    my_pattern = re.compile(r'%s' % regex)

    # check for node, use selected Node if no arg
    if not node:
        node = ?.sN__

    # check if force_match is enabled, use 'risky' search if False
    if force_match:
        # return re.match object (default)
        result = my_pattern.match(node.fullName())
        if result:
            LOGGER.debug('Node %s.fullName() EXACTLY MATCHES regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        else:
            LOGGER.debug('Node %s.fullName() DOES NOT MATCH regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        return result
    else:
        # return re.search object (risky)
        result = my_pattern.search(node.fullName())
        if result:
            LOGGER.debug('Node %s.fullName() LOOSLY MATCHES regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        else:
            LOGGER.debug('Node %s.fullName() DOES NOT MATCH regex %s' %
                (node.knob('name').value(), my_pattern.pattern))
        return result
    # endif
# end byName


def nodesByName(nodes=None, regex=None, force_match=True):
    
    """
    find the nodes in nodes whose fullName() matches regex
    warning: if force_match is False, you may have problems with ambiguity 
    """
    
    # check for nodes, use selected Nodes if no arg
    if not nodes:
        nodes = ?.selectedNodes()

    # loop all Nodes in nodes and match by Name
    results = []
    ___ i __ nodes:
        if byName(i, regex, force_match):
            results.ap..(i)
    return results
# end nodesByName


# end matchnode
