from setuptools import setup, find_packages
import os, re, sys

def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

def get_requires(filename):
    requirements = []
    with open(filename) as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements

project_requirements = get_requires("requirements.txt")

if os.name == 'posix' and sys.version_info[0] < 3: project_requirements.append('subprocess32')

setup(
    name="carbin",
    version=get_version("carbin"),
    url='https://github.com/gottingen/carbin',
    license='bsd',
    description='Cmake bazel package retrieval',
    author='lothar',
    author_email='lijippy@163.com',
    packages=find_packages(),
    package_data={'cmake': ['*.cmake']},
    install_requires=project_requirements,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'carbin = carbin.cli:cli',
        ]
    },
    zip_safe=False
)
