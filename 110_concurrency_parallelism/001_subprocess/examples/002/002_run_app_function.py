from collections import OrderedDict, defaultdict
import os
import platform
import subprocess
import webbrowser

def run_app(self, ws_name, app_name):
    _file = self._workspaces[ws_name][app_name][0]
    if os.path.exists(_file):
        try:
            subprocess.Popen(_file)
        except:
            os.system(self._open_doc[self._platform] + _file)
    else:
        raise ValueError('Exe file no longer exists')


# run_youtube()

def launch_test():
    command = r'C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe'
    subprocess.Popen(command)

# launch_test()