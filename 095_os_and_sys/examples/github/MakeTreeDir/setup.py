from setuptools import setup

with open('README.md','r') as f:
    long_description = f.read()


setup(name='MakeTreeDir',
      version='0.1.4',
      description='OS wrapper python package which checks if a given folder tree path exists and creates them.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Sreekiranar/MakeTreeDir.git',
      authors='Sreekiran A R',
      author_email='sreekiranar@gmail.com',
      license='MIT',
      packages=['MakeTreeDir'],
      install_requires=[], include_package_data=True,
      zip_safe=False)
