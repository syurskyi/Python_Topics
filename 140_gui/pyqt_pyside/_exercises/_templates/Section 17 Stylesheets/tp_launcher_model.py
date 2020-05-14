#!/usr/bin/env python

'''
Data holding (model) class for TP Launcher.
Stores data in the following way:
    Workspaces Ordered Dict {
        WorkspaceName {
            AppName : (App_file_path, Icon_file_path)
            }
        }

has basic accessors and mutators, run and reorder.
Also includes YouTube opening function, hardcoded url though.
'''

____ collections _____ OrderedDict, defaultdict
_____ json
_____ __
_____ platform
_____ subprocess
_____ webbrowser


c_ TP_Launcher_Model(object
    ''' Data holding (model) class for TP Launcher.
    Stores data in the following way:
        Workspaces Ordered Dict {
            WorkspaceName {
                AppName : (App_file_path, Icon_file_path)
                }
            }

    has basic accessors and mutators, run and reorder.
    Also includes YouTube opening function, hardcoded url though.
    '''
    ___  -  
        _workspaces _ OrderedDict
        _open_doc _ defaultdict(lambda: 'open ')
        _open_doc['Windows'] _ 'start '
        _platform _ platform.system

    # ======== WORKSPACES ============

    ___ add_workspace , ws_name
        ''' Add a new workspace, creating ordered dict'''
        _workspaces[ws_name] _ OrderedDict

    ___ get_workspaces 
        ''' returns a list of workspace names '''
        r_ list(_workspaces.keys()) # Python 3.0+ conversion

    ___ delete_workspace , ws_name
        ''' delete workspace by workspace name '''
        del _workspaces[ws_name]

    # ======== APPS ============

    ___ get_app_names , ws_name
        ''' returns list of application or file names, no ext'''
        r_ _workspaces[ws_name].keys

    ___ get_app_icon , ws_name, app_name
        ''' return filepath to icon image'''
        r_ _workspaces[ws_name][app_name][1]

    ___ add_app , ws_name, app_path, icon_path
        ''' add an application and icon file path to the workspace
        dictionary designated
        '''
        app_name _ __.path.splitext(__.path.b..(app_path))[0]
        _workspaces[ws_name][app_name] _ [app_path, icon_path]

    ___ delete_app , ws_name, app_name
        ''' delete app from workspace dict'''
        del _workspaces[ws_name][app_name]

    ___ reorder_apps , ws_name, app_list
        ''' if app/file order has changed, reorder dict'''
        __ _workspaces[ws_name].keys !_ app_list:
            temp _ OrderedDict
            ___ name in app_list:
                temp[name] _ _workspaces[ws_name][name]
            _workspaces[ws_name] _ temp

    ___ run_app , ws_name, app_name
        ''' attempt to run application/file at path if still exists'''
        _file _ _workspaces[ws_name][app_name][0]
        __ __.path.exists(_file
            ___
                subprocess.Popen(_file)
            _____:
                __.system(_open_doc[_platform] + _file)
        ____
            raise ValueError('Exe file no longer exists')

    ___ run_youtube 
        ''' Open my favorite youtube channel! '''
        webbrowser.o..('http://www.youtube.com/TPayneExperience')

    # ======== JSON ============

    ___ write_json_file , path
        ''' write data from ordered dict to json file'''
        w__ o..(path, 'w') __ js_file:
            json.dump(_workspaces, js_file)

    ___ read_json_file , path
        ''' read data from ordered dict to json file'''
        w__ o..(path, 'r') __ js_file:
            _workspaces _ OrderedDict(json.l..(js_file))
