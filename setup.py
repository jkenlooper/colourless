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
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'setuptools',
        'python-colourlovers',
        'pystache',
        ],
    entry_points=("""
      [console_scripts]
      palette=colourless.script:main
      """)
    )
