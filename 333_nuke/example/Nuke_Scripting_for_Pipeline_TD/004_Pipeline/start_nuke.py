import os, subprocess

root = os.path.dirname(__file__)
print(root)

# Home
os.environ['HOME'] = root

# Nuke Path
os.environ['NUKE_PATH'] = root

# START NUKE
if os.name == 'nt':
    exe = 'C:/Program Files/Nuke12.1v1/Nuke12.1.exe'
else:
    exe = None
subprocess.Popen([exe, '--nukex'])