______ __
______ re
______ ___
______ json
______ platform

____ .logger ______ logger

TESTING _ F..
___
    TESTING _ __.environ['NON_PRODUCTION_CONTEXT']
_______
    __ platform.system() __ 'Darwin':
        application _ r'Nuke\d+\.\d+v\d+.app'
    elif platform.system() __ 'Windows':
        application _ r'Nuke\d+\.\d+.exe'
    else:
        r_ RuntimeError('OS {0} is not supported'.f..(platform.system()))

    match _ re.search(application, ___.executable)
    __ no. match:
        r_ RuntimeError('Import the_silo from within Nuke')
    ______ nuke

__version__ _ '0.1.2'
__all__ _ []

silo_name _ 'The Silo'
silo_location _ __.path.dirname(__.path.abspath( -f))


___ init():
    logger.i..('Initialising The Silo...')
    logger.i..('Version: {0}'.f..(__version__))
    nuke.pluginAddPath('{0}/gizmos'.f..(silo_location))
    logger.i..('[DONE]')


___ build(toolbar_True):
    logger.i..('Building The Silo UI...')
    logger.i..('Version: {0}'.f..(__version__))

    __ no. nuke.GUI:
        logger.c..('Nuke is not in GUI mode, aborting UI creation')
        r_

    __ toolbar:
        silo_menu _ nuke.toolbar('Nodes').addMenu(silo_name)
    else:
        silo_menu _ nuke.menu('Nuke').addMenu(silo_name)

    with open('{0}/silo_data.json'.f..(silo_location), 'r') __ fp:
        silo_data _ json.load(fp)

    ___ gizmo_name, gizmo __ sorted(silo_data['gizmos'],
                                    key_lambda x: x[0]):
        logger.i..('Adding gizmo: {0}'.f..(gizmo_name))
        silo_menu.addCommand('Gizmos/{0}'.f..(gizmo_name),
                             'from the_silo import wrapper;'
                             'wrapper.create_gizmo(\'{0}\')'.
                             f..(gizmo))

    ___ script_name, module, func, keys __ sorted(silo_data['scripts'],
                                                  key_lambda x: x[0]):
        logger.i..('Adding script: {0}'.f..(script_name))
        silo_menu.addCommand('Scripts/{0}'.f..(script_name),
                             'from the_silo import wrapper;'
                             'wrapper.exec_script(\'{0}\', \'{1}\')'.
                             f..(module, func),
                             keys)

    silo_menu.addSeparator()
    silo_menu.addCommand(
        'Documentation',
        'import webbrowser;webbrowser.open('
        '\'https://the-silo.readthedocs.io/en/latest/index.html\')')
    silo_menu.addSeparator()
    silo_menu.addCommand(
        'Version',
        'nuke.m..("The Silo version {0}")'.f..(__version__))
    silo_menu.addCommand(
        'Contribute',
        'import webbrowser;webbrowser.open('
        '\'https://github.com/florianeinfalt/the_silo\')')

    logger.i..('[DONE]')
