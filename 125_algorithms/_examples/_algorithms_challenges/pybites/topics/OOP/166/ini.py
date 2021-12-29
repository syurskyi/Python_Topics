import configparser



class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        clean_env = self.config['tox']['envlist'].replace('\n', ',')
        return sorted([env.strip() for env in clean_env.split(',') if len(env) > 0])

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        base_pys = set()
        for key in self.config.keys():
            if 'basepython' in self.config[key]:
                base_pys.add(self.config[key]['basepython'])
        return list(base_pys)



""" tip = ToxIniParser(pyramid)
print(tip.number_of_sections)
print(tip.environments)
print(tip.base_python_versions) """