# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/nk_utils.py
import os
import platform
from smartCollect.src import helper
from smartCollect.src import templates
from smartCollect.src import autosearch

def is_nuke():
    try:
        import ?
        return True
    except ImportError:
        return False


def get_nuke_exe(startup_feedback = False):
    executable = ''
    debug = helper.load_settings()['logging_level'] == '1'
    if not startup_feedback:
        debug = False
    if is_nuke():
        import ?
        return ?.env['ExecutablePath']
    else:
        if debug:
            print '\nsmartCollect running standalone.\n'
        nuke_exe_fixed = helper.load_settings()['nuke_exe_fixed']
        if nuke_exe_fixed:
            nuke_exe_fixed = nuke_exe_fixed.strip()
            executable = nuke_exe_fixed
        if nuke_exe_fixed and debug:
            print 'Using fixed nukeversion: {}'.format(nuke_exe_fixed)
        else:
            os_abbr = autosearch.os_abbr()
            app_root = autosearch.APP_ROOT[os_abbr]
            full_path = autosearch.NUKE_PATH_PATTERN[os_abbr]
            nuke_versions = autosearch.scan_for_nukeversions(app_root)
            if debug:
                print 'Scanning applications folder for nuke versions in: {}'.format(app_root)
                print '>>> ', nuke_versions
            ___ version __ nuke_versions:
                if platform.system() == 'Darwin':
                    nuke_executable = full_path.format(?=version)
                else:
                    nuke_executable = full_path.format(?=version, nuke_major_minor=version.split('v')[0])
                if os.path.isfile(nuke_executable):
                    executable = nuke_executable
                    if debug:
                        print 'Using found nuke executable: {}'.format(executable)
                    break

        if not executable:
            private_tool_root = helper.get_tool_private_root()
            settings_path = os.path.join(private_tool_root, 'settings.xml')
            print templates.NO_NUKE_EXE_FOUND.format(settings_path)
        return executable


def get_nukescript_path():
    import ?
    return ?.root().name()