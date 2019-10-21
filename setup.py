from setuptools import setup
import re

try:
    verstrline = open('webui/_version.py', "rt").read()
except IOError:
    raise RuntimeError("cannot read version file")
else:
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        raise RuntimeError("unable to find version in yourpackage/_version.py")

setup(
    # Application name:
    name="puppet_webapp",

    # Version number (initial):
    version=verstr,

    # Application author details:
    author="Matt Cadorette",
    author_email="mattc@puppet.com",

    # Packages
    packages=["webui"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/ipcrm/puppet_webapp",

    description="Example App",
    test_suite='tests',

    # Dependent packages (distributions)
    install_requires=[
        'Flask==0.10.1',
        'Flask-Testing==0.4.2',
        'itsdangerous==0.24',
        'Jinja2==2.8',
        'MarkupSafe==0.23',
        'Werkzeug==0.15.3',
    ],

)
