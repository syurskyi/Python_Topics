from setuptools ______ setup

with open('README.md','r') as f:
    long_description _ f.read()


setup(name_'MakeTreeDir',
      version_'0.1.4',
      description_'OS wrapper python package which checks __ a given folder tree path exists and creates them.',
      long_description_long_description,
      long_description_content_type_"text/markdown",
      url_'https://github.com/Sreekiranar/MakeTreeDir.git',
      authors_'Sreekiran A R',
      author_email_'sreekiranar@gmail.com',
      license_'MIT',
      packages_['MakeTreeDir'],
      install_requires_[], include_package_data_True,
      zip_safe_False)
