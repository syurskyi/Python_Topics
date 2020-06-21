# subprocess_pipes.py

import subprocess

cat = subprocess.Popen(
    ['cat', 'index.rst'],
    stdout=subprocess.PIPE,
)

grep = subprocess.Popen(
    ['grep', '.. literalinclude::'],
    stdin=cat.stdout,
    stdout=subprocess.PIPE,
)

cut = subprocess.Popen(
    ['cut', '-f', '3', '-d:'],
    stdin=grep.stdout,
    stdout=subprocess.PIPE,
)

end_of_pipe = cut.stdout

print('Included files:')
for line in end_of_pipe:
    print(line.decode('utf-8').strip())

# $ cat index.rst | grep ".. literalinclude" | cut -f 3 -d:

# $ python3 -u subprocess_pipes.py
#
# Included files:
# subprocess_os_system.py
# subprocess_shell_variables.py
# subprocess_run_check.py
# subprocess_run_output.py
# subprocess_run_output_error.py
# subprocess_run_output_error_trap.py
# subprocess_check_output_error_trap_output.py
# subprocess_run_output_error_suppress.py
# subprocess_popen_read.py
# subprocess_popen_write.py
# subprocess_popen2.py
# subprocess_popen3.py
# subprocess_popen4.py
# subprocess_pipes.py
# repeater.py
# interaction.py
# signal_child.py
# signal_parent.py
# subprocess_signal_parent_shell.py
# subprocess_signal_setpgrp.py
