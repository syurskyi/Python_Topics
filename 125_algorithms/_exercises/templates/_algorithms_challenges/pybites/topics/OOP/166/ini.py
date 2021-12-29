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
        clean_env = self.config['tox']['envlist'].replace('\n', ',')
        r.. s..([env.strip() ___ env __ clean_env.split(',') __ l..(env) > 0])

    @property
    ___ base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        base_pys = set()
        ___ key __ self.config.keys():
            __ 'basepython' __ self.config[key]:
                base_pys.add(self.config[key]['basepython'])
        r.. l..(base_pys)



""" tip = ToxIniParser(pyramid)
print(tip.number_of_sections)
print(tip.environments)
print(tip.base_python_versions) """