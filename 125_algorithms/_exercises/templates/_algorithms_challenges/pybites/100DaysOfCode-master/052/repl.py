# code from PyCon talk 'Awesome Commandline Tools by Amjith'
# https://speakerdeck.com/amjith/awesome-commandline-tools
# by https://twitter.com/amjithr
______ sys

from prompt_toolkit ______ prompt
from prompt_toolkit.history ______ FileHistory
from prompt_toolkit.auto_suggest ______ AutoSuggestFromHistory
from prompt_toolkit.contrib.completers ______ WordCompleter
from pygments.lexers.sql ______ SqlLexer

SQLCompleter = WordCompleter(['select', 'show', 'from', 'insert', 'update',
                              'delete', 'drop', 'where'], ignore_case=True)

w___ 1:
    try:
        user_input = prompt(u'SQL>',
                        history=FileHistory('history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                        completer=SQLCompleter,
                        lexer=SqlLexer,
                        )
        print(user_input)
    except (EOFError, KeyboardInterrupt
        print('Goodbye!')
        sys.exit()
