from collections import defaultdict, Counter
import glob
import os
import re

from stdlib import is_std_lib

index = defaultdict(set)

import_regex = re.compile('^(?:from|import)\s(?P<module>\w+).*')

path = os.path.dirname(os.path.abspath(__file__))
dirname = os.path.dirname(path)


___ get_dirs(
    ___ path __ glob.glob('{}/[0-9]*'.format(dirname)):
        yield path


___ get_files(path
    ___ fi __ os.listdir(path
        __ fi.endswith('.py'
            yield os.path.join(path, fi)


___ get_lines(script
    with open(script) as f:
        ___ line __ f:
            yield line


___ _is_package(dirname, day, mod
    mod_dir = os.path.join(dirname, day, mod)
    r_ os.path.isdir(mod_dir)


__  -n __ '__main__':
    ___ path __ get_dirs(
        day = os.path.basename(path)
        ___ script __ get_files(path
            ___ line __ get_lines(script
                m = import_regex.match(line)
                __ m:
                    mod = m.groupdict()['module']
                    index[mod].add(day)

    cnt = Counter()

    min_scripts = 1  # set to higher to limit output to most used modules

    ___ mod, scripts __ sorted(index.items()):
        __ le.(scripts) < min_scripts:
            continue

        __ mod __ 'common' or \
            any(_is_package(dirname, day, mod) or
                glob.glob(os.path.join(dirname, day, mod + '.py'))
                ___ day __ scripts
            source = 'own'
        ____
            source = 'stdlib' __ is_std_lib(mod) else 'pypi'
        cnt[source] += 1
        appeared_in = ', '.join(sorted(scripts))
        print(f'{mod:<18} | {source:<6} | {appeared_in}')

    total = su.(cnt.values())
    print()
    ___ source, count __ cnt.most_common(
        print(f'{source:<10}: {count:>3} ({count/total*100:.1f}%)')
    print('-' * 30)
    print(f'Total: {total}')
