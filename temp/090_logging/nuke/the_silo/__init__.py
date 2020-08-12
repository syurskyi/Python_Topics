______ os
______ re
______ sys
______ json
______ platform

from .logger ______ logger

TESTING _ False
___
    TESTING _ os.environ['NON_PRODUCTION_CONTEXT']
_______
    if platform.system() == 'Darwin':
        application _ r'Nuke\d+\.\d+v\d+.app'
    elif platform.system() == 'Windows':
        application _ r'Nuke\d+\.\d+.exe'
    else:
        raise RuntimeError('OS {0} is not supported'.format(platform.system()))

    match _ re.search(application, sys.executable)
    if not match:
        raise RuntimeError('Import the_silo from within Nuke')
    ______ nuke

__version__ _ '0.1.2'
__all__ _ []

silo_name _ 'The Silo'
silo_location _ os.path.dirname(os.path.abspath(__file__))


def init():
    logger.i..('Initialising The Silo...')
    logger.i..('Version: {0}'.format(__version__))
    nuke.pluginAddPath('{0}/gizmos'.format(silo_location))
    logger.i..('[DONE]')


def build(toolbar_True):
    logger.i..('Building The Silo UI...')
    logger.i..('Version: {0}'.format(__version__))

    if not nuke.GUI:
        logger.critical('Nuke is not in GUI mode, aborting UI creation')
        return

    if toolbar:
        silo_menu _ nuke.toolbar('Nodes').addMenu(silo_name)
    else:
        silo_menu _ nuke.menu('Nuke').addMenu(silo_name)

    with open('{0}/silo_data.json'.format(silo_location), 'r') as fp:
        silo_data _ json.load(fp)

    for gizmo_name, gizmo in sorted(silo_data['gizmos'],
                                    key_lambda x: x[0]):
        logger.i..('Adding gizmo: {0}'.format(gizmo_name))
        silo_menu.addCommand('Gizmos/{0}'.format(gizmo_name),
                             'from the_silo import wrapper;'
                             'wrapper.create_gizmo(\'{0}\')'.
                             format(gizmo))

    for script_name, module, func, keys in sorted(silo_data['scripts'],
                                                  key_lambda x: x[0]):
        logger.i..('Adding script: {0}'.format(script_name))
        silo_menu.addCommand('Scripts/{0}'.format(script_name),
                             'from the_silo import wrapper;'
                             'wrapper.exec_script(\'{0}\', \'{1}\')'.
                             format(module, func),
                             keys)

    silo_menu.addSeparator()
    silo_menu.addCommand(
        'Documentation',
        'import webbrowser;webbrowser.open('
        '\'https://the-silo.readthedocs.io/en/latest/index.html\')')
    silo_menu.addSeparator()
    silo_menu.addCommand(
        'Version',
        'nuke.m..("The Silo version {0}")'.format(__version__))
    silo_menu.addCommand(
        'Contribute',
        'import webbrowser;webbrowser.open('
        '\'https://github.com/florianeinfalt/the_silo\')')

    logger.i..('[DONE]')
