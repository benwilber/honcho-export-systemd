import os
from setuptools import setup, find_packages

from honcho_export_systemd import __version__

HERE = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(HERE, 'README.md')).read()
except:
    long_description = None

setup(
    name='honcho-export-systemd',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,

    # metadata for upload to PyPI
    author='Ben Wilber',
    author_email='benwilber@gmail.com',
    url='https://github.com/benwilber/honcho-export-systemd',
    description='systemd exporter for Honcho.',
    long_description=long_description,
    license='APACHE',
    keywords='sysadmin process procfile honcho systemd',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=['honcho>=0.6.5', 'jinja2>=2.6'],
    entry_points={
        'honcho_exporters': [
            'systemd=honcho_export_systemd.export_systemd:Export',
        ],
    }
)