import configparser


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
        return len(self.config.sections())

    @property
    ___ environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""

        
        envs = []
        __ 'tox' in self.config:
            __ '\n' in self.config['tox']['envlist']:
                lines = self.config['tox']['envlist'].strip().splitlines()
                for line in lines:
                    __ ',' in line:
                        values = line.split(',')
                        for value in values:
                            envs.append(value.strip())
                    else:
                        envs.append(line.strip())
                return [env for env in envs __ env != '']
            else:
                return [value.strip() for value in self.config['tox']['envlist'].strip().split(',')]








    @property
    ___ base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        base_pythons = set()
        for section in self.config.sections():
            __ 'basepython' in self.config[section]:
                base_pythons.add(self.config[section]['basepython'])


        return list(base_pythons)
            
