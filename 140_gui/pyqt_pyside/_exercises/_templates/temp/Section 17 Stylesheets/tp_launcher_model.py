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

from collections import OrderedDict, defaultdict
import json
import os
import platform
import subprocess
import webbrowser


class TP_Launcher_Model(object):
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
    def __init__(self):
        self._workspaces = OrderedDict()
        self._open_doc = defaultdict(lambda: 'open ')
        self._open_doc['Windows'] = 'start '
        self._platform = platform.system()

    # ======== WORKSPACES ============

    def add_workspace(self, ws_name):
        ''' Add a new workspace, creating ordered dict'''
        self._workspaces[ws_name] = OrderedDict()

    def get_workspaces(self):
        ''' returns a list of workspace names '''
        return list(self._workspaces.keys()) # Python 3.0+ conversion

    def delete_workspace(self, ws_name):
        ''' delete workspace by workspace name '''
        del self._workspaces[ws_name]

    # ======== APPS ============

    def get_app_names(self, ws_name):
        ''' returns list of application or file names, no ext'''
        return self._workspaces[ws_name].keys()

    def get_app_icon(self, ws_name, app_name):
        ''' return filepath to icon image'''
        return self._workspaces[ws_name][app_name][1]

    def add_app(self, ws_name, app_path, icon_path):
        ''' add an application and icon file path to the workspace
        dictionary designated
        '''
        app_name = os.path.splitext(os.path.basename(app_path))[0]
        self._workspaces[ws_name][app_name] = [app_path, icon_path]

    def delete_app(self, ws_name, app_name):
        ''' delete app from workspace dict'''
        del self._workspaces[ws_name][app_name]

    def reorder_apps(self, ws_name, app_list):
        ''' if app/file order has changed, reorder dict'''
        if self._workspaces[ws_name].keys() != app_list:
            temp = OrderedDict()
            for name in app_list:
                temp[name] = self._workspaces[ws_name][name]
            self._workspaces[ws_name] = temp

    def run_app(self, ws_name, app_name):
        ''' attempt to run application/file at path if still exists'''
        _file = self._workspaces[ws_name][app_name][0]
        if os.path.exists(_file):
            try:
                subprocess.Popen(_file)
            except:
                os.system(self._open_doc[self._platform] + _file)
        else:
            raise ValueError('Exe file no longer exists')

    def run_youtube(self):
        ''' Open my favorite youtube channel! '''
        webbrowser.open('http://www.youtube.com/TPayneExperience')

    # ======== JSON ============

    def write_json_file(self, path):
        ''' write data from ordered dict to json file'''
        with open(path, 'w') as js_file:
            json.dump(self._workspaces, js_file)

    def read_json_file(self, path):
        ''' read data from ordered dict to json file'''
        with open(path, 'r') as js_file:
            self._workspaces = OrderedDict(json.load(js_file))



# Copyright (c) 2017 Trevor Payne
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
