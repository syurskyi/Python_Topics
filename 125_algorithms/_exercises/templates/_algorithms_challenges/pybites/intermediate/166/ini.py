_______ configparser


c_ ToxIniParser:

    ___ - , ini_file):
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

        
        envs    # list
        __ 'tox' __ config:
            __ '\n' __ config['tox']['envlist']:
                lines = config['tox']['envlist'].s...splitlines()
                ___ line __ lines:
                    __ ',' __ line:
                        values = line.s..(',')
                        ___ value __ values:
                            envs.a..(value.strip())
                    ____:
                        envs.a..(line.strip())
                r.. [env ___ env __ envs __ env != '']
            ____:
                r.. [value.s.. ___ value __ config['tox']['envlist'].s...s..(',')]








    $
    ___ base_python_versions
        """Return a list of all basepython across the ini file"""
        base_pythons = set()
        ___ section __ config.sections():
            __ 'basepython' __ config[section]:
                base_pythons.add(config[section]['basepython'])


        r.. l..(base_pythons)
            
