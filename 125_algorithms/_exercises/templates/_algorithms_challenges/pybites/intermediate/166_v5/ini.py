_______ configparser
_______ __


c_ ToxIniParser:

    ___ - , ini_file
        """Use configparser to load ini_file into self.config"""
        config configparser.ConfigParser()
        config.read(ini_file)

    $
    ___ number_of_sections
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        r.. l..(config.sections

    $
    ___ environments
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        r.. l..({x ___ x __ __.f..(r'[-\w]+', config 'tox'  'envlist' )})

    $
    ___ base_python_versions
        """Return a list of all basepython across the ini file"""
        r.. l..({config[s][i]
                     ___ s __ config.sections()
                     ___ i __ config[s].k.. __ 'basepython' __ i})
