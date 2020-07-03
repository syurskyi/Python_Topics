# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/nk_utils.py
______ __
______ pl..
____ smartCollect.src ______ helper
____ smartCollect.src ______ templates
____ smartCollect.src ______ autosearch

___ is_nuke():
    ___
        ______ ?
        r_ T..
    except ImportError:
        r_ False


___ get_nuke_exe(startup_feedback = False):
    executable = ''
    debug = helper.load_settings()['logging_level'] __ '1'
    __ no. startup_feedback:
        debug = False
    __ is_nuke():
        ______ ?
        r_ ?.env['ExecutablePath']
    ____
        __ debug:
            print '\nsmartCollect running standalone.\n'
        nuke_exe_fixed = helper.load_settings()['nuke_exe_fixed']
        __ nuke_exe_fixed:
            nuke_exe_fixed = nuke_exe_fixed.strip()
            executable = nuke_exe_fixed
        __ nuke_exe_fixed and debug:
            print 'Using fixed nukeversion: {}'.f..(nuke_exe_fixed)
        ____
            os_abbr = autosearch.os_abbr()
            app_root = autosearch.APP_ROOT[os_abbr]
            full_path = autosearch.NUKE_PATH_PATTERN[os_abbr]
            nuke_versions = autosearch.scan_for_nukeversions(app_root)
            __ debug:
                print 'Scanning applications folder for nuke versions in: {}'.f..(app_root)
                print '>>> ', nuke_versions
            ___ version __ nuke_versions:
                __ pl...system() __ 'Darwin':
                    nuke_executable = full_path.f..(?=version)
                ____
                    nuke_executable = full_path.f..(?=version, nuke_major_minor=version.split('v')[0])
                __ __.path.isfile(nuke_executable):
                    executable = nuke_executable
                    __ debug:
                        print 'Using found nuke executable: {}'.f..(executable)
                    break

        __ no. executable:
            private_tool_root = helper.get_tool_private_root()
            settings_path = __.path.join(private_tool_root, 'settings.xml')
            print templates.NO_NUKE_EXE_FOUND.f..(settings_path)
        r_ executable


___ get_nukescript_path():
    ______ ?
    r_ ?.root().name()