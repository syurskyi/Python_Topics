_____ os

c_ settings(
    ___  -  , path_None
        __ path:
            path _ path
        ____
            path _ 'c:/settings.ini'
        data _ __readFile()

    ___ __readFile
        __ os.path.exists(path
            t.. _ open(path, 'r').readlines()
            data _ {}
            __ t..:
                ___ line in [x.strip() ___ x in t..]:
                    key, value _ line.split('=')
                    __ value.isdigit(
                        value _ int(value)
                    elif value.replace('.','').isdigit() and value.count('.') __ 1:
                        value _ float(value)
                    data[key] _ value
            return data
        return __create_default()

    ___ __write_file
        __ data:
            with open(path, 'w') as f:
                ___ key, value in data.items(
                    f.write('%s=%s\n' % (key, value))

    ___ __create_default
        d _ dict(app_'',
                 value_0,
                 path_'')
        return d

    ___ setValue , key, value
        data[key] _ value
        __write_file()

    ___ getValue , key, default_None
        return data.get(key, default)

    ___ getSettings
        return data

s _ settings('c:/mySettings.ini')
s.setValue('app', 'Maya')