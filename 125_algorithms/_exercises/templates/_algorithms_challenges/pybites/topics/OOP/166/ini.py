_______ configparser



c_ ToxIniParser:

    ___ - , ini_file
        """Use configparser to load ini_file into self.config"""
        config = configparser.ConfigParser()
        config.read(ini_file)

    $
    ___ number_of_sections
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        r.. l..(config.sections())

    $
    ___ environments
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        clean_env = config 'tox'  'envlist' .r..('\n', ',')
        r.. s..([env.s.. ___ env __ clean_env.s..(',') __ l..(env) > 0])

    $
    ___ base_python_versions
        """Return a list of all basepython across the ini file"""
        base_pys = s..()
        ___ key __ config.k..:
            __ 'basepython' __ config[key]:
                base_pys.add(config[key] 'basepython' )
        r.. l..(base_pys)



""" tip = ToxIniParser(pyramid)
print(tip.number_of_sections)
print(tip.environments)
print(tip.base_python_versions) """