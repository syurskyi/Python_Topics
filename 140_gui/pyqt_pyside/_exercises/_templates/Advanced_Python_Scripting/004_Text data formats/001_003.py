_____ __

c_ settings(
    ___  -  , path_None
        __ path:
            path _ path
        ____
            path _ 'c:/settings.ini'
        data _ __readFile

    ___ __readFile
        __ __.path.exists(path
            t.. _ o..(path, 'r').readlines
            data _ {}
            __ t..:
                ___ line in [x.strip ___ x in t..]:
                    key, value _ line.split('=')
                    __ value.isdigit(
                        value _ int(value)
                    ____ value.replace('.','').isdigit an. value.count('.') __ 1:
                        value _ fl..(value)
                    data[key] _ value
            r_ data
        r_ __create_default

    ___ __write_file
        __ data:
            w__ o..(path, 'w') __ f:
                ___ key, value in data.items(
                    f.w..('%s=%s\n' % (key, value))

    ___ __create_default
        d _ dict(app_'',
                 value_0,
                 path_'')
        r_ d

    ___ sV.. , key, value
        data[key] _ value
        __write_file

    ___ getValue , key, default_None
        r_ data.get(key, default)

    ___ getSettings
        r_ data

s _ settings('c:/mySettings.ini')
s.sV..('app', 'Maya')