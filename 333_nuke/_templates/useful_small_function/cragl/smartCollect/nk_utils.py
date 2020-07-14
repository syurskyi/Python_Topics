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
    ______ ImportError:
        r_ F..


___ get_nuke_exe(startup_feedback _ F..):
    executable _ ''
    debug _ helper.load_settings()['logging_level'] __ '1'
    __ no. startup_feedback:
        debug _ F..
    __ is_nuke():
        ______ ?
        r_ ?.env['ExecutablePath']
    ____
        __ debug:
            print '\nsmartCollect running standalone.\n'
        nuke_exe_fixed _ helper.load_settings()['nuke_exe_fixed']
        __ nuke_exe_fixed:
            nuke_exe_fixed _ nuke_exe_fixed.strip()
            executable _ nuke_exe_fixed
        __ nuke_exe_fixed an. debug:
            print 'Using fixed nukeversion: {}'.f..(nuke_exe_fixed)
        ____
            os_abbr _ autosearch.os_abbr()
            app_root _ autosearch.APP_ROOT[os_abbr]
            full_path _ autosearch.NUKE_PATH_PATTERN[os_abbr]
            nuke_versions _ autosearch.scan_for_nukeversions(app_root)
            __ debug:
                print 'Scanning applications folder for nuke versions in: {}'.f..(app_root)
                print '>>> ', nuke_versions
            ___ version __ nuke_versions:
                __ pl...system() __ 'Darwin':
                    nuke_executable _ full_path.f..(?_version)
                ____
                    nuke_executable _ full_path.f..(?_version, nuke_major_minor_version.split('v')[0])
                __ __.pa__.isf..(nuke_executable):
                    executable _ nuke_executable
                    __ debug:
                        print 'Using found nuke executable: {}'.f..(executable)
                    break

        __ no. executable:
            private_tool_root _ helper.get_tool_private_root()
            settings_path _ __.pa__.j..(private_tool_root, 'settings.xml')
            print templates.NO_NUKE_EXE_FOUND.f..(settings_path)
        r_ executable


___ get_nukescript_path():
    ______ ?
    r_ ?.root().name()