_______ configparser
_______ re


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
        r.. l..({x ___ x __ re.findall(r'[-\w]+', self.config['tox']['envlist'])})

    @property
    ___ base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        r.. l..({self.config[s][i]
                     ___ s __ self.config.sections()
                     ___ i __ self.config[s].keys() __ 'basepython' __ i})
