_______ configparser


class ToxIniParser:

    ___ __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()

        self.config.read(ini_file)

    @property
    ___ number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        r.. l..(self.config.sections())

    @property
    ___ environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""

        
        envs    # list
        __ 'tox' __ self.config:
            __ '\n' __ self.config['tox']['envlist']:
                lines = self.config['tox']['envlist'].s...splitlines()
                ___ line __ lines:
                    __ ',' __ line:
                        values = line.s..(',')
                        ___ value __ values:
                            envs.a..(value.strip())
                    ____:
                        envs.a..(line.strip())
                r.. [env ___ env __ envs __ env != '']
            ____:
                r.. [value.s.. ___ value __ self.config['tox']['envlist'].s...s..(',')]








    @property
    ___ base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        base_pythons = set()
        ___ section __ self.config.sections():
            __ 'basepython' __ self.config[section]:
                base_pythons.add(self.config[section]['basepython'])


        r.. l..(base_pythons)
            
