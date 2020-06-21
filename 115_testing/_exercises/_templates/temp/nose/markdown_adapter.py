"""
Software API adapter for markdown.py
This module provides a function based API to markdown.py
since markdown.py only provides a CLI.
"""

____ subprocess ______ Popen, PIPE, STDOUT
____ tempfile ______ NamedTemporaryFile
______ __

# This is here so there's one line to change if I want to swap
# out a different script, such as markdown.pl
_interpreter_and_script _ ['python', 'markdown.py']

___ run_markdown(input_text
    """
    The default method when we don't care which method to use.
    """
    r_ run_markdown_pipe(input_text)

___ run_markdown_pipe(input_text
    """
    Simulate: echo 'some input' | python markdown.py
    """
    pipe _ Popen(_interpreter_and_script,
            stdout_PIPE, stdin_PIPE, stderr_STDOUT)
    output _ pipe.communicate(input_input_text)[0]
    r_ output.rstrip()

___ run_markdown_file(input_text
    """
    Simulate: python markdown.py fileName
    """
    temp_file _ NamedTemporaryFile(delete_False)
    temp_file.write(input_text)
    temp_file.close()
    interp_script_and_fileName _ _interpreter_and_script
    interp_script_and_fileName.a..(temp_file.name)
    pipe _ Popen(interp_script_and_fileName,
            stdout_PIPE, stderr_STDOUT)
    output _ pipe.communicate()[0]
    __.unlink(temp_file.name)
    r_ output.rstrip()