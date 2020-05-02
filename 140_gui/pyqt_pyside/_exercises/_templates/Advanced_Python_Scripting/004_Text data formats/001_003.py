_____ os

c_ settings(
    ___  -  , path=None
        __ path:
            path = path
        else:
            path = 'c:/settings.ini'
        data = __readFile()

    ___ __readFile
        __ os.path.exists(path
            text = open(path, 'r').readlines()
            data = {}
            __ text:
                for line in [x.strip() for x in text]:
                    key, value = line.split('=')
                    __ value.isdigit(
                        value = int(value)
                    elif value.replace('.','').isdigit() and value.count('.') __ 1:
                        value = float(value)
                    data[key] = value
            return data
        return __create_default()

    ___ __write_file
        __ data:
            with open(path, 'w') as f:
                for key, value in data.items(
                    f.write('%s=%s\n' % (key, value))

    ___ __create_default
        d = dict(app='',
                 value=0,
                 path='')
        return d

    ___ setValue , key, value
        data[key] = value
        __write_file()

    ___ getValue , key, default=None
        return data.get(key, default)

    ___ getSettings
        return data

s = settings('c:/mySettings.ini')
s.setValue('app', 'Maya')