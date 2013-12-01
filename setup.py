import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

name = "colourless"
version = "0.0.1"

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name=name,
    version=version,
    author='Jake Hickenlooper',
    author_email='jake@weboftomorrow.com',
    description="Create a colour.less file from a colourlovers palette",
    url="https://github.com/jkenlooper/colourless",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python :: 2.7',
        ],
    install_requires=[
        'requests',
        'python-colourlovers',
        'pystache',
        'docopt',
        ],
    entry_points={
        'console_scripts': [
            'colourless = colourless.script:main'
            ]
        }
    )
