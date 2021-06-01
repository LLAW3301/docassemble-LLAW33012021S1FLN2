import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012021S1FLN2',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# Paws Rights Web-App\r\n\r\nThis is an app designed for people in SA with assistance animals, who can often be refused access to Ubers, taxis, public transport, and so on. It helps build a report of each transport refusal, ready to be sent to DPTI. It can also be used to gather anonymous statistics of how many refusals are occuring, what areas these occur in, which transport services are involved, and so on.\r\n\r\n## Authors\r\n\r\nSarah Milne, Louis MacConnell, Alex Priest, Callie Symonds, and Emily Prater\r\n\r\nFor Flinders University, Amanda Muller, and Ellen Fraser-Barbour\r\n\r\nBased on templates by Mark Ferraretto, mark.ferraretto@flinders.edu.au\r\n',
      long_description_content_type='text/markdown',
      author='Mark Ferraretto',
      author_email='mark.ferraretto@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012021S1FLN2/', package='docassemble.LLAW33012021S1FLN2'),
     )

